from delivery_sites import check_distance
from packages import get_delivery_id, reader, truck_1, truck_2, truck_3, package_id, package_dictionary
from datetime import datetime, timedelta, time
from itertools import filterfalse
from packagelookup import print_nicely_formatted

# Greedy Algorithm utilized. Start with the first package in the list and find the closest location among the other packages.
# O(n^2)
def organize_truck_order(truck_list):
    original_list = truck_list[:]
    optimized_truck = []
    max_loops = len(original_list)
    current_location = '1'
    total_miles = 0
    i = 0

    # 1st for loops initizalizes values to be adjusted by the 2nd for loop
    for i in range(0, max_loops):
        shortest_distance = 100.0
        chosen_package = 41
        next_location = '0'
        index_position = 0
        j = 0

        # 2nd for loop find the shortest distance and updates values in the 1st loop accordingly
        for j in range(0, len(original_list)):

            # Check's for final value and send it back to WGU
            if len(original_list) == 1:
                next_location = '1'
                shortest_distance = check_distance(
                    current_location, next_location)
                index_position = j
                chosen_package = original_list[j]
                break

            # If distance is shortest, updates shortest distance values
            search_packID = int(original_list[j])
            test = get_delivery_id(search_packID)
            if check_distance(current_location, test) <= shortest_distance:
                shortest_distance = check_distance(current_location, test)
                next_location = test
                index_position = j
                chosen_package = original_list[j]

        package_id[str(chosen_package)]['delivery_start'] = current_location
        package_id[str(chosen_package)]['delivery_end'] = next_location
        optimized_truck.append(original_list[index_position])
        original_list.pop(index_position)
        current_location = next_location
        total_miles = total_miles + shortest_distance
    return optimized_truck, total_miles


# Returns the truck list with packages organized based on delivery and
# the total miles for delivery and return to hub
# O(N^2)
def package_delivery_system():
    truck_1_organized_list, total_miles_truck_1 = organize_truck_order(truck_1)
    truck_2_organized_list, total_miles_truck_2 = organize_truck_order(truck_2)
    truck_3_organized_list, total_miles_truck_3 = organize_truck_order(truck_3)
    truck_1_start = timedelta(hours=8, minutes=0, seconds=0)
    truck_2_start = timedelta(hours=9, minutes=5, seconds=0)
    truck_3_start = timedelta(hours=10, minutes=0, seconds=0)
    user_check_time = input('Please enter a time in the HH:MM:SS format: ')
    (h, m, s) = user_check_time.split(':')
    convert_user_time = timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    # Truck 1 packages are delivered until the time specified by the user
    if truck_1_start <= convert_user_time:
        copy_list_1 = truck_1_organized_list[:]
        change_to_out_for_delivery(truck_1_organized_list)
        while truck_1_start <= convert_user_time and len(copy_list_1) != 0:
            for index in truck_1_organized_list:
                add_minutes = timedelta(minutes=check_distance_time(index)*60)
                if truck_1_start + add_minutes <= convert_user_time:
                    truck_1_start = truck_1_start + add_minutes
                    change_to_delivered(index, truck_1_start)
                    copy_list_1.remove(index)
                else:
                    truck_1_start = truck_1_start + add_minutes
                    copy_list_1.remove(index)

    # Truck 2 packages are delivered until the time specified by the user
    if truck_2_start <= convert_user_time:
        copy_list_2 = truck_2_organized_list[:]
        change_to_out_for_delivery(truck_2_organized_list)
        while truck_2_start <= convert_user_time and len(copy_list_2) != 0:
            for index in truck_2_organized_list:
                add_minutes = timedelta(minutes=check_distance_time(index)*60)
                if truck_2_start + add_minutes <= convert_user_time:
                    truck_2_start = truck_2_start + add_minutes
                    change_to_delivered(index, truck_2_start)
                    copy_list_2.remove(index)
                else:
                    truck_2_start = truck_2_start + add_minutes
                    copy_list_2.remove(index)

    # Truck 3 packages are delivered until the time specified by the user
    if truck_3_start <= convert_user_time:
        copy_list_3 = truck_3_organized_list[:]
        change_to_out_for_delivery(truck_3_organized_list)
        while truck_3_start <= convert_user_time and len(copy_list_3) != 0:
            for index in truck_3_organized_list:
                add_minutes = timedelta(minutes=check_distance_time(index)*60)
                if truck_3_start + add_minutes <= convert_user_time:
                    truck_3_start = truck_3_start + add_minutes
                    change_to_delivered(index, truck_3_start)
                    copy_list_3.remove(index)
                else:
                    truck_3_start = truck_3_start + add_minutes
                    copy_list_3.remove(index)

    print_nicely_formatted()


# updates packages delivery status to delivered and the time delivered
# O(1)
def change_to_delivered(id_package_list, time_delivered):
    package_id[str(id_package_list)]['delivery_status'] = 'Delivered'
    package_id[str(id_package_list)]['delivered_time'] = time_delivered

# Updates packages delivery status to Out for Delivery
# O(N)
def change_to_out_for_delivery(package_list):
    for index in package_list:
        package_id[str(index)]['delivery_status'] = 'Out for Delivery'

# Checks travel time to go from one point to another
# O(1)
def check_distance_time(id_for_package):
    delivery_start_id = package_id[str(id_for_package)]['delivery_start']
    delivery_end_id = package_id[str(id_for_package)]['delivery_end']
    distance = check_distance(delivery_start_id, delivery_end_id)
    time_adjust = distance / 18
    return(time_adjust)
