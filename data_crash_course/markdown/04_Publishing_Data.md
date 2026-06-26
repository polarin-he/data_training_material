# How to publish your POLARIN TA data?
<style>
.info-box {
    background-color: rgba(128, 128, 128, 0.1);
    border-left: 4px solid rgba(128, 128, 128, 0.25);
    padding: 10px;
    margin: 10px 0;
    border-radius: 4px;
    font-family: monospace;
    font-size: 0.9em;
    color: #333;
}
</style>

<div class="info-box">

**Audience level: Beginner**

**Estimated reading time: 15 minutes**

**Contributor: Daan Kivits (SIOS-KC)**

**Date created: 19-06-2026**

**Date last modified: 22-06-2026**

**License: [GNU GENERAL PUBLIC LICENSE Version 3 (AGPLv3)](https://www.gnu.org/licenses/gpl-3.0.html)** </div>

This notebook explains how to publish your POLARIN TA data in trusted repositories while following **Open Science principles**, all whilst maximizing compliance with the FAIR (Findable, Accessible, Interoperable, Reusable) and CARE (Collective Benefit, Authority to Control, Responsibility, Ethics) data principles. It provides strategies on **where to publish** and **licensing** for maximum reuse and impact.


---

### Learning Objectives
By the end of this notebook, you will:
- Understand the (requirements posed by) **Open Science principles** adopted by Horizon Europe (and therefore also POLARIN)
- Understand **where to publish your POLARIN TA** data in trusted repositories.
- Learn how to **attach a clear data license** to enable reuse.
- Know how to **request an embargo period** if your data needs temporary privacy.

#### Prerequisites
- Completion of **[Notebook 3: Structuring Data](./03_Structuring_Data.ipynb)**
- (Optional but recommended) Access to a **dataset** you want to publish
- (Optional but recommended) Completion of **[Notebook 1: Introduction to FAIR Principles](./01_FAIR.ipynb)** and **[Notebook 2: FAIR is not enough: CARE as an extension to FAIR](./02_CARE.ipynb)**.

---

## 🔍 Where and how to publish your POLARIN TA data?
Before publishing your POLARIN TA data, ensure that:

- your research data is compliant with the **FAIR (Findable, Accessible, Interoperable, Reusable)** and **CARE (Collective Benefit, Authority to Control, Responsibility, and Ethics)** data principles, as much as possible. For guidance on the FAIR data principles, see [this notebook](../data_crash_course/01_FAIR.ipynb) and for guidance on the CARE principles, see [this notebook](../data_crash_course/02_CARE.ipynb).
- your research data is accompanied with **rich metadata**, both in the discovery and use metadata, using metadata standards and controlled vocabularies where possible. For guidance on metadata, see [this notebook](../data_crash_course/03_Structuring_Data.ipynb).

## 🌍 Open Science principles
Open Science aims to make scientific research and its outputs  (publications, research data, methods, and tools) openly accessible, reusable, and collaborative to maximize societal and economic benefits ([Publications Office of the European Union, 2024](https://op.europa.eu/s/Aisq)). Since POLARIN is a Horizon Europe project, it is committed to these **Open Science** principles.

To comply with this rule, you are required to (within the limits of "as open as possible, as closed as necessary"):
- publish your publications and research data used in your publications according to the principle of **"as open as possible, as closed as necessary"**. In practice, this means that you should deposit your data in a **trusted repository** (e.g., CoreTrustSeal, Nestor Seal, ISO 16363, Zenodo, or disciplinary repositories) and make sure they are **openly accessible to anyone**. We have provided a list of recommended repositories for POLARIN data in [this section](#what-data-repository-should-i-publish-my-data-to). 
- provide **detailed descriptions** of the research outputs needed to replicate and validate the conclusions of scientific publications or to validate or re-use research data (e.g., how to access, analyse, versioning, required dependencies, etc.).
- develop and continuously update a Data Management Plan (DMP) and ensure responsible management of research data in line with the FAIR (and CARE) principles in your research projects (see [the last notebook](../data_crash_course/03_Structuring_Data.ipynb) for guidance on DMPs, and [this](../data_crash_course/01_FAIR.ipynb) and [this](../data_crash_course/02_CARE.ipynb) notebook for guidance on FAIR and CARE, respectively).
- comply with any additional requirements stated in the Grant Agreement of your project or work programme. POLARIN only enforces the two requirements above, but this may differ for other projects or work programmes. Always check the Grant Agreement of your project or work programme for any additional requirements.

On top of that, the EU recommends to adopt the following best practices: 
- attach **an open license** (e.g., CC-BY 4.0, CC0, or equivalent) to your research data to enable and maximize reusability. See [this section](#data-licensing) for more information on data licensing.
- share any research outputs **early and open** with the wider scientific community.
- provide **open access to research outputs beyond publications and raw research data**, such as auxiliary data, software, algorithms, code, protocols, models, workflows, or electronic notebooks. See [this section](#what-other-repository-should-i-use) for guidance on where to publish such research outputs.
- involve **citizens, civil society, and end-users** in the collaborative collection, processing, and analysis of research data (i.e., citizen science).
- participate in **open peer-review** .

<div style="
    background-color: rgba(255, 165, 0, 0.2);
    border-left: 4px solid rgba(255, 165, 0, 0.5);
    width: 95%;
    padding: 10px;
    margin: 10px 0;
    border-radius: 4px;
">
NOTE: According to Horizon Europe (and therefore also POLARIN TA), data may be closed under certain conditions:

- It conflicts with **legitimate interests** (e.g., commercial exploitation, patent applications). Horizon Europe rules state that **intellectual property protection comes before open science obligations** when protection and exploitation of project results would be adversely affected by making project results and data available in open access.
- It involves **personal data** (unless anonymized or explicit consent is given).
- It violates **Union competitive interests, security rules, or other Grant Agreement obligations**. </div>

## ⏳ Embargo period
If your POLARIN TA data is **not yet ready for public release**, you can request an **embargo period** from the data center where you will publish your data. This allows you to **keep your data private for a certain period of time** before it becomes publicly available. POLARIN allows an embargo on TA data anywhere between 6 up to 24 months, depending on the needs of the researcher. However, since not every data center handles embargo requests, always check with the data center for their specific embargo possibilities and policies.

Under Horizon Europe law, all metadata of published data must be made openly available as soon as possible under a machine-readable format under a Creative Common Public Domain Dedication ([CC0](https://creativecommons.org/public-domain/#cc0)) or equivalent, regardless of any embargo period on the data it describes. This means that even if your data is under embargo, the metadata must be publicly available.

## 📜 <a id='data-licensing'></a> Data Licensing
Attaching a data license in POLARIN is like adding a clear rulebook to your dataset. It tells others exactly how they can use, share, or build upon your work—removing guesswork and legal uncertainty. Without a license, your data is automatically locked down, which goes against Horizon Europe’s (POLARIN's) Open Science principles and open and collaborative spirit.

A license enables the reuse of our data, i.e. the inclusion of a license makes your data legally interoperable. It also allows for integrating your data into data services, such as the POLARIN Data Hub. By choosing a **open license** (e.g., CC-BY 4.0, CC0, or equivalent) you encourage collaboration, maximize your data’s impact, and meet ethical and funding requirements, all while keeping things simple and transparent for everyone.

## 📁 <a id='what-data-repository-should-i-publish-my-data-to'></a> What repository should I publish my TA data and other research outputs to? 📄
   Publish your data in a **openly accessible, trusted repository** that matches both the scientific domain and study area of your data. Preferably, choose a (meta)data repository that is a part of the POLARIN consortium, i.e. one of the following:

<div style="max-width: 1080px;">

 **Type of (meta)data**                     | **Study area**       | **(Meta)data repository**                                                                                                                                                                                                                      | **FAIRness level of platform** | **Notes**                                                                                                                                                                                                                                
--------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Biodiversity and ecology                   | Arctic               | [ABDS (Arctic Biodiversity Data Service)](https://www.abds.is/index.php/partners/contribute-data) (CAFF)                                                                                                                                       | High                           | Suitable for aggregated biodiversity and ecology data products, has a simple (meta)data publication tool                                                                                                                                 
 Geophysics                                 | Arctic               | [IADC (Italian Arctic Data Center)](https://www.programmaricercaartico.it/en/node/21) (CNR)                                                                                                                                                    | High                           | Suitable for any type of geophysical (meta)data from the Arctic region; unsupervised (meta)data publication not supported, contact [protocollo.isp@pec.cnr.it](mailto:protocollo.isp@pec.cnr.it) to learn more about data publication    
 Geophysics                                 | Antarctic            | NADC (National Antarctic Data Center) (CNR) [data repository (ERDDAP)](https://antarcticdatacenter.cnr.it/erddap/index.html) or [metadata repository (GeoNetwork)](https://antarcticdatacenter.cnr.it/geonetwork/srv/eng/catalog.search#/home) | High                           | Suitable for any type of geophysical (meta)data from the Antarctic region; unsupervised (meta)data publication not supported, contact [protocollo.isp@pec.cnr.it](mailto:protocollo.isp@pec.cnr.it) to learn more about data publication 
 Seismology                                 | Arctic and Antarctic | [POlar SEismic Data Access (POSEDA)](https://geofon.gfz.de/contribute/) (GEOFON/GFZ)                                                                                                                                                           | High                           | Suitable for seismological (meta)data from both polar regions; more information on publishing (meta)data given on the website                                                                                                            
 Geophysics, biodiversity and ecology       | Svalbard             | [SIOS Data Management System (SDMS)](https://sios-svalbard.org/DataSubmission) (SIOS)                                                                                                                                                          | High                           | Suitable for any geophysical, biodiversity and ecology (meta)data from the greater Svalbard region; provides simple (meta)data publication form on the website                                                                           
 Geophysics, biodiversity and ecology       | Arctic               | [Arctic Data Center (ADC)](https://adc.met.no/how-deposit-data) (MET Norway)                                                                                                                                                                   | High                           | Suitable for any geophysical, biodiversity and ecology (meta)data from the Arctic region; need to request a (meta)data publication account                                                                                               
 Documentation, code and analysis workflows | Any                  | [GitHub](https://github.com/)                                                                                                                                                                                                                  | High                           | Suitable for any research output other than data; promotes collaboration and reproducibility                                                                                                                                             
 Any                                        | Arctic and Antarctic | [POLARIN Zenodo Community](https://zenodo.org/communities/eu-polarin/records?q=&l=list&p=1&s=10&sort=newest)                                                                                                                                   | Low                            | Generalist repository, prioritize other repositories to allow your data to be more FAIR;                                                                                                                                                 
 Any                                        | Arctic and Antarctic | [POLARIN GeoNetwork](https://geonetwork.s4polarin.eu/geonetwork/srv/eng/catalog.search)                                                                                                                                                        | Low                            | Generalist repository, prioritize other repositories to allow your data to be more FAIR;                                                                                                                                                 
 Any                                        | Arctic and Antarctic | [POLARIN ERDDAP](https://erddap.s4polarin.eu/erddap/index.html)                                                                                                                                                                                | Low                            | Generalist repository, prioritize other repositories to allow your data to be more FAIR;                                                                                                                                                 

</div>

**⚠️ Important**: Always **discuss publication with the data center** to ensure compliance with their requirements.

---

#### References
European Commission: European Innovation Council and SMEs Executive Agency, European IP helpdesk – Your guide to open science in Horizon Europe, Publications Office of the European Union, 2024, https://data.europa.eu/doi/10.2826/943044

#### Find additional data stewardship training resources in the POLARIN Training Resources Database!
POLARIN has prepared a comprehensive list of training resources on data stewardship, covering the entire data lifetime cycle: from data collection, to transformation, curation, analysis, publication, and more. You can find the POLARIN Training Resources Database [here](https://docs.google.com/spreadsheets/d/1ny4goRAzt8Aj-uqvES-k1lRfJwxhZ0Fb/edit?usp=sharing&ouid=113232285459718566773&rtpof=true&sd=true). Feel free to contribute to the database by adding your own resources, or by suggesting new resources to be added.

> NOTE: Be sure to navigate to the second sheet to view the data stewardship resources! 

#### License
This notebook is licensed under [AGPLv3](https://www.gnu.org/licenses/gpl-3.0.html). You are free to use, adapt, and share it, provided you attribute POLARIN and release derivatives under the same license.

**Attribution**:
> Developed as part of the POLARIN project (Grant Agreement No. 101130949).
