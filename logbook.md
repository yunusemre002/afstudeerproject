# LOGBOOK

# First Results

https://drive.google.com/drive/folders/1AnUnfZbJpZWdKvpxJOniLWIzyFzvSiDI?usp=drive_link

# Some shotcuts
```conda activate napari-env```
```ctrl+K V```


# Paper structure must follow
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

# 23.04.2025 
## Todo list

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

### Value Proposition Canvas v0
![Value Proposition](photos/orginal_fotos/value_proposition_canvas.png)

### Value Proposition Canvas v1 (Last)
![Value proposition v1](/photos/orginal_fotos/value_proposition_canvas_v1.png)


-------
## Current Flow
1. Open Fiji
2. Load the .lif file (2D MAXprojection fluorescence microscopy data)
3. Use AggreCount
4. AggreCount detects aggregates
5. Export 2D results to a CSV file


## Happy Flow

### 1. Load `.tif` File
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

### 5. Cell Segmentation
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


# 12.05.2025
## Todo List
1. Flow diagrams (current + happy)
2. AI breakdown
3. User research (e.g. empathy map) ?? not hard just 10 min
4. Level of Automation ??
5. Which design pattern will you use and wyh (look at the google and choose one of them)
6. Which model have been used (cellpose has been used en last version.) Nuclei and cellbody  detection currrent pc and de process time)
5. De library and the technologies which is used (napari(for 3d visualizations), skime, cellpose(cellbody, nuclei quantification))

## Paper Prototype Base
![paper_prototipe-1_1](/photos/orginal_fotos/paper_prototype_1_1.jpeg)
![paper_prototipe_1_2](/photos/orginal_fotos/paper_prototype_1_2.jpeg)


## Paper Prototype First feedback
![paper_prototipe-1_1](/photos/orginal_fotos/paper_prototype_1_1.jpeg)
![paper_prototipe_2_2](/photos/orginal_fotos/paper_prototype_2_2.jpeg)

<!-- <img src="/photos/paper_prototype_1_1.jpeg" width="45%"> <img src="/photos/paper_prototype_2_2.jpeg" width="47%"> -->

## Current Flow Diagram
![current_flow](/photos/orginal_fotos/current_flow.png)

## Happy Flow Diagram Base
![Happy_flow](/photos/orginal_fotos/happy_flow.png)

## Happy Flow Diagram V1
Feedback loop added.
![Happy_flow_v1](/photos/orginal_fotos/happy_flow_v1.png)


# 13.05.25
## To Do list 
1. Which design pattern will you use and wyh (look at the google and choose one of them)
2. Which model have been used (cellpose has been used en last version.) Nuclei and cellbody  detection currrent pc and de process time)
3. De library and the technologies which is used (napari(for 3d visualizations), skime, cellpose(cellbody, nuclei quantification))
4. User research (e.g. empathy map) ?? not hard just 10 min
5. Level of Automation ??
6. AI breakdown


## Google Design pattern
**Adapt AI with user feedback**
Adapt your AI system with feedback from people, during individual interactions and over time.
Human-AI interactions are a bidirectional feedback loop. AI learns from users to personalize their experiences, and users adapt their behaviors and workflows in response to AI outcomes. Set up feedback mechanisms that can be used to interpret AI outcomes, and account for changes introduced by AI.

---

Cellpose has a adjustable parameter for example diameter or (other two parameter) i can show to user that and explanation with it and i can say if you are not happy the result change the parameter and try one more time. it can be. for example if the model detect the cellkern too big just work with smaal diamaeter but keep in mind it cost time. 

---

## Adaptive AI Through Feedback

Our system design closely follows Google's *Adapt AI with user feedback* design pattern, which emphasizes the importance of creating bidirectional feedback loops between users and AI systems. This pattern encourages dynamic adjustment based on user interaction and evolving expectations.

In our application, segmentation is first performed automatically using default Cellpose-SAM parameters. Immediately after, the user is presented with the result and prompted with:
**"Didn’t get the result you expected?
You can go back, adjust the settings, and try again for a better result."**


This simple prompt initiates a lightweight feedback loop. Users are empowered to modify the `diameter` parameter, which controls the expected object size, and observe how the output changes. Although this form of feedback is implicit—users are not explicitly rating or scoring the results—it directly shapes the behavior of the system and adapts it to the user’s context and goals.

To support a wide range of user expertise, we include a collapsible “Expert Settings” panel, where advanced parameters such as `flow_threshold` and `cellprob_threshold` can be adjusted. This structure aligns with Google's recommendation to support both short-term interaction-level adaptation and long-term personalization, without compromising usability.

By encouraging iterative interaction and adaptation through meaningful user control, our system operationalizes the *Adapt AI with user feedback* principle in a practical and user-friendly way.


SO update de paper prototype:
1. Add feddback icon last page
2. Add parameter settings 2. page


### Technologies Used: Cellpose-SAM and Threshold-Based Aggregate Detection
In this study, we utilized a combination of advanced segmentation and image processing techniques tailored for fluorescence microscopy of neural aggregates. The key components of our pipeline are as follows:

### Cellpose-SAM for Cell Segmentation
For segmenting both the cell bodies and nuclei, we used the latest Cellpose-SAM model. This model is a fusion of the original Cellpose deep learning-based segmentation framework with the Segment Anything Model (SAM) developed by Meta AI. SAM is a transformer-based model that can segment objects in images without requiring class-specific supervision. When combined with Cellpose, it becomes highly effective for biomedical data, where object shapes vary significantly and boundaries may be unclear.

Cell Bodies were segmented from Channel 4 (C4) using Cellpose-SAM with an estimated diameter of 100 pixels.

Cell Nuclei were segmented from Channel 1 (C1) with a diameter of 30 pixels.

Each Z-slice of the 3D microscopy stack was processed independently, and Cellpose-SAM produced a binary mask for each frame. These masks were then reconstructed into a full 3D volume, enabling spatial analysis of cell structures. The use of SAM particularly improved segmentation accuracy in low-contrast and noisy regions.

### Aggregate Detection via Thresholding
Following the segmentation of cells, aggregate regions were identified using intensity-based thresholding on the relevant channels (e.g., Channel 2 for Huntington-related aggregates).

Each Z-slice was processed individually.

Various thresholding methods were explored (e.g., Otsu, adaptive, fixed percentile), but we selected a global fixed threshold, manually tuned to highlight only the bright, dense aggregate regions while minimizing background noise.

Morphological operations (e.g., opening, closing) were applied to refine the binary masks.

The resulting masks were assembled across Z-slices to reconstruct 3D aggregate volumes.

### Application to Our Dataset
The described techniques were applied to multichannel .tif microscopy images obtained from neuronal cultures.

Cell body segmentation was performed on Channel 4, using a diameter of 100, processed slice-by-slice using Cellpose-SAM.

Cell nucleus segmentation was carried out on Channel 1, with diameter set to 30.

Each slice of the stack was independently processed to detect masks, which were then assembled into 3D representations using standard volumetric reconstruction techniques. This enabled both per-slice 2D analysis and full 3D visualization.

Aggregate detection was performed on Channel 2, representing Huntington aggregates. A fixed global threshold was chosen after testing different methods, and 3D aggregate volumes were reconstructed.

The pipeline allows inspection of each Z-slice individually (e.g., which aggregates lie inside or outside of cell boundaries), while also offering full 3D visualization of cell bodies, nuclei, and aggregates using tools like Napari, enabling intuitive interaction and validation.


## Libraries and Tools

The following libraries and tools were used to facilitate the segmentation, analysis, and visualization:

Cellpose: The core library for segmentation, enabling the extraction of cell boundaries and the identification of structures like nuclei.

SAM (Segment Anything Model): Leveraged for its ability to segment objects in the images, especially when class-specific labels were not available.

Napari: A 3D image viewer built on top of Qt and PyQt, used for interactive visualization of the 3D models generated from the segmented cell bodies, nuclei, and aggregates. Napari provides an intuitive interface for zooming, rotating, and interacting with multi-dimensional data, and was key for analyzing results in 3D.

NumPy & SciPy: Fundamental libraries for handling and processing large-scale image data (such as creating arrays from Z-slice stacks and performing image processing operations).

Matplotlib: Used for visualizing 2D slice results and generating various plots to analyze the distribution of cell body and aggregate features across the dataset.

scikit-image: A library for general image processing, including thresholding, morphological operations, and filtering.

The combination of these libraries provides a comprehensive and efficient pipeline for processing and analyzing microscopy data.

## Mental exercises and trials for a solution:

### cellpose 3d
It was considered and tested to detect both cells and nuclei using Cellpose 3D. However, it was experienced that the method did not work on a MacBook M1 (2020), likely due to the high GPU requirements. As a result, a Colab Pro account was used to run the process with a high-performance GPU. Even in this setup, cell and nucleus detection took more than an hour, totaling up to three hours for full processing. Given the lengthy processing time and the dependency on high-end GPUs, it was concluded that this method would not be feasible for the current workflow and impractical to run in different environments. Therefore, this approach was abandoned.

### Threshold Methods for Aggregate Detection
In the aggregate detection step, various thresholding techniques were explored to identify potential aggregate regions based on intensity differences in the microscopy images. Several well-established methods from the literature were tested, including:

- **Otsu Thresholding**  
- **Triangle Method**  
- **Mean Thresholding**  
- **Minimum Thresholding**

Although these methods are commonly used in biomedical image analysis, they did not perform consistently well on our dataset. The heterogeneity in image brightness, contrast, and aggregate density across different samples limited the effectiveness of these thresholding strategies.

As a result, a **general thresholding approach** was adopted. In this method, a global thresholding algorithm is applied, but the threshold value itself is user-adjustable. This parameter can be fine-tuned via the user interface (UI) for each image, allowing for better adaptability to the varying conditions present in individual samples.

This solution provides a flexible balance between automation and manual control, helping to accommodate sample variability while maintaining usability.



# 14.05.25
## TODO List
1. User research (e.g. empathy map) ?? not hard just 10 min
2. AI breakdown Level of Automation ??
3. Update the paper prototype (Add feddback icon last page, Add parameter settings 2. page)
4. focuss on iterations and requariments
5. Run it on 10 images with same color.

## Feedback from Bart
- Run it on 10 images not just one image it is bias. 
- All aggregates must be same color but different intencity with mening.



# 19.05.25
## TODO List
1. Update the paper prototype (Add feddback icon last page, Add parameter settings 2. page)
2. Focuss on iterations and requariments
3. Run it on 10 images with same color.

## feedback paper prototype
1. Show the fotos of the input to user. to choose it.  

## Feedback from Lamia:
- [x] In the Introduction → mention Fiji and the imaris program in the Current section.  
- [x] Remove the sub-question “preprocessing” part, keep only the steps. 
    - [x] Answer this sub-question in the Methodology introduction.  
- [x] Evaluation part — only one person bias, discuss this.  
- [x] Explain what aggregate quantification means in Methodology — location, volume, count.  
- [x] Performance metrics — human evaluation by expert as GOLD STANDARD. Why? There’s no other option.  
- [x] Discussion on 3D aggregation is too specific:  
  - [x] Dataset  
  - [x] Methods — aggregate threshold part  
- [x] AI automation level explained.  
- [x] Remove “Idea proportion” texts, keep just a brief summary.  
- [x] Ask Carolina about ethical concerns.  
- [x] Iteration — clarify that it’s a single iteration (before B4).  
  - [x] Mention timing details.  
- [x] Stakeholder analysis from NOAH Leroy — make it clearer. Focus on biomedical researchers, CureQ Health Lab, all parts.  
  - [x] Delete everything below this, last sentence is important.  
- [x] Current flow included.


All of the feedback which is given from Lamia is done.


# 21.05.25
## TODO List
1. ~~Iteration in the model section~~
2. ~~Requirements (model + product {+UI})~~
3. ~~State of the art~~
4. Teruggekomen op requirements in de discussie
5. Redesign de model PART ?? Or ask it  to Lamia
6. Conclusie
7. Update the Paper Prototype 
    - Add feddback icon last page, 
    - Add parameter settings 2. page
    - Show the fotos of the input to user to choose it.  (Le Roy)
9. Run it on 10 images with same color. (Bart)

![happy flow v2](/photos/orginal_fotos/happy_flow_v2.jpg)

# 22.05.2025
1. ~~Redesign de model PART ?? Or ask it  to Lamia~~
2. Conclusie
3. Update the Paper Prototype 
    - Add feddback icon last page, 
    - Add parameter settings 2. page
    - Show the fotos of the input to user to choose it.  (Le Roy)
4. Run it on 10 images with same color(!). (Bart)

## 2'nd Feedback from Lamia
1. [x] ~~Write more about ethics.~~
2. [x] ~~Restructure the model.~~
3. [x] Use consistent terms: label, annotation, unlabeled etc.
  - [x] First Explain why annotation is important.
- [x] Discussion
  - [x] Highlight what you did well. Say what you achieved.
    - [x] impackt of socacity
  - [x] Mention what is missing. List weaknesses; why? 
    - [x] dataset
    - [x] pretrained model
    - [x] importance of annotation
  - [x] possible improvements.
    - [x] future work
- [ ] Resubmit the assignment form.

# 26.05.2025
1. ~~Download 20 fotos and convert it to .tif file~~
2. Look at the mail of Carolina