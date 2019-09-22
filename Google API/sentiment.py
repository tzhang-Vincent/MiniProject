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
	return score,magnitude