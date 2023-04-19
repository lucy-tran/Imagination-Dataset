import csv
import json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
# Acknowledgement: https://www.geeksforgeeks.org/convert-csv-to-json-using-python/ 

def make_json(csvFilePath, jsonFilePath):
	
	# create an array
	data = []
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.reader(csvf)
		count = 1
		
		# Convert each row into a dictionary
		# and add it to data
		for row in csvReader:
			fileDict = {}
			
			# Assuming a column named 'No' to
			# be the primary key
			fileDict["audio_id"] = count
			captions = '...'.join(row[1:]).split('.')
			print(captions)
			caption_arr = [item.lower() for item in captions if item != '']
			fileDict["caption"] = ', '.join(caption_arr)
			fileDict["audio_path"] = row[0] + ".npy"
			data.append(fileDict)
			count += 1

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=3))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'captions.csv'
jsonFilePath = r'dataset.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
