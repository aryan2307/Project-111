import statistics as stats
import pandas as pd
import csv
import random as rd
import plotly.figure_factory as ff

df = pd.read_csv(r"C:/Users/Admin/Downloads/Project 110/data.csv")
time = df["reading_time"].tolist()

mean = stats.mean(time)
std = stats.stdev(time)
meanList = []


dataSet = []
for i in range(0, 30):
    rand_ind = rd.randint(0, len(time)-1)
    value = time[rand_ind]
    dataSet.append(value)
sample_mean = stats.mean(dataSet)
sample_std = stats.stdev(dataSet)

std1_start, std1_end = mean - std, mean + std
std2_start, std2_end = mean - (2*std), mean + (2*std)
std3_start, std3_end = mean - (3*std), mean + (3*std)
print(f"std1 => start: {std1_start}, end: {std1_end}")
print(f"std2 => start: {std2_start}, end: {std2_end}")
print(f"std3 => start: {std3_start}, end: {std3_end}")
z_score = sample_mean - mean / sample_std
print(f"z score: {z_score}")