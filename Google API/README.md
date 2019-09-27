
Google API has two main functions to help us develop our MVP:<br>
(1) Classification with multiple labels <br>
(2) Sentiment and key words analysis in text

<br>
The example result is like: <br>


![Top 5](https://github.com/tzhang-Vincent/MiniProject/blob/master/Images/top-result.png)

<br>

![Classification](https://github.com/tzhang-Vincent/MiniProject/blob/master/Google%20API/classification.png)
<br>


Using these two functions of Google API, we could find the tweets related to travelling accurately and count their numbers of occurring. Also, we could take advantage of the sentiment analysis to divide the results into two lists: top 5 popular and bottom 5 popular destinations.
<br>


Note Reference: The functions:"classify()", "query_category()", "split_labels()", "similarity()" are referenced by Google NLP API document
<br>
https://cloud.google.com/natural-language/docs/classify-text-tutorial?hl=zh-cn#query_with_text
