"""
 Zack Spurlock - Student ID# 000742176

 Section 2: Annotations
 I)
 Greedy Algorithm utilized. Start with the first package in the list and find the closest location among the other packages.
 That closest package location is popped into an organized package list then checked for the next closest package
 I chose the algorithm because it keeps everything simple
 The greedy algorithm finds the next closest destination at all times and doesn't require a ton of recusrion
 The algorithm meets the requirements of sorting each truck's list of packages by the closest destination starting from WGU (The hub) to the next closest package
 A Heuristic algorithm would meet the requirements and can be kind of similar to a greedy algorithm, however, I think greedy is a little more optimal for this scenario
 for the sake of growth, some kind of dynamic algorithm would be best to really help overall.
 
 J)
 If I were to do this project again, I would definitely utilize functions more, especially for getters/setters
 Often times I'm creating objects/variables that can be utlizied again in other places. This would help avoid double work and clutter.
 
 K)
 Nested Dictionaries are the main data structure I use to host all of my Package information and the Distance Table.

 For my package information, I was able to store every package ID as a key.
 In the nested portion of the package key, contains key/value pairs for all package data.
 Keys = type of data (address, weight, etc), values = specific data to that package (410 S Street, 40, etc)
 This data type made it easy to iterate through, keep organized, and update later

 For my Distance Table, any Location (key), inside the nested dictionary was the destination (key) and distance to that destination (value)
 I was able to call this nested dictionary pretty easily to find the distances between two points
 I call the distance graph with the [current location][destination location] to return the distance
 
 It would be very simple to add locations or packages to the nested dictionaries. You would just add another key for the package or location.
 dictionaries seem to be very expandable and flexible while mainting dependable structure

Tuples could be used for the distance table since those don't ever really need to be edited.
I utilized lists a bunch when I needed to sort some data. Lists are great when you need to sort items, pop them, or append to them. Lists are extremely flexible

"""


import time
from distance_algorithm import organize_truck_order, package_delivery_system
from packages import get_delivery_id, reader, truck_1, truck_2, truck_3
from packagelookup import package_lookup

# starting main menu with options
class main:
    # initialize menu at 0
	menu = 0 


    # Calculate total miles driven for the first time main menu is opened
	truck_1_organized_list, total_miles_truck_1 = organize_truck_order(truck_1)
	truck_2_organized_list, total_miles_truck_2 = organize_truck_order(truck_2)
	truck_3_organized_list, total_miles_truck_3 = organize_truck_order(truck_3)
	all_trucks_total = total_miles_truck_1 + total_miles_truck_2 + total_miles_truck_3
	print("+-----------------------------------------+")
	print('    Total miles to deliver packages:', all_trucks_total)
	print("+-----------------------------------------+")


	# Menu options
	while menu is not 3:
		print("""
 1. Lookup a package
 2. Check Package Status at Specific Time
 3. Exit
			""")
		menu = int(
			input("Please choose one of the following menu options (1-3): "))
		# Takes user to general package information at start of day
		if menu == 1:
			package_lookup()

		# Takes user to package tracking
		if menu == 2:
			package_delivery_system()
