# Hardware Specifications

> [!danger] Vendor Agnostic
> As it is a stated goal of the Clear Skies architecture to remain vendor agnostic the following vendor product highlights are for comparison purposes only and not recommendations or promotions an any specific vendor or products.

## SDDC Servers

The following data compared serveral technical and capacity aspects of potential hardware solutions for a Software Defined Data Center (SDDC) ProxMox server  / PVE node.

### Proxmox VE Server Hardware Requirements

::: {.table-scriptsize}
\scriptsize
| **Category**            | **Bare Minimum** (Lab/Test)                 | **Standalone** (Edge)                          | **Hyperconverged Node** (Cluster)                                 |
| ----------------------- | ------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| **CPU**                 | 1× Dual-Core (Intel/AMD, VT-x/AMD-V) | 1× Quad-Core (i5/i7, Xeon-E, Ryzen 5/7) | 1× 6–12 Core (Xeon-D, Xeon-Silver, Ryzen 9, EPYC)                               |
| **Architecture**        | x86-64                                      | x86-64                                         | x86-64 (SR-IOV & AES-NI support recommended)                      |
| **RAM**                 | 8 GB minimum (test only)                    | 32–64 GB                                       | 64–256 GB (ECC prefered)                                          |
| **Boot / OS Disk**      | 64 GB SATA SSD                              | 128 GB SATA/NVMe SSD                           | 256 GB NVMe SSD (mirrored or ZFS mirror)                          |
| **VM/CT Storage**       | >~ 250 GB  SSD/HDD                          |  >~ 1 TB Single SSD/NVMe                       | 2+ >~2 TB NVMe/SSD                                                |
| **Network Interfaces**  | 2× 1 GbE                                    | 3× 1/2.5 GbE (LAN, WAN, Mgmt)                  | 4–6× 2.5/10 GbE (Mgmt, Ceph, VM LAN, Public, Storage)             |
| **Out-of-Band Mgmt**    | Optional                                    | Optional                                       | Recommended (IPMI, iDRAC, Etc)                                    |
| **Power Supply**        | Single PSU                                  | Single PSU                                     | Recommended Dual hot-swappable PSUs                               |
| **TPM / Secure Boot**   | Optional                                    | Recommended                                    | Required for Microsoft compliance (TPM 2.0)                       |
| **BIOS / Firmware**     | Legacy or UEFI                              | UEFI (coreboot OK)                             | UEFI                                  |
| **Cluster / Ceph Role** | N/A                                         | Optional (single node)                         | Full cluster member (Ceph OSD + Monitor)                          |
| **Performance Target**  | Small lab / field site                      | Small-scale production workloads               | Continuous 24×7 ops with fault tolerance                          |
| **Approx Power Draw**   | 25–40 W                                     | 50–90 W                                        | 80–200 W (depending on drives/NICs)                               |
| **Example Platform**    | Intel NUC, Protectli VP6630                 | Minisforum MS-01, Protectli VP6650             | Supermicro E300, Xeon-D, or 3× Proxmox mini-cluster               |
| **Notes**               | Not for production                          | Great for edge compute or small SDDC           | Use 3 nodes + Ceph + replication; no single failure halts cluster |
:::


