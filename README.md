# NBA-MVP-Prediction

![michael-jordan-mvp-1998](https://user-images.githubusercontent.com/113871039/210287850-a40ad38f-1b1c-42d6-a624-4d82cb120547.jpeg)



by: Troy Hendrickson

# Overview 
This project analyzes existing data about various individuals - some who have been an NBA MVP(most valuable player), and many who have not. To be an MVP in the NBA is easily one of the most challenging individual accomplishments. Voting for MVP is never easy, though some years there are more clear winners than others. And yet, there are also times when a player might seem like an obvious choice for MVP but he still doesn’t win the award.  We use this data in order to develop a predictive model that can aid a stakeholder, The NBA MVP voting panel, in determining whether or not a player should be MVP based on stats. Although this data does not specifically discuss a players specific team success, advanced stats are being taken into effect to evaluate how the game is played today and what attributes coaches and teams deem to be valuable to win nowadays. After utilizing the process of exploratory data analysis, we create several classification models to eventually reach the model with the highest and most appropriate recall.

# Business Understanding
Until the 1979–80 season, the MVP was selected by a vote of NBA players. Since the 1980–81 season, the award is decided by a panel of sportswriters and broadcasters throughout the United States and Canada. Each member of the voting panel casts a vote for first to fifth place selections. Unless there is a unanimous MVP which has only happened once when Stephen Curry won the award in 2015-16, the voting process can be very scrutinized amongst the league among players, coaches, and team officials. The goal here is to create a model that can output the player who is most worthy of the award without any second guessing. 

# Data Analysis
The data that I used for this project comes from a dataset from [FiveThirtyEight](https://data.fivethirtyeight.com/), 'The Best NBA Players, According To RAPTOR' and also a data set from [Kaggle](https://www.kaggle.com/datasets/ryanrabbott/nba-mvp-predictor-dataset?select=NBA_MVP_Predictor_Dataset_2023_November_10th.csv) titled 'NBA MVP Predictor Dataset'. This source is comprised of advanced stats that go beyond the box score and takes into effect the pace of the game, spacing, and the offensive and defensive nuances of the game. This gives stats of all players dating back to 2013 and takes into account of players who have been MVP and who has not. 

The data set included over 33 columns and over 7,000 rows of data that included all advanced stats from past and present once both data sets were merged together. This classification project included the taget variable which was the column `mvp` that gave a numerical value of 0 if a player was not MVP and a value of 1 if a player is an MVP. I kept the latest data that was labeled 2023 seperate from the merged data so that I can use the latest data to test the model on to predict who will be MVP this current year. 


# Exploratory Data Analysis
While cleaning the data by dropping any duplicates that were included in the merge and dropping any null values that occured as well, some exploratory data analysis (EDA) was done to see exactly what MVP's in past have looked like compared to the rest of the league. The advanced stats also helped to determine the best defensive rated players in the league per year to see if defense is something that is taken into account when choosing an MVP. The data also showed that just because a player scores a lot during a season also doesn't mean that they are a shoe in to become an MVP as well.  
![defense](https://user-images.githubusercontent.com/113871039/210636557-b095e813-78da-4d91-b38d-4a3ff6ed5aa8.png)

![scoring title](https://user-images.githubusercontent.com/113871039/210636708-363626e1-3ad4-472d-aadf-31438a70afa9.png)

## Handling Imbalanced Data
Being that the data set only included 9 MVP's out of over 5,000 players in the data set, it is clear that the data is supremely imbalanced. There were about 3 different techniques I used throughout the modeling phase to handle the imbalnce which included over-sampling, under-sampling, and SMOTE. I used all three of these different techniques sporadically to determine the best model. 

# Modeling
After a train test split of the data, I ran about 8 different models to determine which one was the best. For the most part, I focused heavily on recall because I wanted to reduce the number of false negatives as much as possible. False negatives, meaning that a player who were said to not be MVP's but should be, I felt were the most damaging to the model. I also wanted the number of false positives to be as low as possible too because false positives meant that players who were said to be MVP's but should not be. 

The 8 different models that were: 
<img width="877" alt="Screen Shot 2023-01-04 at 3 22 13 PM" src="https://user-images.githubusercontent.com/113871039/210643176-37dd9829-892a-4f9f-9da1-4d4a0a86c518.png">

The reason the first model was chosen is that even though there were other models that had better recall scores, the false positives were a lot higher than the first model. The first model gave the best of bost worlds in which it produced a good recall score and showed to have the least amount of false negatives and false positives. 

![confusion mtx](https://user-images.githubusercontent.com/113871039/210649888-e84e1ba2-7475-4fda-a7a1-893e5e79e928.png)


# Limitations & Next Steps
Some of the limitations that were faced while doing this project is team performance. Almost always a player becomes MVP not only because they themselves are great, but their teams are great too as a result. It was hard to predict who will be MVP this year because the most recent data was only up to November 10th. Teams are known to go on hot or cold streaks throughout the 82 game season so it is tough to predict if a team that started out doing well will continue to do so and vice versa. Same concept goes with players in which some players start the season out very hot and cool off throughout the season and vice versa. This can also result in recency bias in which most fans will gravitate towards a player that is playing well right now. 
Another limitation can be injuries and load management. Players get hurt all the time so it can be hard to predict if a player will or will not be MVP not knowing if the inevitable is in front of them. Also teams are sitting healthy players because of a past injury to lessen the risk of them getting hurt in the future. This process is called load management which causes players to miss games. The more missed games, the less likely it is for a player to be MVP. 

# Observations & Conclusions
Out of the 9 MVPs in the data set, the model that was chosen predicted to be 88% correct. However, all the models for the most part had players that stood out the most while predicting this years MVP. Nikola Jokic looked to be the top winner of the award in which he showed up first on 6 out the 8 models that were ran. Giannis Antetokounmpo showed up second in 5 out of the 8 models and 3rd was a mix up. The model that was chosed had Luka Doncic as 3rd which is the name we will go with for 3rd place.

# For More Information

Please full evaluation breakdown, please check out my [Deployed Model](https://tkhendrix22-nba-mvp-prediction-streamlit-4s7b44.streamlit.app/)


├── Data
├── Images
├──.DS_Store
├──.gitignore
├── MVP Prediction Notebook.ipynb
├── README.md
├── Streamlit.py
├── file1.csv
├── finalpipe1.pkl
└── requirements.txt

