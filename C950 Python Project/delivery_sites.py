import csv

# The data type I utlized for Distance Table CSV was a nested dictionary
distance_graph = {}

with open('WGUPS Distance Table.csv', mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        # O(N) 
        distance_graph[row[0]] = {
            'location_id':row[0],
            'location_name':row[1],
            'location_address':row[2],
            '1':row[3],
            '2':row[4],
            '3':row[5],
            '4':row[6],
            '5':row[7],
            '6':row[8],
            '7':row[9],
            '8':row[10],
            '9':row[11],
            '10':row[12],
            '11':row[13],
            '12':row[14],
            '13':row[15],
            '14':row[16],
            '15':row[17],
            '16':row[18],
            '17':row[19],
            '18':row[20],
            '19':row[21],
            '20':row[22],
            '21':row[23],
            '22':row[24],
            '23':row[25],
            '24':row[26],
            '25':row[27],
            '26':row[28],
            '27':row[29]
    }

# Function to find the distance between two locations
# O(1)
def check_distance(starting_location,ending_location):
    distance = float(distance_graph[starting_location][ending_location])
    return distance

# Function used to find the ID of the location by inputting the address
# O(N)
def match_delivery_address(package_address):
    delivery_id = ""
    for row in distance_graph:
        if distance_graph[row]['location_address'] == package_address:
            delivery_id = distance_graph[row]['location_id']
            return delivery_id



                              
                              
