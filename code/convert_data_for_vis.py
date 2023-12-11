import csv
from datetime import datetime

startTime = datetime.now()



# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_dict(csvFilePath):
	
	# create a dictionary
	data_dict = {}
	
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary 
		# and add it to data
		for rows in csvReader:
			
			if (rows['directorate'] == 'WATER AND SANITATION'):
				key = rows['official_suburb']
				if key in data_dict:
					data_dict[key] += 1
				else:
					data_dict[key] = 1

	return data_dict	
    
    
	# Open a json writer, and use the json.dumps() 
	# function to dump data
	
		
# Driver Code

# Decide the two file paths according to your 
# computer system
csvFilePath = r'data/sr_hex.csv'
testFilePath = r'data/sr_hex_data.txt'

# Call the make_json function
data = make_dict(csvFilePath)
values = []

for k in data.keys():
	if (k != ''):
		values.append({"name": k, "service requests": data[k]})


sorted_suburbs = sorted(values, key=lambda x:x["service requests"])[::-1]

with open(testFilePath, 'w', encoding='utf-8') as jsonf:
	jsonf.write(str(sorted_suburbs))

elapsed_time = datetime.now() - startTime
print(f"Elapsed time: {elapsed_time.total_seconds():.2f} seconds")