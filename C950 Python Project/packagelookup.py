from packages import package_dictionary, combine_full_address, package_id
import time

# Function used to check the status of a package at the start of the day.
# O(1)
def package_lookup():
	user_input = 0
	user_input = int(input('Check details of package. Enter 1 - 40: '))
	if user_input in range(1,40):
		user_input = str(user_input)
		print("*********************************")
		package_dictionary(user_input)
		print("*********************************")
		time.sleep(3)
		user_input = int(user_input)
	if user_input not in range(1,40):
		print('Invalid Entry')
		time.sleep(3)


# Function to cleanly print the data required for the course
# O(N)
def print_nicely_formatted():
	for index in package_id:
		print("Package ID:", index, "| Address:", combine_full_address(index), "| Deadline:", 
		package_id[index]['delivery_deadline'], '| Package Weight:', package_id[index]['weight'], 
		'| Delivery Status:', package_id[index]['delivery_status'], '| Time Delivered:', package_id[index]['delivered_time'])