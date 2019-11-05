# A program that normalizes given columns in a csv file
import csv
import pandas
import numpy 
from sklearn.preprocessing import data

# Function that takes solar data and inserts the essential data needed to 'isolated_data.csv'
def isolate_data():
	with open('_data/isolated_data.csv', 'a') as isolated_data:
		# Reading data & initializing column names
		colnames = ['Date', 'Voltage', 'Watts', 'Integer', '#']
		data = pandas.read_csv('_data/SolarDump03062019.csv', names=colnames)

		# Appending data to isolated data file
		data[['Date', 'Watts']].to_csv(isolated_data, header=None, index=False)

# Function that normalizes the data in 'isolated_data.csv'
def normalize_data():
	with open('_data/normalized_data.csv', 'a') as normdata:
		# Reading the isolated data to work with
		with open('_data/isolated_data.csv', 'r') as isolated_data:
			# Grabbing watts specifically 
			colnames = ['Date', 'Watts']
			file = pandas.read_csv(isolated_data, names=colnames)
			watts = file.Watts
			
			# Normalizing array with sklearn
			processed_data = data.minmax_scale(watts, feature_range=(0, 1), axis=0, copy=True)
		
			# Testing scaled data
			print(processed_data) 

			# Appending data to normalized data file
			# processed_data.to_csv(normdata, header=None, index=False)

# Calling functions
# isolate_data()
normalize_data()