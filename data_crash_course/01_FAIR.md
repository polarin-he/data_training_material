# Introduction to the FAIR data principles
<div style="
    background-color: rgba(128, 128, 128, 0.1);
    border-left: 4px solid rgba(128, 128, 128, 0.3);
    padding: 10px;
    margin: 10px 0;
    border-radius: 4px;
    font-family: monospace;
    font-size: 0.9em;
    color: #333;
">

**Audience level: Beginner**

**Estimated reading time: 15-20 minutes**

**Contributor: Zoé Brasseur (SIOS-KC); Daan Kivits (SIOS-KC)**

**Date created: 18-06-2026**

**Date last modified: 18-06-2026**

**License: [GNU GENERAL PUBLIC LICENSE Version 3 (AGPLv3)](https://www.gnu.org/licenses/gpl-3.0.html)** </div>

Research data are valuable scientific outputs. Making data FAIR helps ensure that research results can be discovered, understood, verified, and reused by others. FAIR data practices increase the visibility and impact of research, improve transparency and reproducibility, and reduce duplication of effort.

#### Learning Objectives
By the end of this notebook, you will be able to:
1. Explain the purpose of the FAIR principles.
2. Describe the four pillars of FAIR: Findable, Accessible, Interoperable, and Reusable.
3. Recognize common examples of FAIR and non-FAIR data practices.
4. Apply the FAIR principles when preparing datasets for publication or sharing.

#### Prerequisites
No prior knowledge of data management is required. Basic familiarity with: research data, metadata (information describing data) and data repositories is helpful but not essential.

#### What are the FAIR guiding principles?
FAIR stands for Findable, Accessible, Interoperable and Reusable. 
The FAIR principles describe how (meta)data and other digital research objects should be organized and described so they can be more easily accessed, understood, exchanged, and reused by both humans and computational systems. 
![The FAIR guiding principles as described by The Turing Way project. Source: Scriberia, licensed CC-BY 4.0](../sources/images/FAIR_turing.svg)
*The FAIR guiding principles as described by The Turing Way project. Source: Scriberia, licensed CC-BY 4.0*


### Why are the FAIR principles needed? 
Providing other researchers with access to your data and/or to rich metadata describing data facilitates discovery, strengthens transparency and reproducibility, and improves research efficiency by enabling reuse. Major funders and research infrastructures in Europe promote FAIR to maximize the value, integrity, and impact of publicly funded research. 


### How you can you make sure your data is FAIR?
#### Findable
*For data to be (re)used, your first need to be able to find them. Metadata and data should be easy to find for both humans and computers.*
| Principle | What to do |
|-----------|------------|
|**F1 (Meta)data are assigned a globally unique and persistent identifier** | <u>Bad example</u>: the dataset only exist as mydataset.xksx on your laptop. <br><u>What to do</u>: Upload your dataset to data repository that will assign it a persistent identifier such as a DOI (Digital Object Identifier).|
|**F2 Data are described with rich metadata (defined by R1 below)**|<u>What to do</u>: along your data, provide information such as: measurement location, sampling dates, instrument used, units, contact person, keywords, data processing description. Someone unfamiliar with your project should understand your dataset without having to contact you!|
|**F3 Metadata clearly and explicitly include the identifier of the data they describe**| The metadata and the dataset they describe are usually separate files. The association between a metadata file and the dataset should be made explicit by mentioning a dataset’s globally unique and persistent identifier in the metadata.<br><u>What to do</u>: make sure you mention the dataset DOI in the metadata.|
|**F4 (Meta)data are registered or indexed in a searchable resource**| Identifiers and rich metadata descriptions alone will not ensure ‘findability’ on the internet.<br><u>Bad example</u> the data are stored only on a lab website with no indexing.<br><u>What to do</u>: deposit your data in a data repository where researchers can easily find it through a search interface.|


#### Accessible
*Once the user/machine finds the required data, they need to know how they can be accessed, possibly including authentication and authorisation.*
| Principle | What to do |
|-----------|------------|
|**A1 (Meta)data are retrievable by their identifier using a standardised communications protocol** | <u>Bad example</u>: researchers must email you personally to access the file with your data. <br><u>What to do</u>: make sure your DOI resolves to a webpage where the data can be downloaded, ideally by both humans and machines.|
|**A1.1 The protocol is open, free, and universally implementable**| <u>Bad example</u>: Access requires proprietary software used only within one institution.<br><u>Good example</u>: The data are accessible through HTTPS, which every browser understands.|
|**A1.2 The protocol allows for an authentication and authorisation procedure, where necessary**| Note that data remain FAIR even when access is controlled. For example, if a dataset contains sensitive data, it is ok to implement access request or log in through an approved system before downloading the data.|
|**A2. Metadata are accessible, even when the data are no longer available**|If the dataset is withdrawn, it is important that researchers can still find the metadata to know that the dataset existed. The data repository therefore should still show the dataset title, authors, abstract, DOI, and a reason for removal. |

#### Interoperable
*Data should be compatible with other datasets and tools. This requires using standardized vocabularies and formats, facilitating integration with other data sources.*
| Principle | What to do |
|-----------|------------|
|**I1 (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.** | <u>Bad example</u>: data are stored in a proprietary format (example: Microsoft Excel file) or a format that computers cannot easily read (example: scanned PDF table). <br><u>What to do</u>: use a format such as CSV, NetCDF, JSON, Darwin Core Archive.|
|**I2 (Meta)data use vocabularies that follow FAIR principles**| Use a recognized vocabulary following community standards. For example, use “air_temperature” instead of “Temp”. Different datasets can then be combined more easily.|
|**I3 (Meta)data include qualified references to other (meta)data**| If other observations were useful for your measurements, mention them explicitly in your metadata. For example: “This dataset was generated using meteorological observations from Dataset DOI: xxx”.|


#### Reusable
*The ultimate goal of FAIR is to optimise the reuse of data. To achieve this, metadata and data should be well-described so that they can be replicated and/or combined in different settings. This entails clear licensing, detailed provenance information, and adherence to community standards.*
| Principle | What to do |
|-----------|------------|
|**R1 (Meta)data are richly described with a plurality of accurate and relevant attributes** | The (meta)data should richly describes the context under which the data was generated and the scope of the data. This may include calibration procedures, uncertainties, quality-control flags, instrument settings, or sampling protocols. You should be as generous as possible in providing metadata, even including information that may seem irrelevant.|
|**R1.1 (Meta)data are released with a clear and accessible data usage license**| A clear usage license should be provided so researchers can immediately know how the data may be reused. Example: License CC BY 4.0|
|**R1.2. (Meta)data are associated with detailed provenance**| The metadata should explain who collected the data, when, where, which instrument was used, which processing steps where applied.|
|**R1.3 (Meta)data meet domain-relevant community standards**|It is easier to reuse datasets if the data is organised in a standardised way, using well-established file formats, common vocabulary or a common template. If community standards or best practices for data archiving and sharing exist, they should be followed so that researchers in the field can immediately understand the data. Useful resources you might want to check out: https://schema.datacite.org/ or https://cfconventions.org/.|


### FAIR Self-Assessment Checklist
Before publishing your data, ask yourself:

| Principle | Question |
|-----------|----------|
| F1 | Does my dataset have a DOI or PID? |
| F2 | Have I described it well enough for a stranger to understand it? |
| F3 | Does the metadata explicitly point to the dataset? |
| F4 | Can someone find it through a repository search? |
| A1 | Can it be retrieved through a standard web protocol? |
| A1.1 | Is the protocol open and widely supported? |
| A1.2 | If access is restricted, is there a clear authentication process? |
| A2 | Will metadata remain available even if data disappear? |
| I1 | Are the files machine-readable and non-proprietary? |
| I2 | Am I using community vocabularies? |
| I3 | Have I linked related datasets properly? |
| R1 | Is there enough context for reuse? |
| R1.1 | Is there a clear license? |
| R1.2 | Is the provenance documented? |
| R1.3 | Does the dataset follow community standards? |

### The CARE principles as an extension to the FAIR principles
Does your research involve handling, managing and/or analysing Indigenous data? If so, you should consider applying the CARE Principles for Indigenous Data Governance. Whereas the FAIR data principles provide technical guidance on data documentation and sharing, the CARE data principles provide the neccessary ethical and legal boundary conditions. Please read up on the CARE Principles in the next notebook [here](./01_CARE.ipynb). 

## References used in this notebook
- Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data, 3, 160018.
- https://www.openaire.eu/how-to-make-your-data-fair 
- https://www.go-fair.org/fair-principles/
- https://sisu.ut.ee/andmehaldus/fair-data/?lang=en 
- https://www.eresearch.uni-goettingen.de/de/knowledge-base/explain-data/fair-principles/
- https://www.gofair.us/fair-principles
- https://openneuroscience.org/Governance/FAIR-Principles
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9562067/
- https://training.galaxyproject.org/training-material/topics/fair/tutorials/fair-intro/tutorial.html
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11177558/
- https://www.nnlm.gov/resources/data/data-glossary/fair-principles
- https://www.ouvrirlascience.fr/wp-content/uploads/2018/11/FAIR-Principles.pdf
- https://faircookbook.elixir-europe.org/content/recipes/introduction/brief-FAIR-principles.html
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11177558/
- https://www.gofair.foundation/a1
- https://data-guidelines.scilifelab.se/topics/fair-principles/
- https://www.eresearch.uni-goettingen.de/knowledge-base/explain-data/fair-principles/
