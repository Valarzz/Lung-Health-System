import os
import pandas as pd
import shutil
import random
import json
import click

@click.command()
@click.option('--dataset', help='Input your image path')
def get_json(dataset):
	root = dataset

	file = pd.read_csv('BBox_List_2017.csv')
	df = pd.DataFrame(file)

	for row in df.iterrows():
		ele = []
		name = row[1]['Image Index']
		lei = row[1]['Finding Label']
		x1 = row[1]['Bbox [x']
		y1 = row[1]['y']
		w = row[1]['w']
		h = row[1]['h]']
		x2 = x1 + w
		y2 = y1 + h
		json_file = {"labels": [{"y1": y1, "x2": x2, "x1": x1, "y2": y2, "name": lei}]}
		json_str = json.dumps(json_file)
		with open(root +'\\'+ name.split('.')[0] + '.json', 'w') as json_file:
			json_file.write(json_str)

if __name__ == '__main__':
	get_json()



