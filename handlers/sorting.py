# COMPANY = "CoolAsia"
VERISON = "1.0"

# Date and time
from datetime import datetime

# Emails
import smtplib
import urllib2
import socket
import urlparse
import hmac
import base64
import hashlib

import logging
import urllib

from google.appengine.api import taskqueue
from model.admin_account import postalRecordDB

import itertools

# sorting function for company
import sorting_company

def sort_by_postals_chunck(starting_address, postal_sequence_list, vehicle_quantity, email, has_return,
                           priority_capacity, priority_capacity_comp, api_user,
                           sort_company, truck_capacity_grp, options_truck):
    starting_address = str(starting_address)

    if sort_company == "true":
        starting_address_seq = [starting_address, "", "", ""]
    else:
        starting_address_seq = [starting_address, 0, 0]

    # Postal_dictionary to store same postal codes into 10
    # Postal_list refers to the unique list of postals codes
    # Order_dict to store all the specific details pertaining to the order

    grp_truck = []

    if sort_company == "true":

        postal_dictionary, postal_list, order_dict, capacity_dic, capacity_list, company_list = sorting_company.setLists_company(
            postal_sequence_list)
    else:
        postal_dictionary, postal_list, order_dict, capacity_dic, capacity_list = setLists(postal_sequence_list)

    # Sorted Postal Code
    postal_sorted = sort_by_postals(starting_address, postal_sequence_list, sort_company)

    if priority_capacity == "true":

        # If the OrderID and Load Capacity are not complete
        if checker_order_capacity(postal_sequence_list) == True:

            # Propose Route
            num_of_truck = len(postal_sorted) / float(vehicle_quantity)
            vehicle_postal_list_new = chunkIt(postal_sorted, num_of_truck)

            # Current Route
            num_of_truck_1 = len(postal_list) / float(vehicle_quantity)
            vehicle_current_postal_list = chunkIt(postal_list, num_of_truck_1)

            # Sequence Route
            num_of_truck_seq = len(postal_list) / float(vehicle_quantity)
            vehicle_postal_list_new_seq = chunkIt(postal_list, num_of_truck_seq)

        # Else OrderID and Load Capacity are complete
        else:

            # Find Postal code that match to the Current cargo unit
            result_postal = []
            result_postal_seq = []

            for i in range(len(postal_sorted)):
                postal = postal_sorted[i]

                for x in range(len(postal_sequence_list)):
                    order_postal = postal_sequence_list[x]

                    postal2 = order_postal[0]
                    orderId = order_postal[1]
                    capacity = order_postal[2]

                    # If postal codes has length of 5
                    if len(postal2) == 5:
                        postal2 = "0" + postal2

                    # If postal codes match, display the relevant Capacity loads
                    if postal == postal2:
                        result_postal_seq.append([postal, orderId, capacity])
                        result_postal.append([postal, capacity])

            # Chunk the Postal code according to minimum truck capacity
            # Define and assign variables for truck
            truck_dictionary = truck_details(truck_capacity_grp)

            # Chunk according to Capacity / No of truck
            vehicle_postal_list_new = list(chunk_to_sum_no_truck(result_postal, *truck_capacity_grp, **truck_dictionary))

            # Current Route
            vehicle_current_postal_list = list(chunk_to_sum_no_truck(capacity_list, *truck_capacity_grp, **truck_dictionary))

            # for Postal Seq
            vehicle_postal_list_new_seq = list(chunk_to_sum_no_truck_sequence(result_postal_seq, *truck_capacity_grp, **truck_dictionary))

            # for Current Postal Seq
            vehicle_postal_list_orig_seq = list(chunk_to_sum_no_truck_sequence(postal_sequence_list, *truck_capacity_grp, **truck_dictionary))

            # example output of truck
            "for 2 = {'max_1': 2, 'max_2': 2, 'truck_1': 'MK100', 'truck_2': 'MK200', 'target_2': 7, 'target_1': 8}"

            list_truck = []

            count = 0

            for x in range(len(vehicle_postal_list_new_seq)):
                new_x = vehicle_postal_list_new_seq[x]

                count += 1
                # if the truck input fields is set by three
                if len(truck_capacity_grp) == 3:

                    min_truck1 = truck_dictionary['max_1']
                    min_truck2 = truck_dictionary['max_2']

                    truck_name1 = truck_dictionary['truck_1']
                    truck_name2 = truck_dictionary['truck_2']
                    truck_name3 = truck_dictionary['truck_3']

                    if count <= int(min_truck1):

                        list_truck.append(truck_name1)

                    # reset the max 1
                    elif count - int(min_truck1) <= int(min_truck2):

                        list_truck.append(truck_name2)

                    else:

                        list_truck.append(truck_name3)

                # if the truck input fields is set by two
                elif len(truck_capacity_grp) == 2:

                    min_truck1 = truck_dictionary['max_1']

                    # variable from truck dictionary
                    truck_name1 = truck_dictionary['truck_1']
                    truck_name2 = truck_dictionary['truck_2']

                    if count <= int(min_truck1):

                        list_truck.append(truck_name1)

                    else:

                        list_truck.append(truck_name2)
                else:

                    min_truck1 = truck_dictionary['max_1']
                    truck_name1 = truck_dictionary['truck_1']

                    if count <= int(min_truck1):

                        list_truck.append(truck_name1)

            grp_truck.append(list_truck)

            # Number of vehicle allocated
            num_of_vehicles = len(vehicle_postal_list_new)
            vehicle_quantity = num_of_vehicles

    elif sort_company == "true" and priority_capacity_comp == "true":

        result_postal = []
        result_postal_seq = []

        for i in range(len(postal_sorted)):
            postal = postal_sorted[i]

            for x in range(len(postal_sequence_list)):
                order_postal = postal_sequence_list[x]

                postal2 = order_postal[0]
                orderId = order_postal[1]
                capacity = order_postal[2]
                campany_id = order_postal[3]

                # If postal codes has length of 5
                if len(postal2) == 5:
                    postal2 = "0" + postal2

                # If postal codes match, display the relevant Capacity loads
                if postal == postal2:
                    result_postal_seq.append([postal, orderId, capacity, campany_id])
                    result_postal.append([postal, capacity])

        # Define and assign variables for truck
        truck_dictionary_comp = truck_details(truck_capacity_grp)

        # Chunk according to Capacity / No of truck
        vehicle_postal_list_new = list(chunk_to_sum_no_truck_comp(result_postal, *truck_capacity_grp, **truck_dictionary_comp))

        # Current Route
        vehicle_current_postal_list = list(chunk_to_sum_no_truck_comp(capacity_list, *truck_capacity_grp, **truck_dictionary_comp))

        # For proposed Postal Sequence
        vehicle_postal_list_new_seq = list(chunk_to_sum_no_truck_seq_comp(result_postal_seq, *truck_capacity_grp, **truck_dictionary_comp))

        # For Current Postal Sequence  # vehicle_postal_list_orig_seq
        vehicle_postal_list_orig_seq = list(chunk_to_sum_no_truck_seq_comp(postal_sequence_list, *truck_capacity_grp, **truck_dictionary_comp))

    else:

        # Route for Multiple Trucks's optimisation
        # 1. Chunk the list
        # 2. Find the postal codes match, display to the relevant Order ID

        # Consolidate Delivery for Multiple Companies using Multiple Truck's optimisation
        # 1. Chunk the list
        # 2. Find postal code match to the current relevant order ID

        # Proposed Route
        vehicle_postal_list_new = chunkIt(postal_sorted, vehicle_quantity)

        # Current Route
        vehicle_current_postal_list = chunkIt(postal_list, vehicle_quantity)

        result_postal_orders2 = []
        current_postal_orders = []

        if sort_company == "true":

            # Proposed Postal code sequence display in UI:
            # result_postal_orders2 = []

            for new_list in vehicle_postal_list_new:
                new_list_chuncked = new_list

                result_postal_orders1 = []

                for chunked in new_list_chuncked:
                    new_postal_code = chunked

                    for x in range(len(postal_sequence_list)):
                        old_postal_sequence = postal_sequence_list[x]

                        postal_old = old_postal_sequence[0]
                        order_id = old_postal_sequence[1]
                        capacity_load = old_postal_sequence[2]
                        campany_id = old_postal_sequence[3]

                        if new_postal_code == postal_old:
                            result_postal_orders1.append([new_postal_code, order_id, capacity_load, campany_id])

                result_postal_orders2.append(result_postal_orders1)

        else:

        # if options_truck == "true":

            # Proposed Postal code sequence display in UI:
            for new_list in vehicle_postal_list_new:
                new_list_chuncked = new_list

                result_postal_orders1 = []

                for chunked in new_list_chuncked:
                    new_postal_code = chunked

                    for x in range(len(postal_sequence_list)):
                        old_postal_sequence = postal_sequence_list[x]

                        postal_old = old_postal_sequence[0]
                        order_id = old_postal_sequence[1]
                        capacity_load = old_postal_sequence[2]

                        if new_postal_code == postal_old:
                           result_postal_orders1.append([new_postal_code, order_id, capacity_load])

                result_postal_orders2.append(result_postal_orders1)

            # Proposed Postal code sequence display in UI:
            for current_list in vehicle_current_postal_list:
                current_list_chuncked = current_list

                current_postal = []

                for current_chunck in current_list_chuncked:
                    current_chuncked = current_chunck

                    for x in range(len(postal_sequence_list)):
                        old_postal_sequence = postal_sequence_list[x]

                        postal_old = old_postal_sequence[0]
                        order_id = old_postal_sequence[1]
                        capacity_load = old_postal_sequence[2]

                        if current_chuncked == postal_old:
                           current_postal.append([current_chuncked, order_id, capacity_load])

                current_postal_orders.append(current_postal)

        # Propose Route w/ OrderID & Load Capacity display in UI
        vehicle_postal_list_new_seq = result_postal_orders2
        vehicle_postal_list_orig_seq = current_postal_orders

        # vehicle_capacity = 0

    # Adding HQ Postal Code in truck delivery route < Returning vehicle >
    if has_return == "true":

        for vehicle_postal_list_return in vehicle_postal_list_new:
            vehicle_postal_list_return.append(starting_address)

        for vehicle_postal_list_return_curent in vehicle_current_postal_list:
            vehicle_postal_list_return_curent.append(starting_address)

        for vehicle_postal_list_return_seq in vehicle_postal_list_new_seq:
            vehicle_postal_list_return_seq.append(starting_address_seq)

        for vehicle_postal_list_orig_seq_order in vehicle_postal_list_orig_seq:
            vehicle_postal_list_orig_seq_order.append(starting_address_seq)

    origin_destination = startingpoint_latlong(starting_address)

    # Set the default value to Timestamp as unique ID
    compare_id = datetime.now().strftime('%Y%m%d%H%m%f')

    # Data storing postal code
    ############################
    # Converting to string of this Proposed data
    proposedPostlal = convert_to_string(vehicle_postal_list_new)

    # Converting to string of this Current data
    currentdPostlal = convert_to_string(vehicle_current_postal_list)

    # Converting to string of this Sequence data
    proposed_postal_array = []
    proposed_order_array = []
    proposed_cargo_array = []

    current_postal_array = []
    current_order_array = []
    current_cargo_array = []

    # if priority_capacity == "true":
    # Propose Sequence
    for index in range(len(vehicle_postal_list_new_seq)):
        updated_postal_seq = vehicle_postal_list_new_seq[index]

        postal_array_inner = []
        order_array_inner = []
        cargo_array_inner = []

        for order_list in updated_postal_seq:

            postal_array_inner.append(order_list[0])
            order_array_inner.append(order_list[1])
            cargo_array_inner.append(order_list[2])

        proposed_postal_array.append(postal_array_inner)
        proposed_order_array.append(order_array_inner)
        proposed_cargo_array.append(cargo_array_inner)

    # Current Sequence
    for index in range(len(vehicle_postal_list_orig_seq)):
        current_postal_seq = vehicle_postal_list_orig_seq[index]

        postal_array_inner = []
        order_array_inner = []
        cargo_array_inner = []

        for order_list in current_postal_seq:

            postal_array_inner.append(order_list[0])
            order_array_inner.append(order_list[1])
            cargo_array_inner.append(order_list[2])

        current_postal_array.append(postal_array_inner)
        current_order_array.append(order_array_inner)
        current_cargo_array.append(cargo_array_inner)

    # Proposed List
    proposed_postal_grp = convert_to_string(proposed_postal_array)
    proposed_order_grp = convert_to_string(proposed_order_array)
    proposed_cargo_grp = convert_to_string(proposed_cargo_array)

    # Current List
    current_postal_grp = convert_to_string(current_postal_array)
    current_order_grp = convert_to_string(current_order_array)
    current_cargo_grp = convert_to_string(current_cargo_array)

    # Truck Details:
    grp_truck_name = convert_to_string(grp_truck)

    num_user_load = "true"

    # User Count
    if api_user == "true":
        print "Data are from API User"

        taskqueue.add(url='/sorting-proposed-api',
                      params=({'compare_id': compare_id,
                               'starting_address': starting_address,
                               # 'origin_destination': origin_destination,
                               'proposedPostlal': proposedPostlal,
                               'currentdPostlal': currentdPostlal,
                               'has_return': has_return,
                               'email': email,
                               'num_of_vehicle': vehicle_quantity,
                               #'vehicle_capacity': vehicle_capacity,
                               'num_user_load': num_user_load
                               })
                      )

    else:
        print ('Route task added to the queue.')
        taskqueue.add(url='/sorting-proposed',

                      params=({'compare_id': compare_id,
                               'starting_address': starting_address,

                               'proposedPostlal': proposed_postal_grp,
                               'proposed_order_grp': proposed_order_grp,
                               'proposed_cargo_grp': proposed_cargo_grp,

                               'currentdPostlal': current_postal_grp,
                               'current_order_grp': current_order_grp,
                               'current_cargo_grp': current_cargo_grp,

                               'grp_truck_name': grp_truck_name,
                               'has_return': has_return,

                               'email': email,
                               'num_of_vehicle': vehicle_quantity,
                               'priority_capacity': priority_capacity,
                               'sort_company': sort_company,
                               'num_user_load': num_user_load,

                               })
                      )

    # Return the result again to "Sorting_prep.py"
    return origin_destination, vehicle_postal_list_new, vehicle_current_postal_list, vehicle_postal_list_new_seq, grp_truck

# Function for assigning Variable to Truck Types:

def chunk_to_sum_no_truck_comp(iterable, *list, **params):

    chunk_sum = 0.0
    chunk = []
    array = []

    # If else = if type truck capacity input = 3, 2 and 1
    # Enter Max Truck Capacity *
    # target_1 = params['target_1']
    # - - - - - - - - - - - - - - - #
    # No. of Truck
    # max_1 = params['max_1']
    # - - - - - - - - - - - - - - - #
    # e.g: Each truck has a capacity of 3 (box),
    # company have 3 truck available : 3 x 3 = 9
    # group_truck = target_1 * max_1

    if len(list) == 3:

        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']
        target_3 = params['target_3']

        # No. of Truck
        max_1 = params['max_1']
        max_2 = params['max_2']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9
        # group_truck = target_1 * max_1
        group_truck_1 = target_1 * max_1
        group_truck_2 = target_2 * max_2

        for key, item in iterable:
            chunk_sum += item

            if len(array) <= group_truck_1:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)

            elif len(array) <= group_truck_2:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)
            else:

                if chunk_sum > target_3:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)

            array.append(chunk)

    elif len(list) == 2:

        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']

        # No. of Truck
        max_1 = params['max_1']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9
        # group_truck = target_1 * max_1
        group_truck = target_1 * max_1

        for key, item in iterable:
            chunk_sum += item

            if len(array) <= group_truck:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)
            else:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)

            array.append(chunk)

    else:

        # if one type of truck input:
        target_1 = params['target_1']

        for key, item in iterable:
            chunk_sum += item

            if chunk_sum > target_1:

                yield chunk
                chunk = [key]
                chunk_sum = item
            else:
                chunk.append(key)

    if chunk:
        yield chunk

def chunk_to_sum_no_truck_seq_comp(iterable, *list, **params):

    chunk_sum = 0.0
    chunk = []
    array = []

    # If else = if type truck capacity input = 3, 2 and 1
    # Enter Max Truck Capacity *
    # target_1 = params['target_1']
    # - - - - - - - - - - - - - - - #
    # No. of Truck
    # max_1 = params['max_1']
    # - - - - - - - - - - - - - - - #
    # e.g: Each truck has a capacity of 3 (box),
    # company have 3 truck available : 3 x 3 = 9
    # group_truck = target_1 * max_1
    if len(list) == 3:

        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']
        target_3 = params['target_3']

        # No. of Truck
        max_1 = params['max_1']
        max_2 = params['max_2']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9
        # group_truck = target_1 * max_1
        group_truck_1 = target_1 * max_1
        group_truck_2 = target_2 * max_2

        for x in range(len(iterable)):
            chunk_seq = iterable[x]

            key = chunk_seq[0]
            order = chunk_seq[1]
            item = chunk_seq[2]
            comp = chunk_seq[3]

            chunk_sum += item

            if len(array) <= group_truck_1:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [[key, order, item, comp]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item, comp])

            elif len(array) <= group_truck_2:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [[key, order, item, comp]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item, comp])
            else:

                if chunk_sum > target_3:

                    yield chunk
                    chunk = [[key, order, item, comp]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item, comp])

            array.append(chunk)

    elif len(list) == 2:

        print "Hello"
        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']

        # No. of Truck
        max_1 = params['max_1']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9
        # group_truck = target_1 * max_1
        group_truck = target_1 * max_1

        for x in range(len(iterable)):
            chunk_seq = iterable[x]

            key = chunk_seq[0]
            order = chunk_seq[1]
            item = chunk_seq[2]
            comp = chunk_seq[3]

            chunk_sum += item

            if len(array) <= group_truck:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [[key, order, item, comp]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item, comp])
            else:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [[key, order, item, comp]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item, comp])

            array.append(chunk)

    else:

        target_1 = params['target_1']
        max_1 = params['max_1']
        group_truck_1 = target_1 * max_1

        for x in range(len(iterable)):
            chunk_seq = iterable[x]

            key = chunk_seq[0]
            order = chunk_seq[1]
            item = chunk_seq[2]
            comp = chunk_seq[3]

            chunk_sum += item

            if len(array) <= group_truck_1:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [[key, order, item, comp]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item, comp])

            # else:
            #
            #     if chunk_sum > target_2:
            #
            #         yield chunk
            #         chunk = [[key, order, item, comp]]
            #         chunk_sum = item
            #     else:
            #         chunk.append([key, order, item, comp])

            array.append(chunk)

    if chunk:
        yield chunk

# Function for Truck Capacity - no sequence format

def truck_details(list):

    target_list = []
    max_list = []
    truck_name_list = []
    truck_dictionary = {}

    if len(list) == 2:

        for i in range(0, len(list)):
            # Retrieve each truck pair
            truck_pair = list[i]

            # Lay dow the items of truck_pair
            truck_name = str(truck_pair[0].strip())
            target = int(truck_pair[1])
            max = int(truck_pair[2])

            # append each items:
            truck_name_list.append(truck_name)
            target_list.append(target)
            max_list.append(max)

        truck_1 = truck_name_list[0]
        truck_2 = truck_name_list[1]
        target_1 = target_list[0]
        target_2 = target_list[1]
        max_1 = max_list[0]
        max_2 = max_list[0]

        truck_dictionary = {
            "truck_1": truck_1,
            "truck_2": truck_2,
            "target_1": target_1,
            "target_2": target_2,
            "max_1": max_1,
            "max_2": max_2,
        }

    elif len(list) == 3:
        # if the type of Truck are to 3:

        for i in range(0, len(list)):
            # Retrieve each truck pair
            truck_pair = list[i]

            # Lay dow the items of truck_pair
            truck_name = str(truck_pair[0].strip())
            target = int(truck_pair[1])
            max = int(truck_pair[2])

            # append each items:
            truck_name_list.append(truck_name)
            target_list.append(target)
            max_list.append(max)

        truck_1 = truck_name_list[0]
        truck_2 = truck_name_list[1]
        truck_3 = truck_name_list[2]
        target_1 = target_list[0]
        target_2 = target_list[1]
        target_3 = target_list[2]
        max_1 = max_list[0]
        max_2 = max_list[1]
        max_3 = max_list[2]

        truck_dictionary = {
            "truck_1": truck_1,
            "truck_2": truck_2,
            "truck_3": truck_3,
            "target_1": target_1,
            "target_2": target_2,
            "target_3": target_3,
            "max_1": max_1,
            "max_2": max_2,
            "max_3": max_3,
        }

    else:

        # if type of truck is 1:
        # Lay dow the items of truck_pair

        for i in list:
            list2 = i
            truck_1 = str(list2[0])
            target_1 = int(list2[1])
            max_1 = int(list2[2])

            truck_dictionary = {
                "truck_1": truck_1,
                "target_1": target_1,
                "max_1": max_1,
            }

    return truck_dictionary

def chunk_to_sum_no_truck(iterable, *list, **params):

    chunk_sum = 0.0
    chunk = []
    array = []

    # If else = if type truck capacity input = 3, 2 and 1

    if len(list) == 3:

        " {'max_3': 1, 'max_2': 2, 'target_1': 5, 'target_2': 7, 'target_3': 5, 'truck_3': 'Mk30000', 'truck_2': 'MK200', 'truck_1': 'MK100', 'max_1': 2} "
        # target_1 x max_1 == 5 x 2 = 10
        # target_2 x max_2 == 7 x 2 = 14

        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']
        target_3 = params['target_3']

        # No. of Truck
        max_1 = params['max_1']
        max_2 = params['max_2']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9
        # group_truck = target_1 * max_1
        group_truck_1 = target_1 * max_1
        group_truck_2 = target_2 * max_2

        for key, item in iterable:
            chunk_sum += item

            if len(array) <= group_truck_1:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)

            elif (len(array) - group_truck_1) <= group_truck_2:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)
            else:

                if chunk_sum > target_3:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)

            array.append(chunk)

    elif len(list) == 2:

        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']

        # No. of Truck
        max_1 = params['max_1']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9
        # group_truck = target_1 * max_1
        group_truck = target_1 * max_1

        for key, item in iterable:
            chunk_sum += item

            if len(array) <= group_truck:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)
            else:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [key]
                    chunk_sum = item
                else:
                    chunk.append(key)

            array.append(chunk)

    else:

        # if one type of truck input:
        target_1 = params['target_1']

        for key, item in iterable:
            chunk_sum += item

            if chunk_sum > target_1:

                yield chunk
                chunk = [key]
                chunk_sum = item
            else:
                chunk.append(key)

    if chunk:
        yield chunk

# Function for Truck Capacity - sequence format
def chunk_to_sum_no_truck_sequence(iterable, *list, **params):

    chunk_sum = 0.0

    chunk = []
    array = []

    # If else = if type truck capacity input = 3, 2 and 1
    # List  - the group of trucks
    # Params - are the value of Truck dictionary
    """
    sample dict of truck
    {
    'max_1': 2, 'max_2': 2, 'max_3': 1,
    'target_1': 5, 'target_2': 7, 'target_3': 5,
    'truck_1': 'MK100', 'truck_2': 'MK200', 'truck_3': 'Mk30000',
    }
    """
    # Get number of truck entered in the fields
    if len(list) == 3:

        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']
        target_3 = params['target_3']

        # No. of Truck
        max_1 = params['max_1']
        max_2 = params['max_2']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9
        # group_truck = target_1 * max_1
        group_truck_1 = target_1 * max_1
        group_truck_2 = target_2 * max_2

        for x in range(len(iterable)):

            chunk_seq = iterable[x]

            key = chunk_seq[0]
            order = chunk_seq[1]
            item = chunk_seq[2]

            chunk_sum += item

            if len(array) <= group_truck_1:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [[key, order, item]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item])

            elif (len(array) - group_truck_1) <= group_truck_2:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [[key, order, item]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item])
            else:

                if chunk_sum > target_3:

                    yield chunk
                    chunk = [[key, order, item]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item])

            array.append(chunk)

    elif len(list) == 2:

        # Enter Max Truck Capacity *
        target_1 = params['target_1']
        target_2 = params['target_2']

        # No. of Truck
        max_1 = params['max_1']

        # e.g: Each truck has a capacity of 3 (box),
        # company have 3 truck available : 3 x 3 = 9

        group_truck = target_1 * max_1

        for x in range(len(iterable)):
            chunk_seq = iterable[x]

            key = chunk_seq[0]
            order = chunk_seq[1]
            item = chunk_seq[2]

            chunk_sum += item

            if len(array) <= group_truck:

                if chunk_sum > target_1:

                    yield chunk
                    chunk = [[key, order, item]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item])
            else:

                if chunk_sum > target_2:

                    yield chunk
                    chunk = [[key, order, item]]
                    chunk_sum = item
                else:
                    chunk.append([key, order, item])

            array.append(chunk)

    else:

        # if one type of truck input:
        target_1 = params['target_1']

        for x in range(len(iterable)):
            chunk_seq = iterable[x]

            key = chunk_seq[0]
            order = chunk_seq[1]
            item = chunk_seq[2]

            chunk_sum += item

            if chunk_sum > target_1:

                yield chunk
                chunk = [[key, order, item]]
                chunk_sum = item
            else:
                chunk.append([key, order, item])
    # edit
    if chunk:
        yield chunk

# Sorting happening here:
def sort_by_postals(starting_address, postal_sequence_list, sort_company):

    # Set the up the required lists
    # Postal_dictionary to store same postal codes into 10
    # Postal_list refers to the unique list of postal codes
    # Order_dict to store all the specific details pertaining to the order

    if sort_company == "true":

        postal_dictionary, postal_list, order_dict, capacity_dic, capacity_list, company_list = sorting_company.setLists_company(
            postal_sequence_list)
    else:
        # Get the starting address
        postal_dictionary, postal_list, order_dict, capacity_dic, capacity_list = setLists(postal_sequence_list)

    starting_address = str(starting_address)

    # Obtain ranked postal codes
    areaCodeRanking_dict = createPostalRanking()

    # Sort the postal code using AreCodeRanking Dictionary
    custPostal_arr_sorted = sortPostalArray(areaCodeRanking_dict, postal_list)

    # Split postal codes into list for each vehicle
    # vehicle_postal_list = chunkIt(custPostal_arr_sorted, num_of_vehicle)
    vehicle_postal_list = chunkIt(custPostal_arr_sorted, 1)

    # Set the Starting postal code near in 1st rank of postal code
    actual_vehicle_postal_list = []
    starting_address_arr = []

    starting_address_arr.append(starting_address)
    starting_rank = setPostalRank(areaCodeRanking_dict, starting_address_arr).values()[0]

    actual_vehicle_postal = []

    # List of sorted Postal Code >= Single Hq Postal Code
    for vehicle_postal in vehicle_postal_list:

        ranked_postal = setPostalRank(areaCodeRanking_dict, vehicle_postal)

        less_than_starting_point = []

        if len(ranked_postal) > 0:

            filtered_postal = ((k, v) for k, v in ranked_postal.items() if v >= int(starting_rank))
            sorted_postal = sorted(dict(filtered_postal).items(), key=lambda x: (x[1], x[0]), reverse=False)


            for key in sorted_postal:
                less_than_starting_point.append(str(key).split(",")[0].replace("(", "").replace("'", ""))

            # 2nd batch
            filtered_postal = ((k, v) for k, v in ranked_postal.items() if v < int(starting_rank))

            if len(sorted_postal) > 0:
                sorted_postal = sorted(dict(filtered_postal).items(), key=lambda x: (x[1], x[0]), reverse=False)

            else:
                sorted_postal = sorted(dict(filtered_postal).items(), key=lambda x: (x[1], x[1]))

            for key in sorted_postal:
                less_than_starting_point.append(str(key).split(",")[0].replace("(", "").replace("'", ""))

            actual_vehicle_postal.append(less_than_starting_point)

    # print ('actual_vehicle_postal'), actual_vehicle_postal
    for actual_vehicle_postals in actual_vehicle_postal:
        actual_vehicle_postal_new = actual_vehicle_postals

        return actual_vehicle_postal_new

def chunk_to_sum2_comp(iterable, target):
    chunk_sum = 0.0
    chunk = []

    for x in range(len(iterable)):
        chunk_seq = iterable[x]

        key = chunk_seq[0]
        order = chunk_seq[1]
        item = chunk_seq[2]
        comp = chunk_seq[3]

        chunk_sum += item

        if chunk_sum > target:
            yield chunk
            chunk = [[key, order, item, comp]]
            chunk_sum = item
        else:
            chunk.append([key, order, item, comp])
    if chunk:
        yield chunk

def chunk_to_sum2(iterable, target):
    chunk_sum = 0.0
    chunk = []
    for x in range(len(iterable)):
        chunk_seq = iterable[x]

        key = chunk_seq[0]
        order = chunk_seq[1]
        item = chunk_seq[2]

        chunk_sum += item

        if chunk_sum > target:
            yield chunk
            chunk = [[key, order, item]]
            chunk_sum = item
        else:
            chunk.append([key, order, item])
    if chunk:
        yield chunk

def chunk_to_sum(iterable, target):
    chunk_sum = 0.0
    chunk = []

    for key, item in iterable:
        chunk_sum += item

        if chunk_sum > target:
            yield chunk
            chunk = [key]
            chunk_sum = item
        else:
            chunk.append(key)
    if chunk:
        yield chunk

def checker_order_capacity(iterable):
    for i in range(0, len(iterable)):
        order = iterable[i]

        if order[0] and order[2] == 0:
            return True

def checker_order_capacity_comp(iterable):
    for i in range(0, len(iterable)):
        order = iterable[i]

        if order[0] and order[2] == 0:
            return True


def convert_to_string(iterable):
    result_str = ""

    for postal_code in iterable:

        if not result_str:
            result_str += str(postal_code)
        else:
            result_str += "_" + str(postal_code)

    result_str = result_str.replace("[", "").replace("]", "").replace("\'", "")

    return result_str


def convert_to_string_truck(vehicle_postal_list_seq):

    result_str = ""

    # iterate the 2 dimensional array
    for vehicle_count in range(len(vehicle_postal_list_seq)):

        seq_lists = vehicle_postal_list_seq[vehicle_count]

        # Convert to String
        if not result_str:
            result_str += str(seq_lists)
        else:
            result_str += "_" + str(seq_lists)

        # result_str = result_str.replace(", ", "-").replace("\'", "").replace("[", "").replace("]", "")
        result_str = result_str.replace("[", "").replace("]", "")

        # print "result_str", result_str

    return result_str


def startingpoint_latlong(starting_address):

    compare_startPos = postalRecordDB.check_if_exists(starting_address)

    if compare_startPos == None:

        if starting_address[0] == "0":
            starting_address = starting_address.lstrip("0")
            compare_startPos = postalRecordDB.check_if_exists(starting_address)
        else:
            print('starting_point')
            nearest_postal_code = postalRecordDB.query().filter(postalRecordDB.postal_code > starting_address).get(
                keys_only=True)
            compare_startPos = nearest_postal_code.id()

    latlong = postalRecordDB.get_by_id(compare_startPos)

    laglongSource = []

    laglongSource.append(latlong.lat)
    laglongSource.append(',')
    laglongSource.append(latlong.long)
    origin_destination = ''.join(laglongSource)

    return origin_destination


def setLists(list):
    # Create a dictionary of postal codes with values of order id
    # One postal code can have more than 1 order Id || 2 order
    postal_dictionary = {}

    # Postal list will contain all unique postal codes
    postal_list = []
    # capacity list will contain all capacity of postal codes
    capacity_list = []

    # Create Order dictionary to store all the values that relate to the specific order
    order_dict = {}

    # Create Capacity dictionary to store all the values that relate to the specific order
    capacity_dic = {}

    for i in range(0, len(list)):

        order = list[i]

        print "order_list", order

        postal_list.append(order[0])
        capacity_list.append([order[0], int(order[2])])

        if order[1] and order[2] not in postal_dictionary.keys():
            postal_dictionary[order[0]] = []

        postal_dictionary[order[0]].append(str(order[1]))
        postal_dictionary[order[0]].append(order[2])

        if order[0] and order[2] not in order_dict.keys():
            order_dict[order[1]] = []

        for j in range(0, len(order)):
            order_dict[order[1]].append(str(order[j]))

        if order[0] and order[1] not in capacity_dic.keys():
            capacity_dic[order[2]] = []

        for k in range(0, len(order)):
            capacity_dic[order[2]].append(str(order[k]))

    return postal_dictionary, postal_list, order_dict, capacity_dic, capacity_list


# Sort the postal array
def sortPostalArray(areaCodeRanking_dict, list):
    # Hash for the ranked but unsorted postal codes
    custPostal_dict_unsorted = {}

    # Array to store current sequence of postal codes
    currentSeq = []

    # For every postal codes, obtain and assign the respective rank
    for postal in list:

        # Convert into string and remove white spaces
        postal_str = str(postal)
        postal_str = postal_str.strip()

        # Check if postal code is a valid value i.e. Contains only five or six digits
        if not str.isdigit(postal_str) or len(postal_str) != 5 and len(postal_str) != 6:
            return None

        # Add "0" in front of five digit postal codes
        if len(postal_str) == 5:
            postal_str = "0" + postal_str

        # Record current sequence of postal codes
        currentSeq.append(postal_str)

        # Obtain rank for postal code
        rank = areaCodeRanking_dict[postal_str[0:2]]

        # Store postal code and rank into hash
        custPostal_dict_unsorted[postal_str] = rank

    # Sort the hash by rank then postal
    custPostal_arr_sorted = sorted(custPostal_dict_unsorted, key=lambda key: (int(custPostal_dict_unsorted[key]), key))

    # Send email with current and sorted sequence of postal codes
    # sendEmail(currentSeq, custPostal_arr_sorted)
    # Return result
    return custPostal_arr_sorted


# Set the postal with Rank
def setPostalRank(areaCodeRanking_dict, list):
    # Hash for the ranked but unsorted postal codes

    custPostal_dict_unsorted = {}

    # Array to store current sequence of postal codes
    currentSeq = []

    # For every postal codes, obtain and assign the respective rank
    for postal in list:

        # Convert into string and remove white spaces
        postal_str = str(postal)
        postal_str = postal_str.strip()

        # Check if postal code is a valid value i.e. Contains only five or six digits
        if not str.isdigit(postal_str) or len(postal_str) != 5 and len(postal_str) != 6:
            return None

        # Add "0" in front of five digit postal codes
        if len(postal_str) == 5:
            postal_str = "0" + postal_str

        # Record current sequence of postal codes
        currentSeq.append(postal_str)

        # Obtain rank for postal code
        rank = areaCodeRanking_dict[postal_str[0:2]]

        # Store postal code and rank into hash
        custPostal_dict_unsorted[postal_str] = rank
    return custPostal_dict_unsorted


def chunkIt(seq, num):
    # method used to break down a list into equal parts
    avg = float(len(seq)) / float(num)

    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def createPostalRanking():
    # Hash for area codes and rank
    areaCodeRanking_dict = {}

    # Fix the dict
    areaCodeRanking_dict['63'] = 1
    areaCodeRanking_dict['70'] = 2
    areaCodeRanking_dict['71'] = 3
    areaCodeRanking_dict['69'] = 4
    areaCodeRanking_dict['68'] = 5
    areaCodeRanking_dict['72'] = 6
    areaCodeRanking_dict['73'] = 7
    areaCodeRanking_dict['76'] = 8
    areaCodeRanking_dict['75'] = 9
    areaCodeRanking_dict['77'] = 10
    areaCodeRanking_dict['78'] = 11
    areaCodeRanking_dict['79'] = 12
    areaCodeRanking_dict['80'] = 13
    areaCodeRanking_dict['56'] = 14
    areaCodeRanking_dict['55'] = 15
    areaCodeRanking_dict['36'] = 16
    areaCodeRanking_dict['37'] = 17
    areaCodeRanking_dict['53'] = 18
    areaCodeRanking_dict['54'] = 19
    areaCodeRanking_dict['82'] = 20
    areaCodeRanking_dict['50'] = 21
    areaCodeRanking_dict['51'] = 22
    areaCodeRanking_dict['49'] = 23
    areaCodeRanking_dict['81'] = 24
    areaCodeRanking_dict['48'] = 25
    areaCodeRanking_dict['52'] = 26
    areaCodeRanking_dict['46'] = 27
    areaCodeRanking_dict['47'] = 28
    areaCodeRanking_dict['41'] = 29
    areaCodeRanking_dict['40'] = 30
    areaCodeRanking_dict['42'] = 31
    areaCodeRanking_dict['44'] = 32
    areaCodeRanking_dict['45'] = 33
    areaCodeRanking_dict['43'] = 34
    areaCodeRanking_dict['04'] = 35
    areaCodeRanking_dict['01'] = 36
    areaCodeRanking_dict['07'] = 37
    areaCodeRanking_dict['08'] = 38
    areaCodeRanking_dict['09'] = 39
    areaCodeRanking_dict['15'] = 40
    areaCodeRanking_dict['10'] = 41
    areaCodeRanking_dict['11'] = 42
    areaCodeRanking_dict['14'] = 43
    areaCodeRanking_dict['25'] = 44
    areaCodeRanking_dict['24'] = 45
    areaCodeRanking_dict['23'] = 46
    areaCodeRanking_dict['05'] = 47
    areaCodeRanking_dict['06'] = 48
    areaCodeRanking_dict['16'] = 49
    areaCodeRanking_dict['17'] = 50
    areaCodeRanking_dict['03'] = 51
    areaCodeRanking_dict['18'] = 52
    areaCodeRanking_dict['22'] = 53
    areaCodeRanking_dict['30'] = 54
    areaCodeRanking_dict['21'] = 55
    areaCodeRanking_dict['33'] = 56
    areaCodeRanking_dict['20'] = 57
    areaCodeRanking_dict['19'] = 58
    areaCodeRanking_dict['39'] = 59
    areaCodeRanking_dict['38'] = 60
    areaCodeRanking_dict['34'] = 61
    areaCodeRanking_dict['35'] = 62
    areaCodeRanking_dict['32'] = 63
    areaCodeRanking_dict['31'] = 64
    areaCodeRanking_dict['57'] = 65
    areaCodeRanking_dict['29'] = 66
    areaCodeRanking_dict['28'] = 67
    areaCodeRanking_dict['26'] = 68
    areaCodeRanking_dict['27'] = 69
    areaCodeRanking_dict['58'] = 70
    areaCodeRanking_dict['67'] = 71
    areaCodeRanking_dict['66'] = 72
    areaCodeRanking_dict['59'] = 73
    areaCodeRanking_dict['60'] = 74
    areaCodeRanking_dict['65'] = 75
    areaCodeRanking_dict['64'] = 76
    areaCodeRanking_dict['61'] = 77
    areaCodeRanking_dict['12'] = 78
    areaCodeRanking_dict['13'] = 79
    areaCodeRanking_dict['62'] = 80

    return areaCodeRanking_dict


def sendEmail(COMPANY, VERISON, vehicle_type, current, new):

    currentDateTime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    # Check for connection to internet
    try:

        response = urllib2.urlopen('http://www.google.com', timeout=5)

        # Check for connection to Gmail SMTP server
        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            newJoined = "New Sequence: "
            # for i in new:
            # newJoined = newJoined + "\n"+" ".join(i)
            for i in range(0, len(new)):
                newJoined = newJoined + "\n" + "Vehicle " + str(i + 1) + "\n" + " ".join(new[i])

            content = "\nDate: " + currentDateTime + "\nCompany Name: " + COMPANY + "\nVerison: " + VERISON + "\nVehicle Type: " + vehicle_type + "\nCurrent Sequence : " + "\n" + " ".join(
                map(str, current)) + "\n" + newJoined
            # Store all csv into content
            mail.ehlo()
            mail.starttls()
            mail.login('comparerouterp@gmail.com', 'compare123')  # login
            mail.sendmail('comparerouterp@gmail.com', 'comparerouterp@gmail.com', content)  # cha
            mail.close()

        except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):

            print("error email")

    except urllib2.URLError as err:

        print("error")


#########################################
# Generate a digital clientID + signature
#########################################

def signUrl(my_url):
    my_url = my_url + "&client=gme-republicpolytechnic"
    url = urlparse.urlparse(my_url)

    privateKey = "nJxJLqiWuL68EBCc_nPpepmGmKE="

    # We only need to sign the path+query part of the string
    urlToSign = url.path + "?" + url.query

    # Decode the private key into its binary format
    decodedKey = base64.urlsafe_b64decode(privateKey)

    # Create a signature using the private key and the URL-encoded
    # string using HMAC SHA1. This signature will be binary.
    signature = hmac.new(decodedKey, urlToSign, hashlib.sha1)

    # Encode the binary signature into base64 for use within a URL
    encodedSignature = base64.urlsafe_b64encode(signature.digest())
    originalUrl = url.scheme + "://" + url.netloc + url.path + "?" + url.query

    # print("Full URL: " + originalUrl + "&signature=" + encodedSignature)
    return originalUrl + "&signature=" + encodedSignature
