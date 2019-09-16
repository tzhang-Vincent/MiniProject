# MiniProject


Contributer: <br>
Zhang Ting              ztvince@bu.edu <br>
Haik Harry Martirosyan  Haikm@bu.edu

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
<br>
(We mainly focus on the travelling user story)<br>
<br>We would like to analyze popular twitter feeds in determining popular travel destinations and public positive or negative reactions to them. We will give out the lists containing top 5 and bottom 5 destinations as output results.
<br>
<br>
##  Architecture
<br>

![Flowchart](https://github.com/tzhang-Vincent/MiniProject/blob/master/Flowchart.jpg)

<br>
1. Want to grab data from twitter.
<br>
2. Need to then store it in a some type of large storage product
<br>
3. We will then copy the initial data stored so as to maintain an original version as well as a version to analyze
<br>
4. Run through software to analyze text and image data from tweets
Use various image datasets from popular destinations to help train system
Text-determine reactions whether positive or negative
Images -output location and name of site
Store in system and assign either a favorable or unfavorable reaction to each picture 
depending on majority of reactions 
<br>
5. Output list of most liked and least liked images with assigned locations
<br>
