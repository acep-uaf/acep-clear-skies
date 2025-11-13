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


## Server Comparison

::: {.table-scriptsize}
\scriptsize
| Product | CPU (Make + Cores) | RAM (GB) | OS Disk | VM Disk(s) | 1–2 Gb NICs | 10 Gb NICs | Rack (U) | Power (W max) | Price (USD) |
|:--|:--|:--:|:--|:--|:--:|:--:|:--:|:--:|:--:|
| Qotom Q30900GE S13 Series | Intel 8th/10th Gen (2C) | 32 | 2.5-inch SATA SSD/HDD 0 TB | Mini PCIe mSATA SSD x1 0 TB; M.2 Wi-Fi E-Key (2230) x1 0 TB | 8 | 0 | 1U | 30 | $489 |
| MINIS FORUM MS-A2 | AMD Ryzen 9 9955HX (16C) | 96 | M.2 2280/U.2 NVMe SSD 2 TB | M.2 2280/22110 NVMe SSD x1 0 TB | 2 | 2 | 2U (approx.) | 130 | $1495.9 |
| Protectli VP6630 | Intel Core i3 (4C) | 96 | NVMe SSD 4 TB | SATA SSD x1 1 TB | 6 | 2 | 1U | 40 | $1651 |
| Protectli VP6650 | Intel Core i5 (4C) | 96 | NVMe SSD 4 TB | SATA SSD x1 1 TB | 6 | 2 | 1U | 45 | $1811 |
| MINIS FORUM MS-S1 Max | AMD Ryzen (16C) | 128 | NVMe SSD 2 TB | – | 0 | 2 | 2U | 130 | $2503.9 |
| Lancelot 1199-SR | Intel Xeon (8C) | 128 | NVMe SSD 1 TB | SAS HDD x4 16 TB | 2 | 4 | 1U | 250 | $5199 |
| ProLiant DL145 Gen11 | AMD EPYC 8124P (16C) | 128 | SATA SSD 0.96 TB | SATA SSD x1 3.84 TB | 2 | 0 | 1U | 350 | $11250.0 |
| Lancelot 1898-N12 | Intel Xeon Silver 4514Y (32C) | 256 | NVMe SSD 1.0 TB | NVMe SSD x2 15.36 TB | 0 | 6 | 1U | 600 | $11727.0 |
| ProLiant DL325 Gen11 | AMD EPYC 9124 (16C) | 128 | SATA SSD 3.84 TB | SATA SSD x2 – TB | 2 | 0 | 1U | 400 | $16231.82 |
| PowerEdge R6615 | AMD EPYC 9224 (24C) | 96 | SATA SSD 0.96 TB | SATA SSD x4 3.84 TB | 2 | 2 | 1U | 450 | $19401.16 |
| ASRock Jupiter X600 (35W) | AMD Ryzen 9000/8000/7000 Series (AM5) (–C) | 96 | M.2 2280 NVMe SSD 0 TB | SATA 2.5-inch HDD/SSD x1 0 TB | 2 | 0 | 1U (approx.) | – | – |
:::
\small


## Server Specifications


### Qotom Q30900GE S13 Series

![Qotom Q30900GE S13 Series](lib/img/Qotom_Q30900se-s13.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel 8th/10th Gen (2 cores, 4 threads) |
| Memory | 32 GB DDR4 SO-DIMM 2133/2400 MHz |
| OS Disk | 2.5-inch SATA SSD/HDD 0 TB |
| VM Disk(s) | Mini PCIe mSATA SSD x1 0 TB; M.2 Wi-Fi E-Key (2230) x1 0 TB |
| 1–2 Gb NICs | 8 |
| 10 Gb NICs | 0 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 7.7, 'w': 4.8, 'h': 1.9} |
| Power Draw (W) | Idle 10 / Max 30 |
| Power Input | DC 12 V Jack (5.5 mm × 2.5 mm) |
| Management | BMC: False, BIOS: UEFI |
| Supported OS | Windows 10, Linux (Ubuntu 24.04 LTS, Proxmox VE, OPNsense) |
| Price (USD) | $489 |
| Product Page | [Link](https://www.qotom.net/product/MiniPC_Q30900SE_S13_Series.html) |




### MINIS FORUM MS-A2

![MINIS FORUM MS-A2](lib/img/Minisforum_MS-A2.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD Ryzen 9 9955HX (16 cores, 32 threads) |
| Memory | 96 GB DDR5 SO-DIMM 5600 MHz |
| OS Disk | M.2 2280/U.2 NVMe SSD 2 TB |
| VM Disk(s) | M.2 2280/22110 NVMe SSD x1 0 TB |
| 1–2 Gb NICs | 2 |
| 10 Gb NICs | 2 |
| Rack Units | 2U (approx.) |
| Dimensions (in) | {'l': 7.7, 'w': 7.4, 'h': 1.9} |
| Power Draw (W) | Idle 35 / Max 130 |
| Power Input | DC 19V/12.63A Adapter |
| Management | BMC: False, BIOS: UEFI Secure Boot |
| Supported OS | Windows 11, Linux (Ubuntu 24.04 LTS, Proxmox VE) |
| Price (USD) | $1495.9 |
| Product Page | [Link](https://store.minisforum.com/products/minisforum-ms-a2?variant=46843404943605) |




### Protectli VP6630

![Protectli VP6630](lib/img/Protectli_VP6630.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Core i3 (4 cores, 8 threads) |
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
| Price (USD) | $1651 |
| Product Page | [Link](https://protectli.com/product/vp6630/) |




### Protectli VP6650

![Protectli VP6650](lib/img/Protectli_VP6650.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Core i5 (4 cores, 8 threads) |
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
| Price (USD) | $1811 |
| Product Page | [Link](https://protectli.com/product/vp6650/) |




### MINIS FORUM MS-S1 Max

![MINIS FORUM MS-S1 Max](lib/img/Minisforum_MS-S1-Max.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD Ryzen (16 cores, 32 threads) |
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
| Price (USD) | $2503.9 |
| Product Page | [Link](https://store.minisforum.com/products/minisforum-ms-s1-max-mini-pc) |




### Lancelot 1199-SR

![Lancelot 1199-SR](lib/img/ASL_Lancelot_1199SR.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Xeon (8 cores, 16 threads) |
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
| Price (USD) | $5199 |
| Product Page | [Link](https://www.aslab.com/products/rackmount/customize/lancelot1199sr.cgi) |




### ProLiant DL145 Gen11

![ProLiant DL145 Gen11](lib/img/HP_ProLiant_DL145_Gen11.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD EPYC 8124P (16 cores, 32 threads) |
| Memory | 128 GB DDR5-4800 ECC Registered (HPE SmartMemory) |
| OS Disk | SATA SSD 0.96 TB |
| VM Disk(s) | SATA SSD x1 3.84 TB |
| 1–2 Gb NICs | 2 |
| 10 Gb NICs | 0 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 27.5, 'w': 17.5, 'h': 1.7} |
| Power Draw (W) | Idle 95 / Max 350 |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI / iLO 6 |
| Supported OS | Proxmox VE, Ubuntu 24.04 LTS, Red Hat Enterprise Linux 9, Windows Server 2025 |
| Price (USD) | $11250.0 |
| Product Page | [Link](https://buy.hpe.com/us/en/compute/rack-servers/proliant-dl100-servers/proliant-dl145-server/hpe-proliant-dl145-gen11/p/1014845266) |




### Lancelot 1898-N12

![Lancelot 1898-N12](lib/img/ASL_Lancelot_1898-N12.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | Intel Xeon Silver 4514Y (32 cores, 64 threads) |
| Memory | 256 GB DDR5-4800 ECC Registered |
| OS Disk | NVMe SSD 1.0 TB |
| VM Disk(s) | NVMe SSD x2 15.36 TB |
| 1–2 Gb NICs | 0 |
| 10 Gb NICs | 6 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 28.0, 'w': 17.6, 'h': 3.4} |
| Power Draw (W) | Idle 180 / Max 600 |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI / ASPEED AST2600 |
| Supported OS | Rocky Linux 8.10, Red Hat Enterprise Linux 8.10, Ubuntu 24.04 LTS, Proxmox VE 8 |
| Price (USD) | $11727.0 |
| Product Page | [Link](https://www.asus.com/Server-Workstation/Servers/1U-2U-Rack-Servers/RS700-E11-RS12U/) |




### ProLiant DL325 Gen11

![ProLiant DL325 Gen11](lib/img/HP_ProLiant_DL235_Gen11.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD EPYC 9124 (16 cores, 32 threads) |
| Memory | 128 GB DDR5-4800 ECC Registered (HPE SmartMemory) |
| OS Disk | SATA SSD 3.84 TB |
| VM Disk(s) | SATA SSD x2 – TB |
| 1–2 Gb NICs | 2 |
| 10 Gb NICs | 0 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 28.0, 'w': 17.5, 'h': 1.7} |
| Power Draw (W) | Idle 110 / Max 400 |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI / iLO 6 |
| Supported OS | Proxmox VE, Ubuntu 24.04 LTS, Red Hat Enterprise Linux 9, Windows Server 2025 |
| Price (USD) | $16231.82 |
| Product Page | [Link](https://buy.hpe.com/us/en/compute/rack-servers/proliant-dl300-servers/proliant-dl325-server/hpe-proliant-dl325-gen11/p/1014689141) |




### PowerEdge R6615

![PowerEdge R6615](lib/img/Dell_PowerEdge_R6615.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD EPYC 9224 (24 cores, 48 threads) |
| Memory | 96 GB DDR5-5600 ECC RDIMM |
| OS Disk | SATA SSD 0.96 TB |
| VM Disk(s) | SATA SSD x4 3.84 TB |
| 1–2 Gb NICs | 2 |
| 10 Gb NICs | 2 |
| Rack Units | 1U |
| Dimensions (in) | {'l': 28.0, 'w': 17.1, 'h': 1.7} |
| Power Draw (W) | Idle 120 / Max 450 |
| Power Input | AC 100–240V |
| Management | BMC: True, BIOS: UEFI / iDRAC9 Express 16G |
| Supported OS | Proxmox VE, Ubuntu Server 24.04 LTS, Red Hat Enterprise Linux 9, Windows Server 2025 |
| Price (USD) | $19401.16 |
| Product Page | [Link](https://www.dell.com/en-us/shop/cty/pdp/spd/poweredge-r6615/pe_r6615_tm_vi_vp_sb?configurationid=1759700b-2877-411f-bf22-461cea367d8e) |




### ASRock Jupiter X600 (35W)

![ASRock Jupiter X600 (35W)](lib/img/ASRock_Jupiter-X600.jpg)


**Specifications**

| Spec | Value |
|:--|:--|
| CPU | AMD Ryzen 9000/8000/7000 Series (AM5) (– cores, – threads) |
| Memory | 96 GB DDR5 SO-DIMM 6400+(OC)MHz |
| OS Disk | M.2 2280 NVMe SSD 0 TB |
| VM Disk(s) | SATA 2.5-inch HDD/SSD x1 0 TB |
| 1–2 Gb NICs | 2 |
| 10 Gb NICs | 0 |
| Rack Units | 1U (approx.) |
| Dimensions (in) | {'l': 7.05, 'w': 7.01, 'h': 1.34} |
| Power Draw (W) | Idle – / Max – |
| Power Input | DC 19V Adapter |
| Management | BMC: False, BIOS: UEFI BIOS |
| Supported OS | Windows 10 64-bit, Windows 11 64-bit, Linux (Ubuntu compatible) |
| Price (USD) | $– |
| Product Page | [Link](https://www.asrock.com/nettop/AMD/Jupiter%20X600/index.us.asp) |


