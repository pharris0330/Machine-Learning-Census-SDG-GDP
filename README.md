# AdaBoost and Random Forest Regression of GDP and sustanable development goals

## Project Summary
This report explains how I constructed a regression model to to conduct an analysis of indicators and determine the strength of those feautures to predict economic/SDG gsuccess with the ultimate goal of using the findings to improve local communities. 

Tasks performed in this repo include:
- Webscraping Census data and collecting Bereau of Economic Analysis data
- Preprocessing of data to determine strongest featurs and predictive power
- Regression modeling of features to determine best predictive model
- Created DASH Plotly/Streamlit webapp to display findings

### 1. Background
**Inspiration:** The sustainable development goals (sdg) are tool created by the United Nations to determine how areas throught the planet are performing dvelopmentally in numerous areas. 
"The Sustainable Development Goals or Global Goals are a collection of 17 interlinked global goals designed to be a "blueprint to achieve a better and more sustainable future for all". The SDGs were set up in 2015 by the United Nations General Assembly and are intended to be achieved by the year 2030." -UN
In addition to the sdg the gross domestic product is also often utilized to measure econmic success. I am interested in finding a feature of economic success with the hopes of better understanding how to improve the economics of my local community. 

I attempted to create a model that could predict the sdg'sor GDP for Metropolitan Statistical Areas and states in the US. My hope is that I can use the insight from this project to collect local data and predict the current and future state of a community and focus on the most important features to improve any areas under performing indicators.

### 2. Notebook Structure
- All tasks are performed in __[notebook 2.1]

(https://github.com/amytaylor330/CNN_for_Dance_Music_Classification_repost/blob/master/Part_II/2.1_1D_CNN_for_Multiclassification_of_Techno_Labels.ipynb)__


- The file structure for the datasets used to complete this project are shown below. These additional folders and associated files can be downloaded from dropbox __[here](https://www.dropbox.com/sh/1oqs7l54u5pzpxj/AADCodQE2mG1pfFszu3t8V7Ca?dl=0)__ (with the exception of song_specs.npy and genres.npy, due to size constraints).

```
Datafolio
  |
  |---datasets
  |       2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)
  |       2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)  
   |       2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)
  |       2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)
  |       2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)
  |       lobster_theramin.csv
  |       ostgut_ton.csv
  |       song_specs.npy  (processed mel-spec input array for network. Not available for download)
  |       genres.npy      (associated label inputs for network. Not available for download)
  |
  |---downloads
         |       sdg excel 2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)
         |       gdp from BEA 2018_Bdata.csv   (dataframe of business indicators from the American Community Survey)
         |---kompakt            (folder containing 929 mp3 files)
         |---lobster_theramin   (folder containing 929 mp3 files)
         |---ostgut_ton         (folder containing 929 mp3 files)
```
### 3. Data Collection
**Data Selection:**
Five publicly available Spotify playlists were chosen by performing a google search for the respective record label name. Each label represents a different "genre", or fairly recognizable style of techno music. The number of usable tracks in each playlist ranged from 145 to 439 tracks. It was interesting to find that only 25% of tracks in the Lobster Theramin playlist had an available mp3 link. The reasons for this might be due to different licensing restrictions from this label, or perhaps using a different access token (such as Authorization Code flow rather than Client Credentials) would provide the link.

|Record label| (My Personal) Description of Label | Spotify link|# of Tracks in Playlist| # of Tracks with mp3|
|---| --- | --- |--- | --- |
| Drumcode |percussive, festival techno, filter sweeps common |https://open.spotify.com/playlist/2a9vewgAKwZoYkJVBqJoLH | 712 | 322 |
| Ostgut Ton |dark, experimental, minimal, heady |https://open.spotify.com/playlist/6Edpq3cmRdPdIyzU4J80TC | 318 | 318 |
| Lobster Theramin | lofi, emotive, acid, rolling textures| https://open.spotify.com/playlist/215TGFgN1aCZ94BBouUYKv | 568 | 145 |
| Kompakt | minimal, ambient, experimental|https://open.spotify.com/playlist/7nU5hYoDxu0DmdRm2DQRUt, https://open.spotify.com/playlist/3kCDl9f7jQ8sjVN8wInerl |445 | 439 |
| Dirtybird | deep house / tech house, club tracks|https://open.spotify.com/playlist/2XlbQn0hmv6eH8C16CGIN2 | 244| 205|






### 4. Spectrogram conversion and preprocessing
See __[Part_I](https://github.com/amytaylor330/CNN_for_Dance_Music_Classification_repost/blob/master/Part_I/README.md)__ for explanation.

### 5. Neural Network Architecture
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