import argparse
import io
import json
import os

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import numpy
import six


# Analyze the sentiment of each tweet text and assign them the corresponding score
def sentiment_analysis(text):
	document = language.types.Document(
		content=text,
		type=language.enums.Document.Type.PLAIN_TEXT)
	language_client=language.LanguageServiceClient()
	result=language_client.analyze_sentiment(document)
	score = result.document_sentiment.score
	magnitude = result.document_sentiment.magnitude
	print("score is ",score)
	print("magnitude is ",magnitude)
	return score,magnitude


if __name__ == '__main__':
	sentiment_analysis("Yesterday, I took a train trip from Boston to the New York City. It is really a good experience for my vacation and I enjoy it. During my trip, I took some photos inside the train and recorded lots of amazing scenes")