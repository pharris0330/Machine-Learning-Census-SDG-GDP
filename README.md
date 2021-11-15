# AdaBoost and Random Forest Regression of GDP and sustainable development goals

## Project Summary
This report explains how I constructed a regression model to conduct an analysis of economic success indicators to determine the strength of feautures. The project will use machine learning to predict economic/sustainable development goal success with the ultimate goal of using the findings to improve local communities. 

Tasks performed in this repo include:
- Webscraping Census data and collecting Bereau of Economic Analysis data
- Preprocessing of data to determine strongest featurs and predictive power
- Regression modeling of features to determine best predictive model
- Created DASH Plotly/Streamlit webapp to display findings

### 1. Background
**Inspiration:** Machine learning can be a powerful in the area of local community develoment. The sustainable development goals (sdg) are a tool created by the United Nations to determine how areas throught the planet are performing in numerous areas important to the development of a region.The sdg can be a useful benchmark in finding strong local development variables. 

In addition to the sdg the gross domestic product is also often utilized to measure economic success of an area. I am interested in finding a feature of economic success with the hopes of better understanding how to improve the economics of my local community. 

I attempted to create a model that could predict the sdg's or GDP for Metropolitan Statistical Areas and states in the US. My hope is that I can use the insight from this project to collect local data and predict the current and future state of a community and focus on the most important features to improve any under performing areas.

### 2. Notebook Structure
- All tasks are placed in [my project repo](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP)


```
Datafolio
  |
  |---datasets
  |       2018_Sdata.csv   (dataframe of business indicators from the American Community Survey)
  |       2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)  
   |      2019_Bdata.csv   (dataframe of business indicators from the American Community Survey)
  |       2019_Sdata.csv   (dataframe of business indicators from the American Community Survey)
  |       gdp_2018.csv   (dataframe of the US GDP in the Metropolitan Statistical Areas (MSA) for 2018)
  |       gdp_2019.csv   (dataframe of the US GDP in the MSAs for 2019)
  |
  |---downloads
         |       2019USCitiesIndexResults.xlsx (excel spreadsheet of 2019 sdg indicators for US MSAs)
         |       2018USCitiesIndexResults.xlsx (excel spreadsheet of 2018 sdg indicators for US MSAs)
         |       2018GDP.xlsx (excel spreadsheet of the 2018 US GDP from the Bureau of Economic Analysis)
         |       2019GDP.xlsx (excel spreadsheet of the 2019 US GDP from the Bureau of Economic Analysis)
```
### 3. Data Collection
**Data Selection:**

[American Community Survery (ACS):](https://www.census.gov/programs-surveys/acs/)

The Census Data offers an API to collect data. The data I utilized came from the ACS. Selection of the census features were based on the data index in the UN sdg dateset. 

"The American Community Survey (ACS) helps local officials, community leaders, and businesses understand the changes taking place in their communities. It is the premier source for detailed population and housing information about our nation." *Census Bureau*

[Bureau of Economic Analysis (BEA) Survey:](https://www.bea.gov/about/who-we-are)

Economist at BEA produce the gross domestic product and other statistics for the Department of Commerce for use by numerous entities. 

"The Bureau of Economic Analysis (BEA) promotes a better understanding of the U.S. economy by providing the most timely, relevant, and accurate economic accounts data in an objective and cost-effective manner." *BEA

[Sustainable Development Goals (SDG):](https://sdgs.un.org/goals)

"The Sustainable Development Goals or Global Goals are a collection of 17 interlinked global goals designed to be a "blueprint to achieve a better and more sustainable future for all". The SDGs were set up in 2015 by the United Nations General Assembly and are intended to be achieved by the year 2030." *-UN*

### 4. EDA

The data from the Census Bureau utilized to create features for the models were obtained from multiple tables on the Census API. SDG and GDP data were downloaded from there respective sites. Once the requisite data was obtained it was then merged. Nulls were taken into consideration and were either removed or replaced with the column average depending on the situation. After data cleaning and wrangling was complete over ten datasets were created to model with and create the web apps. Much time was taken to format the different dateset for the DASH plotly and Streamlit web apps due to there different required formats. 

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/GDPv.SDG.PNG)

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/bachv.gdp.PNG)

SDG Census corellation

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/coorelations%20SDG%20Census.PNG)

Census bureau corellation

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/coorelations.PNG)

2019 SDG score statistics

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/coorelations.PNG)

2019 GDP statistics

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/coorelations.PNG)


### 5. Modeling

Modeling was conducted with KNN, AdaBoost, Random Forest, Decision Tree, and Extra Tree. The model selected for optimization was Random Forest. The primary tool used to optimize the model was scikit-learn's Grid Search CV. The best parameters selected {'max_depth': 4, 'n_estimators': 150}. Cross-Validation = 5.

SDG vs. GDP scores

![SDG vs. GDP scores](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/SDGv.GDPtable.PNG)

Census vs. GDP scores

![Census vs. GDP scores](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/SDGv.GDPtable.PNG)

### 6. Feature importance

Median income rose to the top of feature importance with the SDG Census data. 

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/feature%20importance%20sdg%20census.PNG)

Education attainment rose to the top of feature importance with the GDP Census data. 

![ALt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/feature%20importance%20census%20gdp.PNG)

### 6. Dashboards

DASH plotly

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/bach_gdp_dash.PNG)

DASH Ployly 

![Alt text](https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP/blob/main/Images/model_dash.PNG)

### 7. Results

The Census variables I utilized didn't correlate well with the sustainable development goals. The best model for sdg vs. GDP was XGBoost (test-.99, test-.39).

The Census features I chose correlated well to the US GDP. The best model for Census vs. GDP was Random Forest using Grid Search optimization (test-.96, test-.93).

The median income was starkly higher corellated with the SDG score than the GDP. With further study it would be interesting to see why that if there is a particular reason for that finding. It is also interesting to note that the census features seem to fit better with the GDP than the developmnent scores. Many studies state "economic development" seems to reach more of the populace than "economic growth".

The best feature was Education Attainment in both models. Employment and level of home occupancy were also at top. The presence of graduate degrees weights heavily above the other features. For economical attainment of success highly educated populace is the norm.

In follow on studies I plan to include environmental, social, and behavioral data. Local data, though not as easy to obtain, would prove very helpful. With further study this insight could prove helpful to improve the GDP and SDG of local communities.

 



