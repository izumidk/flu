#Determining the relative contributions of immune history and strain-matching in responses to influenza vaccines 2014
## Pre-Vaccine Titer vs Response (Post/Pre Titer) 2014 Figure 1

This repo contains the code to reproduce Figure 1
Data analysis Process found on [ImmPort](https://www.immport.org/docs/reference/InfluenzaVaccination_SDY212_Tab-v2.2017.html)
Raw data available on [ImmPort](https://www.immport.org/shared/study/SDY640)

## Reproducing Analysis
###Overview
Figure 1 visualizes pre vaccine titers vs response in a scatter plot

###Data
HAI data was generated for pre and post vaccine titers (day 0 and >day25) for a cohort of young and old volunteers
Titers were determined by HIAyear3 document in protocols folder

###Folder Structure
gitfolder contains code, data and analysis folders
code contains scripts to take in data, analyze data, and produce figures (deposited in analysis folder)
data folder contains necessary .txt files for this analysis


###Instalation 
This Analysis was done on Python 3.8.1
You will need to install pip and then pip install the packages
`<pip install -r requirements.txt>`

####Running Code
In code folder
`<hai_import_data_2014.py>` must be run first
	Takes in arm_2_subject.txt, subject.txt, and hai_result.txt
	Change path name 
	Returns subjects_2014.csv and hai_2014.csv in analysis folder
`<hai_analysis_2014.py>` run second
	Takes in subjects_2014.csv and hai_2014.csv
	Returns hai_analysis_2014.csv in analysis folder
`<hai_figures_2014.py>` run third
	Takes in hai_analysis_2014.csv
	Returns 2014_Fig_1.html in analysis folder

