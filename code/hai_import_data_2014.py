import pandas as pd



###MAKE TABLE OF SUBJECT INFORMATION (subjects_2014)
#takes in subject.txt (demographic info) and makes pandas dataframe 
subject_file_2014 = "/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/data/subject.txt"
subjects_all_2014 = pd.read_table(subject_file_2014, sep="\t")

#make table with relevant info about each subject
subjects_2014 = subjects_all_2014[['SUBJECT_ACCESSION', 'ANCESTRAL_POPULATION', 'ETHNICITY', 'GENDER', 'RACE']]

#take in subject age to add to subjects_2014
subject_age_file_2014 = "/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/data/arm_2_subject.txt"
subject_age_all_2014 = pd.read_table(subject_age_file_2014, sep="\t")

#make datafrema of subject acession, age, and category
subject_age_2014= subject_age_all_2014[['SUBJECT_ACCESSION', 'MAX_SUBJECT_AGE', 'SUBJECT_PHENOTYPE' ]]

#add age data to subjects_2014
subjects_2014 = pd.merge(subjects_2014, subject_age_2014, 
                                  left_on='SUBJECT_ACCESSION', right_on='SUBJECT_ACCESSION')

#export finalized data table to csv
subjects_2014.to_csv(r"/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/analysis/subjects_2014.csv", index = False)



###MAKE A TABLE OF HAI DATA
#takes in HAI data and makes table
hai_result_file_2014 = "/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/data/hai_result.txt"
hai_all_2014 = pd.read_table(hai_result_file_2014, sep="\t")

#make table with relevant info about each subject
hai_2014=hai_all_2014[['SUBJECT_ACCESSION','STUDY_TIME_COLLECTED','VALUE_PREFERRED','COMMENTS']]
hai_2014.to_csv(r"/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/analysis/hai_2014.csv", index = False)


