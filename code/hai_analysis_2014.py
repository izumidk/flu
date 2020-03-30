import pandas as pd 
import numpy as np


# Read clean data from file 'hai_2014.csv' and 'subjects_2014.csv'
# (in the same directory that your python process is based)
hai_2014 = pd.read_csv("/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/analysis/hai_2014.csv") 
subjects_2014 = pd.read_csv("/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/analysis/subjects_2014.csv")


#PREVAX Table
#make dataframe of only pre vaccination data (day0)
study_pre_2014 = hai_2014[hai_2014['STUDY_TIME_COLLECTED'] == 0].copy()
# rename the VALUE_PREFERRED column to 'PREVAX' and 'COMMENTS' column to "VIRUS_STRAIN"
study_pre_2014.rename(columns = {"VALUE_PREFERRED" : "PREVAX"}, inplace=True)
study_pre_2014.rename(columns = {"COMMENTS" : "VIRUS_STRAIN"}, inplace=True)
# and drop the now pointless STUDY_TIME_COLLECTED column.
study_pre_2014.drop(['STUDY_TIME_COLLECTED'], axis=1, inplace=True)


#POSTVAX Table
#make a dataframe of only post (25 or more days after vaccination)
study_post_2014 = hai_2014[hai_2014['STUDY_TIME_COLLECTED'] != 0].copy()
# rename the VALUE_PREFERRED column to 'Post-Vax' and 'COMMENTS' column to "VIRUS_STRAIN"
study_post_2014.rename(columns={'VALUE_PREFERRED':'POSTVAX'}, inplace=True)
study_post_2014.rename(columns = {"COMMENTS" : "VIRUS_STRAIN"}, inplace=True)
# and drop the now pointless STUDY_TIME_COLLECTED column.
study_post_2014.drop(['STUDY_TIME_COLLECTED'], axis=1, inplace=True)


#Join Tables matching by subject acession and virus strain to have pre/post in one row
join_columns = ['SUBJECT_ACCESSION','VIRUS_STRAIN']
hai_values_2014 = pd.merge(study_pre_2014, study_post_2014, left_on=join_columns, 
	right_on=join_columns)


#HAI ANALYSIS- calculate differences in vaccine response
#calculate the fold change in titer 
hai_values_2014['FOLD_CHANGE'] = hai_values_2014['POSTVAX'] / hai_values_2014['PREVAX']
hai_values_2014['FOLD_CHANGE_LOG2'] = np.log2(hai_values_2014['FOLD_CHANGE'])
#add a categorical column here for future boxplot
#hai_values_2014['response'] = np.where(hai_values_2014.FOLD_CHANGE_LOG2>=2, "High","Low")
#hai_values_2014

#add subject information for each subject and virus strain row
hai_analysis_2014 = pd.merge(hai_values_2014, subjects_2014,
                             left_on='SUBJECT_ACCESSION', right_on='SUBJECT_ACCESSION' )

hai_analysis_2014.to_csv(r"/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/analysis/hai_analysis_2014.csv", 
	index = False)
