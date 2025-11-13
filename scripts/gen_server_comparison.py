#!/usr/bin/env python3
import json, pathlib

SRC = pathlib.Path("data/servers")
OUT = pathlib.Path("lib/md/server_comparison.md")

# -------------------------------
# Utility helpers
# -------------------------------

def safe(v):
    return str(v) if v not in (None, "", [], {}) else "–"

def safe_price(v):
    """Return numeric price for sorting; non-numeric sorts last."""
    try:
        return float(str(v).replace("$", "").replace(",", "").strip())
    except Exception:
        return float("inf")

def get_storage_summary(storage):
    """Split storage into OS and VM disks."""
    if not storage:
        return ("–", "–")
    if len(storage) == 1:
        s = storage[0]
        return (f"{s.get('type','')} {s.get('capacity_each_tb','–')} TB", "–")
    osdisk = storage[0]
    vmdisks = storage[1:]
    os_str = f"{osdisk.get('type','')} {osdisk.get('capacity_each_tb','–')} TB"
    vm_str = "; ".join([
        f"{d.get('type','')} x{d.get('count','–')} {d.get('capacity_each_tb','–')} TB"
        for d in vmdisks
    ])
    return (os_str, vm_str)

def get_nic_counts(nics):
    """Return count of 1–2 Gb and ≥10 Gb NICs."""
    if not nics:
        return (0, 0)
    gbit, ten = 0, 0
    for n in nics:
        try:
            speed = float(n.get("speed_gbps", 0))
        except ValueError:
            speed = 0
        count = int(n.get("count", 1))
        if speed <= 2.5:
            gbit += count
        elif speed >= 10:
            ten += count
    return (gbit, ten)

# -------------------------------
# Load server JSON files
# -------------------------------

def load_servers():
    servers = []
    for f in sorted(SRC.glob("*.json")):
        if f.name.lower().startswith("make_model"):  # skip template
            continue
        try:
            with f.open() as fh:
                data = json.load(fh)
                servers.append((f.stem, data))
        except Exception as e:
            print(f"⚠️  Skipping {f.name}: {e}")
    return servers

# -------------------------------
# Markdown generation
# -------------------------------

def make_summary_table(servers):
    """Generate the summary comparison table with fenced div and LaTeX sizing."""
    header = (
        "| Product | CPU (Make + Cores) | RAM (GB) | OS Disk | VM Disk(s) | "
        "1–2 Gb NICs | 10 Gb NICs | Rack (U) | Power (W max) | Price (USD) |\n"
        "|:--|:--|:--:|:--|:--|:--:|:--:|:--:|:--:|:--:|\n"
    )

    rows = []
    for _, s in servers:
        sp = s.get("specs", {})
        cpu = sp.get("cpu", {})
        mem = sp.get("memory", {})
        storage = sp.get("storage", [])
        nics = sp.get("network", [])
        power = sp.get("power", {})
        chassis = sp.get("chassis", {})

        osdisk, vmdisk = get_storage_summary(storage)
        gbit, ten = get_nic_counts(nics)
        cpu_str = f"{safe(cpu.get('model'))} ({safe(cpu.get('cores'))}C)"

        price_val = s.get("price_usd")
        if price_val in (None, "", "–"):
            price_str = "–"
        else:
            price_str = f"${price_val}"


        row = "| " + " | ".join([
            safe(s.get("product")),
            cpu_str,
            safe(mem.get("capacity_gb")),
            safe(osdisk),
            safe(vmdisk),
            str(gbit),
            str(ten),
            safe(chassis.get("rack_units")),
            safe(power.get("draw_w", {}).get("max")),
            price_str
        ]) + " |"
        rows.append(row)

    return (
        "## Server Comparison\n\n"
        "::: {.table-scriptsize}\n"
        "\\scriptsize\n"
        + header
        + "\n".join(rows)
        + "\n:::\n\\small\n"
    )

def make_detail_section(filename_stem, server):
    """Generate detailed per-product markdown with link inside table."""
    s = server
    sp = s.get("specs", {})
    cpu = sp.get("cpu", {})
    mem = sp.get("memory", {})
    ch = sp.get("chassis", {})
    pw = sp.get("power", {})
    mgmt = sp.get("management", {})
    os_support = ", ".join(sp.get("os_support", []))
    osdisk, vmdisk = get_storage_summary(sp.get("storage"))
    gbit, ten = get_nic_counts(sp.get("network"))

    img_name = f"{filename_stem}.jpg"

    lines = []
    lines.append(f"### {safe(s.get('product'))}\n")
    lines.append(f"![{s.get('product')}](lib/img/{img_name})\n")

    # Start the specifications table
    lines.append("\n**Specifications**\n")
    lines.append("| Spec | Value |")
    lines.append("|:--|:--|")
    lines.append(f"| CPU | {safe(cpu.get('model'))} ({safe(cpu.get('cores'))} cores, {safe(cpu.get('threads'))} threads) |")
    lines.append(f"| Memory | {safe(mem.get('capacity_gb'))} GB {safe(mem.get('type'))} |")
    lines.append(f"| OS Disk | {safe(osdisk)} |")
    lines.append(f"| VM Disk(s) | {safe(vmdisk)} |")
    lines.append(f"| 1–2 Gb NICs | {gbit} |")
    lines.append(f"| 10 Gb NICs | {ten} |")
    lines.append(f"| Rack Units | {safe(ch.get('rack_units'))} |")
    lines.append(f"| Dimensions (in) | {safe(ch.get('dimensions_in'))} |")
    lines.append(f"| Power Draw (W) | Idle {safe(pw.get('draw_w',{}).get('idle'))} / Max {safe(pw.get('draw_w',{}).get('max'))} |")
    lines.append(f"| Power Input | {safe(pw.get('input_type'))} |")
    lines.append(f"| Management | BMC: {safe(mgmt.get('bmc'))}, BIOS: {safe(mgmt.get('bios'))} |")
    lines.append(f"| Supported OS | {os_support} |")
    lines.append(f"| Price (USD) | ${safe(s.get('price_usd'))} |")

    # ✅ Add Product Page as final table row
    url = s.get("url")
    if url and url != "–":
        lines.append(f"| Product Page | [Link]({url}) |")

    lines.append("\n\n")
    return "\n".join(lines)


# -------------------------------
# Main
# -------------------------------

def main():
    servers = load_servers()
    if not servers:
        print("No servers found.")
        return

    # Sort purely by numeric price
    servers.sort(key=lambda x: safe_price(x[1].get("price_usd")))

    md_parts = [make_summary_table(servers)]
    md_parts.append("\n## Server Specifications\n")
    for fname, s in servers:
        md_parts.append("\n" + make_detail_section(fname, s))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(md_parts))
    print(f"✅ Wrote {OUT}")

if __name__ == "__main__":
    main()
