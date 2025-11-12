# Hardware Specifications

> [!danger] Vendor Agnostic
> As it is a stated goal of the Clear Skies architecture to remain vendor agnostic the following vendor product highlights are for comparison purposes only and not recommendations or promotions an any specific vendor or products.

# SDDC Servers

## Proxmox VE Server Hardware Requirements

::: {.table-scriptsize}
\scriptsize
| Category                | Bare Minimum (Lab/Test)                     | Standalone (Production Edge)                   | Hyperconverged Node (Zero-SPoF Cluster)                           |
| ----------------------- | ------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| **CPU**                 | 1× Dual-Core 64-bit (Intel/AMD, VT-x/AMD-V) | 1× Quad-Core 64-bit (i5/i7, Xeon-E, Ryzen 5/7) | 1× 6–12 Core (Xeon-D, Xeon-Silver, Ryzen 9, EPYC)                 |
| **Architecture**        | x86-64                                      | x86-64                                         | x86-64 (SR-IOV & AES-NI support recommended)                      |
| **RAM**                 | 8 GB minimum (test only)                    | 32–64 GB ECC preferred                         | 64–256 GB ECC required                                            |
| **Boot / OS Disk**      | 64 GB SATA SSD                              | 128 GB SATA/NVMe SSD                           | 256 GB NVMe SSD (mirrored or ZFS mirror)                          |
| **VM/CT Storage**       | Single SSD/HDD                              | Separate data SSD or ZFS mirror                | NVMe or enterprise SSD pool (ZFS RAID-Z1/RAID-10)                 |
| **Network Interfaces**  | 1× 1 GbE                                    | 3× 1 GbE or 2.5 GbE (LAN, WAN, Mgmt)           | 4–6× 2.5/10 GbE (Mgmt, Ceph, VM LAN, Public, Storage)             |
| **Out-of-Band Mgmt**    | Optional                                    | Recommended (IPMI/iKVM)                        | Required (IPMI, iDRAC, or similar)                                |
| **Power Supply**        | Single PSU                                  | Single high-quality PSU                        | Redundant or hot-swappable PSUs                                   |
| **TPM / Secure Boot**   | Optional                                    | Recommended                                    | Required for compliance (TPM 2.0)                                 |
| **BIOS / Firmware**     | Legacy or UEFI                              | UEFI (coreboot OK)                             | UEFI with PXE/iSCSI boot support                                  |
| **Cluster / Ceph Role** | N/A                                         | Optional (single node)                         | Full cluster member (Ceph OSD + Monitor)                          |
| **Performance Target**  | Small lab / dev                             | Small-scale production workloads               | Continuous 24×7 ops with fault tolerance                          |
| **Approx Power Draw**   | 25–40 W                                     | 50–90 W                                        | 80–200 W (depending on drives/NICs)                               |
| **Example Platform**    | Intel NUC, Protectli VP6600                 | Minisforum MS-01, Protectli VP6630             | Supermicro E300, Xeon-D, or 3× Proxmox mini-cluster               |
| **Notes**               | Not for production                          | Great for edge compute or small SDDC           | Use 3 nodes + Ceph + replication; no single failure halts cluster |
:::

# Server Comparison

::: {.table-scriptsize}
\scriptsize
| Product | CPU (Make + Cores) | RAM (GB) | OS Disk | VM Disk(s) | 1–2 Gb NICs | 10 Gb NICs | Rack (U) | Power (W max) | Price (USD) |
|:--|:--|:--:|:--|:--|:--:|:--:|:--:|:--:|:--:|
| Protectli VP6630 | Intel Core i3 (6-Port Model) (4 C) | 96 | NVMe SSD 4 TB | SATA SSD x1 1 TB | 6 | 2 | 1U | 40 | $1651 |
| Protectli VP6650 | Intel Core i5 (6-Port Model) (4 C) | 96 | NVMe SSD 4 TB | SATA SSD x1 1 TB | 6 | 2 | 1U | 45 | $1811 |
| ProLiant DL145 Gen11 | AMD EPYC 8004 series (Zen4c) (– C) | – | – | – | 0 | 0 | 2U | – | – |
| Qotom Q30921SE S13 | Intel Celeron 4305U or Core (8th–10th Gen) (2 C) | 32 | M.2 SSD 0 TB | SATA SSD/HDD x1 0 TB | 6 | 2 | – | 30 | $489 |
| MINISFORUM MS-S1 Max | AMD Ryzen AI Max+ 395 (16 C) | 128 | NVMe SSD 2 TB | – | 0 | 2 | 2U | 130 | $2503.9 |
| PowerEdge R6615 | AMD EPYC 9004 series (– C) | – | – | – | 2 | 0 | 1U | – | – |
| ProLiant DL235 Gen11 | AMD EPYC 9004 (– C) | – | – | – | 0 | 0 | 1U | – | – |
| Lancelot 1199-SR | Intel Xeon E-2478 (8 C) | 128 | NVMe SSD 1 TB | SAS HDD x4 16 TB | 2 | 4 | 1U | 250 | $5199 |
:::

 --- 

## Protectli VP6630

![Protectli VP6630](lib/img/Protectli_VP6630.jpg)

[Product Page](https://protectli.com/product/vp6630/)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Core i3 (6-Port Model) (4 cores, 8 threads) |
| Memory | 96 GB 2x48GB DDR5-5600 SO-DIMM |
| OS Disk | NVMe SSD 4 TB |
| VM Disk(s) | SATA SSD x1 1 TB |
| 1–2 Gb NICs | 6 |
| 10 Gb NICs | 2 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 7.5, 'w': 7.0, 'h': 3.0} |
| Power Draw (W) | Idle 15 / Max 40 |
| Power Input | DC 19.5V (IEC Type B) |
| Management | BMC: False, BIOS: coreboot (Open Source) |
| Supported OS | Proxmox VE, OPNsense, Ubuntu 24.04 LTS |
| Price (USD) | 1651 |

 --- 

## Protectli VP6650

![Protectli VP6650](lib/img/Protectli_VP6650.jpg)

[Product Page](https://protectli.com/product/vp6650/)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Core i5 (6-Port Model) (4 cores, 8 threads) |
| Memory | 96 GB 2x48GB DDR5-5600 SO-DIMM |
| OS Disk | NVMe SSD 4 TB |
| VM Disk(s) | SATA SSD x1 1 TB |
| 1–2 Gb NICs | 6 |
| 10 Gb NICs | 2 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 7.5, 'w': 7.0, 'h': 3.0} |
| Power Draw (W) | Idle 15 / Max 45 |
| Power Input | DC 19.5V (IEC Type B) |
| Management | BMC: False, BIOS: coreboot |
| Supported OS | Proxmox VE, OPNsense, Ubuntu 24.04 LTS |
| Price (USD) | 1811 |

 --- 


## Qotom Q30921SE S13

![Qotom Q30921SE S13](lib/img/Qotom_Q30921SE-S13.jpg)

[Product Page](https://www.qotom.net/mini-pc/q30900se-s13-series.html)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Celeron 4305U or Core (8th–10th Gen) (2 cores, 2 threads) |
| Memory | 32 GB DDR4 SO-DIMM 2133/2400MHz |
| OS Disk | M.2 SSD 0 TB |
| VM Disk(s) | SATA SSD/HDD x1 0 TB |
| 1–2 Gb NICs | 6 |
| 10 Gb NICs | 2 |
| Rack Units | – |
| Dimensions (in) | {'l': 7.7, 'w': 4.8, 'h': 1.9} |
| Power Draw (W) | Idle 10 / Max 30 |
| Power Input | DC 12V Jack |
| Management | BMC: False, BIOS: UEFI |
| Supported OS | OPNsense, Proxmox VE, Ubuntu 24.04 LTS |
| Price (USD) | 489 |

 --- 

## MINISFORUM MS-S1 Max

![MINISFORUM MS-S1 Max](lib/img/Minisforum_MS-S1-Max.jpg)

[Product Page](https://store.minisforum.com/products/minisforum-ms-s1-max-mini-pc)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD Ryzen AI Max+ 395 (16 cores, 32 threads) |
| Memory | 128 GB LPDDR5x-8000 |
| OS Disk | NVMe SSD 2 TB |
| VM Disk(s) | – |
| 1–2 Gb NICs | 0 |
| 10 Gb NICs | 2 |
| Rack Units | 2U |
| Dimensions (in) | {'l': 8.7, 'w': 8.1, 'h': 3.0} |
| Power Draw (W) | Idle 35 / Max 130 |
| Power Input | DC 12V/26.6A (320W adapter) |
| Management | BMC: False, BIOS: UEFI Secure Boot |
| Supported OS | Windows 11 Pro, Ubuntu 24.04 LTS, Proxmox VE |
| Price (USD) | 2503.9 |

 --- 

## PowerEdge R6615

![PowerEdge R6615](lib/img/Dell_PowerEdge_R6615.jpg)

[Product Page](https://www.dell.com/en-us/shop/cty/pdp/spd/poweredge-r6615)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD EPYC 9004 series (– cores, – threads) |
| Memory | – GB DDR5 4800 ECC RDIMM |
| OS Disk | – |
| VM Disk(s) | – |
| 1–2 Gb NICs | 2 |
| 10 Gb NICs | 0 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 28.0, 'w': 17.1, 'h': 1.7} |
| Power Draw (W) | Idle – / Max – |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI / iDRAC9 |
| Supported OS | Proxmox VE, Ubuntu 24.04 LTS, RHEL 9 |
| Price (USD) | – |

 --- 

## ProLiant DL145 Gen11

![ProLiant DL145 Gen11](lib/img/HP_ProLiant_DL145_Gen11.jpg)

[Product Page](https://buy.hpe.com/us/en/compute/rack-servers/proliant-dl100-servers/proliant-dl145-gen11/p/1014845266)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD EPYC 8004 series (Zen4c) (– cores, – threads) |
| Memory | – GB DDR5 ECC RDIMM |
| OS Disk | – |
| VM Disk(s) | – |
| 1–2 Gb NICs | 0 |
| 10 Gb NICs | 0 |
| Rack Units | 2U |
| Dimensions (in) | {'l': 28.0, 'w': 17.5, 'h': 3.4} |
| Power Draw (W) | Idle – / Max – |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI / iLO 6 |
| Supported OS | Proxmox VE, Ubuntu 24.04 LTS, RHEL 9 |
| Price (USD) | – |

 --- 

## ProLiant DL235 Gen11

![ProLiant DL235 Gen11](lib/img/HP_ProLiant_DL235_Gen11.jpg)

[Product Page](https://buy.hpe.com/us/en/compute/rack-servers/proliant-dl300-servers/proliant-dl325-server/hpe-proliant-dl325-gen11/p/1014689141)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD EPYC 9004 (– cores, – threads) |
| Memory | – GB DDR5 SmartMemory |
| OS Disk | – |
| VM Disk(s) | – |
| 1–2 Gb NICs | 0 |
| 10 Gb NICs | 0 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 28.0, 'w': 17.5, 'h': 1.7} |
| Power Draw (W) | Idle – / Max – |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI / iLO 6 |
| Supported OS | Proxmox VE, Ubuntu 24.04 LTS, RHEL 9 |
| Price (USD) | – |

 --- 

## Lancelot 1199-SR

![Lancelot 1199-SR](lib/img/ASL_Lancelot_1199SR.jpg)

[Product Page](https://www.aslab.com/products/rackmount/customize/lancelot1199sr.cgi)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Xeon E-2478 (8 cores, 16 threads) |
| Memory | 128 GB DDR5-4800 ECC RDIMM |
| OS Disk | NVMe SSD 1 TB |
| VM Disk(s) | SAS HDD x4 16 TB |
| 1–2 Gb NICs | 2 |
| 10 Gb NICs | 4 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 25.6, 'w': 17.2, 'h': 1.7} |
| Power Draw (W) | Idle 95 / Max 250 |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI with BMC (AST2600) |
| Supported OS | Proxmox VE, Ubuntu 24.04 LTS, Ceph |
| Price (USD) | 5199 |

 --- 



# Switches
