```conda activate napari-env```
Samenvatting
• Introductie
 - Context, Probleem, Bestaand werk, Gat, Voorstel
• Achtergrond
- Basiskennis (literatuur)
- State of the art (literatuur)
- Stakeholder-analyse
• Requirements
- Product (inclusief gebruikersinterface)
- Model
• Prototype
- Idee generatie en value proposition
- Flow diagrams en AI breakdown
- Gebruikersonderzoek (empathy map bijvoorbeeld)
- (Paper) Prototype
• Model
- Methodologie (dataset, architecture, ...)
- Resultaten (performance en andere kwaliteitsmaten)
- Conclusie
• Discussie
- Implicaties, Future work, Aanbevelingen
- Terugkomen op requirements
• Bronnenlijst (overweeg het gebruik van een referentiemanager
1 https://www.ieee.org/conferences/publishing/templates.html
2 https://www.acm.org/publications/authors/submissions


# Installing Cellpose
in order to download the cellpose envoriement I follow this instructures [cellpose link](https://cellpose.readthedocs.io/en/latest/index.html) 

```python -m cellpose``` 

# Communication with Carolina
---
I asked some question to Carolina via mail:

```text
Tue 22 Apr, 12:25 
to c.konrdorferrangel-2, j.b.antonissen, b.m.l.baselmans

Title: Image Processing-Based Quantification of Neural Aggregates for Huntington’s Disease Detection
Main Research Question:
How can image processing methods be implemented to quantify neural aggregates in microscopy images for Huntington’s disease detection?
Sub-Questions:
1. What preprocessing steps are necessary to enhance image quality for accurate aggregate detection?
2. How can cells be effectively detected in microscopy data before quantifying neural aggregates within them? 

I am planning to work based on this title and these research questions. Does it look appropriate to you? 
I’m working with .lif files. Which channel or channels (e.g., HA?) should I focus on for the best results?
Below is the workflow I’ve created:

Load the .lif file
Select the relevant channel
Merge the Z-slices (3D to 2D)
Detect cell boundaries
Find aggregates within those boundaries
However, cell detection is currently not working well. I will focus on it.  Why do you emphasize 3D? What are the advantages and disadvantages of working with 3D images versus 2D projections (like stacked 8 Z-slices)?
Until now, I’ve been collapsing the 3D data into a 2D image for easier processing. Do you think this is a valid method, or are there better alternatives for working with 3D data directly?
In the attached PDF file, I worked with a .lif image and tried to identify protein aggregates. You can ignore the code sections — the photos are the most important part.  Do you think the last image reflects the main goal of the project?
```
# literatuur reserch 


# Todo list
## 23.04.2025 
1. Read expert workshop slides 
2. Complete Introduction 
3. Compelete Background 
4. Mension about paper which you have read and reseach which you have done with lamia and self in the logbook, so hier.

### Proggess
* Introduction and background part has been wrote. It looks like compleete. I have got a mail from carolina about the answer of my question and it is more clear now. The project must be 3d image progessing. And the name of the paper and main question eddited. 

* The order of the Z-Stacks is not true in the python. I have been bussy wiht this error for 4 days i coudnt solve it yet. 



# 24.04.2025
1. **Requiremernts:** Look at the lessons notes and create and requirements.
2. **Prototype:** Look at the lessons notes. And bring something to requirements.
3. 

### Requirements Table

| ID  | Domain        | Type           | Requirement Statement                                                                 | Justification                                                                 | MoSCoW |
|-----|---------------|----------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------|
| R1  | Image Analysis | Functional     | The system **must** detect all individual cells in the microscopy images.              | Accurate cell detection is essential to locate and quantify neural aggregates. | Must   |
| R2  | Image Analysis | Functional     | The system **must** process the HA and CCT1 channel  of the microscopy data.                | HA channel  specifically marks the Huntington-related aggregates. CCT1 channel is usefull to see cell body.         | Must   |
| R3  | Preprocessing  | Functional     | The system **should** apply noise reduction before segmentation.                       | Reducing noise helps prevent false detections in cell boundaries.              | Should |
| R4  | Aggregates     | Functional     | The system **must** quantify aggregates larger than a defined intensity threshold.     | Only aggregates above the threshold are considered relevant. | Must   |
| R5  | Output         | Non-functional | The output **should** include a CSV file with cell positions, aggregate count, and size.| Allows easy further analysis and validation by domain experts.                | Should |
| R6  | I/O Format     | Functional     | The system **must** accept only `.lif` files as input for 3D microscopy analysis.      | Ensures compatibility with standardized imaging data used in this project.     | Must   |
| R7  | Output         | Functional     | The system **must** generate a structured file (CSV or JSON) with aggregate count, location, and their association with detected cells. | Provides interpretable results for downstream analysis and biological insight. | Must   |
| R8  | Output         | -----          | The system **could** generate annotated image projections for visual inspection.       | Helps researchers visually verify the detection quality and segmentation.       | Could  |
| R9  | System	Compatibility         | ---          | The system should be compatible with Windows, macOS, and Linux for broader accessibility.       | Makes the tool available to a wider user base.       | Should  |


Vragen naar Caroline
* What is your current metodololy for quantification of aggregate? like
    1. Get .lif file (3D fluorescence microscopy data)
    2. Open Fiji
    3. Open AggreCount
    4. AggreCount picks the most intensieve z-stacks
    5. AggreCount finds aggregates
    4. get results for CSV file (2d)

* Wat is your current metodology?



# 28.04.2025
## Todo List
1. Write about Wyh 3d is important. 
2. (prototype) Idea generation and value proposition
3. Flow diagrams
4. AI breakdown
4. User research (e.g. empathy map)
5. (Paper) Prototype
6. which design pattern will you use and wyh (look at the google and choose one of them)

o Design, Development and Results of a prototype
• Design and development are part of the methods
• The prototype itself is a result
• For your paper, don't include theories you can't defend with source
o HvA Master Applied AI Design Class is not a source


## Value Proposition V1
### Customer Jobs
1. Detect and quantify cellular structures in fluorescence microscopy images.
2. Identify and measure aggregates within individual cells.
3. Obtain consistent and reproducible results across different samples.
4. Minimize manual workload and reduce analysis time.

### Pains
1. Lack of publicly available annotated datasets for microscopy images.
2. Very few or no open-source solutions available in the current literature.
3. Absence of ground truth datasets to validate analysis methods.
4. Challenges in segmenting small, dim aggregates.


### Gains
1. Faster and automated microscopy data analysis.
2. Improved accuracy and reliability in detecting and quantifying structures.
3. Objective, quantitative results that support research conclusions.
4. Easy-to-use workflows with minimal manual input.
5. More scalable and reproducible research processes.

### Value Map
### Products & Services
1. Automated cell detection algorithms.
2. Aggregate detection and quantification tools (position, size, count analysis).
3. User-friendly analysis interface with adjustable parameters.
4. A complete analysis pipeline.

### Pain Relievers
1. Find an open-source annotated dataset to overcome the lack of available labeled data for training and validation.
2. Create a self-solution by combining one or more existing methods developed for related problems and applying them to this specific case 
3. Optimizing preprocessing steps for noisy and low-contrast images.

### Gain Creators
1. Major time savings by eliminating manual annotation.
2. Reliable detection even for small and weak aggregates.
3. Higher-quality, reproducible data supporting robust research.
4. Accelerated and streamlined research workflows.


# 29.04.2025

## 🔬 Value Proposition V2 (Last)

### 🎯 Customer Jobs
1. Detect and quantify cellular structures in 3D fluorescence microscopy images.  
2. Identify and measure mutant huntingtin aggregates within individual cells.  
3. Obtain consistent and reproducible quantification results across different samples.  
4. Reduce manual workload and streamline the image analysis workflow.

### 😟 Pains
1. Lack of publicly available annotated 3D microscopy datasets.  
2. Very few or no open-source solutions available in the current literature for 3D aggregate quantification.
3. Absence of ground truth data for validating analysis results.  
4. Challenges in segmenting small and weakly fluorescent aggregates in 3D volumes.

### ✨ Gains
1. Faster and automated analysis of 3D fluorescence microscopy images.  
2. Improved reliability and consistency in detecting and quantifying aggregates.  
3. Objective and reproducible results for aggregate-level quantification.  
4. User-friendly analysis workflow with minimal manual intervention.  
5. Scalable image processing methods applicable across multiple experiments.

---

## 🛠 Value Map

### 🧪 Products & Services
1. Automated cell and aggregate detection tools for 3D microscopy images.  
2. Aggregate quantification modules (location, size, count).  
3. A modular, user-friendly analysis pipeline implemented in Python.  
4. Adjustable parameters for flexible preprocessing and analysis control.

### 🔧 Pain Relievers
1. Find an open-source annotated dataset to overcome the lack of available labeled data for training and validation. 
2. Combine multiple existing algorithms into a tailored workflow specifically optimized for 3D fluorescence image analysis. 
3. Robust preprocessing pipeline tailored for noisy and complex 3D image data.

### 🚀 Gain Creators
1. Significant time savings by reducing manual annotation and segmentation.  
2. Robust detection performance, even for small and low-contrast aggregates.  
3. Higher data quality and reproducibility for downstream research.  
4. Streamlined workflows that accelerate scientific insight from microscopy images.

![Value Proposition](photos/Value%20Proposition%20Canvas.png)


-------
## Current Flow
1. Open Fiji
2. Load the .lif file (3D fluorescence microscopy data)
3. Use AggreCount
4. Let AggreCount select the most intense z-stacks
5. Detect aggregates
6. Export 2D results to a CSV file



## Happy Flow

### 1. Load `.lif` File
- Import full multichannel 3D fluorescence microscopy data  
- Supported via libraries like `bioformats` or `aicsimageio`

### 2. Display File Metadata and Channel Previews
- Show image info: number of channels, dimensions, number of Z-slices  
- Display intensity-based preview for each channel (e.g., max-projection or middle slice)  
- Highlight the most intense Z-slice per channel for easy recognition

### 3. User Selects Relevant Channel(s)
- User selects which channel(s) to analyze (e.g., C2 = aggregates, C0 = nuclei)

### 4. Preprocess Image Stack
- Apply 3D denoising and contrast normalization  
- Preserve all Z-slices — no projection used

### 5. (Optional) Cell Segmentation
- Use nuclear channel to detect and segment cell regions  
- Enables per-cell aggregate quantification

### 6. 3D Aggregate Detection
- Detect aggregates in selected channel(s) across the full Z-stack  
- Use 3D thresholding, connected components, or ML-based segmentation

### 7. Quantification
- For each aggregate, extract:
  - Volume  
  - Position (x, y, z)  
  - Intensity metrics  
- (Optional) Link aggregates to cells for per-cell stats

### 8. Export Results
- Output quantification results in CSV or JSON  
- Include image metadata and selected channels for traceability

### 9. (Optional) Visualization
- Provide 3D visualizations or annotated Z-stack overlays for result validation


## Solution of the z-slice problem:
When you are try to anysis the foto of the cell
Python has a problem, when it works with the .lif file. it can open it but it struggle to show correct order of the z-slices, it shows just rondom slices. Now i have a solition. it is just convert file to .tiff file. 


# 30.04.2025
1. Look at one more time to requirements 
    * Product (inclusief gebruikersinterface)
    * Model
2. 