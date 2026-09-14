# Crash Data Analysis
## Tasks
- [ ] Download the initial project files: this file and `main.py`
- [ ] Write your first commit adding these files in your repository
- [ ] Inspect the code in `main.py`
- Fill in missing sections of `readme.md`
  - [ ] Fill in *Initial Program Behaviour* section
  - [ ] Fill in the *Basic Analysis Feature* section
- [ ] Commit the changes to `readme.md` and push the changes to your eng-git repository

## Initial Program Behavior
Fill in this section outlining what the program does.
Focus on: 
This program calls the function main() that presents tables and graphs based on crash data. main() uses another function menu_select() to print all the three options:[0] Crash Severity Report,[1] Crash Reports Over Time Graph and [2] Exit. If user inputs 2, the program will print "Bye". If user inputs 1, the program will print "Not Implemented Yet". If user inputs 1, then the program will continously let user input "Year:" and "Speed Limit:". After this, the program calls another function print_crash_severity_report() to print a table outlining the number of crashes in a given year for a given speed limit. In this function, another function unique_values() is called, to return all unique severity types. In the end, the output display "Crash Severity by Classification" \n "Speed:(userinput)" \n "Year:(userinput)" and each severity type followed by their count numbers.
- the form of the initial data
- the meaning of user inputs and program outputs from the program user's perspective

## Dependencies
Fill in this section listing any libraries that the program requires to run.
- Data (Waka Kotahi) CC BY 4.0
- [Pandas](https://pandas.pydata.org/)

## How to Run
To execute this program run following command from a terminal:

`python3 main.py`

## Future Development
Fill in this section outlining features that you would like to expand beyond the minimum features outlined in the second part of the assignment.

### Basic Analysis Feature
You will need to outline at least one analysis that you plan to implement. Please include details on sources of new data required to complete this analysis.

This analysis must feature at least one [matplotlib](https://matplotlib.org/) graph.

My plan 1: To investigate the correlations between number of crashes in different severity types and the year, under a certain speed limit.
To be more specific, use year data (column name == 'crashYear', in CAS_data.csv) as the x-axis and the count number of different severity types (sum up by type with column name == 'crashSeverity') as the y-axis, legend is severity type.
Graph used: Stackplots (as shown in matplotlib), in this case, year is on the x-axis, count numbers are on the y-axis and serverity type is the legend in different colors.

My plan 2: To generate a heatmap of different crash severity type, the density of the heatmap is based on the number of a crash severity type, the x axis is different regions.
Detail: each block in the heatmap represents the number of a specific severity type of crash in a specific region in new zealand. The value of the number: sum up of same region and same severity type, x-annotation : different regions (colname == 'region'), y-annotation: different types of severity (colname == 'crashSeverity')
Graph used: Annotated heatmap (as shown in matplotlib). With this graph being generated, we can visualise the density of defferent crash severity in different region in new zealand.


Examples of basic analysis:

- correlating the speed limit and the severity of crashes
- graphing the number of traffic incidences over time
- ...

### Advanced Features
You are to provide a set of features you will research and develop. They should use libraries **not** presented in the course.

For example you could:

- develop a traffic dashboard using libraries like [streamlit](https://pypi.org/project/streamlit/), [panel](https://pypi.org/project/panel/) or [dash](https://dash.plotly.com/)
- generate Choropleths using [plotly](https://plotly.com/python/choropleth-maps/) that display geographic information on a map
- connect to an Application Programming Interface (API) using [requests](https://pypi.org/project/requests/) to integrate live data into your program

## Citations
As you develop your project you will use a variety of resources. Cite and reference each as using the APA style 7th edition.

- Waka Kotahi. _Crash Analysis System (CAS) data_ [Review of  Crash Analysis System (CAS) data]. Retrieved January 13, 2025, from https://opendata-nzta.opendata.arcgis.com/datasets/8d684f1841fa4dbea6afaefc8a1ba0fc_0/explore