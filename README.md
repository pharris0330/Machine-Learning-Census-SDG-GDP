# AdaBoost and Random Forest Regression of GDP and sustanable development goals

## Project Summary
This report explains how I constructed a regression model to to conduct an analysis of indicators and determine the strength of those feautures to predict economic/SDG gsuccess with the ultimate goal of using the findings to improve local communities. 

Tasks performed in this repo include:
- Webscraping Census data and collecting Bereau of Economic Analysis data
- Preprocessing of data to determine strongest featurs and predictive power
- Regression modeling of features to determine best predictive model
- Created DASH Plotly/Streamlit webapp to display findings

### 1. Background
**Inspiration:** The sustainable development goals (sdg) are a tool created by the United Nations to determine how areas throught the planet are performing in numerous areas important to the development of a region. 

In addition to the sdg the gross domestic product is also often utilized to measure econmic success. I am interested in finding a feature of economic success with the hopes of better understanding how to improve the economics of my local community. 

I attempted to create a model that could predict the sdg's or GDP for Metropolitan Statistical Areas and states in the US. My hope is that I can use the insight from this project to collect local data and predict the current and future state of a community and focus on the most important features to improve any areas under performing indicators.

### 2. Notebook Structure
- All tasks are placed in __[my project repo(https://github.com/pharris0330/Machine-Learning-Census-SDG-GDP)


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

__[American Community Survery (ACS):](https://www.census.gov/programs-surveys/acs/)

The Census Data offers an API to collect data. The data I utilized came from the ACS. Selection of the census features were based on the data index in the UN sdg dateset. 

"The American Community Survey (ACS) helps local officials, community leaders, and businesses understand the changes taking place in their communities. It is the premier source for detailed population and housing information about our nation." *Census Bureau*

__[Bureau of Economic Analysis (BEA) Survey:](https://www.bea.gov/about/who-we-are)

Economist at BEA produce the gross domestic product and other statistics for the Department of Commerce for use by numerous entities. 

"The Bureau of Economic Analysis (BEA) promotes a better understanding of the U.S. economy by providing the most timely, relevant, and accurate economic accounts data in an objective and cost-effective manner." *BEA

__[Sustainable Development Goals (SDG):](https://sdgs.un.org/goals)

"The Sustainable Development Goals or Global Goals are a collection of 17 interlinked global goals designed to be a "blueprint to achieve a better and more sustainable future for all". The SDGs were set up in 2015 by the United Nations General Assembly and are intended to be achieved by the year 2030." *-UN*

### 4. EDA

The data from the Census Bureau utilized to create features for the models were obtained from multiple tables on the Census API. SDG and GDP data were downloaded from there respective sites. Once the requisite data was obtained it was then merged. Nulls were taken into consideration and were either removed or replaced with the column average depending on the situation. After data cleaning and wrangling was complete over ten datasets were created to model with and create the web apps. Much time was taken to format the different dateset for the DASH plotly and Streamlit web apps due to there different required formats. 

![Alt text](https://github.com/amytaylor330/CNN_for_Dance_Music_Classification_repost/blob/master/Part_II/images/results.png)



### 5. Modeling
The same network structure optimized in Part_I was applied here without further optimization. See __[Part_I](https://github.com/amytaylor330/CNN_for_Dance_Music_Classification_repost/blob/master/Part_I/README.md)__ for explanation.

![Alt text](https://github.com/amytaylor330/CNN_for_Dance_Music_Classification_repost/blob/master/Part_I/images/network_architecture.png)

### 6. Results
The 1D CNN was able to predict the correct techno label with 66% accuracy on the training set and 56% accuracy on the test set. Interestingly, a network consisting of only one convolution layer produced similar results, so the network did not appear to be learning more with additional layers. Compared to Part_I, this model could likely have been improved with a different dimension reduction layer other than global max pooling, which is probably recognizing if a certain musical sound is present anywhere in the sound clip and could be contributing to misclassification.

![Alt text](https://github.com/amytaylor330/CNN_for_Dance_Music_Classification_repost/blob/master/Part_II/images/results.png)

Also not surprisingly, the easiest label to recognize was Drumcode (which has a very distinct flavor), while the hardest was Lobster Theramin, which is certainly more diverse, but also had the least number of samples available.

|Label| Total # in Test Set| Overall Accuracy| Most likely to be Misclassified As|
|---|---|---|---|
|Kompakt| 440| 53% | Drumcode > Ostgut Ton |
|Drumcode|320| 82.2 % | Kompakt or Dirtybird |
|Dirtybird|210| 55.2% | Drumcode |
|Lobster Theramin| 140| 20% | Drumcode or Dirtybird |
|Ostgut ton| 320| 49.9% | Kompakt |