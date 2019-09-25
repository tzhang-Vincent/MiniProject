import argparse
import io
import json
import os
import re
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import numpy
import six
import sentiment
import classification


def welcome():
	print("Combining Twitter API and Google NLP API, our product could provide you a Top travelling destinations list!")

def outputList(top_num):


def get_input():
	number=input("Please Enter a Integer Less than 20 to Decide the Top N")
	return number
if __name__ == '__main__':
	welcome()
	top_num=get_input()
	
	outputList(top_num)

