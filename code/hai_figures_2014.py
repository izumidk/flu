import numpy as np
import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.io as pio
from scipy import stats


# Read analysis file 'hai_analysis_2014.csv' 
# (in the same directory that your python process is based)
hai_analysis_2014 = pd.read_csv("/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/analysis/hai_analysis_2014.csv") 

# group the data in order to generate plots.
hai_by_virus_2014 = hai_analysis_2014.groupby('VIRUS_STRAIN')

#palette for generating transparency
rgba_palette = ["rgba(255,165,0,0.5)", 
                "rgba(0,128,128,0.5)",
                "rgba(128,0,128,0.5)",
                "rgba(128,0,0,0.5)",
                "rgba(230,230,250,0.5)"]


#FUNCTIONS to implement jitter in scatterplots
def rand_jitter(arr):
    stdev = .001*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev

# for log value of data
def rand_jitter_log(arr):
    stdev = .01*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev

##GRAPH LOG OF PRE VS POST/PRE VACCINATION
# set up an empty list to store traces:
data6 = []
# set up counter for changing color at each iteration of the loop
m = 0
for vstrain, gp in hai_by_virus_2014:
    # Define traces for each virus strain:
    vtrace = go.Scatter(
        x = rand_jitter_log(np.log2(gp.PREVAX)),
        y = rand_jitter_log(gp.FOLD_CHANGE_LOG2),
        name = vstrain + " Strain",
        mode = "markers",
        marker = {
            "size" : 10,
            "color" : rgba_palette[m],
            "line" : {
                "width": 2,
                "color" : rgba_palette[m]
            }
        }
    )
    # increment counter!
    m += 1
    # add trace to data
    data6.append(vtrace)

# add annotation to the plot
note = go.Scatter(
    x = [10.3, 10.3],
    y = [1, 3],
    mode='text',
    textfont = {"color" : "rgb(100,100,100)"},
    text = ["Low Response", "High Response"],
    showlegend=False
)
data6.append(note)

# define layout for this plot
layout6 = go.Layout(
    title = "HAI Response vs. Pre-Vaccination HAI Titers",
    xaxis = {
        "title": "HAI Titer - log2(Pre-Vaccination)",
        "titlefont" : {
            "size" : 16,
            "color" : "rgb(107, 107, 107)"
        },
        "tickfont" : {
            "size" : 12,
            "color" : "rgb(107, 107, 107)"
        }
    },
    yaxis ={
        "title": "HAI Response log2(Post/Pre-Vaccination)",
        "titlefont" : {
            "size" : 16,
            "color" : "rgb(107, 107, 107)"
        },
        "tickfont" : {
            "size" : 12,
            "color" : "rgb(107, 107, 107)"
        }
    },
    
     
)

# create a figure object:
fig6 = go.Figure(data=data6, layout=layout6)
pio.write_html(fig6, file='/Users/izumidk/Dropbox (MIT)/20.440/fluprodect/analysis/2014_Fig_1.html', auto_open=True)


