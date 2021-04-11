import plotly.express
import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
population_std_dev = statistics.stdev(data)

print("Mean:", population_mean)

def randomSetOfmean(counter):
    dataSet = []
    
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataSet.append(value)
        
    mean2 = statistics.mean(dataSet)
    
    return mean2

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["reading_time"])
    fig.show()

def setup():
    mean_list = []

    for i in range(0, 1000):
        set_of_means = randomSetOfmean(30)
        mean_list.append(set_of_means)
    
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("Sampling mean", mean)

setup()