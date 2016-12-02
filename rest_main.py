import webapp2
import mimetypes
import os
import time
from datetime import datetime
import base64
import urlparse
from httplib import HTTPResponse

import logging
import json
import itertools
import pickle

import operator

from operator import itemgetter
from collections import defaultdict

import urllib
# ------ sorting -----
from handlers import sorting, sorting_prep

from model.user_account import UserAccount
from model.admin_account import postalRecordDB

from google.appengine.api import taskqueue


'''
{
  "status": "ok",
  "data_result": [
    {
      "vehicle_details": {
        "grp_truck": [
          [
            "AAA"
          ]
        ]
      },
      "required_fields": {
        "priority_capacity": "true",
        "starting_postal": "461051",
        "propose_result": [
          [
            [
              "460102",
              "Order10",
              1,
              1
            ],
            [
              "469001",
              "Order01",
              1,
              1
            ],
            [
              "431011",
              "Order09",
              1,
              1
            ],
            [
              "098585",
              "Order05",
              1,
              1
            ],
            [
              "109680",
              "Order06",
              1,
              1
            ],
            [
              "278986",
              "Order08",
              1,
              1
            ],
            [
              "596740",
              "Order04",
              1,
              1
            ],
            [
              "596937",
              "Order03",
              1,
              1
            ],
            [
              "760450",
              "Order02",
              1,
              1
            ],
            [
              "560405",
              "Order07",
              1,
              1
            ],
            [
              "461051",
              0,
              0,
              0
            ]
          ]
        ],
        "has_return": "true"
      },
      "total_summary_saving": {
        "propose_distance": 88.685,
        "total_savings": 25.637263122589303,
        "current_distance": 119.26
      },
      "geo_code_latlng": {
        "latlng_array": [
          [
            [
              "1.334002",
              "103.937209"
            ],
            [
              "1.322995",
              "103.922194"
            ],
            [
              "1.30161",
              "103.882607"
            ],
            [
              "1.264241",
              "103.822287"
            ],
            [
              "1.280195",
              "103.815126"
            ],
            [
              "1.31153",
              "103.795481"
            ],
            [
              "1.34211",
              "103.767283"
            ],
            [
              "1.337952",
              "103.765192"
            ],
            [
              "1.422128",
              "103.844128"
            ],
            [
              "1.361599",
              "103.853662"
            ],
            [
              "1.323477",
              "103.942084"
            ]
          ]
        ]
      }
    }
  ]
}
'''

def checkInRequest(field, request):
    # if myconstants.DEBUG:
    #     logging.debug(field)

    if field in request:
        return request[field], []
    else:
        return None, [field + " missing"]

"""
{
    "starting_postal": "461051",
    "order_details": [
                     ["469001", "Order01", 1],
                      ["760450", "Order02", 1],
                      ["596937", "Order03", 1],
                      ["596740", "Order04", 1],
                      ["098585", "Order05", 1],
                      ["109680", "Order06", 1],
                      ["560405", "Order07", 1],
                      ["278986", "Order08", 1],
                      ["431011", "Order09", 1],
                      ["460102", "Order10", 1]

                    ],
    "truck_details":
    	[
      		{
	           "type_of_truck": "AAA",
	           	"truck_capacity": 10,
				"num_of_truck": 1
	      	}

      	],
    "has_return": "true",
    "priority_capacity": "true"
}
"""

class Truck_capacity_API(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Headers'] = 'Authorization'
        self.response.headers['Access-Control-Allow-Headers'] = 'Cache-Control'
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'
        self.response.headers['Content-Type'] = 'application/json;charset=utf-8'

        email = self.request.get('userId')
        api_key = self.request.get('keyId')

        # Error list for invalid postal codes
        errors = []

        api_user = "false"
        auth_user = UserAccount.check_API_auth(email, api_key)

        # Sorting postal code sequence code
        postal_sequence_list = []
        postal_sequence_current = []

        # Error Message
        error_valid_msg_truck = "Add more truck! <br />The minimum balance number for delivery truck "
        error_capacity_msg_truck = " - exceeding capacity"
        error_capacity_num_truck = "Maximum 15 Trucks only"
        error_capacity_cargo_unit = "Please check the input cargo unit - Location Details"

        maximum_truck = 15

        if auth_user == None:
            errors.extend(['Incorrect email or API Key'])

        if auth_user == True:
            api_user = "true"

        # Checking for Credit Access
        credits_account = UserAccount.check_credit_usage(email)

        if credits_account == None:
            errors.extend(['Error in Credits Access'])

        response = {}

        request_str = self.request.body
        logging.info(request_str)

        if len(errors) == 0:

            try:
                data = json.loads(request_str)
            except:
                errors.extend(['Error in JSON'])

        if len(errors) == 0:

            starting_postal, error = checkInRequest('starting_postal', data)
            errors.extend(error)

            order_details, error = checkInRequest('order_details', data)
            errors.extend(error)

            truck_details, error = checkInRequest('truck_details', data)
            errors.extend(error)

            # trigger value
            has_return, error = checkInRequest('has_return', data)
            errors.extend(error)

            priority_capacity, error = checkInRequest('priority_capacity', data)
            errors.extend(error)

            # Grp truck details
            # Type of Truck
            truck_capacity_grp = []

            for truck_detail in truck_details:
                # extract the truck
                type_of_truck = truck_detail["type_of_truck"]
                truck_capacity = truck_detail["truck_capacity"]
                num_of_truck = truck_detail["num_of_truck"]

                truck_capacity_grp.append([str(type_of_truck), int(truck_capacity), int(num_of_truck)])

            # count the capacity
            limit_sum = 0

            # count num of truck
            truck_sum = 0

            for num_truck in range(0, len(truck_capacity_grp)):
                current_num = truck_capacity_grp[num_truck]
                capacity_limit = current_num[1]
                num_truck = current_num[2]

                limit_sum += capacity_limit
                truck_sum += num_truck

            # Show error if reach maximum truck allowed
            if truck_sum > maximum_truck:
                logging.info('Warning! ' + error_capacity_num_truck)
                errors.extend(['Warning! ' + error_capacity_num_truck])

            # add zero
            # For empty order id and capacity
            # temp_comp = ['0', '0', '0']
            # forEmp_OrderID_Cap = ['0', '0']
            # temp_comp = ['0']

            # Counter checking of Postal Code
            num_post_code = 0

            for index in range(0, len(order_details)):

                """ ['760450', 'Order02', '2'] """

                num_post_code += 1
                postal_pair = order_details[index]

                # Show error if one column only
                if len(postal_pair) == 1:
                    logging.info(postal_pair)
                    errors.extend([error_capacity_cargo_unit])
                    break

                # Show error if the two column
                if len(postal_pair) == 2:
                    logging.info(postal_pair)
                    errors.extend([error_capacity_cargo_unit])
                    break

                # Add 4th column for indexing in DataStore
                # if len(postal_pair) == 3:
                #     postal_pair.extend(temp_comp)

                # extract each column of Delivery Location Details
                postal_code = str(postal_pair[0])
                order_id = str(postal_pair[1])
                track_capacity = postal_pair[2]
                # temp_id = postal_pair[3]

                # Check if the postal code is 5 digit only
                if len(str(postal_code)) == 5:
                    # add "0" in the index of Postal Code
                    postal_code = "0" + postal_code

                # Check if the 3rd column is integer or number
                cargo_unit = RepresentsInt(track_capacity)

                if not cargo_unit:
                    errors.extend([postal_code + ' Error in track_capacity'])
                    break

                # Check if postal code is a valid value i.e. Contains only five or six digits
                if not str.isdigit(postal_code) or len(str(postal_code)) != 6:

                    logging.info('Warning! Postal Code error')
                    errors.extend(['Please check '+postal_code+ ' is not valid it should be 6 digit'])

                # Check the limit capacity of the truck
                if int(track_capacity) > int(limit_sum):
                    logging.info('Warning! ' + postal_code + error_capacity_msg_truck)
                    errors.extend(['Warning! '+postal_code + error_capacity_msg_truck])

                    break

                postal_sequence_current.append(str(postal_code))
                postal_sequence_list.append([str(postal_code), str(order_id), int(track_capacity)])

                # - - - - - - HQ Starting point Lat Long - - - - - #

            # maximum of 3 fields for truck
            # Additional Field of Truck 2
            # type_of_truck_1
            # truck_capacity_1
            # num_of_truck_1

            # Additional Field of Truck 3
            # type_of_truck_2
            # truck_capacity_2
            # num_of_truck_2

            # For Non Multi Truck
            options_truck = "false"
            priority_capacity_comp = "false"
            sort_company = "false"
            vehicle_quantity = 0

            if len(errors) == 0:

                origin_destination, propose_result, current_result, vehicle_postal_list_new_seq, grp_truck = sorting.sort_by_postals_chunck(
                    int(starting_postal),
                    postal_sequence_list,
                    int(vehicle_quantity),
                    email, has_return,
                    priority_capacity,
                    priority_capacity_comp,
                    api_user, sort_company, truck_capacity_grp, options_truck)

                # Vehicle Result base of the priority:
                result_num_truck = len(propose_result)

                # Show error if the Number of truck is not enough
                if int(len(propose_result)) > int(truck_sum):
                    errors.extend([error_valid_msg_truck + " is " + str(result_num_truck)])

                # Converting HQ to lat & long value
                current_distance = sorting_prep.result_distance_latlng(current_result, origin_destination, num_post_code)
                proposed_distance = sorting_prep.result_distance_latlng(propose_result, origin_destination, num_post_code)

                # GeoCode Map
                latlng_array = map_visible(propose_result)

                # Converting the total percentage saving of distance
                difference_total = current_distance - proposed_distance
                percentage_savings = (difference_total / current_distance) * 100

                if len(errors) == 0:

                    # Converting JSON
                    response['status'] = 'ok'
                    response['data_result'] = [
                            {
                                "required_fields": {
                                    "starting_postal": starting_postal,
                                    "propose_result": vehicle_postal_list_new_seq,
                                    "has_return": has_return,
                                    "priority_capacity": priority_capacity,
                                    },
                                "geo_code_latlng": {
                                    "latlng_array": latlng_array
                                },
                                "vehicle_details": {

                                    "grp_truck": grp_truck
                                    },
                                "total_summary_saving": {
                                    "propose_distance": proposed_distance,
                                    "current_distance": current_distance,
                                    "total_savings": percentage_savings
                                    }
                            }
                        ]

            else:
                errors.extend(['Error in Process'])

        if len(errors) > 0:
            response['status'] = 'error'
            response['errors'] = errors

        logging.info(response)
        self.response.out.write(json.dumps(response, indent=3))

"""
{
    "starting_postal": "461051",
    "order_details": [
                      ["469001", "Order01"],
                      ["760450", "Order02"],
                      ["596937", "Order03"],
                      ["596740", "Order04"],
                      ["098585", "Order05"],
                      ["109680", "Order06"],
                      ["560405", "Order07"],
                      ["278986", "Order08"],
                      ["431011", "Order09"],
                      ["460102", "Order10"]

                    ],
    "number_of_vehicle" : 1,
    "has_return": "true",
    "options_truck": "true"
}

"""

class Multi_truck_API(webapp2.RequestHandler):

    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Headers'] = 'Authorization'
        self.response.headers['Access-Control-Allow-Headers'] = 'Cache-Control'
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'
        self.response.headers['Content-Type'] = 'application/json;charset=utf-8'

        # api_key = self.request.authorization

        email = self.request.get('userId')
        api_key = self.request.get('keyId')

        # Error list for invalid postal codes
        errors = []

        api_user = "false"
        auth_user = UserAccount.check_API_auth(email, api_key)

        if auth_user == None:
            errors.extend(['Incorrect email or API Key'])

        if auth_user == True:
            api_user = "true"

        # Checking for Credit Access
        credits_account = UserAccount.check_credit_usage(email)

        if credits_account == None:
            errors.extend(['Error in Credits Access <br />'])

        response = {}
        request_str = self.request.body
        logging.info(request_str)

        if len(errors) == 0:

            try:
                data = json.loads(request_str)

            except:

                errors.extend(['Error in JSON'])

        if len(errors) == 0:

            starting_postal, error = checkInRequest('starting_postal', data)
            errors.extend(error)

            order_details, error = checkInRequest('order_details', data)
            errors.extend(error)

            number_of_vehicle, error = checkInRequest('number_of_vehicle', data)
            errors.extend(error)

            has_return, error = checkInRequest('has_return', data)
            errors.extend(error)

            options_truck, error = checkInRequest('options_truck', data)
            errors.extend(error)

            # Sorting postal code sequence code
            postal_sequence_list = []
            postal_sequence_current = []

            # For empty order
            temp_order_id = ['0']
            # forEmp_Capt = ['0', '0']

            # Validation for Vehicle
            if not number_of_vehicle:
                errors.extend(["number_of_vehicle" + " is empty"])

            # starting point 5 digit
            if len(str(starting_postal)) == 5:
                    starting_postal = "0" + starting_postal

            # if below 5 digit
            if len(str(starting_postal)) != 6:
                logging.info('Warning! error')
                errors.extend(['Starting Postal code is not valid, it should be 6 digit'])

            # Counter checking of Postal Code
            num_post_code = 0

            for index in range(0, len(order_details)):
                num_post_code += 1
                postal_pair = order_details[index]

                """ [u'760450', u'Order02'] """

                if len(postal_pair) == 1:
                    logging.info(postal_pair)
                    postal_pair.extend(temp_order_id)

                # if len(postal_pair) == 2:
                #     logging.info(postal_pair)
                #     postal_pair.extend(forEmp_Capt)

                postal_code = str(postal_pair[0])
                order_id = str(postal_pair[1])

                # track_capacity = int(postal_pair[2])
                # temp_id = postal_pair[3]

                if len(str(postal_code)) == 5:
                    postal_code = "0" + postal_code

                # Check if postal code is a valid value i.e. Contains only five or six digits
                if not str.isdigit(postal_code) or len(str(postal_code)) != 6:
                    logging.info('Warning! Postal Code error')
                    errors.extend(['Please check '+postal_code+ ' is not valid it should be 6 digit'])

                postal_sequence_current.append(str(postal_code))
                postal_sequence_list.append([str(postal_code), str(order_id)])

            # - - - - - - HQ Starting point Lat Long - - - - - #

            # For Non Multi Truck
            priority_capacity = "false"
            sort_company = "false"
            priority_capacity_comp = "false"

            truck_capacity_grp = []

            if len(errors) == 0:

                origin_destination, postal_result, current_result, proposed_postal_seq, current_postal_seq, grp_truck = sorting.sort_by_postals_chunck(
                    int(starting_postal),
                    postal_sequence_list,
                    int(number_of_vehicle),
                    email, has_return,
                    priority_capacity,
                    priority_capacity_comp,
                    api_user, sort_company, truck_capacity_grp, options_truck)

                '''['postal_result', 'order_id']'''

                # Converting HQ to lat & long value
                # origin_destination = self.convert_hq(str(starting_postal))
                current_distance = sorting_prep.result_distance_latlng(current_result, origin_destination, num_post_code)
                proposed_distance = sorting_prep.result_distance_latlng(postal_result, origin_destination, num_post_code)

                # GeoCode Map
                latlng_array = map_visible(postal_result)

                # Converting the total percentage saving of distance
                difference_total = current_distance - proposed_distance
                percentage_savings = (difference_total / current_distance) * 100

                # Send JSON Response
                response['status'] = 'ok'
                response['data_result'] = [
                        {
                            "required_fields": {
                                "starting_postal": starting_postal,
                                "propose_result": proposed_postal_seq,
                                "has_return": has_return
                                },

                            "geo_code_latlng": {
                                "latlng_array": latlng_array
                            },

                            "vehicle_priority": {
                                "vehicle_num": number_of_vehicle
                                },

                            "total_summary_saving": {
                                "proposed_distance": proposed_distance,
                                "current_distance": current_distance,
                                "total_savings": percentage_savings
                                }
                        }
                    ]

            else:
                errors.extend(['Error in Process'])

        else:
            errors.extend(['Error in JSON-Data'])

        if len(errors) > 0:
            response['status'] = 'error'
            response['errors'] = errors

        logging.info(response)
        self.response.out.write(json.dumps(response, indent=3))

"""
# for companies
{
     "companies_hq": [
     	{
          "starting_postal": "469001"
     	},
     	{
          "starting_postal": "389458"
     	}
     ],
     "order_details": [
            ["469001", "Order01", 1, "Company_1"],
            ["760450", "Order02", 1, "Company_1"],
            ["596937", "Order03", 1, "Company_1"],
            ["596740", "Order04", 1, "Company_1"],
            ["098585", "Order05", 1, "Company_1"],
            ["109680", "Order06", 1, "Company_1"],
            ["560405", "Order07", 1, "Company_2"],
            ["278986", "Order08", 1, "Company_2"],
            ["431011", "Order09", 1, "Company_2"],
            ["460102", "Order10", 1, "Company_2"],
            ["159921", "Order11", 1, "Company_2"],
            ["258500", "Order12", 1, "Company_2"]
     ],

     "multi_truck_details": [
     	{
          "number_of_vehicle": 1
     	},
     	{
          "number_of_vehicle": 1
        }],
     "num_comp_val" : 2,
     "has_return": "true",
     "priority_capacity_comp": "false",
     "sort_company": "true"
}

///

{
     "companies_hq": [
     	{
          "starting_postal": "469001"
     	},
     	{
          "starting_postal": "389458"
     	}
     ],
     "order_details": [
            ["469001", "Order01", 1, "Company_1"],
            ["760450", "Order02", 1, "Company_1"],
            ["596937", "Order03", 1, "Company_1"],
            ["596740", "Order04", 1, "Company_1"],
            ["098585", "Order05", 1, "Company_1"],
            ["109680", "Order06", 1, "Company_1"],
            ["560405", "Order07", 1, "Company_2"],
            ["278986", "Order08", 1, "Company_2"],
            ["431011", "Order09", 1, "Company_2"],
            ["460102", "Order10", 1, "Company_2"],
            ["159921", "Order11", 1, "Company_2"],
            ["258500", "Order12", 1, "Company_2"]
     ],

     "multi_truck_details": [
	    	{
	      		"type_of_truck": "AAA",
	      		"truck_capacity": 3,
	      		"num_of_truck": 1
	    	},
	    	{
	      		"type_of_truck": "BBB",
	      		"truck_capacity": 3,
	      		"num_of_truck": 1
	    	}],
  "num_comp_val" : 2,
     "has_return": "true",
     "priority_capacity_comp": "true",
     "sort_company": "true"
}
"""

class Multi_companies_API(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Headers'] = 'Authorization'
        self.response.headers['Access-Control-Allow-Headers'] = 'Cache-Control'
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'
        self.response.headers['Content-Type'] = 'application/json;charset=utf-8'

        # api_key = self.request.authorization

        email = self.request.get('userId')
        api_key = self.request.get('keyId')

        # Error list for invalid postal codes
        errors = []

        api_user = "false"
        auth_user = UserAccount.check_API_auth(email, api_key)

        if auth_user == None:
            errors.extend(['Incorrect email or API Key'])

        if auth_user == True:
            api_user = "true"

        # Checking for Credit Access
        credits_account = UserAccount.check_credit_usage(email)

        if credits_account == None:
            errors.extend(['Error in Credits Access <br />'])

        response = {}
        request_str = self.request.body
        logging.info(request_str)

        if len(errors) == 0:
            try:
                data = json.loads(request_str)

            except:
                errors.extend(['Error in JSON'])

        if len(errors) == 0:

            companies_hq, error = checkInRequest('companies_hq', data)
            errors.extend(error)

            order_details, error = checkInRequest('order_details', data)
            errors.extend(error)

            multi_truck_details, error = checkInRequest('multi_truck_details', data)
            errors.extend(error)

            has_return, error = checkInRequest('has_return', data)
            errors.extend(error)

            sort_company, error = checkInRequest('sort_company', data)
            errors.extend(error)

            priority_capacity_comp, error = checkInRequest('priority_capacity_comp', data)
            errors.extend(error)

            num_comp_val, error = checkInRequest('num_comp_val', data)
            errors.extend(error)

            # extracting data section
            starting_postal_list = []
            truck_sequence_list = []
            truck_capacity_grp = []
            postal_sequence_current = []
            postal_sequence_company = []
            company_list_grp = []

            # Truck capacity Groupings
            truck_capacity_list_c1 = []
            truck_capacity_grp_comp1 = []

            # extract starting points:
            for starting_point in companies_hq:
                starting = starting_point["starting_postal"]

                # add zero in front if 5 digit only
                if len(str(starting)) == 5:
                    starting = "0" + starting

                # if below 5 digit
                if len(str(starting)) != 6:
                    logging.info('Warning! error')
                    errors.extend(['Starting Postal code is not valid, it should be 6 digit'])

                starting_postal_list.append(starting)

            if priority_capacity_comp == "true":

                # extract truck details list:
                for num_truck in multi_truck_details:

                    type_of_truck = num_truck["type_of_truck"]
                    truck_capacity = num_truck["truck_capacity"]
                    num_of_truck = num_truck["num_of_truck"]

                    truck_capacity_list_c1.append([[str(type_of_truck), int(truck_capacity), int(num_of_truck)]])

                truck_capacity_grp_comp1.extend(truck_capacity_list_c1)

            else:

                # extract vehicle list:
                for num_truck in multi_truck_details:
                    vehicle_truck = num_truck["number_of_vehicle"]
                    truck_sequence_list.append(vehicle_truck)

            # Counter checking of Postal Code
            num_post_code = 0

            # extract order details:
            for index in range(0, len(order_details)):

                # Counter checking of Postal Code
                num_post_code += 1

                postal_pair = order_details[index]

                if len(postal_pair) == 1:
                    logging.info(postal_pair)
                    errors.extend(['Please check the postal sequence input'])
                    break

                postal_code = str(postal_pair[0])
                order_id = str(postal_pair[1])
                truck_capacity = postal_pair[2]
                company = postal_pair[3]

                if len(str(postal_code)) == 5:
                    postal_code = "0" + postal_code

                # Check if postal code is a valid value i.e. Contains only five or six digits
                if not str.isdigit(postal_code) or len(str(postal_code)) != 6:
                    logging.info('Warning! Postal Code error')
                    errors.extend(['Please check ' + postal_code + ' is not valid, it should be 6 digit'])

                postal_sequence_current.append([str(postal_code), str(order_id), int(truck_capacity), str(company)])

            # extract company groupings:
            for company in range(len(postal_sequence_current)):
                companyList = postal_sequence_current[company]
                company_list_grp.append(companyList)

            for key, group in itertools.groupby(company_list_grp, operator.itemgetter(3)):

                # group as per company
                postal_sequence_company.append(list(group))

            # validation for company
            if int(len(postal_sequence_company)) != num_comp_val:
                errors.extend(['Please Check the number of company inputs'])

            # print len(item_dict['result'][0]['run'])

            # For Non Multi Truck
            options_truck = "false"
            priority_capacity = "false"
            vehicle_quantity = 0
            num_user_load = "true"

            if len(errors) == 0:

                propose_result_company = []
                current_result_company = []

                origin_result_company = []

                propose_result_sequence = []
                current_result_sequence = []

                grp_truck_sequence = []

                latlng_array_list = []
                result_route_value = []

                if priority_capacity_comp == "true":

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

                else:

                    for starting_post, company_sequence, vehicle_quantity in itertools.izip(starting_postal_list, postal_sequence_company, truck_sequence_list):
                        origin_destinations, propose_result, current_result, proposed_postal_list_seq, current_postal_list_seq, grp_truck = sorting.sort_by_postals_chunck(
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

                        propose_result_sequence.append(proposed_postal_list_seq)
                        current_result_sequence.append(current_postal_list_seq)

                        grp_truck_sequence.append(grp_truck)

                        # GeoCode Map
                        latlng_array = map_visible(propose_result)
                        latlng_array_list.append(latlng_array)

                # Converting the postal code to total distance
                for origin_destination, current_result_comp, propose_result_comp in itertools.izip(origin_result_company, current_result_company, propose_result_company):

                    current_route_value = sorting_prep.result_distance_latlng(current_result_comp, origin_destination, num_post_code)
                    propose_route_value = sorting_prep.result_distance_latlng(propose_result_comp, origin_destination, num_post_code)

                    # Converting the total percentage saving of distance
                    difference_total = current_route_value - propose_route_value
                    percentage_savings = (difference_total / current_route_value) * 100

                    proposed_route_val = round(propose_route_value, 2)
                    current_route_val = round(current_route_value, 2)
                    savings_route_val = round(percentage_savings, 2)

                    # Total_summary_saving
                    result_route_value.append([str(current_route_val), str(proposed_route_val), str(savings_route_val)])

                # # For Google MAP
                # result_list_arr = []
                # for propose_result_company_1 in propose_result_company:
                #     for propose_result_company_2 in propose_result_company_1:
                #         result_list_arr.append(propose_result_company_2)

                # Converting to string of this Proposed data
                proposed_postal = sorting.convert_to_string(propose_result_company)

                proposed_cons_array = []
                current_cons_array = []

                # Proposed
                for consolidated_proposed in propose_result_sequence:
                    for proposed_comp in consolidated_proposed:
                        proposed_cons_array.append(proposed_comp)

                # Current
                for consolidated_current in current_result_sequence:
                    for proposed_comp in consolidated_current:
                        current_cons_array.append(proposed_comp)

                # Convert to Dictionary
                postal_list_sequence = {
                    "proposed_postal_list_seq": proposed_cons_array,
                    "current_postal_list_seq": current_cons_array,
                }

                # starting_postal_list
                starting_list_seqeunce = {
                    "starting_address": starting_postal_list
                }

                # propose_result_company
                propose_result_seqeunce = {
                    "proposed_postal": propose_result_company
                }
                # grp_truck
                grp_truck_sequence_1 = {
                    "grp_truck_name": grp_truck_sequence
                }

                # truck_sequence_list
                truck_sequence_sequence = {
                    "num_of_vehicle": truck_sequence_list
                }

                # Compressing data
                postal_list_compress = pickle.dumps(postal_list_sequence)
                starting_address_compress = pickle.dumps(starting_list_seqeunce)
                proposed_postal_compress = pickle.dumps(propose_result_seqeunce)
                grp_truck_compress = pickle.dumps(grp_truck_sequence_1)
                truck_sequence_compress = pickle.dumps(truck_sequence_sequence)

                # taskqueue.add(url='/sorting-proposed-api',
                #               params=({
                #                   # 'compare_id': compare_id,
                #                   'starting_address': starting_address_compress,
                #                   'postal_list_compress': postal_list_compress,
                #                   'proposed_postal': proposed_postal_compress,
                #                   'grp_truck_name': grp_truck_compress,
                #
                #                   'num_of_vehicle': truck_sequence_compress,
                #
                #                   'sort_company': sort_company,
                #                   'options_truck': options_truck,
                #                   'priority_capacity': priority_capacity,
                #
                #                   'has_return': has_return,
                #                   'email': email,
                #                   'num_user_load': num_user_load,
                #
                #               })
                #               )

                # Send API JSON Response Update

                response['status'] = 'ok'
                response['sort_company'] = 'true'
                response['data_result'] = [
                    {
                        "required_fields": {
                            "starting_postal": starting_postal_list,
                            "propose_results": propose_result_sequence,
                            "has_return": has_return
                        },
                        "geo_code_latlng": {
                            "latlng_array": latlng_array_list
                        },
                        "total_summary_saving": {
                            "total_savings": result_route_value
                        }
                    }
                ]

            else:
                errors.extend(['Error in process'])
        else:
            errors.extend(['Error in JSON-Data'])

        if len(errors) > 0:
            response['status'] = 'error'
            response['errors'] = errors

        logging.info(response)
        self.response.out.write(json.dumps(response, indent=3))


def RepresentsInt(num):

    try:
        int(num)
        return True

    except ValueError:

        return False


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

def postalcode_latlong(postal):

        # Validation for Task Q
        compare_postal = postalRecordDB.check_if_exists(postal)

        if compare_postal == None:

            if postal[0] == "0":
                current_post = postal.lstrip("0")
                compare_postal = postalRecordDB.check_if_exists(current_post)
            else:
                print('load')
                nearestPostalCode = postalRecordDB.query().filter(postalRecordDB.postal_code >= postal).get(keys_only=True)
                compare_postal = nearestPostalCode.id()

        latlong = postalRecordDB.get_by_id(compare_postal)

        laglongSource = []
        laglongSource.append(latlong.lat)
        laglongSource.append(',')
        laglongSource.append(latlong.long)
        destinations = ''.join(laglongSource)

        return destinations

app = webapp2.WSGIApplication([
    ('/api/multi_truck/v1', Multi_truck_API),
    ('/api/truck_capacity/v1', Truck_capacity_API),
    ('/api/multi_companies/v1', Multi_companies_API)
], debug=True)