import csv
from datetime import datetime

startTime = datetime.now()



# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_map_array(csvFilePath):
	
	# create a list
	data_dict = {}
	visited_suburbs = []
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary 
		# and add it to data
		for rows in csvReader:
			if (rows["official_suburb"]) not in visited_suburbs and rows['official_suburb'] != '':
				visited_suburbs.append(rows['official_suburb'])
				if (rows['latitude'] and rows['longitude']):
					data_dict[rows['official_suburb']] = {
					"type": "Feature",
					"geometry": { "type": "Point", "coordinates": [ rows['longitude'], rows['latitude']] },
					"properties": {'count': 1, 'name': rows['official_suburb']},
					}
			else:
				if (rows['official_suburb'] != ''):
					data_dict[rows['official_suburb']]['properties']['count'] += 1

	
	return data_dict
    
    
	# Open a json writer, and use the json.dumps() 
	# function to dump data
	
		
# Driver Code

# Decide the two file paths according to your 
# computer system
csvFilePath = r'data/sr_hex.csv'
testFilePath = r'data/sr_hex_map_data.txt'

# Call the make_json function
data_dict = make_map_array(csvFilePath)
data = list(data_dict.values())


with open(testFilePath, 'w', encoding='utf-8') as jsonf:
	jsonf.write(str(data))

elapsed_time = datetime.now() - startTime
print(f"Elapsed time: {elapsed_time.total_seconds():.2f} seconds")