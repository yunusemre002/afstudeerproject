
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



## 24.04.2025
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
    1. Get .lif file
    2. Open Fiji
    3. Open AggreCount
    4. get results for CSV file (2d)

* Wat is your 
