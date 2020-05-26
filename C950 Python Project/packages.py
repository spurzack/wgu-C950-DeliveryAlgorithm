import csv
import time
import delivery_sites
from delivery_sites import match_delivery_address

# This function prints details for packages
# O(1)
def package_dictionary(searched_package_id):
    print("Package ID:", searched_package_id)
    print('Address:', combine_full_address((searched_package_id)))
    print('Delivery Deadline:',
          package_id[searched_package_id].get('delivery_deadline'))
    print('Weight:', package_id[searched_package_id].get('weight'), 'Kilos')
    print('Special Information:',
          package_id[searched_package_id].get('package_rules'))
    print('Truck Assignment:', package_id[searched_package_id].get('truck'))
    return print('Delivery Status:', package_id[searched_package_id].get('delivery_status'))

# This function concatenates the full address into a single string
# O(1)
def combine_full_address(searched_id):
    package_id_other = str(searched_id)
    address = package_id[package_id_other].get('address')
    city = package_id[package_id_other].get('city')
    state = package_id[package_id_other].get('state')
    zip_code = package_id[package_id_other].get('zip_code')
    full_address = address + ', ' + city + ', ' + state + " " + zip_code
    return full_address

# Function counts the total packages in a truck
# O(N)
def count_in_truck(truck_number):
    count = 0
    for pid in package_id:
        if package_id[pid]['truck'] == truck_number:
            count = count + 1
    return count


# Nested dicitonary data type was utilized for storing all package information.
package_id = {}

with open('WGUPS Package File.csv', mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        # This process opens the CSV package file
        # Assigns all the package details to a dictionary/hash
        # O(N)
        package_id[row[0]] = {'address': row[1], 'city': row[2], 'state': row[3],
                              'zip_code': row[4], 'delivery_deadline': row[5],
                              'weight': row[6], 'package_rules': row[7],
                              'delivery_status': 'At Hub', 'truck': 'Not Assigned',
                              'delivery_start': '1', 'delivery_end': 'Not Assigned', 'delivered_time': 'Undelivered'
                              }
    for pid in package_id:
        # Assigns each package to a truck 1,2 or 3 based on rules
        # O(N)
        if 'Wrong address' in package_id[pid]['package_rules']:
            package_id[pid]['truck'] = 3
            package_id[pid]['address'] = '410 S State St'
            package_id[pid]['zip_code'] = '84111'
        if 'Can only' in package_id[pid]['package_rules']:
            package_id[pid]['truck'] = 2
        if 'Delayed' in package_id[pid]['package_rules']:
            package_id[pid]['truck'] = 2
        if package_id[pid]['delivery_deadline'] != 'EOD':
            package_id[pid]['truck'] = 1
        if package_id[pid]['truck'] == 'Not Assigned':

            # Assigns any non-special rules packages between trucks 2 and 3
            if count_in_truck(2) < count_in_truck(3):
                package_id[pid]['truck'] = 2
            else:
                package_id[pid]['truck'] = 3

    truck_1 = []
    truck_2 = []
    truck_3 = []

    # Creates a list of packages in each truck
    # O(N)
    for pid in package_id:
        if package_id[pid]['truck'] == 1:
            add_to_truck = int(pid)
            truck_1.append(add_to_truck)
        if package_id[pid]['truck'] == 2:
            add_to_truck = int(pid)
            truck_2.append(add_to_truck)
        if package_id[pid]['truck'] == 3:
            add_to_truck = int(pid)
            truck_3.append(add_to_truck)


# Function takes the delivery address of a package
# Matches that address to a location ID
# O(1)
def get_delivery_id(test_package_id):
    package_id_string = str(test_package_id)
    package_delivery_address = package_id[package_id_string]['address']
    return(match_delivery_address(package_delivery_address))
