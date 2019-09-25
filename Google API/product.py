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
from enum import Enum

class destination(Enum):
	A=1
	B=2
	C=3

def welcome():
	print("Combining Twitter API and Google NLP API, our product could provide you a Top travelling destinations list!")

def outputList(top_num):
	return 0
def get_input():
	number=input("Please Enter a Integer Less than 20 to Decide the Top N\n")
	return number
if __name__ == '__main__':
	welcome()
	top_num=get_input()
	score_list=[]
	for name,member in destination.__members__.items():
		score_list.append(classification.split_txt("C:/Users/Vincent/Desktop/MiniProject/Google API/tweets/{}.txt".format(name),"{}".format(name)))
	# classification.FileForm("C:/Users/Vincent/Desktop/MiniProject/Google API/data/A","A_score")
	# outputList(top_num)

