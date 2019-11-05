# A program that normalizes a data set with the given equation
import csv
import pandas
from sklearn.preprocessing import MinMaxScaler

# Function that takes solar data and inserts the essential data needed to 'isolated_data.csv'
def isolate_data():
	with open('_data/isolated_data.csv', 'a') as isolated_data:
		# Reading data & initializing column names
		colnames = ['Date', 'Voltage', 'Watts', 'Integer', '#']
		data = pandas.read_csv('_data/SolarDump03062019.csv', names=colnames)

		# Appending data to isolated data file
		data[['Date', 'Watts']].to_csv(isolated_data, header=None, index=False)

# Function that normalizes the data in 'isolated_data.csv'
# A+(x-a)(B-A)/(b-a)
# A = Set max range
# B = Set min range
# a = Observed max value
# b = Observed min value
# x = All other values that are not the max or min
def normalize_data():
	# Reading the isolated data to work with
	colnames = ['Date', 'Watts']
	data = pandas.read_csv('_data/isolated_data.csv', 'r', names=colnames)

	# Sklearn preprocessing MinMaxScaler() to normalize data
	normalized_data = 

# Calling functions
# isolate_data()