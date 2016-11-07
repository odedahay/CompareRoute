# Date and time
from datetime import datetime

import webapp2
from handlers import base
from model.admin_account import postalRecordDB, PostalRecordDB_alert

# Function created:
import sorting
import validation_checker

# Library function
import json
import urllib
import urllib2
import logging
import re
import time
import itertools
import operator
from itertools import groupby



from operator import itemgetter
from collections import defaultdict

from model.user_account import UserAccount

# urlfetch.set_default_fetch_deadline(60)

class SortingPrep(webapp2.RequestHandler):
    def post(self):

        # Obtain user inputs from Compare page
        # Route By Truck
        starting_postal = self.request.get("starting_postal")
        vehicle_quantity = self.request.get("vehicle_quantity")

        # Route By Capacity
        # 1 R-B-T
        starting_postal_cap = self.request.get("starting_postal_cap")
        type_of_truck = self.request.get("type_of_truck")
        truck_capacity = self.request.get("truck_capacity")
        num_of_truck = self.request.get("num_of_truck")

        # 2
        type_of_truck_1 = self.request.get("type_of_truck_1")
        truck_capacity_1 = self.request.get("truck_capacity_1")
        num_of_truck_1 = self.request.get("num_of_truck_1")

        # 3
        type_of_truck_2 = self.request.get("type_of_truck_2")
        truck_capacity_2 = self.request.get("truck_capacity_2")
        num_of_truck_2 = self.request.get("num_of_truck_2")

        # Route By Companies
        # for i in range(0, 5):
        #     starting_postal_1 = self.request.get("starting_postal_{}".format(i))

        # Sort companies default fields
        starting_postal_1 = self.request.get("starting_postal_1")
        starting_postal_2 = self.request.get("starting_postal_2")
        starting_postal_3 = self.request.get("starting_postal_3")
        starting_postal_4 = self.request.get("starting_postal_4")
        starting_postal_5 = self.request.get("starting_postal_5")
        starting_postal_6 = self.request.get("starting_postal_6")

        vehicle_quantity_1 = self.request.get("vehicle_quantity_1")
        vehicle_quantity_2 = self.request.get("vehicle_quantity_2")
        vehicle_quantity_3 = self.request.get("vehicle_quantity_3")
        vehicle_quantity_4 = self.request.get("vehicle_quantity_4")
        vehicle_quantity_5 = self.request.get("vehicle_quantity_5")
        vehicle_quantity_6 = self.request.get("vehicle_quantity_6")

        # Route By Companies - Capacity
        # vehicle_capacity = self.request.get("truck_capacity")
        # vehicle_type = self.request.get('vehicle_type')

        # main fields for Truck Capacity in Sort companies
        type_of_truck_c1 = self.request.get("type_of_truck_c1")
        type_of_truck_c2 = self.request.get("type_of_truck_c2")
        type_of_truck_c3 = self.request.get("type_of_truck_c3")
        type_of_truck_c4 = self.request.get("type_of_truck_c4")
        type_of_truck_c5 = self.request.get("type_of_truck_c5")
        type_of_truck_c6 = self.request.get("type_of_truck_c6")

        truck_capacity_c1 = self.request.get("truck_capacity_c1")
        truck_capacity_c2 = self.request.get("truck_capacity_c2")
        truck_capacity_c3 = self.request.get("truck_capacity_c3")
        truck_capacity_c4 = self.request.get("truck_capacity_c4")
        truck_capacity_c5 = self.request.get("truck_capacity_c5")
        truck_capacity_c6 = self.request.get("truck_capacity_c6")

        num_of_truck_c1 = self.request.get("num_of_truck_c1")
        num_of_truck_c2 = self.request.get("num_of_truck_c2")
        num_of_truck_c3 = self.request.get("num_of_truck_c3")
        num_of_truck_c4 = self.request.get("num_of_truck_c4")
        num_of_truck_c5 = self.request.get("num_of_truck_c5")
        num_of_truck_c6 = self.request.get("num_of_truck_c6")

        # 1st fields for capacity truck
        type_of_truck_cc1 = self.request.get("type_of_truck_cc1")
        type_of_truck_cc2 = self.request.get("type_of_truck_cc2")
        type_of_truck_cc3 = self.request.get("type_of_truck_cc3")

        truck_capacity_cc1 = self.request.get("truck_capacity_cc1")
        truck_capacity_cc2 = self.request.get("truck_capacity_cc2")
        truck_capacity_cc3 = self.request.get("truck_capacity_cc3")

        num_of_truck_cc1 = self.request.get("num_of_truck_cc1")
        num_of_truck_cc2 = self.request.get("num_of_truck_cc2")
        num_of_truck_cc3 = self.request.get("num_of_truck_cc3")

        # 2nd fields for Capacity Truck
        type_of_truck_cc21 = self.request.get("type_of_truck_cc21")
        type_of_truck_cc22 = self.request.get("type_of_truck_cc22")
        type_of_truck_cc23 = self.request.get("type_of_truck_cc23")

        truck_capacity_cc21 = self.request.get("truck_capacity_cc21")
        truck_capacity_cc22 = self.request.get("truck_capacity_cc22")
        truck_capacity_cc23 = self.request.get("truck_capacity_cc23")

        num_of_truck_cc21 = self.request.get("num_of_truck_cc21")
        num_of_truck_cc22 = self.request.get("num_of_truck_cc22")
        num_of_truck_cc23 = self.request.get("num_of_truck_cc23")

        # 3rd field for Capacity Truck
        type_of_truck_cc31 = self.request.get("type_of_truck_cc21")
        type_of_truck_cc32 = self.request.get("type_of_truck_cc22")
        type_of_truck_cc33 = self.request.get("type_of_truck_cc23")

        truck_capacity_cc31 = self.request.get("truck_capacity_cc21")
        truck_capacity_cc32 = self.request.get("truck_capacity_cc22")
        truck_capacity_cc33 = self.request.get("truck_capacity_cc23")

        num_of_truck_cc31 = self.request.get("num_of_truck_cc21")
        num_of_truck_cc32 = self.request.get("num_of_truck_cc22")
        num_of_truck_cc33 = self.request.get("num_of_truck_cc23")

        # Field truck counter
        add_truck_cc1_1 = self.request.get("add_truck_cc1_1")
        add_truck_cc1_2 = self.request.get("add_truck_cc1_2")

        add_truck_cc2_1 = self.request.get("add_truck_cc2_1")
        add_truck_cc2_2 = self.request.get("add_truck_cc2_2")

        add_truck_cc3_1 = self.request.get("add_truck_cc3_1")
        add_truck_cc3_2 = self.request.get("add_truck_cc3_2")

        postal_sequence = self.request.get("postal_sequence")
        email = self.request.get("email")
        has_return = self.request.get("has_return")

        options_truck = self.request.get("optionsTruck")
        priority_capacity = self.request.get("priority_capacity")
        priority_capacity_comp = self.request.get("priority_capacity_comp")

        sort_company = self.request.get('sort_company')
        num_comp_val = self.request.get('num_comp_val')

        # - - - - - - - - -  REQUEST - - - - - - - - - - #

        # Error Variables:
        error_StartingPoint = " Invalid Starting postal code <br />"
        error_Num_of_truck = "Add more Truck! <br />The minimum balance number for delivery truck  "
        error_valid_msg_truck = "Add more Truck! <br />The minimum balance number for delivery truck "

        response = {}
        errors = []

        # Check if the user if has valid credits
        credits_account = UserAccount.check_credit_usage(email)
        if credits_account == None:

            print "Error in Credits Account"
            errors.extend(["Error in Credits Access <br />"])

        # Remove trailing whitespaces
        postal_sequence = postal_sequence.strip()

        # Split up the input by newlines
        postal_sequence_split = str(postal_sequence).split("\n")

        # For storage of a full valid sequence of postal codes
        postal_sequence_list = []
        postal_sequence_current = []
        list_of_companies = []

        # Empty Array for Route By Capacity
        truck_capacity_list = []
        truck_capacity_list_1 = []
        truck_capacity_list_2 = []

        # Type of Truck
        truck_capacity_grp = []

        # Type of Truck - Company
        # truck_capacity_list_c = []
        truck_capacity_list_c1 = []
        truck_capacity_list_c2 = []
        truck_capacity_list_c3 = []
        truck_capacity_list_c4 = []
        truck_capacity_list_c5 = []
        truck_capacity_list_c6 = []

        # Field 1 sub truck
        truck_capacity_list_cc1 = []
        truck_capacity_list_cc2 = []

        # Field 2 sub truck
        truck_capacity_list_cc21 = []
        truck_capacity_list_cc22 = []

        # Field 3rd sub truck
        truck_capacity_list_cc31 = []
        truck_capacity_list_cc32 = []

        truck_capacity_list_cc1_grp = []
        truck_capacity_list_cc2_grp = []
        truck_capacity_list_cc3_grp = []

        truck_capacity_list_cc21_grp = []
        truck_capacity_list_cc23_grp = []

        # Type of Truck
        truck_capacity_grp_comp1 = []
        truck_capacity_grp_comp2 = []

        # Empty Array for Route by Companies
        starting_postal_list = []
        vehicle_quantity_list = []

        # For empty order id and capacity
        forEmp_OrderID_Cap = ['0', '0']
        forEmp_Capt = ['0']

        # truck_type = ["truck_1", "truck_2"]

        compare_id = datetime.now().strftime('%Y%m%d%H%m%f')

        # if options_truck == "true":

        # For Route by Truck Capacity validation
        if priority_capacity == "true":

            starting_postal = starting_postal_cap

            if type_of_truck_1 and not type_of_truck_2:

                truck_capacity_list.extend([str(type_of_truck), int(truck_capacity), int(num_of_truck)])
                truck_capacity_list_1.extend([str(type_of_truck_1), int(truck_capacity_1), int(num_of_truck_1)])
                truck_capacity_grp.extend([truck_capacity_list, truck_capacity_list_1])

            elif type_of_truck_2:

                truck_capacity_list.extend([str(type_of_truck), int(truck_capacity), int(num_of_truck)])

                # Append all value for truck 2
                truck_capacity_list_1.extend([str(type_of_truck_1), int(truck_capacity_1), int(num_of_truck_1)])
                truck_capacity_list_2.extend([str(type_of_truck_2), int(truck_capacity_2), int(num_of_truck_2)])

                # grp all list truck
                truck_capacity_grp.extend([truck_capacity_list, truck_capacity_list_1, truck_capacity_list_2])

            else:

                truck_capacity_list.extend([str(type_of_truck), int(truck_capacity), int(num_of_truck)])
                truck_capacity_grp.extend([truck_capacity_list])

        if sort_company == "true":

            if priority_capacity_comp == "true":

                # Store all HQ postal code and Vehicle count accordingly
                if int(num_comp_val) == 2:

                    # truck 1 field > add 2nd truck field
                    if add_truck_cc1_1 and not add_truck_cc1_2:

                        truck_capacity_list_c1.extend([str(type_of_truck_c1), int(truck_capacity_c1), int(num_of_truck_c1)])
                        truck_capacity_list_cc1.extend([str(type_of_truck_cc1), int(truck_capacity_cc1), int(num_of_truck_cc1)])

                        truck_capacity_list_cc1_grp.extend([truck_capacity_list_c1, truck_capacity_list_cc1])

                    #  truck 1 field > add 3rd truck field
                    elif add_truck_cc1_1 and add_truck_cc1_2:

                        truck_capacity_list_c1.extend([str(type_of_truck_c1), int(truck_capacity_c1), int(num_of_truck_c1)])
                        truck_capacity_list_cc1.extend([str(type_of_truck_cc1), int(truck_capacity_cc1), int(num_of_truck_cc1)])
                        truck_capacity_list_cc2.extend([str(type_of_truck_cc2), int(truck_capacity_cc2), int(num_of_truck_cc2)])

                        truck_capacity_list_cc1_grp.extend([truck_capacity_list_c1, truck_capacity_list_cc1, truck_capacity_list_cc2])

                    else:

                        truck_capacity_list_c1.extend([[str(type_of_truck_c1), int(truck_capacity_c1), int(num_of_truck_c1)]])
                        truck_capacity_list_cc1_grp = truck_capacity_list_c1

                    #######
                    # field 2

                    if add_truck_cc2_1 and not add_truck_cc2_2:

                        truck_capacity_list_c2.extend([str(type_of_truck_c2), int(truck_capacity_c2), int(num_of_truck_c2)])
                        truck_capacity_list_cc21.extend([str(type_of_truck_cc21), int(truck_capacity_cc21), int(num_of_truck_cc21)])

                        truck_capacity_list_cc2_grp.extend([truck_capacity_list_c2, truck_capacity_list_cc21])

                    #  truck 2 field > add 3rd truck field
                    elif add_truck_cc2_1 and add_truck_cc2_2:

                        truck_capacity_list_c2.extend([str(type_of_truck_c2), int(truck_capacity_c2), int(num_of_truck_c2)])
                        truck_capacity_list_cc21.extend([str(type_of_truck_cc21), int(truck_capacity_cc21), int(num_of_truck_cc21)])
                        truck_capacity_list_cc22.extend([str(type_of_truck_cc22), int(truck_capacity_cc22), int(num_of_truck_cc22)])

                        truck_capacity_list_cc2_grp.extend([truck_capacity_list_c2, truck_capacity_list_cc21, truck_capacity_list_cc22])

                    else:
                        truck_capacity_list_c2.extend([[str(type_of_truck_c2), int(truck_capacity_c2), int(num_of_truck_c2)]])
                        truck_capacity_list_cc2_grp = truck_capacity_list_c2

                    # Grouping Section
                    truck_capacity_grp_comp1.extend([truck_capacity_list_cc1_grp, truck_capacity_list_cc2_grp])

                if int(num_comp_val) == 3:

                    # truck 1 field > add 2nd truck field
                    if add_truck_cc1_1 and not add_truck_cc1_2:

                        truck_capacity_list_c1.extend([str(type_of_truck_c1), int(truck_capacity_c1), int(num_of_truck_c1)])
                        truck_capacity_list_cc1.extend([str(type_of_truck_cc1), int(truck_capacity_cc1), int(num_of_truck_cc1)])

                        truck_capacity_list_cc1_grp.extend([truck_capacity_list_c1, truck_capacity_list_cc1])

                    #  truck 1 field > add 3rd truck field
                    elif add_truck_cc1_1 and add_truck_cc1_2:

                        truck_capacity_list_c1.extend([str(type_of_truck_c1), int(truck_capacity_c1), int(num_of_truck_c1)])
                        truck_capacity_list_cc1.extend([str(type_of_truck_cc1), int(truck_capacity_cc1), int(num_of_truck_cc1)])
                        truck_capacity_list_cc2.extend([str(type_of_truck_cc2), int(truck_capacity_cc2), int(num_of_truck_cc2)])

                        truck_capacity_list_cc1_grp.extend([truck_capacity_list_c1, truck_capacity_list_cc1, truck_capacity_list_cc2])

                    else:

                        truck_capacity_list_c1.extend([[str(type_of_truck_c1), int(truck_capacity_c1), int(num_of_truck_c1)]])
                        truck_capacity_list_cc1_grp = truck_capacity_list_c1

                    #######
                    # 2nd input field

                    if add_truck_cc2_1 and not add_truck_cc2_2:

                        truck_capacity_list_c2.extend([str(type_of_truck_c2), int(truck_capacity_c2), int(num_of_truck_c2)])
                        truck_capacity_list_cc21.extend([str(type_of_truck_cc21), int(truck_capacity_cc21), int(num_of_truck_cc21)])

                        truck_capacity_list_cc2_grp.extend([truck_capacity_list_c2, truck_capacity_list_cc21])

                    #  truck 2 field > add 3rd truck field
                    elif add_truck_cc2_1 and add_truck_cc2_2:

                        truck_capacity_list_c2.extend([str(type_of_truck_c2), int(truck_capacity_c2), int(num_of_truck_c2)])
                        truck_capacity_list_cc21.extend([str(type_of_truck_cc21), int(truck_capacity_cc21), int(num_of_truck_cc21)])
                        truck_capacity_list_cc22.extend([str(type_of_truck_cc22), int(truck_capacity_cc22), int(num_of_truck_cc22)])

                        truck_capacity_list_cc2_grp.extend([truck_capacity_list_c2, truck_capacity_list_cc21, truck_capacity_list_cc22])

                    else:
                        truck_capacity_list_c2.extend([[str(type_of_truck_c2), int(truck_capacity_c2), int(num_of_truck_c2)]])
                        truck_capacity_list_cc2_grp = truck_capacity_list_c2

                     #######
                    # 3rd input field

                    if add_truck_cc3_1 and not add_truck_cc3_2:

                        truck_capacity_list_c3.extend([str(type_of_truck_c3), int(truck_capacity_c3), int(num_of_truck_c3)])
                        truck_capacity_list_cc31.extend([str(type_of_truck_cc31), int(truck_capacity_cc31), int(num_of_truck_cc31)])

                        truck_capacity_list_cc3_grp.extend([truck_capacity_list_c3, truck_capacity_list_cc31])

                    #  truck 2 field > add 3rd truck field
                    elif add_truck_cc3_1 and add_truck_cc3_2:

                        truck_capacity_list_c3.extend([str(type_of_truck_c3), int(truck_capacity_c3), int(num_of_truck_c3)])
                        truck_capacity_list_cc31.extend([str(type_of_truck_cc31), int(truck_capacity_cc31), int(num_of_truck_cc31)])
                        truck_capacity_list_cc32.extend([str(type_of_truck_cc32), int(truck_capacity_cc32), int(num_of_truck_cc32)])

                        truck_capacity_list_cc3_grp.extend([truck_capacity_list_c3, truck_capacity_list_cc31, truck_capacity_list_cc32])

                    else:
                        truck_capacity_list_c3.extend([[str(type_of_truck_c3), int(truck_capacity_c3), int(num_of_truck_c3)]])
                        truck_capacity_list_cc3_grp = truck_capacity_list_c3

                    # Grouping Section
                    truck_capacity_grp_comp1.extend([truck_capacity_list_cc1_grp, truck_capacity_list_cc2_grp, truck_capacity_list_cc3_grp])

                    print "truck_capacity_grp_comp1", truck_capacity_grp_comp1

                # if int(num_comp_val) == 4:

                #
                # if int(num_comp_val) == 5:

                #
                # if int(num_comp_val) == 6:


            # Store Postal code and Vehicle
            starting_postal_list.append(str(starting_postal_1))
            vehicle_quantity_list.append(vehicle_quantity_1)

            if int(num_comp_val) == 2:
                starting_postal_list.append(str(starting_postal_2))
                vehicle_quantity_list.append(vehicle_quantity_2)

            if int(num_comp_val) == 3:
                starting_postal_list.extend([str(starting_postal_2), str(starting_postal_3)])
                vehicle_quantity_list.extend([vehicle_quantity_2, vehicle_quantity_3])

            if int(num_comp_val) == 4:
                starting_postal_list.extend([str(starting_postal_2), str(starting_postal_3), str(starting_postal_4)])
                vehicle_quantity_list.extend([vehicle_quantity_2, vehicle_quantity_3, vehicle_quantity_4])

            if int(num_comp_val) == 5:
                starting_postal_list.extend([str(starting_postal_2), str(starting_postal_3), str(starting_postal_4), str(starting_postal_5)])
                vehicle_quantity_list.extend([vehicle_quantity_2, vehicle_quantity_3, vehicle_quantity_4, vehicle_quantity_5])

            if int(num_comp_val) == 6:
                starting_postal_list.extend([str(starting_postal_2), str(starting_postal_3), str(starting_postal_4), str(starting_postal_5), str(starting_postal_6)])
                vehicle_quantity_list.extend([vehicle_quantity_2, vehicle_quantity_3, vehicle_quantity_4, vehicle_quantity_5, vehicle_quantity_6])

            # Route by Companies, Considering Route by Truck Capacity validation

        # - - - - - Lat-long for Starting point HQ - - - - - #
        else:

            # Add "0" in front of five digit postal codes
            if len(starting_postal) == 5:
                starting_postal = "0" + starting_postal

            # Remove "0" if  no record found
            starting_postal_hq = postalRecordDB.check_if_exists(starting_postal)

            if starting_postal_hq == None:

                errors.extend([starting_postal, error_StartingPoint])

                # if int(vehicle_quantity) >= 17:
                #     errors.extend(['Number vehicle maximum 17 only'])

        # Counter checking of Postal Code
        num_post_code = 0

        # Extract the postal pair and validate the postal code while ignoring first line of headers
        # Note: Order ID is untouched as we do not know their format
        for index in range(1, len(postal_sequence_split)):

            num_post_code = num_post_code + 1

            # Retrieve each postal pair
            postal_pair = postal_sequence_split[index]

            # Replace all tab spaces with normal spaces and remove trailing whitespace
            postal_pair = postal_pair.replace("\t", " ")
            postal_pair = postal_pair.strip()

            # Split the order ID/postal code pair by normal spacing
            postal_pair_split = postal_pair.split(" ")

            if len(postal_pair_split) == 2:
                postal_pair_split.extend(forEmp_Capt)

            if len(postal_pair_split) != 3:
                postal_pair_split.extend(forEmp_OrderID_Cap)

            # If Postal Code reverse in textbox
            postal_code = str(postal_pair_split[0])
            order_id = str(postal_pair_split[1])
            truck_volume = int(postal_pair_split[2])

            # Postal Code Validation entry

            # Add "0" in front of five digit postal codes
            if len(postal_code) == 5:
                postal_code = "0" + postal_code

            # Any Postal Code below 4 will throw error
            if len(postal_code) <= 4:
                errors.extend(["  Please Check ", postal_code, ", Postal Code should only be 6 digits <br />"])

            # The value 830000 is for invalid postal codes (Currently we have up to 82xxxx only)
            if not str.isdigit(postal_code) or int(postal_code) >= 830000:
                errors.extend([postal_code, ' Invalid postal codes'])

            # Route by Capacity:
            if priority_capacity == "true":

                # Check each postal vol. is not above to "truck_capacity" e.g. 11 > 10
                if truck_volume > int(truck_capacity):
                    errors.extend([postal_code, " exceeding to the minimum Truck Capacity <br />"])

            if sort_company == "true":

                if len(postal_pair_split) == 3:
                    print "Please add Company in 4th column <br/ >"
                    errors.extend(['Please add Company in 4th column  <br/ >'])

                if len(errors) == 0:
                    sorted_comp = postal_pair_split[3]
                    postal_sequence_list.append([postal_code, str(order_id), int(truck_volume), sorted_comp])
                    list_of_companies.append(sorted_comp)
            else:
                postal_sequence_list.append([postal_code, str(order_id), int(truck_volume)])
            postal_sequence_current.append(postal_code)

        if len(errors) == 0:

            # If errors are found in the postal sequence, send response with error
            # Else, call the sorting algorithm and and send response with the sorted postal codes

            # API Sensor
            api_user = "none"

            if sort_company == "true":

                """ each company will separated and this will indicate the color plotting in map like vehicle count """
                """ Vehicle-color will same method of color as for Company separation """

                # Create variable for each request
                company_list_grp = []
                postal_sequence_company = []

                # for Company Sorting
                propose_result_company = []
                current_result_company = []
                origin_result_company = []
                propose_result_sequence = []
                result_route_value = []
                latlng_array_list = []
                vehicle_list_grp = []

                for company in range(len(postal_sequence_list)):
                    companyList = postal_sequence_list[company]
                    company_list_grp.append(companyList)

                for key, group in itertools.groupby(company_list_grp, operator.itemgetter(3)):
                    # group as per company
                    postal_sequence_company.append(list(group))

                # Get All Name of the companies:
                seen = {}
                name_of_companies = [seen.setdefault(x, x) for x in list_of_companies if x not in seen]

                # Start of validation
                if int(len(postal_sequence_company)) != int(num_comp_val):
                    errors.extend(['Please Check Number of company inputs'])

                # Data Distribute through parallel loop according to number of company request
                if priority_capacity_comp == "true":

                    # Add in dictionary the value of truck capacity
                    truck_capacity_dict = {

                        "truck_capacity_c1": truck_capacity_c1,
                        "truck_capacity_cc1": truck_capacity_cc1,
                        "truck_capacity_cc2": truck_capacity_cc2,

                        "truck_capacity_c2": truck_capacity_c2,
                        "truck_capacity_cc21": truck_capacity_cc21,
                        "truck_capacity_cc22": truck_capacity_cc22,

                        "truck_capacity_c3": truck_capacity_c3,
                        "truck_capacity_cc31": truck_capacity_cc31,
                        "truck_capacity_cc32": truck_capacity_cc32,

                    }

                    # Check if the company is exceeding:
                    errors_result = validation_checker.cargo_unit_checker_for_comp(num_comp_val, postal_sequence_company, **truck_capacity_dict)

                    if errors_result != "":

                        # Convert the variable to error list
                        errors = errors_result

                    # Calling function for sorting and chunking
                    for starting_post, company_sequence, truck_capacity_grp in itertools.izip(starting_postal_list, postal_sequence_company, truck_capacity_grp_comp1):

                        origin_destinations, propose_result, current_result, vehicle_postal_list_new_seq, grp_truck = sorting.sort_by_postals_chunck(
                            starting_post,
                            company_sequence,
                            vehicle_quantity,
                            email, has_return,
                            priority_capacity,
                            priority_capacity_comp,
                            api_user, sort_company, truck_capacity_grp, options_truck)

                        propose_result_company.append(propose_result)
                        current_result_company.append(current_result)
                        origin_result_company.append(origin_destinations)
                        propose_result_sequence.append(vehicle_postal_list_new_seq)

                        # GeoCode Map
                        latlng_array = map_visible(propose_result)
                        latlng_array_list.append(latlng_array)

                    # Create function for validation Truck Capacity
                    # A function to check if the company is exceeding:

                    # # Function for validation
                    # result_numTruck = validation_checker.minimum_truck_checker_comp(num_comp_val, propose_result_company, starting_postal_list,
                    #                                                        num_of_truck_c1, num_of_truck_cc1,
                    #                                                        num_of_truck_c2, num_of_truck_cc21,
                    #                                                        num_of_truck_c3, num_of_truck_cc31,
                    #                                                        type_of_truck_c2,type_of_truck_cc1,type_of_truck_cc21,
                    #                                                        type_of_truck_c1,
                    #                                                        type_of_truck_c3,
                    #                                                        add_truck_cc1, add_truck_cc2,add_truck_cc3)
                    #
                    # errors.extend(result_numTruck)

                    # Check if they have two company
                    if int(num_comp_val) == 2:

                        company_1 = int(len(propose_result_company[0]))
                        company_2 = int(len(propose_result_company[1]))

                        # 2nd fields Opend and 1 field for 2nd company
                        if add_truck_cc1_1 and not add_truck_cc1_2:

                            if company_1 > int(num_of_truck_c1) + int(num_of_truck_cc1):
                                errors.extend([error_Num_of_truck, " for ", type_of_truck_cc1, " is ", (company_1 - int(num_of_truck_c1)), "<br />"])

                        elif add_truck_cc1_1 and add_truck_cc1_2:

                            if company_1 > (int(num_of_truck_c1) + int(num_of_truck_cc1) + int(num_of_truck_cc2)):
                                errors.extend([error_Num_of_truck, " for ", type_of_truck_cc2, " is ", company_1 - (int(num_of_truck_c1) + int(num_of_truck_cc1)), "<br />"])

                        else:
                            # if the First Field have only entered value
                            if int(company_1) > int(num_of_truck_c1):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_c1, " is ", company_1, "<br />"])

                        # 2nd Fields

                        if add_truck_cc2_1 and not add_truck_cc2_2:

                            if company_2 > int(num_of_truck_c2) + int(num_of_truck_cc21):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_cc21, " is ", (company_1 - int(num_of_truck_c2)), "<br />"])

                        elif add_truck_cc2_1 and add_truck_cc2_2:

                            if company_2 > int(num_of_truck_c2) + int(num_of_truck_cc21) + int(num_of_truck_cc22):
                                errors.extend([error_Num_of_truck, " for ", type_of_truck_cc2, " is ", company_1 - (int(num_of_truck_c2) + int(num_of_truck_cc21)), "<br />"])
                        else:

                            if int(company_2) > int(num_of_truck_c2):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_c2, " is ", company_2, "<br />"])

                    if int(num_comp_val) == 3:

                        company_1 = int(len(propose_result_company[0]))
                        company_2 = int(len(propose_result_company[1]))
                        company_3 = int(len(propose_result_company[2]))

                        # 2nd fields Opend and 1 field for 2nd company
                        if add_truck_cc1_1 and not add_truck_cc1_2:

                            if company_1 > int(num_of_truck_c1) + int(num_of_truck_cc1):
                                errors.extend([error_Num_of_truck, " for ", type_of_truck_cc1, " is ", (company_1 - int(num_of_truck_c1)), "<br />"])

                        elif add_truck_cc1_1 and add_truck_cc1_2:

                            if company_1 > (int(num_of_truck_c1) + int(num_of_truck_cc1) + int(num_of_truck_cc2)):
                                errors.extend([error_Num_of_truck, " for ", type_of_truck_cc2, " is ", company_1 - (int(num_of_truck_c1) + int(num_of_truck_cc1)), "<br />"])

                        else:
                            # if the First Field have only entered value
                            if int(company_1) > int(num_of_truck_c1):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_c1, " is ", company_1, "<br />"])

                        # 2nd Fields

                        if add_truck_cc2_1 and not add_truck_cc2_2:

                            if company_2 > int(num_of_truck_c2) + int(num_of_truck_cc21):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_cc21, " is ", (company_1 - int(num_of_truck_c2)), "<br />"])

                        elif add_truck_cc2_1 and add_truck_cc2_2:

                            if company_2 > int(num_of_truck_c2) + int(num_of_truck_cc21) + int(num_of_truck_cc22):
                                errors.extend([error_Num_of_truck, " for ", type_of_truck_cc2, " is ", company_1 - (int(num_of_truck_c2) + int(num_of_truck_cc21)), "<br />"])
                        else:

                            if int(company_2) > int(num_of_truck_c2):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_c2, " is ", company_2, "<br />"])

                        # 3rd Fields
                        if add_truck_cc3_1 and not add_truck_cc3_2:

                            if company_3 > int(num_of_truck_c3) + int(num_of_truck_cc31):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_cc31, " is ", (company_3 - int(num_of_truck_c3)), "<br />"])

                        elif add_truck_cc3_1 and add_truck_cc3_2:

                            if company_3 > int(num_of_truck_c3) + int(num_of_truck_cc31) + int(num_of_truck_cc32):
                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_cc32, " is ", company_3 - (int(num_of_truck_c3) + int(num_of_truck_cc31)), "<br />"])
                        else:

                            if int(company_3) > int(num_of_truck_c3):

                                errors.extend([error_Num_of_truck, " for ",  type_of_truck_c3, " is ", company_3, "<br />"])

                else:

                    for starting_post, company_sequence, vehicle_quantity in itertools.izip(starting_postal_list, postal_sequence_company, vehicle_quantity_list):

                        origin_destinations, propose_result, current_result, vehicle_postal_list_new_seq, grp_truck = sorting.sort_by_postals_chunck(
                            starting_post,
                            company_sequence,
                            vehicle_quantity,
                            email, has_return,
                            priority_capacity,
                            priority_capacity_comp,
                            api_user, sort_company, truck_capacity_grp, options_truck)

                        propose_result_company.append(propose_result)
                        current_result_company.append(current_result)
                        origin_result_company.append(origin_destinations)
                        propose_result_sequence.append(vehicle_postal_list_new_seq)
                        vehicle_list_grp.append(vehicle_quantity)

                        # GeoCode Map
                        latlng_array = map_visible(propose_result)

                        latlng_array_list.append(latlng_array)

                # Converting the postal code to total distance
                for origin_destination, current_result_comp, propose_result_comp in itertools.izip(origin_result_company, current_result_company, propose_result_company):

                    current_route_value = result_distance_latlng(current_result_comp, origin_destination, num_post_code)
                    propose_route_value = result_distance_latlng(propose_result_comp, origin_destination, num_post_code)

                    # Converting the total percentage saving of distance
                    difference_total = current_route_value - propose_route_value
                    percentage_savings = (difference_total / current_route_value) * 100

                    proposed_route_val = round(propose_route_value, 2)
                    current_route_val = round(current_route_value, 2)
                    savings_route_val = round(percentage_savings, 2)

                    # Total_summary_saving
                    result_route_value.append([str(current_route_val), str(proposed_route_val), str(savings_route_val)])

                # For Google MAP
                result_list_arr = []
                for propose_result_company_1 in propose_result_company:
                    for propose_result_company_2 in propose_result_company_1:
                        result_list_arr.append(propose_result_company_2)

                # Converting JSON
                # Send this JSON file to ajax function > compare_route.js

                response['status'] = 'ok'
                response['sort_company'] = 'true'
                response['data_result'] = [
                    {
                        "required_fields": {
                            "starting_postal": starting_postal_list,
                            "propose_result": result_list_arr,
                            "propose_results": propose_result_company,
                            "postal_sequence": propose_result_sequence,
                            "name_of_companies": name_of_companies,
                            "has_return": has_return
                        },
                        "geo_code_latlng": {
                            "latlng_array": latlng_array_list
                        },
                        "vehicle_priority": {
                            "vehicle_num": vehicle_quantity
                        },
                        "capacity_priority": {
                            "priority_capacity": priority_capacity,
                            "vehicle_capacity": vehicle_list_grp,
                            # "truck_capacity_grp_c": truck_capacity_grp_c,
                        },
                        "total_summary_saving": {
                            "total_savings": result_route_value
                        }
                    }
                ]

            else:

                # - - - - - - - - - This is for Non-company sorting - - - - - - #
                """ Route By Truck and Route by Capacity """

                origin_destination, propose_result, current_result, vehicle_postal_list_new_seq, grp_truck = sorting.sort_by_postals_chunck(
                    int(starting_postal),
                    postal_sequence_list,
                    int(vehicle_quantity),
                    email, has_return,
                    priority_capacity,
                    priority_capacity_comp,
                    api_user, sort_company, truck_capacity_grp, options_truck)

                # Validate if the capacity truck is according to available "num_of_truck"
                # result_num_truck = is number of truck is used through capacity
                result_num_truck = len(propose_result)

                if priority_capacity == "true":

                    # Vehicle Result base of the priority:
                    vehicle_quantity = len(vehicle_postal_list_new_seq)

                    # if add_truck_capacity_1:
                    #     print "hello--111"

                    print "truck_capacity_grp", truck_capacity_grp

                    if len(truck_capacity_grp) == 1:
                        if int(result_num_truck) > int(num_of_truck):
                            errors.extend([error_valid_msg_truck,  type_of_truck, " is ", result_num_truck])

                    elif len(truck_capacity_grp) == 2:
                        if int(result_num_truck) > int(num_of_truck) + int(num_of_truck_1):
                            errors.extend([error_valid_msg_truck,  type_of_truck_1, " is ", int(result_num_truck) - int(num_of_truck)])

                    elif len(truck_capacity_grp) == 3:
                        if int(result_num_truck) > int(num_of_truck) + int(num_of_truck_1) + int(num_of_truck_2):
                            errors.extend([error_valid_msg_truck, type_of_truck_2, " is ", int(result_num_truck) - ( int(num_of_truck) + int(num_of_truck_1) )])

                # Converting the postal code to lat_long
                propose_route_value = result_distance_latlng(propose_result, origin_destination, num_post_code)
                current_route_value = result_distance_latlng(current_result, origin_destination, num_post_code)

                # GeoCode Map
                latlng_array = map_visible(propose_result)

                # print "latlng_array", latlng_array

                # Converting the total percentage saving of distance
                difference_total = current_route_value - propose_route_value
                percentage_savings = (difference_total / current_route_value) * 100

                # Converting JSON
                response['status'] = 'ok'
                response['data_result'] = [
                        {
                            "required_fields": {
                                "starting_postal": starting_postal,
                                "propose_result": propose_result,
                                "postal_sequence": vehicle_postal_list_new_seq,
                                "has_return": has_return
                                },
                            "geo_code_latlng": {
                                "latlng_array": latlng_array
                            },
                            "vehicle_priority": {
                                "vehicle_num": vehicle_quantity
                                },
                            "capacity_priority": {
                                "priority_capacity": priority_capacity,
                                "vehicle_type": grp_truck,
                               #"vehicle_type": truck_capacity_grp,
                               # "vehicle_capacity": vehicle_capacity,
                                },
                            "total_summary_saving": {
                                "propose_distance": propose_route_value,
                                "current_distance": current_route_value,
                                "total_savings": percentage_savings
                                }
                        }
                    ]
        else:
            errors.extend(['Error in process'])

        if len(errors) > 0:
            response['status'] = 'error'
            response['errors'] = errors

        logging.info(response)
        self.response.out.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.out.write(json.dumps(response, indent=3))

    def formatResultForCallback_current(self, result_current):
        # Final result string
        result_str = ""

        # Adding underscore for JavaScript to split later
        for postal_code in result_current:

            if not result_str:
                result_str += str(postal_code)
            else:
               result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "")

        # Return formatted result string
        return result_str


# GeoCode Latlng MAP - single company
def map_visible(propose_result):
    latlng_array = []

    for vehicle_postal in propose_result:
        lat_long_Source = []

        for current_post in vehicle_postal:
            # Convert to Lat-Long the postal code
            destinations = postalcode_latlong(current_post)

            # For Geo-Code MAP
            lat_long_value_map = str(destinations)
            lat_long_value_map = lat_long_value_map.split(",")
            lat_long_Source.append(lat_long_value_map)

        # - - -  for lat & long value with vehicle number- - - #
        latlng_array.append(lat_long_Source)

    return latlng_array

# GeoCode Latlng for Summary:
def Latlng_value_list(propose_result, origin_destination):

    # if numPostCode is > 200:
    # Chunk the postal code by 2 and convert to laltlong
    # Then append to list and sent to JS to convert it.

    latlng_value = ""
    for vehicle_postal in propose_result:
        for current_post in vehicle_postal:

            # Convert to Lat-Long the postal code
            destinations = postalcode_latlong(current_post)

            if not destinations:
                latlng_value += str(destinations)
            else:
                latlng_value += "&loc=" + str(destinations)

    result_value = origin_destination + latlng_value

    return result_value

# GeoCode Latlng
def postalcode_latlong(postal):

        # Validation for Task Q
        compare_postal = postalRecordDB.check_if_exists(postal)

        if compare_postal == None:

            # Remove "0" if still no record found
            if postal[0] == "0":

                print "Adding Zero"
                current_post = postal.lstrip("0")
                compare_postal = postalRecordDB.check_if_exists(current_post)

            else:

                print('NO POSTAL CODE RECORD')

                nearest_postal_code = postalRecordDB.query().filter(postalRecordDB.postal_code > postal).get(keys_only=True)
                compare_postal = nearest_postal_code.id()

        latlong = postalRecordDB.get_by_id(compare_postal)

        laglongSource = []

        laglongSource.append(latlong.lat)

        laglongSource.append(',')
        laglongSource.append(latlong.long)
        destinations = ''.join(laglongSource)

        return destinations


# Summary Distance
def result_distance_latlng(propose_result, origin_destination, num_post_code):

    if num_post_code <= 69:
        print "Below 0-69 postal code"
        result_str = ""

        for postal_code in propose_result:
            if not result_str:
                result_str += str(postal_code)
            else:
                result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes and back to list object
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "").replace("_", ", ")
        result_str = result_str.strip()
        result_str_split = result_str.split(",")

        batch_1_val = latlong_summary_starting(result_str_split, origin_destination)
        route_distance = float(batch_1_val) / 1000

        return route_distance

    elif 70 <= num_post_code <= 130:
    # if num_post_code <= 130:
        """ 70 <= num_post_code <= 130: """
        print "Normal above 70-130 postal code"

        result_str = ""
        for postal_code in propose_result:
            if not result_str:
                result_str += str(postal_code)
            else:
                result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes and back to list object
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "").replace("_", ", ")

        result_str = result_str.strip()
        result_str_split = result_str.split(",")

        # Chunk it
        result_str_chunk = sorting.chunkIt(result_str_split, 2)

        # Assign per batch
        batch_1 = result_str_chunk[0]
        batch_2 = result_str_chunk[1]

        # Get the last item of 1st Batch
        last_item = batch_1[-1]

        # Insert the 'lastItemB' in the index of next list
        # To continue the route distance
        batch_2.insert(0, last_item)

        # - - - - - Get value of list object- - - - - - #
        batch_1_val = latlong_summary_starting(batch_1, origin_destination)
        batch_2_val = latlong_summary(batch_2)

        # taskqueue.add(url='/summary-result',
        #               params=({'origin_destination': origin_destination,
        #                        'result_str': result_str,
        #                       }))

        # # Sum up all batches
        route_distance_add = batch_1_val + batch_2_val
        route_distance = float(route_distance_add) / 1000

        return route_distance

    elif 136 <= num_post_code <= 255:

        """136 <= num_post_code <= 255: """
        print "This is his is normal 135 / 4"

        result_str = ""

        for postal_code in propose_result:
            if not result_str:
                result_str += str(postal_code)
            else:
                result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes and back to list object
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "").replace("_", ", ")
        result_str = result_str.strip()
        result_str_split = result_str.split(",")

        # Chunk it
        result_str_chunk = sorting.chunkIt(result_str_split, 4)

        batch_1 = result_str_chunk[0]
        batch_2 = result_str_chunk[1]

        # Get Last item and insert in the index
        last_item_1 = batch_1[-1]
        batch_2.insert(0, last_item_1)

        batch_3 = result_str_chunk[2]
        batch_4 = result_str_chunk[3]

        # Get Last item and insert in the index
        last_item_2 = batch_2[-1]
        batch_3.insert(0, last_item_2)
        last_item_3 = batch_3[-1]
        batch_4.insert(0, last_item_3)

        #  - - - - - Get value of list object- - - - - - #

        batch_1_val = latlong_summary_starting(batch_1, origin_destination)
        batch_2_val = latlong_summary(batch_2)
        batch_3_val = latlong_summary(batch_3)
        batch_4_val = latlong_summary(batch_4)

        # Sum up the two batch
        route_distance_add = batch_1_val + batch_2_val + batch_3_val + batch_4_val
        route_distance = float(route_distance_add) / 1000

        return route_distance

    elif 256 <= num_post_code <= 370:

        print "This is his is normal 256 / 6"
        result_str = ""
        for postal_code in propose_result:
            if not result_str:
                result_str += str(postal_code)
            else:
                result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes and back to list object
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "").replace("_", ", ")
        result_str = result_str.strip()
        result_str_split = result_str.split(",")

        # Chunk it
        result_str_chunk = sorting.chunkIt(result_str_split, 6)

        # Separate each part of Chunk object
        batch_1 = result_str_chunk[0]
        batch_2 = result_str_chunk[1]

        # Get Last item and insert in the index
        last_item_1 = batch_1[-1]
        batch_2.insert(0, last_item_1)

        batch_3 = result_str_chunk[2]
        batch_4 = result_str_chunk[3]

        # Get Last item and insert in the index
        last_item_2 = batch_2[-1]
        batch_3.insert(0, last_item_2)
        last_item_3 = batch_3[-1]
        batch_4.insert(0, last_item_3)

        batch_5 = result_str_chunk[4]
        batch_6 = result_str_chunk[5]

        # Get Last item and insert in the index
        last_item_4 = batch_4[-1]
        batch_5.insert(0, last_item_4)
        last_item_5 = batch_5[-1]
        batch_6.insert(0, last_item_5)

        #  - - - - - Get value of list object- - - - - - #

        batch_1_val = latlong_summary_starting(batch_1, origin_destination)
        batch_2_val = latlong_summary(batch_2)
        batch_3_val = latlong_summary(batch_3)
        batch_4_val = latlong_summary(batch_4)
        batch_5_val = latlong_summary(batch_5)
        batch_6_val = latlong_summary(batch_6)

        # Sum up the two batch
        route_distance_add_array = []
        route_distance_add_array.extend([batch_1_val, batch_2_val, batch_3_val, batch_4_val, batch_5_val, batch_6_val])

        route_distance_add = sum(route_distance_add_array)
        route_distance = float(route_distance_add) / 1000

        return route_distance

    elif 371 <= num_post_code <= 500:

        """ 371 <= num_post_code <= 500: WIll update this side"""
        print "This is his is normal 371 / 10 *10"

        result_str = ""

        for postal_code in propose_result:
            if not result_str:
                result_str += str(postal_code)
            else:
                result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes and back to list object
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "").replace("_", ", ")
        result_str = result_str.strip()
        result_str_split = result_str.split(",")

        # Chunk it
        result_str_chunk = sorting.chunkIt(result_str_split, 10)

        if len(result_str_chunk) == 11:

            # Separate each part of Chunk object
            batch_1 = result_str_chunk[0]
            batch_2 = result_str_chunk[1]

            # Get Last item and insert in the index
            last_item_1 = batch_1[-1]
            batch_2.insert(0, last_item_1)

            batch_3 = result_str_chunk[2]
            batch_4 = result_str_chunk[3]

            # Get Last item and insert in the index
            last_item_2 = batch_2[-1]
            batch_3.insert(0, last_item_2)
            last_item_3 = batch_3[-1]
            batch_4.insert(0, last_item_3)

            batch_5 = result_str_chunk[4]
            batch_6 = result_str_chunk[5]

            # Get Last item and insert in the index
            last_item_4 = batch_4[-1]
            batch_5.insert(0, last_item_4)
            last_item_5 = batch_5[-1]
            batch_6.insert(0, last_item_5)

            batch_7 = result_str_chunk[6]
            batch_8 = result_str_chunk[7]

            last_item_6 = batch_6[-1]
            batch_7.insert(0, last_item_6)
            last_item_7 = batch_7[-1]
            batch_8.insert(0, last_item_7)

            batch_9 = result_str_chunk[8]
            batch_10 = result_str_chunk[9]

            last_item_8 = batch_8[-1]
            batch_9.insert(0, last_item_8)
            last_item_9 = batch_9[-1]
            batch_10.insert(0, last_item_9)

            batch_11 = result_str_chunk[10]

            last_item_10 = batch_10[-1]
            batch_11.insert(0, last_item_10)

            #  - - - - - Get value of list object- - - - - - #
            batch_1_val = latlong_summary_starting(batch_1, origin_destination)
            batch_2_val = latlong_summary(batch_2)
            batch_3_val = latlong_summary(batch_3)
            batch_4_val = latlong_summary(batch_4)
            batch_5_val = latlong_summary(batch_5)
            batch_6_val = latlong_summary(batch_6)
            batch_7_val = latlong_summary(batch_7)
            batch_8_val = latlong_summary(batch_8)
            batch_9_val = latlong_summary(batch_9)
            batch_10_val = latlong_summary(batch_10)
            batch_11_val = latlong_summary(batch_11)

            # Sum up the two batch
            route_distance_add_array = []
            route_distance_add_array.extend([batch_1_val, batch_2_val, batch_3_val, batch_4_val, batch_5_val,
                                             batch_6_val, batch_7_val, batch_8_val, batch_9_val, batch_10_val,
                                             batch_11_val])

            route_distance_add = sum(route_distance_add_array)
            route_distance = float(route_distance_add) / 1000
            return route_distance

        else:

            # Separate each part of Chunk object
            batch_1 = result_str_chunk[0]
            batch_2 = result_str_chunk[1]

            # Get Last item and insert in the index
            last_item_1 = batch_1[-1]
            batch_2.insert(0, last_item_1)

            batch_3 = result_str_chunk[2]
            batch_4 = result_str_chunk[3]

            # Get Last item and insert in the index
            last_item_2 = batch_2[-1]
            batch_3.insert(0, last_item_2)
            last_item_3 = batch_3[-1]
            batch_4.insert(0, last_item_3)

            batch_5 = result_str_chunk[4]
            batch_6 = result_str_chunk[5]

            # Get Last item and insert in the index
            last_item_4 = batch_4[-1]
            batch_5.insert(0, last_item_4)
            last_item_5 = batch_5[-1]
            batch_6.insert(0, last_item_5)

            batch_7 = result_str_chunk[6]
            batch_8 = result_str_chunk[7]

            last_item_6 = batch_6[-1]
            batch_7.insert(0, last_item_6)
            last_item_7 = batch_7[-1]
            batch_8.insert(0, last_item_7)

            batch_9 = result_str_chunk[8]
            batch_10 = result_str_chunk[9]

            last_item_8 = batch_8[-1]
            batch_9.insert(0, last_item_8)
            last_item_9 = batch_9[-1]
            batch_10.insert(0, last_item_9)

            #  - - - - - Get value of list object- - - - - - #
            time.sleep(2)

            batch_1_val = latlong_summary_starting(batch_1, origin_destination)
            batch_2_val = latlong_summary(batch_2)
            batch_3_val = latlong_summary(batch_3)
            batch_4_val = latlong_summary(batch_4)
            batch_5_val = latlong_summary(batch_5)
            batch_6_val = latlong_summary(batch_6)
            batch_7_val = latlong_summary(batch_7)
            batch_8_val = latlong_summary(batch_8)
            batch_9_val = latlong_summary(batch_9)
            batch_10_val = latlong_summary(batch_10)

            # Sum up the two batch
            route_distance_add_array = []
            route_distance_add_array.extend([batch_1_val, batch_2_val, batch_3_val, batch_4_val, batch_5_val,
                                             batch_6_val, batch_7_val, batch_8_val, batch_9_val, batch_10_val])

            route_distance_add = sum(route_distance_add_array)
            route_distance = float(route_distance_add) / 1000
            return route_distance

    elif 501 <= num_post_code <= 751:

        """ 501 <= num_post_code <= 750: """
        print "This is his is normal 501 / 24"

        result_str = ""

        for postal_code in propose_result:
            if not result_str:
                result_str += str(postal_code)
            else:
                result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes and back to list object
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "").replace("_", ", ")
        result_str = result_str.strip()
        result_str_split = result_str.split(",")

        # Chunk it
        result_str_chunk = sorting.chunkIt(result_str_split, 26)

        if len(result_str_chunk) == 27:
            # Separate each part of Chunk object
            batch_1 = result_str_chunk[0]
            batch_2 = result_str_chunk[1]

            # Get Last item and insert in the index
            last_item_1 = batch_1[-1]
            batch_2.insert(0, last_item_1)

            batch_3 = result_str_chunk[2]
            batch_4 = result_str_chunk[3]

            # Get Last item and insert in the index
            last_item_2 = batch_2[-1]
            batch_3.insert(0, last_item_2)
            last_item_3 = batch_3[-1]
            batch_4.insert(0, last_item_3)

            batch_5 = result_str_chunk[4]
            batch_6 = result_str_chunk[5]

            # Get Last item and insert in the index
            last_item_4 = batch_4[-1]
            batch_5.insert(0, last_item_4)
            last_item_5 = batch_5[-1]
            batch_6.insert(0, last_item_5)

            batch_7 = result_str_chunk[6]
            batch_8 = result_str_chunk[7]

            last_item_6 = batch_6[-1]
            batch_7.insert(0, last_item_6)
            last_item_7 = batch_7[-1]
            batch_8.insert(0, last_item_7)

            batch_9 = result_str_chunk[8]
            batch_10 = result_str_chunk[9]

            last_item_8 = batch_8[-1]
            batch_9.insert(0, last_item_8)
            last_item_9 = batch_9[-1]
            batch_10.insert(0, last_item_9)

            batch_11 = result_str_chunk[10]
            batch_12 = result_str_chunk[11]

            last_item_10 = batch_10[-1]
            batch_11.insert(0, last_item_10)
            last_item_11 = batch_11[-1]
            batch_12.insert(0, last_item_11)

            batch_13 = result_str_chunk[12]
            batch_14 = result_str_chunk[13]

            last_item_12 = batch_12[-1]
            batch_13.insert(0, last_item_12)
            last_item_13 = batch_13[-1]
            batch_14.insert(0, last_item_13)

            batch_15 = result_str_chunk[14]
            batch_16 = result_str_chunk[15]

            last_item_14 = batch_14[-1]
            batch_15.insert(0, last_item_14)
            last_item_15 = batch_15[-1]
            batch_16.insert(0, last_item_15)

            batch_17 = result_str_chunk[16]
            batch_18 = result_str_chunk[17]

            last_item_16 = batch_16[-1]
            batch_17.insert(0, last_item_16)
            last_item_17 = batch_17[-1]
            batch_18.insert(0, last_item_17)

            batch_19 = result_str_chunk[18]
            batch_20 = result_str_chunk[19]

            last_item_18 = batch_18[-1]
            batch_19.insert(0, last_item_18)
            last_item_19 = batch_19[-1]
            batch_20.insert(0, last_item_19)

            batch_21 = result_str_chunk[20]
            batch_22 = result_str_chunk[21]

            last_item_20 = batch_20[-1]
            batch_21.insert(0, last_item_20)
            last_item_21 = batch_21[-1]
            batch_22.insert(0, last_item_21)

            batch_23 = result_str_chunk[22]
            batch_24 = result_str_chunk[23]

            last_item_22 = batch_22[-1]
            batch_23.insert(0, last_item_22)
            last_item_23 = batch_23[-1]
            batch_24.insert(0, last_item_23)

            batch_25 = result_str_chunk[24]
            batch_26 = result_str_chunk[25]

            last_item_24 = batch_24[-1]
            batch_25.insert(0, last_item_24)
            last_item_25 = batch_25[-1]
            batch_26.insert(0, last_item_25)

            batch_27 = result_str_chunk[26]

            last_item_26 = batch_26[-1]
            batch_27.insert(0, last_item_26)

            #  - - - - - Get value of list object- - - - - - #

            batch_1_val = latlong_summary_starting(batch_1, origin_destination)
            batch_2_val = latlong_summary(batch_2)
            batch_3_val = latlong_summary(batch_3)
            batch_4_val = latlong_summary(batch_4)
            batch_5_val = latlong_summary(batch_5)
            batch_6_val = latlong_summary(batch_6)
            batch_7_val = latlong_summary(batch_7)
            batch_8_val = latlong_summary(batch_8)
            batch_9_val = latlong_summary(batch_9)
            batch_10_val = latlong_summary(batch_10)
            batch_11_val = latlong_summary(batch_11)
            batch_12_val = latlong_summary(batch_12)
            batch_13_val = latlong_summary(batch_13)
            batch_14_val = latlong_summary(batch_14)
            batch_15_val = latlong_summary(batch_15)
            batch_16_val = latlong_summary(batch_16)
            batch_17_val = latlong_summary(batch_17)
            batch_18_val = latlong_summary(batch_18)
            batch_19_val = latlong_summary(batch_19)
            batch_20_val = latlong_summary(batch_20)
            batch_21_val = latlong_summary(batch_21)
            batch_22_val = latlong_summary(batch_22)
            batch_23_val = latlong_summary(batch_23)
            batch_24_val = latlong_summary(batch_24)
            batch_25_val = latlong_summary(batch_25)
            batch_26_val = latlong_summary(batch_26)
            batch_27_val = latlong_summary(batch_27)


            # Sum up the two batch
            route_distance_add_array = []
            route_distance_add_array.extend([batch_1_val, batch_2_val, batch_3_val, batch_4_val, batch_5_val,
                                             batch_6_val, batch_7_val, batch_8_val, batch_9_val, batch_10_val,
                                             batch_11_val, batch_12_val, batch_13_val, batch_14_val, batch_15_val,
                                             batch_16_val, batch_17_val, batch_18_val, batch_19_val, batch_20_val,
                                             batch_21_val, batch_22_val, batch_23_val, batch_24_val, batch_25_val,
                                             batch_26_val, batch_27_val])

            route_distance_add = sum(route_distance_add_array)
            route_distance = float(route_distance_add) / 1000

            return route_distance
        else:
            # Separate each part of Chunk object
            batch_1 = result_str_chunk[0]
            batch_2 = result_str_chunk[1]

            # Get Last item and insert in the index
            last_item_1 = batch_1[-1]
            batch_2.insert(0, last_item_1)

            batch_3 = result_str_chunk[2]
            batch_4 = result_str_chunk[3]

            # Get Last item and insert in the index
            last_item_2 = batch_2[-1]
            batch_3.insert(0, last_item_2)
            last_item_3 = batch_3[-1]
            batch_4.insert(0, last_item_3)

            batch_5 = result_str_chunk[4]
            batch_6 = result_str_chunk[5]

            # Get Last item and insert in the index
            last_item_4 = batch_4[-1]
            batch_5.insert(0, last_item_4)
            last_item_5 = batch_5[-1]
            batch_6.insert(0, last_item_5)

            batch_7 = result_str_chunk[6]
            batch_8 = result_str_chunk[7]

            last_item_6 = batch_6[-1]
            batch_7.insert(0, last_item_6)
            last_item_7 = batch_7[-1]
            batch_8.insert(0, last_item_7)

            batch_9 = result_str_chunk[8]
            batch_10 = result_str_chunk[9]

            last_item_8 = batch_8[-1]
            batch_9.insert(0, last_item_8)
            last_item_9 = batch_9[-1]
            batch_10.insert(0, last_item_9)

            batch_11 = result_str_chunk[10]
            batch_12 = result_str_chunk[11]

            last_item_10 = batch_10[-1]
            batch_11.insert(0, last_item_10)
            last_item_11 = batch_11[-1]
            batch_12.insert(0, last_item_11)

            batch_13 = result_str_chunk[12]
            batch_14 = result_str_chunk[13]

            last_item_12 = batch_12[-1]
            batch_13.insert(0, last_item_12)
            last_item_13 = batch_13[-1]
            batch_14.insert(0, last_item_13)

            batch_15 = result_str_chunk[14]
            batch_16 = result_str_chunk[15]

            last_item_14 = batch_14[-1]
            batch_15.insert(0, last_item_14)
            last_item_15 = batch_15[-1]
            batch_16.insert(0, last_item_15)

            batch_17 = result_str_chunk[16]
            batch_18 = result_str_chunk[17]

            last_item_16 = batch_16[-1]
            batch_17.insert(0, last_item_16)
            last_item_17 = batch_17[-1]
            batch_18.insert(0, last_item_17)

            batch_19 = result_str_chunk[18]
            batch_20 = result_str_chunk[19]

            last_item_18 = batch_18[-1]
            batch_19.insert(0, last_item_18)
            last_item_19 = batch_19[-1]
            batch_20.insert(0, last_item_19)

            batch_21 = result_str_chunk[20]
            batch_22 = result_str_chunk[21]

            last_item_20 = batch_20[-1]
            batch_21.insert(0, last_item_20)
            last_item_21 = batch_21[-1]
            batch_22.insert(0, last_item_21)

            batch_23 = result_str_chunk[22]
            batch_24 = result_str_chunk[23]

            last_item_22 = batch_22[-1]
            batch_23.insert(0, last_item_22)
            last_item_23 = batch_23[-1]
            batch_24.insert(0, last_item_23)

            batch_25 = result_str_chunk[24]
            batch_26 = result_str_chunk[25]

            last_item_24 = batch_24[-1]
            batch_25.insert(0, last_item_24)
            last_item_25 = batch_25[-1]
            batch_26.insert(0, last_item_25)

            #  - - - - - Get value of list object- - - - - - #

            batch_1_val = latlong_summary_starting(batch_1, origin_destination)
            batch_2_val = latlong_summary(batch_2)
            batch_3_val = latlong_summary(batch_3)
            batch_4_val = latlong_summary(batch_4)
            batch_5_val = latlong_summary(batch_5)
            batch_6_val = latlong_summary(batch_6)
            batch_7_val = latlong_summary(batch_7)
            batch_8_val = latlong_summary(batch_8)
            batch_9_val = latlong_summary(batch_9)
            batch_10_val = latlong_summary(batch_10)
            batch_11_val = latlong_summary(batch_11)
            batch_12_val = latlong_summary(batch_12)
            batch_13_val = latlong_summary(batch_13)
            batch_14_val = latlong_summary(batch_14)
            batch_15_val = latlong_summary(batch_15)
            batch_16_val = latlong_summary(batch_16)
            batch_17_val = latlong_summary(batch_17)
            batch_18_val = latlong_summary(batch_18)
            batch_19_val = latlong_summary(batch_19)
            batch_20_val = latlong_summary(batch_20)
            batch_21_val = latlong_summary(batch_21)
            batch_22_val = latlong_summary(batch_22)
            batch_23_val = latlong_summary(batch_23)
            batch_24_val = latlong_summary(batch_24)
            batch_25_val = latlong_summary(batch_25)
            batch_26_val = latlong_summary(batch_26)

            # Sum up the two batch
            route_distance_add_array = []
            route_distance_add_array.extend([batch_1_val, batch_2_val, batch_3_val, batch_4_val, batch_5_val,
                                             batch_6_val, batch_7_val, batch_8_val, batch_9_val, batch_10_val,
                                             batch_11_val, batch_12_val, batch_13_val, batch_14_val, batch_15_val,
                                             batch_16_val, batch_17_val, batch_18_val, batch_19_val, batch_20_val,
                                             batch_21_val, batch_22_val, batch_23_val, batch_24_val, batch_25_val,
                                             batch_26_val])

            route_distance_add = sum(route_distance_add_array)
            route_distance = float(route_distance_add) / 1000

            return route_distance

    elif 752 <= num_post_code <= 850:
        """ 850 <= num_post_code <= 750: """
        print "This is this is normal 850 / 34"

        result_str = ""

        for postal_code in propose_result:
            if not result_str:
                result_str += str(postal_code)
            else:
                result_str += "_" + str(postal_code)

        # Remove square brackets and single quotes and back to list object
        result_str = result_str.replace("[", "").replace("]", "").replace("\'", "").replace("_", ", ")
        result_str = result_str.strip()
        result_str_split = result_str.split(",")

        # Chunk it
        result_str_chunk = sorting.chunkIt(result_str_split, 34)

        if len(result_str_chunk) == 35:
            # Separate each part of Chunk object
            batch_1 = result_str_chunk[0]
            batch_2 = result_str_chunk[1]

            # Get Last item and insert in the index
            last_item_1 = batch_1[-1]
            batch_2.insert(0, last_item_1)

            batch_3 = result_str_chunk[2]
            batch_4 = result_str_chunk[3]

            # Get Last item and insert in the index
            last_item_2 = batch_2[-1]
            batch_3.insert(0, last_item_2)
            last_item_3 = batch_3[-1]
            batch_4.insert(0, last_item_3)

            batch_5 = result_str_chunk[4]
            batch_6 = result_str_chunk[5]

            # Get Last item and insert in the index
            last_item_4 = batch_4[-1]
            batch_5.insert(0, last_item_4)
            last_item_5 = batch_5[-1]
            batch_6.insert(0, last_item_5)

            batch_7 = result_str_chunk[6]
            batch_8 = result_str_chunk[7]

            last_item_6 = batch_6[-1]
            batch_7.insert(0, last_item_6)
            last_item_7 = batch_7[-1]
            batch_8.insert(0, last_item_7)

            batch_9 = result_str_chunk[8]
            batch_10 = result_str_chunk[9]

            last_item_8 = batch_8[-1]
            batch_9.insert(0, last_item_8)
            last_item_9 = batch_9[-1]
            batch_10.insert(0, last_item_9)

            batch_11 = result_str_chunk[10]
            batch_12 = result_str_chunk[11]

            last_item_10 = batch_10[-1]
            batch_11.insert(0, last_item_10)
            last_item_11 = batch_11[-1]
            batch_12.insert(0, last_item_11)

            batch_13 = result_str_chunk[12]
            batch_14 = result_str_chunk[13]

            last_item_12 = batch_12[-1]
            batch_13.insert(0, last_item_12)
            last_item_13 = batch_13[-1]
            batch_14.insert(0, last_item_13)

            batch_15 = result_str_chunk[14]
            batch_16 = result_str_chunk[15]

            last_item_14 = batch_14[-1]
            batch_15.insert(0, last_item_14)
            last_item_15 = batch_15[-1]
            batch_16.insert(0, last_item_15)

            batch_17 = result_str_chunk[16]
            batch_18 = result_str_chunk[17]

            last_item_16 = batch_16[-1]
            batch_17.insert(0, last_item_16)
            last_item_17 = batch_17[-1]
            batch_18.insert(0, last_item_17)

            batch_19 = result_str_chunk[18]
            batch_20 = result_str_chunk[19]

            last_item_18 = batch_18[-1]
            batch_19.insert(0, last_item_18)
            last_item_19 = batch_19[-1]
            batch_20.insert(0, last_item_19)

            batch_21 = result_str_chunk[20]
            batch_22 = result_str_chunk[21]

            last_item_20 = batch_20[-1]
            batch_21.insert(0, last_item_20)
            last_item_21 = batch_21[-1]
            batch_22.insert(0, last_item_21)

            batch_23 = result_str_chunk[22]
            batch_24 = result_str_chunk[23]

            last_item_22 = batch_22[-1]
            batch_23.insert(0, last_item_22)
            last_item_23 = batch_23[-1]
            batch_24.insert(0, last_item_23)

            batch_25 = result_str_chunk[24]
            batch_26 = result_str_chunk[25]

            last_item_24 = batch_24[-1]
            batch_25.insert(0, last_item_24)
            last_item_25 = batch_25[-1]
            batch_26.insert(0, last_item_25)

            batch_27 = result_str_chunk[26]
            batch_28 = result_str_chunk[27]

            last_item_26 = batch_26[-1]
            batch_27.insert(0, last_item_26)
            last_item_27 = batch_27[-1]
            batch_28.insert(0, last_item_27)

            batch_29 = result_str_chunk[28]
            batch_30 = result_str_chunk[29]

            last_item_28 = batch_28[-1]
            batch_29.insert(0, last_item_28)
            last_item_29 = batch_29[-1]
            batch_30.insert(0, last_item_29)

            batch_31 = result_str_chunk[30]
            batch_32 = result_str_chunk[31]

            last_item_30 = batch_30[-1]
            batch_31.insert(0, last_item_30)
            last_item_31 = batch_31[-1]
            batch_32.insert(0, last_item_31)

            batch_33 = result_str_chunk[32]
            batch_34 = result_str_chunk[33]

            last_item_32 = batch_32[-1]
            batch_33.insert(0, last_item_32)
            last_item_33 = batch_33[-1]
            batch_34.insert(0, last_item_33)

            batch_35 = result_str_chunk[34]

            last_item_34 = batch_34[-1]
            batch_35.insert(0, last_item_34)

            #  - - - - - Get value of list object- - - - - - #

            batch_1_val = latlong_summary_starting(batch_1, origin_destination)
            batch_2_val = latlong_summary(batch_2)
            batch_3_val = latlong_summary(batch_3)
            batch_4_val = latlong_summary(batch_4)
            batch_5_val = latlong_summary(batch_5)
            batch_6_val = latlong_summary(batch_6)
            batch_7_val = latlong_summary(batch_7)
            batch_8_val = latlong_summary(batch_8)
            batch_9_val = latlong_summary(batch_9)
            batch_10_val = latlong_summary(batch_10)
            batch_11_val = latlong_summary(batch_11)
            batch_12_val = latlong_summary(batch_12)
            batch_13_val = latlong_summary(batch_13)
            batch_14_val = latlong_summary(batch_14)
            batch_15_val = latlong_summary(batch_15)
            batch_16_val = latlong_summary(batch_16)
            batch_17_val = latlong_summary(batch_17)
            batch_18_val = latlong_summary(batch_18)
            batch_19_val = latlong_summary(batch_19)
            batch_20_val = latlong_summary(batch_20)
            batch_21_val = latlong_summary(batch_21)
            batch_22_val = latlong_summary(batch_22)
            batch_23_val = latlong_summary(batch_23)
            batch_24_val = latlong_summary(batch_24)
            batch_25_val = latlong_summary(batch_25)
            batch_26_val = latlong_summary(batch_26)
            batch_27_val = latlong_summary(batch_27)
            batch_28_val = latlong_summary(batch_28)
            batch_29_val = latlong_summary(batch_29)
            batch_30_val = latlong_summary(batch_30)
            batch_31_val = latlong_summary(batch_31)
            batch_32_val = latlong_summary(batch_32)
            batch_33_val = latlong_summary(batch_33)
            batch_34_val = latlong_summary(batch_34)
            batch_35_val = latlong_summary(batch_35)

            # Sum up the two batch
            route_distance_add_array = []
            route_distance_add_array.extend([batch_1_val, batch_2_val, batch_3_val, batch_4_val, batch_5_val,
                                            batch_6_val, batch_7_val, batch_8_val, batch_9_val, batch_10_val,
                                            batch_11_val, batch_12_val, batch_13_val, batch_14_val, batch_15_val,
                                            batch_16_val, batch_17_val, batch_18_val, batch_19_val, batch_20_val,
                                            batch_21_val, batch_22_val, batch_23_val, batch_24_val, batch_25_val,
                                            batch_26_val, batch_27_val, batch_28_val, batch_29_val, batch_30_val,
                                            batch_31_val, batch_32_val, batch_33_val, batch_34_val, batch_35_val])

            route_distance_add = sum(route_distance_add_array)
            route_distance = float(route_distance_add) / 1000

            return route_distance

        else:

            # Separate each part of Chunk object
            batch_1 = result_str_chunk[0]
            batch_2 = result_str_chunk[1]

            # Get Last item and insert in the index
            last_item_1 = batch_1[-1]
            batch_2.insert(0, last_item_1)

            batch_3 = result_str_chunk[2]
            batch_4 = result_str_chunk[3]

            # Get Last item and insert in the index
            last_item_2 = batch_2[-1]
            batch_3.insert(0, last_item_2)
            last_item_3 = batch_3[-1]
            batch_4.insert(0, last_item_3)

            batch_5 = result_str_chunk[4]
            batch_6 = result_str_chunk[5]

            # Get Last item and insert in the index
            last_item_4 = batch_4[-1]
            batch_5.insert(0, last_item_4)
            last_item_5 = batch_5[-1]
            batch_6.insert(0, last_item_5)

            batch_7 = result_str_chunk[6]
            batch_8 = result_str_chunk[7]

            last_item_6 = batch_6[-1]
            batch_7.insert(0, last_item_6)
            last_item_7 = batch_7[-1]
            batch_8.insert(0, last_item_7)

            batch_9 = result_str_chunk[8]
            batch_10 = result_str_chunk[9]

            last_item_8 = batch_8[-1]
            batch_9.insert(0, last_item_8)
            last_item_9 = batch_9[-1]
            batch_10.insert(0, last_item_9)

            batch_11 = result_str_chunk[10]
            batch_12 = result_str_chunk[11]

            last_item_10 = batch_10[-1]
            batch_11.insert(0, last_item_10)
            last_item_11 = batch_11[-1]
            batch_12.insert(0, last_item_11)

            batch_13 = result_str_chunk[12]
            batch_14 = result_str_chunk[13]

            last_item_12 = batch_12[-1]
            batch_13.insert(0, last_item_12)
            last_item_13 = batch_13[-1]
            batch_14.insert(0, last_item_13)

            batch_15 = result_str_chunk[14]
            batch_16 = result_str_chunk[15]

            last_item_14 = batch_14[-1]
            batch_15.insert(0, last_item_14)
            last_item_15 = batch_15[-1]
            batch_16.insert(0, last_item_15)

            batch_17 = result_str_chunk[16]
            batch_18 = result_str_chunk[17]

            last_item_16 = batch_16[-1]
            batch_17.insert(0, last_item_16)
            last_item_17 = batch_17[-1]
            batch_18.insert(0, last_item_17)

            batch_19 = result_str_chunk[18]
            batch_20 = result_str_chunk[19]

            last_item_18 = batch_18[-1]
            batch_19.insert(0, last_item_18)
            last_item_19 = batch_19[-1]
            batch_20.insert(0, last_item_19)

            batch_21 = result_str_chunk[20]
            batch_22 = result_str_chunk[21]

            last_item_20 = batch_20[-1]
            batch_21.insert(0, last_item_20)
            last_item_21 = batch_21[-1]
            batch_22.insert(0, last_item_21)

            batch_23 = result_str_chunk[22]
            batch_24 = result_str_chunk[23]

            last_item_22 = batch_22[-1]
            batch_23.insert(0, last_item_22)
            last_item_23 = batch_23[-1]
            batch_24.insert(0, last_item_23)

            batch_25 = result_str_chunk[24]
            batch_26 = result_str_chunk[25]

            last_item_24 = batch_24[-1]
            batch_25.insert(0, last_item_24)
            last_item_25 = batch_25[-1]
            batch_26.insert(0, last_item_25)

            batch_27 = result_str_chunk[26]
            batch_28 = result_str_chunk[27]

            last_item_26 = batch_26[-1]
            batch_27.insert(0, last_item_26)
            last_item_27 = batch_27[-1]
            batch_28.insert(0, last_item_27)

            batch_29 = result_str_chunk[28]
            batch_30 = result_str_chunk[29]

            last_item_28 = batch_28[-1]
            batch_29.insert(0, last_item_28)
            last_item_29 = batch_29[-1]
            batch_30.insert(0, last_item_29)

            batch_31 = result_str_chunk[30]
            batch_32 = result_str_chunk[31]

            last_item_30 = batch_30[-1]
            batch_31.insert(0, last_item_30)
            last_item_31 = batch_31[-1]
            batch_32.insert(0, last_item_31)

            batch_33 = result_str_chunk[32]
            batch_34 = result_str_chunk[33]

            last_item_32 = batch_32[-1]
            batch_33.insert(0, last_item_32)
            last_item_33 = batch_33[-1]
            batch_34.insert(0, last_item_33)

            #  - - - - - Get value of list object- - - - - - #

            batch_1_val = latlong_summary_starting(batch_1, origin_destination)
            batch_2_val = latlong_summary(batch_2)
            batch_3_val = latlong_summary(batch_3)
            batch_4_val = latlong_summary(batch_4)
            batch_5_val = latlong_summary(batch_5)
            batch_6_val = latlong_summary(batch_6)
            batch_7_val = latlong_summary(batch_7)
            batch_8_val = latlong_summary(batch_8)
            batch_9_val = latlong_summary(batch_9)
            batch_10_val = latlong_summary(batch_10)
            batch_11_val = latlong_summary(batch_11)
            batch_12_val = latlong_summary(batch_12)
            batch_13_val = latlong_summary(batch_13)
            batch_14_val = latlong_summary(batch_14)
            batch_15_val = latlong_summary(batch_15)
            batch_16_val = latlong_summary(batch_16)
            batch_17_val = latlong_summary(batch_17)
            batch_18_val = latlong_summary(batch_18)
            batch_19_val = latlong_summary(batch_19)
            batch_20_val = latlong_summary(batch_20)
            batch_21_val = latlong_summary(batch_21)
            batch_22_val = latlong_summary(batch_22)
            batch_23_val = latlong_summary(batch_23)
            batch_24_val = latlong_summary(batch_24)
            batch_25_val = latlong_summary(batch_25)
            batch_26_val = latlong_summary(batch_26)
            batch_27_val = latlong_summary(batch_27)
            batch_28_val = latlong_summary(batch_28)
            batch_29_val = latlong_summary(batch_29)
            batch_30_val = latlong_summary(batch_30)
            batch_31_val = latlong_summary(batch_31)
            batch_32_val = latlong_summary(batch_32)
            batch_33_val = latlong_summary(batch_33)
            batch_34_val = latlong_summary(batch_34)

            # Sum up the two batch
            route_distance_add_array = []
            route_distance_add_array.extend([batch_1_val, batch_2_val, batch_3_val, batch_4_val, batch_5_val,
                                            batch_6_val, batch_7_val, batch_8_val, batch_9_val, batch_10_val,
                                            batch_11_val, batch_12_val, batch_13_val, batch_14_val, batch_15_val,
                                            batch_16_val, batch_17_val, batch_18_val, batch_19_val, batch_20_val,
                                            batch_21_val, batch_22_val, batch_23_val, batch_24_val, batch_25_val,
                                            batch_26_val, batch_27_val, batch_28_val, batch_29_val, batch_30_val,
                                            batch_31_val, batch_32_val, batch_33_val, batch_34_val])

            route_distance_add = sum(route_distance_add_array)
            route_distance = float(route_distance_add) / 1000

            return route_distance

    else:
        errors = []
        errors.extend(['Exceeding volume in postal code'])

        return errors


def latlong_summary(list):

    url_disc = "http://dev.logistics.lol:5000/viaroute?"
    proposed_latlong = ""

    for current_post in list:
        current_post = current_post.strip()

        # Convert to Lat-Long the postal code
        destinations = postalcode_latlong(current_post)

        if not destinations:
            proposed_latlong += str(destinations)
        else:
            proposed_latlong += "&loc=" + str(destinations)

    proposed_result = proposed_latlong
    proposed_api = url_disc + proposed_result

    dist_val = urllib2.urlopen(proposed_api, timeout=60)

    wjson = dist_val.read()
    distance2 = json.loads(wjson)

    distance_val = distance2['route_summary']['total_distance']

    return distance_val


def latlong_summary_starting(list, origin_destination):

    url_disc = "http://dev.logistics.lol:5000/viaroute?loc="
    proposed_latlong = ""

    for current_post in list:
        current_post = current_post.strip()

        # Convert to Lat-Long the postal code
        destinations = postalcode_latlong(current_post)

        if not destinations:
            proposed_latlong += str(destinations)
        else:
            proposed_latlong += "&loc=" + str(destinations)

    proposed_result = origin_destination + proposed_latlong
    proposed_api = url_disc + proposed_result

    # result = urlfetch.fetch(url_disc, method='POST', deadline=30)

    dist_val = urllib2.urlopen(proposed_api, timeout=60)

    # - - - - - - -#

    # resource = urlfetch.fetch("http://tinyurl.com/api-create.php", urlfetch.POST)

    # # logging.info(resource.content)
    # # self.response.out.write(resource.content)

    # - - - - - - -#
    wjson = dist_val.read()
    distance2 = json.loads(wjson)
    distance_val = distance2['route_summary']['total_distance']

    return distance_val


# - - - - - validation for company number - - - - - #

# Function to iterate the number of companies and return to UI
class SortingPrep_comp(webapp2.RequestHandler):
    def post(self):

        postal_sequence = self.request.get("postal_sequence")
        priority_capacity_comp = self.request.get("priority_capacity_comp")

        # - - - - - - - - -  REQUEST - - - - - - - - - - #

        # Error list for invalid postal codes
        no_record_postal = []

        response = {}
        errors = []

        # Remove trailing whitespaces
        postal_sequence = postal_sequence.strip()

        # Split up the input by newlines
        postal_sequence_split = str(postal_sequence).split("\n")

        # For storage of a full valid sequence of postal codes
        postal_sequence_list = []
        list_of_companies = []
        postal_sequence_current = []

        # Counter checking of Postal Code
        num_post_code = 0

        # Extract the postal pair and validate the postal code while ignoring first line of headers
        # Note: Order ID is untouched as we do not know their format
        for index in range(1, len(postal_sequence_split)):
            num_post_code = num_post_code + 1

            # Retrieve each postal pair
            postal_pair = postal_sequence_split[index]

            # Replace all tab spaces with normal spaces and remove trailing whitespace
            postal_pair = postal_pair.replace("\t", " ")
            postal_pair = postal_pair.strip()

            # Split the order ID/postal code pair by normal spacing
            postal_pair_split = postal_pair.split(" ")

            if len(postal_pair_split) == 3:
                print 'Please add Company in 4th column'
                errors.extend(['Please add Company in 4th column <br />'])

            if len(errors) == 0:
                postal_code = str(postal_pair_split[0])
                order_id = str(postal_pair_split[1])
                track_capacity = int(postal_pair_split[2])
                sorted_comp = postal_pair_split[3]

                postal_sequence_current.append(postal_code)
                postal_sequence_list.append([postal_code, str(order_id), int(track_capacity), sorted_comp])
                list_of_companies.append(sorted_comp)

        # - - - - - - HQ Starting point Lat Long - - - - - #
        """ each company will separated and this will indicate the color plotting in map like vehicle count """
        """ Vehicle-color will same method of color as for Company separation """

        # Create variable for each request
        company_list_grp = []
        postal_sequence_company = []

        for company in range(len(postal_sequence_list)):
            companyList = postal_sequence_list[company]
            company_list_grp.append(companyList)

        for key, group in itertools.groupby(company_list_grp, operator.itemgetter(3)):
            # group as per company
            postal_sequence_company.append(list(group))

        # Get All Name of the companies:
        seen = {}
        name_of_companies = [seen.setdefault(x, x) for x in list_of_companies if x not in seen]

        # count the company
        num_comp_val = int(len(postal_sequence_company))

        # Converting JSON
        response['status'] = 'ok'
        response['sort_company'] = 'true'
        response['data_valid_company'] = [
            {
                "required_fields": {
                    "propose_results": postal_sequence_company,
                    "name_of_companies": name_of_companies,
                    "priority_capacity_comp": priority_capacity_comp,
                    "num_comp_val": num_comp_val,
                }

            }
        ]
        # else:
        #     errors.extend(['Error in Postal Code'])

        if len(errors) > 0:
            response['status'] = 'error'
            response['errors'] = errors

        logging.info(response)
        self.response.out.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.out.write(json.dumps(response, indent=3))


app = webapp2.WSGIApplication(routes=[
    (r'/sorting', SortingPrep),
    (r'/sorting_comp', SortingPrep_comp)
], config=base.sessionConfig, debug=True)
