### Design Review Notes for Project PJCA007334 - VILLE DE SHERBROOKE DANSE ET THEATRE

Here are a few points identified during the design review that may warrant further attention or clarification. These are not necessarily "problems" but are areas that could be sources of questions or require coordination during implementation.

### 1. Discrepancies in the "Excedent" (Surplus) Section

The drawing `AV2006 (EXCÉDENT)` highlights a difference between the number of devices specified in the Bill of Materials (BOM) and the number shown on the drawings. This could indicate planned spares or items that have not yet been assigned a location.

*   **Volume Controllers (`CV2-`):** The BOM calls for 3, but only 1 is in the drawings.
*   **Pendant Speakers (`HP3-10`):** The BOM calls for 10, but only 9 are in the drawings.
*   **Wall Plate (`PL-`):** The BOM calls for 2, but only 1 is in the drawings.

**Potential Issue:** This could lead to confusion for the installation team regarding whether these are spare parts or if they are missing from the installation plans. Clarification on the intended use/location of these "surplus" items is recommended.

### 2. Undefined Device Placement

In the `APPAREILS MOBILES` (Mobile Devices) section (drawing `AV2005`), the Wi-Fi access points (`AP1-01`, `AP1-02`) are marked with: *"EMPLACEMENT ET CONNEXION À DÉTERMINER SUR PLACE"* (Location and connection to be determined on-site).

**Potential Issue:** Leaving the final placement of Wi-Fi access points to be decided on-site can be risky. A proper Wi-Fi survey is usually recommended to ensure optimal coverage, and not defining this in the plan could lead to poor performance or installation delays. It is advisable to conduct a site survey and finalize these locations in the design documents.

### 3. Client-Supplied Equipment

Several key components are marked as *"PAR CLIENT"* (Client Supplied), including:

*   `OFE.BS1-01`: ClearCom Master Intercom Station in the main server rack.
*   `OFE.PC1-01`: An operator computer in the Régie (Control Room).

**Potential Issue:** This is a coordination point rather than a design flaw. It's critical to ensure that the exact models provided by the client are fully compatible with the rest of the system (e.g., correct connectors, software versions, power requirements) and that they are available on-site at the required time. Detailed specifications from the client for these items should be obtained and verified against the system's requirements.

### 4. "Future" Use Connections

On the lighting console (`LXMIX1-01`) in the Régie, the audio and mic inputs are marked as *"(FUTURE)"*.

**Note:** This is not a problem but clarifies that this functionality is not part of the current scope of work, though the capability is present for future expansion. This is a good practice for indicating potential upgrade paths.
