# MiniProject


Contributer: <br>
Zhang Ting              ztvince@bu.edu <br>
Haik Harry Martirosyan  haikm@bu.edu

Goal is to create a sentiment analysis of the most visited cities in the world and rank them with the highest and lowest sentiment.

## User Stories

### Travel
<br>I, as an avid backpacker, would like to use information from popular twitter handles to gain an insight on what countries have beautiful landscapes for me to backpack through for a set amount of time. 

<br>I, as an amateur photographer, want to use twitter to determine from popular twitter handles to gain an insight on what photography destinations are highly visited/liked and vice versa to help me build a portfolio. 

<br>I, as a new traveler, want to use twitter accounts in regards to finding the best countries to visit for a new traveler, including low crime rates and ease of traversing the local cities.
<br>
### Cooking
<br>I, as an amateur chef youtuber, want to learn which food dishes are the most popular for me to make as well so that my channel can become more popular

<br>I, as a terrible cook who burns everything, wants to find the most liked beginner tutorial videos so that I don’t waste my time on bad tutorials or more advanced ones
<br>
### Flying
<br>I, as a frequent flier, want to utilize airline twitter news feeds to determine the airlines that receive the most complaints because of flight delays so I can avoid them.
<br>
### Sports
<br>I, as a twitter user who only cares about the tweets related to sports, I would like the product to help me filter out the tweets relevant to the sports news and tips.
<br>
### Normal
<br>I, as a twitter user who likes posting about my own daily life, I would like to increase my twitter’s popularity through the product by seeing which posts have the most likes
<br>
### Image-to-Text
<br>I, as a twitter user who likes viewing only texts and sometimes is unable to understand the actual meaning of the images posted by others, I would like to view the text description of the images posted by others. I can make it easier for me to understand what others try to present.
<br>
### Positive
<br> I, as a twitter user who doesn’t want to view the negative tweets from others, I would like the product to help me screen out only the tweets with positive or neutral messages.
<br>
<br>
## Minimum Viable Product

(We mainly focus on the travelling user story)<br>
We would like to analyze popular twitter feeds in determining popular travel destinations and public positive or negative reactions to them. We will give out the lists containing top 5 and bottom 5 destinations as output results.
## Architecture

Here comes our architecture: <br>

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/system.jpg)


<br>
1. Want to grab data from twitter.
<br>
2. Need to then store it in a some type of large storage product
<br>
3. Will then copy the initial data stored so as to maintain an original version as well as a version to analyze
<br>
4. Run through software to analyze text and image data from tweets<br>
a. Use various image and text datasets from popular destinations to help train system<br>
b. Text-determine reactions whether positive or negative<br>
c. Images -output location and name of site<br>
d. Store in system and assign either a favorable or unfavorable reaction to each picture depending on majority of reactions<br>
5. Output list of most liked and least liked images with assigned locations
<br>

## How does the system work exactly?

Our system can be mainly divided into three parts: Twitter API part, Google API part and the connection & UI part.

### Twitter API
In the folder "Twitter API", we have our tweets_pull_V2.py as our twitter tool to pull the tweets about specific destinations from twitter handles down to our local drive. Each txt file stored in the local drive corresponds to a specific tourists destination.

### Google API
After setting the Google NLP API path in the local shell, we are able to take advantage of the API's sentiment function to analyze the sentiment score and magnitude of each tweet line. By splitting the single txt file into several single lines by '\n', the API will help us analyze each single line's emotion and gives out a score and magnitude for them. Then using some math formula and calculation, we could have final score for each tourist destination. After analyzing all of them, we will sort the score_list which contains the final score by their primary key "score" and return the top N or bottom N results. The number N depends on the UI input.

### UI Connection Part
1. Our system also has a User Interface which can make our product more user friendly.

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/ui1.png)

2. Our UI has several parts: N input, Search Label, Choice for top or bottom, and the final result text box on the right side
After clicking N input part, user could input the N number by himself.

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/ui2.png)

3. After clicking Label, user could choose specific label for tweets. But our project only support the label "/Travel/Tourists Destinations"

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/ui3.png)

4. After clicking choice label, user could choose top N or bottom N to show in the text box right side.

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/ui4.png)

5. After finishing filling all the input parts in the UI, user could just simply click the "Start" button to start the product processing.

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/ui5.png)

6.The tweets combination about a specific destination is stored in local folder "City_tweet_txt".

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/local-tweet.png)

Each single line of a specific destination txt will be stored as a seperate txt file in the local folder "data/{destination}"

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/single_local.png)

7. After the process, the result will show on the text box on the right side.<br>
eg. Top 5:

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/top-result.png)

Bottom 5:

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/bottom-result.png)

## Test
We use the twitter API pull about 41 txt files about 41 travelling destinations and store them in local drive. Each txt file has about 20-70 single lines seperating by '\n'. And it takes about 1 minute.<br>
Then we do the process of splitting the text, analyzing their sentiment, sorting the list and calculated the results which takes about 15 minutes.<br>
Our final tetsing results for top 5 / bottom 5 travelling destinations are shown as below:

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/ui3.png)

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/top-result.png)

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/bottom-result.png)
