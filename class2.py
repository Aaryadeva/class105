import csv
import pandas as pd
import plotly_express as px

with open('graphs/class2.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
#to remove header from CSV
file_data.pop(0)

total_entries=len(file_data)

total_marks=0

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks/total_entries

file = pd.read_csv('graphs/class2.csv')
fig = px.scatter(file,x='Student Number',y='Marks')
fig.update_layout(shapes=[
    dict(
        type='line',
        x0=0,x1=total_entries,
        y0=mean,y1=mean
    )
])
fig.show()

