# Title: [Insert Title, e.g., POLARIN Data Stewardship Training Template]
#### **Topic: [Insert Topic, e.g., "Data Documentation with Metadata"]**

**Audience level: [Beginner/Intermediate/Advanced]**

**Estimated reading time: [X minutes]**

**Contributor: [Your Name]**

**Date created: [YYYY-MM-DD]**

**Date last modified: [YYYY-MM-DD]**

**License: [GNU GENERAL PUBLIC LICENSE Version 3 (AGPLv3)](https://www.gnu.org/licenses/gpl-3.0.html)**

#### Introduction

**Purpose**: Briefly explain the importance of this topic in 2-3 sentences.
Example:
> "This notebook introduces [topic], a critical aspect of data stewardship that ensures your data is [FAIR principle, e.g., 'findable and reusable']. By the end, you will be able to [key skill]."

#### Learning Objectives
By the end of this notebook, you will:
1. [Objective 1, e.g., "Understand the basics of metadata."]
2. [Objective 2, e.g., "Apply a metadata standard to your dataset."]
3. [Objective 3, e.g., "Use a tool to generate metadata."]

#### Prerequisites
- Basic familiarity with [e.g., Python/Jupyter Notebooks].
- Access to [e.g., a dataset or tool, if applicable].
- (Optional) Completion of [related notebook/topic].

## [Section Title, e.g., "The use of metadata standards and controlled vocabularies"]
**Explanation**:
[Briefly explain the concept, e.g., "The use of the right metadata standards and controlled vocabularies makes your data more FAIR: they make your data more Findable (F), Accessible (A), Interoperable (A), and Reusable (R). Metadata standards describe _which_ attributes should be included in the metadata, whereas controlled vocabularies describe _how_ these attributes should be described in the metadata. A widely-adopted, cross-disciplinary metadata standard is the [Attribute Convention for Data Discovery (ACDD)](https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3)." Examples of widely-adopted, cross-disciplinary controlled vocabularies are the [GCMD Keywords](https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all?gtm_scheme=all) or [Climate and Forecast (CF) metadata conventions](https://cfconventions.org/cf-conventions/cf-conventions.html)] 

**Example**:
Let's create a set of metadata for a dataset that adheres to the ACDD v1.3, CF v1.8, and GCMD Science, GCMD Locations, and GCMD Providers conventions.

```python
metadata = {
    "title": "Example Dataset",
    "summary": "This is an example dataset",
    "keywords": "GCMDSK: EARTH SCIENCE > CLIMATE INDICATORS > CRYOSPHERIC INDICATORS > ICE EXTENT, GCMDSK: EARTH SCIENCE > CRYOSPHERE > SNOW/ICE > ICE EXTENT, GCMDLOC: GEOGRAPHIC REGION > NORTHERN HEMISPHERE, GCMDPROV: GOVERNMENT AGENCIES-NON-US > NORWAY > NO/MET",
    "conventions": "ACDD-1.3, CF-1.8"
}
print(metadata)
```

**Your Turn**
Replace the example above with a dataset relevant to your field.

```python
# [Contributor: Add your code/example here]
metadata = {
}
print(metadata)
```


### Key Takeaways
- [Takeaway 1, e.g., "Metadata standards like ACDD improve FAIRness of research data."]
- [Takeaway 2, e.g., "Metadata standards describe _which_ attributes should be included in the metadata, whereas controlled vocabularies describe _how_ these attributes should be described in the metadata"]
- [Takeaway 3]

### Additional Resources
- [Link 1: Relevant tool/documentation]
- [Link 2: POLARIN Training Resources Database]
- [Link 3: External tutorial]

#### License
This notebook is licensed under [AGPLv3]. You are free to use, adapt, and share it, provided you attribute POLARIN and release derivatives under the same license.

**Attribution**:
> "Developed as part of the POLARIN project (Grant Agreement No. 101130949)."
