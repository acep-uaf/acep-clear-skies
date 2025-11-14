# Introduction

### Vision Statement

**Clear Skies** is a locally grown initiative to build **community-owned, cloud-free digital infrastructure** across rural Alaskan microgrid communities.  It empowers rurual communities to host and secure their own data, communications, and operational systems right where they live and work without reliance on distant cloud services.

By bringing computing power, cybersecurity, and communications back under local control, **Clear Skies** advances *digital sovereignty* as as a modern expression of community self-determination while strengthening self-reliance and resiliency, ensuring continuity during network outages, and creates a foundation for innovation that reflects Alaska’s values of **independence, stewardship**, and **cooperation**.

The Clear Skies reference architecture can be implemented in scalable layers, from physical infrastructure to regional collaboration, and can be used for a wide range of application use cases from test beds and training grounds to power plant networks and emergency communication systems.

## Problem Statement

Alaska has the worlds highest concentration of island-ed micro-grids in the world.   The remote communities are not connected by roads or transmission lines.  Most generate power primarily with diesel, and the fuel is expensive, especially if the community is not on a the coast or river systems where fuel can be barged in.  For those remote communities fuel must be flown in.

Internet access in these communities is also a constrained resource.   Some coastal communities have access to high speed fiber optic connections, while others have been limited to expensive geosynchronous satellite communications.  Though in 2 of the last  3 years, sea ice has cut burred cables resulting several month service outages.   Low earth orbit (LEO)[@LowEarthOrbit2025] satellite systems have be come available in recent years, however also carries the unaddressed risk of Kessler syndrome[@KesslerSyndrome2025], where a cascading collision of satellites starts a chain reaction leaving the entire LEO orbital space unusable for potentially centuries.

Rural Alaskan micro-grid communities range between less than a hundred to over 3000 people.  The energy utilities in these communities are commonly operated by a handful of individuals.  Staffing rural utilities is a challenging balance between keeping energy costs low and attracting skilled workers.

For much of the United States, the Federal Energy Regulatory Commission (FERC)[@HomePageFederal] is the regulator agency that governs energy utilities in the U.S.   FERC mandates that energy utilities in the United States to follow the North American Electric Reliability Corporation (NERC)[@NERC] Critical Infrastructure Protection (CIP)[@ReliabilityStandards] standards in regards to cybersecurity compliance for energy utilities Operational Technology networks.  However compliance criteria are based largely on transmission capabilities.   Because no utility in Alaska is connected to the lower 48 power grid, Alaska utilities have been effectively exempt from cybersecurity regulation.  Recently the Railbelt Reliability Council (RRC)[@AlaskaRailbeltReliability2025] has drafted a set of modified CIP standards[@CIPCriticalInfrastructure2025] for the State of Alaska which are based on the NERC CIP standards but tuned to accommodate Alaskan specific criteria.  Once adopted by the Regulatory Commission of Alaska (RCA)[@RegulatoryCommissionAlaska] the RRC CIP standards are expected to become a regulator compliance requirement for those Alaskan power producer connected to the Railbelt energy grid.

While the RRC CIP standards address the comprehensive scope of risks for critical energy infrastructure, rural islanded Alaskan microgrids will remain largely exempt from compliance because they do not meet the transmission criteria.   Additionally meeting cybersecurity standards would represent a significant cost to rural communities already struggling with the cost of energy.   Not only would these communities need to pay for expensive cybersecurity expertise, but would likely mean expensive upgrades to existing network equipment.
