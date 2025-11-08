

# Technology Selection
_Design and Implementation Blueprint for the Clear Skies Architecture_

This section details the specific technologies, configurations, and open-source components recommended for each layer and tier of the Clear Skies architecture.  
Selections emphasize **resilience**, **local autonomy**, and **open interoperability** across all deployment scales.

---

## Layer 0 — Hardware Foundations

### Tier 1 — Camp Site
*Portable / Training-Scale Deployment*
- Example hardware platforms (NUC, MiniPC, low-power servers)
- Typical storage configuration (ZFS mirror, 1 GbE)
- Lightweight Proxmox or single-node SDDC
- Local UPS / Power considerations

### Tier 2 — Village Site
*Community-Scale Deployment*
- Cluster of 3 × MiniPC/Protectli-class nodes
- Ceph or ZFS-replicated storage
- Dual OPNsense firewall HA pair
- Local PoE switch with VLAN segmentation
- External backup (USB or second site)



![Zero Single Point of Failure SDDC](lib/diag/SDDC.excalidraw.png)

### Tier 3 — Regional Site
*Federated Multi-Community Hub*
- Enterprise-grade rackmount servers (ECC RAM, redundant PSU)
- 10 GbE backplane networking
- Dedicated Ceph cluster
- Multi-site replication and Tailscale/Headscale federation

---

## Layer 1 — Cyberinfrastructure (CI)
- Virtualization Platform: **Proxmox VE / KVM**
- Networking Stack: **OPNsense**, **FRR**, VLAN trunking
- Storage: **Ceph**, **ZFS**, **Restic/Borg**
- Identity: **Keycloak**, **Smallstep CA**
- Monitoring: **Prometheus**, **Grafana**, **Loki**, **Wazuh**
- Configuration: **Ansible** or **Chef**

---

## Layer 2 — Local Services
- OT/SCADA: **Rapid SCADA**, **OpenPLC**, **Ignition Edge**
- IIoT: **Mosquitto (MQTT)**, **Node-RED**, **Grafana**, **LoRaWAN**
- Comms: **Matrix (Synapse)**, **Jitsi**, **Rocket.Chat**
- Cybersecurity: **Zeek**, **Suricata**, **Wazuh**, **Elastic**
- Education / Research: **JupyterHub**, **Docker / LXC Sandboxes**
- Data: **PostgreSQL**, **GeoServer**, **Nextcloud**


### Industrial Internet of Thing (IIoT)

![IIoT](lib/diag/IIoT_Architecture.excalidraw.png)

---

## Layer 3 — Community Connections
- Secure Networking: **Tailscale / Headscale (ZTNA Mesh)**
- Federation: **Keycloak Federation**, **Smallstep cross-trust**
- Data Sync: **Syncthing**, **rsync**, **MinIO Gateway**
- Shared Visualization: **Grafana Federation**, **Kibana Dashboards**
- Optional: Integration with **FirstNet**, **Starlink**, or terrestrial backhaul for redundancy




