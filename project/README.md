[Information on editing a Markdown document](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

# Data

## Source

(1-2 paragraphs) Describe where the data came. If data are on-line, provide links.

The data of which I am analyzing for my final project is around 10 processed electron precipitation .nc arrays from the Medium Energy Proton/Electron Detector (MEPED) aboard the EUMETSAT MetOp Satelite. The base data was procured from the POES database on the NOAA Website at https://www.ncei.noaa.gov/data/poes-metop-space-environment-monitor/access/l1a/v01r00/2023/noaa15/, after which it was run through a python script to filter proton contamination and subsampled to a 16-second cadence. The cadence is an incredibly important element of the processed data because it is the smallest interval that both older and newer MEPED data runs at. In 2012, there was a switch in cadence from 16-second averaged count rates to 2-second averaged count rates.





## Interpretation

(1-2 paragraphs) Describe what is measured at a basic level. Provide links to 1-2 high-level descriptions (web pages or papers). This should be a text version of your two-minute overview.

MEPED contains 2 proton and 2 electron telescopes
90 degree and 0-degree detectors
6 proton channels 
3 electron channels (~ 25 keV to 2500 MeV)
Include the 0° and 90° count rates at 16-second cadence (Pettit et al., 2021) 
Bounce Loss Cone (BLC) flux is calculated from both detectors
Each file represents one day of data collection
By taking the mean of the electron counts in each channel for each file, we get an average for the entire day.


https://repository.library.noaa.gov/view/noaa/15751/noaa_15751_DS1.pdf

# Exploratory Data Analysis

Provide 1-3 plots that characterize general features of the data. These plots will be revised as you project progresses. The first version should be of what you presented the first time.

![Project Screenshot](stats/project/project_Ia.png)

# Statistical Test

## Description

Explain what you want to quantify with statistical methods. Provide references to any equations used.

You can use plain text for equations, e.g., y=mx+b, or LaTeX, e.g., $y=mx+b$.

## Results

Present the results of your analysis. Include tables and plots.

# References

Add references to any web page or paper that you read as you worked on this project.

Example:

* [Wheatland, 2000](https://iopscience.iop.org/article/10.1086/312739/pdf)

# Grading

Final project presentations, 4:30-7:10 pm in the same room as class. [Final Exam Schedule](https://registrar.gmu.edu/fall-2026-final-exam-schedule/)

Project presentations (10-20 minutes)

Guidelines:
1. Present exploratory data analysis results that are relevant to part 2.
2. Discuss question that you want to answer that requires statistical methods. Discuss related literature, if relevant.
3. Review theory
4. Present results related to question

You may use PPT or present from your README.md file.

Grading:
* All revisions discussed during previous class presentations addressed
* Theory correct
* Results correct
