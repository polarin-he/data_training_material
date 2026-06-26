# How to use the POLARIN Data Hub?
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

**Estimated reading time: 20 minutes**

**Contributor: Rachele Bordoni (ETT)**

**Date created: 27-05-2026**

**Date last modified: 09-06-2026**

**License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)** </div>

This notebook gives you a practical overview of the [POLARIN Data Hub](https://s4polarin.eu/) and its main tools. By the end, you will know where to find polar datasets, how to explore them visually, and how to understand the Virtual Access framework that makes this data openly available.

---

#### Learning objectives
By the end of this notebook, you will:
1. Understand the purpose and structure of the POLARIN Data Hub.
2. Know how to navigate the main sections of the Data Hub.
3. Be able to find a dataset, explore it on the map, and understand how to cite it correctly.

#### Prerequisites
- No programming knowledge required — this notebook is descriptive and navigational.
- A web browser and internet access.
- ((Optional but recommended)) Familiarity with basic concepts of FAIR data principles.

---

## 1. What is the POLARIN Data Hub?
The [POLARIN Data Hub](https://s4polarin.eu/) is the central entry point for discovering and accessing polar research data from across the POLARIN network. It aggregates datasets, metadata, and data services from multiple international polar Research Infrastructures (RIs) into a single, unified portal — making polar data more findable, accessible, and reusable for scientists, data stewards, and stakeholders. The Data Hub was developed as part of the POLARIN project, funded by the EU Horizon Europe programme (Grant Agreement No. 101130949).

The Data Hub aims to bring together:
- **research stations** in both the Arctic and Antarctic
- **research vessels**
- **data infrastructures**
- **core reporitories**

Data is served through a **semantically consistent and standardized metadata catalogue**, making it easier to search, compare, and reuse data across different sources and disciplines.

The Data Hub is publicly accessible — no login or application is needed to browse and download data.

**The main menu of the Data Hub includes the following sections:**

| Menu Item | What it does |
|---|---|
| Research Infrastructures | Directory of all POLARIN RIs, with links to their websites and a shortcut to filter the Data Selection by RI |
| Virtual Access | Description of the open data access framework |
| Data Selection | Search and filter datasets in the catalog |
| Data Viewer | Visualize data coverage on an interactive map |
| POLARIN PROMPT | AI-powered interface to query polar data |
| Reanalysis & Plots | Pre-built dashboards for reanalysis data |
| Data Cookbook | Interactive Jupyter Book with data analysis examples |
| POLARIN Zenodo Community | Open repository of published POLARIN datasets |
| GitHub | Code and notebooks from the POLARIN community |

---
## 2. Research Infrastructures

**Explanation**:
The [Research Infrastructures](https://s4polarin.eu/research-infrastructures/) section provides a **list** of all polar RIs connected to the POLARIN network. This includes Arctic and Antarctic research stations, research vessels and icebreakers, observatories, and data repositories.

Each RI is listed with a brief description and a link to its **own website**, where you can find more detailed information about its scientific mandate, location, facilities, and data holdings.

**How to use it**:
1. Go to [https://s4polarin.eu/research-infrastructures/](https://s4polarin.eu/research-infrastructures/)
2. Browse the list of RIs to familiarize yourself with the POLARIN network.
3. Click the **external link** next to any RI to visit its dedicated website for more information.
4. Click the **magnifying glass icon** (🔍) next to any RI to jump directly to the Data Selection pre-filtered for that RI — a quick shortcut to see all datasets contributed by that specific infrastructure.

**Why it matters for data stewardship**:
knowing which RI produced a dataset helps you correctly acknowledge the data source and understand its geographic and thematic scope — both of which are essential for proper data citation and reuse.

---
## 3. Virtual Access: open polar data for everyone

**Explanation**:
in the context of POLARIN, [Virtual Access](https://s4polarin.eu/virtual-access/) (VA) refers to the provision of user-friendly, free of charge, and open online access to services provided by polar RIs — including scientific data, metadata, and data services.

VA is openly available to **all users without a selection process**. It enables researchers, policymakers, and stakeholders by providing evidence-based information for sustainable management of polar environments, particularly in the context of climate change and human activity impacts.

POLARIN supports VA by connecting data, metadata, data services, and data products from multiple polar RI through the **POLARIN metadata catalogue**. This catalogue provides access to diverse (meta)data sources in a semantically consistent and interoperable manner, and serves them in a way that is compatible with various metadata standards and exchange protocols. The technical and operational work required to host, curate, maintain, and deliver these resources ensures that they remain discoverable, reliable, and usable throughout the project lifetime.

> ⚠️ **By definition, the POLARIN metadata catalogue the only catalogue that stores POLARIN VA data.** If a dataset from a POLARIN RI is not exposed through the catalogue, it does not count as VA and therefore POLARIN cannot ensure the discoverability of these data through the Data Hub.

All datasets and services provided through VA are integrated into the POLARIN metadata catalogue and exposed through the POLARIN Data Hub in line with **FAIR principles**. In practice, POLARIN VA enforces data integration at the **discovery level**: all VA datasets are Findable, Accessible, and Reusable through the catalogue. Full Interoperability (the "I" in FAIR) is not enforced at this stage, given the varying levels of data architecture maturity across the participating RIs. This means that while you can always find and access VA data through the Data Hub, the format and structure of the underlying data may vary between datasets.

**How to cite POLARIN Virtual Access data**:

When using data provided through POLARIN Virtual Access, you must:
1. Provide the **dataset PID** (e.g., its DOI).
2. Acknowledge the **RI** that owns the data.
3. Include the following acknowledgement:

> *"This work used data provided through POLARIN Virtual Access under EU Horizon Europe Grant Agreement No. 101130949."*

⚠️ **Note**: Always check the individual dataset license for any additional requirements.

---
## 4. Data Selection
**Explanation**:
the [Data Selection](https://s4polarin.eu/data-catalog/) is the **main search interface** of the POLARIN Data Hub. It lets you browse and filter the unified metadata catalogue to find datasets from across the POLARIN network.

**How to use it**:
1. Go to [https://s4polarin.eu/data-catalog/](https://s4polarin.eu/data-catalog/)
2. Use the search bar or filters (by Research Infrastructure, Earth System, Location, etc.) to narrow down datasets.
3. Search for a dataset entry to view part of its metadata record — including title, description, Earth System, Research Infrastructure and access links.
4. Follow the dataset's DOI or access link to browse its full metadata record and access the data.

---
## 5. Data Viewer

**Explanation**:
the [Data Viewer](https://s4polarin.eu/data-coverage/data-viewer/) is an **interactive map-based tool** that lets you visually explore the spatial coverage of datasets available in the POLARIN network. It is particularly useful for quickly assessing which data is available in a given region, before committing to a download.

**How to use it**:
1. Go to [https://s4polarin.eu/data-coverage/data-viewer/](https://s4polarin.eu/data-coverage/data-viewer/)
2. Pan and zoom on the map to navigate to your area of interest or use the filters on the lateral menu.
3. Use the layer controls to toggle between different datasets.
4. Click on data points or to get more details, access the data and metadata and, whenever possible, plot the data.

**When to use the Data Viewer vs. the Data Selection**:

| Use case | Recommended tool |
|---|---|
| I want to **search for a specific dataset** by name or keyword | Data Selection |
| I want to **see what data is available** in a geographic area | Data Viewer |
| I want to **compare spatial coverage** of multiple datasets | Data Viewer |
| I need the **DOI or metadata** of a specific dataset | Data Selection & Data Viewer|

---
## 6. POLARIN PROMPT: AI-assisted data discovery

**Explanation**:
the [POLARIN PROMPT](https://bo.isp.cnr.it/llm-dashboard/) is an **AI-powered interface** (Large Language Model dashboard) that lets you query and explore POLARIN data using natural language — for example:

- *"What temperature datasets are available for the Svalbard region?"*
- *"Show me datasets with salinity measurements from Arctic research stations."*
- *"Which datasets cover the period 2018–2022 in the Southern Ocean?"*

**How to use it**:
1. Go to [https://bo.isp.cnr.it/llm-dashboard/](https://bo.isp.cnr.it/llm-dashboard/)
2. Type your question or data request in natural language in the chat interface.
3. The AI will interpret your query and return relevant dataset suggestions, metadata summaries, or direct links to data.
4. Use the results to identify datasets of interest, then access them via the Data Selection or POLARIN ERDDAP.

**When is POLARIN PROMPT most useful?**

| Scenario | POLARIN PROMPT |
|---|---|
| I'm not sure what data exists for my topic | ✅ Great starting point |
| I want to download data programmatically | 🔸 Can suggest datasets |
| I want to explore data interactively in natural language | ✅ Ideal |
| I need precise filtering by variable, time, location | 🔸 May need follow-up |

> ⚠️ **Note**: As with any AI tool, always verify the dataset information returned by POLARIN PROMPT against the official metadata records in the Data Selection before using the data in a publication.

---
## 7. Reanalysis & Plots: visual dashboards for polar data

**Explanation**:
the [Reanalysis & Plots](https://bo.isp.cnr.it/dashboard_polarin/) dashboard provides **pre-built interactive visualizations** of polar reanalysis data and observational products. This is a no-code tool — ideal for researchers who want to quickly explore atmospheric or oceanographic trends without writing any code.

**What you can do with it**:
- Visualize reanalysis fields (e.g., temperature, wind, sea ice) over polar regions.
- Compare different time periods or variables through interactive plots.
- Export figures for use in presentations or publications.

**How to use it**:
1. Go to [https://bo.isp.cnr.it/dashboard_polarin/](https://bo.isp.cnr.it/dashboard_polarin/)
2. Select the variable and geographic region of interest from the dashboard controls.
3. Adjust the time period and other parameters as needed.
4. Explore the interactive plot — hover for values, zoom, or pan.
5. Use the export/download button to save the figure.

> 💡 This tool is particularly useful for **quick overviews and context-setting** — e.g., to understand the climatological background before diving into station-level data via ERDDAP.

---
## 8. The POLARIN Data Cookbook

**Explanation**:
the [POLARIN Data Cookbook](https://s4polarin.eu/data-coverage/data_cookbook/intro.html) is an interactive **Jupyter Book** — a collection of annotated notebooks that demonstrate how to collect, access, and process polar ocean observations using POLARIN data and tools.

It is aimed at researchers who want ready-to-run, documented examples they can adapt for their own analyses.

**Current chapters**:

| Chapter | Topic | Link |
|---|---|---|
| 1 | POLARIN's ERDDAP querying: tabledap | [Open](https://s4polarin.eu/data-coverage/data_cookbook/chapters/chapter1/polarin_erddap_querying_tabledap.html) |
| 2 | Assessing Ocean Circulation, Carbon Uptake, and Environmental Changes | [Open](https://s4polarin.eu/data-coverage/data_cookbook/chapters/chapter2/polarin_bottles.html) |
| 3 | POLARIN's ERDDAP datasets distribution in time and space | [Open](https://s4polarin.eu/data-coverage/data_cookbook/chapters/chapter3/polarin_data_catalogue.html) |

**How to run the Cookbook notebooks**:

Option A — **Binder** (no installation required):
Each chapter has a Binder link at the top of the page. Click it to open and run the notebook directly in your browser.
Example: [Run Chapter 1 on Binder](https://mybinder.org/v2/gh/POLAR-RESEARCH-INFRASTRUCTURE-NETWORK/jupyter-notebooks/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks_binder%2Fpolarin_erddap_querying_tabledap.ipynb)

Option B — **Download and run locally**:
1. Go to the [POLARIN GitHub repository](https://github.com/POLAR-RESEARCH-INFRASTRUCTURE-NETWORK/jupyter-notebooks).
2. Clone or download the repository.
3. Install the required dependencies (see the repository README).
4. Open the notebooks in JupyterLab or Jupyter Notebook.

> 📌 The Cookbook source files (`.ipynb`) are also directly downloadable from each chapter page — look for the `.ipynb` download button at the top right of any chapter.

---
## 9. Additional Resources in the Data Hub

**Explanation**:
Beyond the core data discovery tools, the POLARIN Data Hub provides several additional resources worth knowing about:

- **[POLARIN Zenodo Community](https://zenodo.org/communities/eu-polarin/records)**: A curated collection of datasets published by POLARIN partners on Zenodo. All datasets here are open access and have a DOI.

- **[GitHub – POLARIN Community](https://github.com/POLAR-RESEARCH-INFRASTRUCTURE-NETWORK)**: The POLARIN GitHub organization hosts code, notebooks, and tools developed by the community — including the source notebooks for the Data Cookbook.


---
## Summary

In this notebook, you have learned:

✅ The POLARIN Data Hub ([s4polarin.eu](https://s4polarin.eu/)) is a single entry point to polar research data from across the POLARIN network.

✅ **Virtual Access** provides free, open, and publicly available data — no application needed.

✅ When using POLARIN VA data, always cite the dataset DOI, acknowledge the RI, and include the POLARIN grant acknowledgement.

✅ The **Data Selection** is the right tool to search for specific datasets by keyword, variable, or region.

✅ The **Data Viewer** lets you visually explore data coverage on an interactive map.

✅ **POLARIN PROMPT** ([bo.isp.cnr.it/llm-dashboard](https://bo.isp.cnr.it/llm-dashboard/)) — AI-powered interface for exploring data through natural language queries.

✅ **Reanalysis & Plots** ([bo.isp.cnr.it/dashboard_polarin](https://bo.isp.cnr.it/dashboard_polarin/)) — interactive no-code dashboard for visualizing polar reanalysis and observational data.

✅ **Data Cookbook** ([s4polarin.eu/data-coverage/data_cookbook](https://s4polarin.eu/data-coverage/data_cookbook/intro.html)) — a library of ready-to-run Jupyter notebooks with documented polar data analysis examples.


---

### Next steps
- Explore the [POLARIN Zenodo Community](https://zenodo.org/communities/eu-polarin/records) to browse published datasets.
- Check the [POLARIN GitHub](https://github.com/POLAR-RESEARCH-INFRASTRUCTURE-NETWORK) for community notebooks and code.

#### Find additional data stewardship training resources in the POLARIN Training Resources Database!
POLARIN has prepared a comprehensive list of training resources on data stewardship, covering the entire data lifetime cycle: from data collection, to transformation, curation, analysis, publication, and more. You can find the POLARIN Training Resources Database [here](https://docs.google.com/spreadsheets/d/1ny4goRAzt8Aj-uqvES-k1lRfJwxhZ0Fb/edit?usp=sharing&ouid=113232285459718566773&rtpof=true&sd=true). Feel free to contribute to the database by adding your own resources, or by suggesting new resources to be added.

> NOTE: Be sure to navigate to the second sheet to view the data stewardship resources! 

#### License
This notebook is licensed under [AGPLv3](https://www.gnu.org/licenses/gpl-3.0.html). You are free to use, adapt, and share it, provided you attribute POLARIN and release derivatives under the same license.

**Attribution**:
> Developed as part of the POLARIN project (Grant Agreement No. 101130949).
