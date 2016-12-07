// Pre-load the textarea with data so
// that it can show the demo when the page renders //

function dummyPostalCode(){
    var $postalSequence = $("#postal_sequence");

    var postal_pair = [
                  // Multi Trucks
//                "Postal_Code Order_ID Time_from Time_to",
//                "369974 Order01 09:00:00 12:00:00",
//                "760450 Order02 07:00:00 8:00:00",
//                "596937 Order03 13:00:00 14:00:00",
//                "596740 Order04 10:00:00 11:00:00",
//                "560405 Order05 09:30:00 10:20:00",
//                "543262 Order06 15:00:00 18:00:00",
//                "520156 Order07 14:00:00 17:00:00",
//                "469001 Order08 09:00:00 12:00:00",
//                "760450 Order09 11:00:00 11:30:00",
//                "596937 Order10 13:00:00 15:00:00",
//                "596740 Order11 16:00:00 17:00:00",
//                "098585 Order12 13:00:00 15:00:00",
//                "109680 Order13 16:00:00 17:00:00",
//                "189637 Order14 15:00:00 18:00:00",

                // Truck Capacity
                "Postal_Code Order_ID Time_from Time_to",
                "369974 Order01 1 09:00:00 12:00:00",
                "760450 Order02 1 07:00:00 8:00:00",
                "596937 Order03 1 13:00:00 14:00:00",
                "596740 Order04 1 10:00:00 11:00:00",
                "560405 Order05 1 09:30:00 10:20:00",
                "543262 Order06 1 15:00:00 18:00:00",
                "520156 Order07 1 14:00:00 17:00:00",
                "469001 Order08 1 09:00:00 12:00:00",
                "760450 Order09 1 11:00:00 11:30:00",
                "596937 Order10 1 13:00:00 15:00:00",
                "596740 Order11 1 16:00:00 17:00:00",
                "098585 Order12 1 13:00:00 15:00:00",
                "109680 Order13 1 16:00:00 17:00:00",
                "189637 Order14 1 15:00:00 18:00:00",

                 //Multi Truck
//                "Postal_Code Order_ID",
//                "380011	Order1",  //369974
//                "760450	Order2",
//                "596937	Order3",
//                "596740	Order4",
//                "560405	Order5",
//                "543262	Order6",
//                "520156	Order7",
//                "460102	Order8",
//                "408561	Order9",
//                "389458	Order10",
//                "49317	Order11",
//                "560326	Order12",
//                "431011	Order13",
//                "469001	Order14	",

                // Multi Companies

//                "Postal_Code Order_ID",
//                "369974	Order1	1	Company_A",
//                "760450	Order2	1	Company_A",
//                "596937	Order3	1	Company_A",
//                "596740	Order4	1	Company_A",
//                "560405	Order5	1	Company_A",
//                "543262	Order6	1	Company_A",
//                "520156	Order7	1	Company_A",
//                "460102	Order8	1	Company_A",
//                "408561	Order9	1	Company_A",
//                "389458	Order10	1	Company_A",
//                "49317	Order11	1	Company_A",
//                "560326	Order12	1	Company_A",
//                "431011	Order13	1	Company_A",
//                "469001	Order14	1	Company_A",


//               "369974 Order01 1 companyA",
//               "760450 Order02 1 companyA",
//               "596937 Order03 1 companyA",
//               "596740 Order04 1 companyA",
//               "560405 Order05 1 companyA",
//               "543262 Order06 1 companyA",
//               "520156 Order07 1 companyA",
////               "460102 Order08 1 companyA",
////               "408561 Order09 1 companyA",
////               "389458 Order10 1 companyA",
////               "049317 Order11 1 companyA",
////               "560326 Order12 1 companyA",
////               "431011 Order13 1 companyA",
//               "469001 Order01 1 companyB",
//			    "760450 Order02 1 companyB",
//				"596937 Order03 1 companyB",
//				"596740 Order04 1 companyB",
//				"098585 Order05 1 companyB",
//				"109680 Order06 1 companyB",
//				"189637 Order07 1 companyB",
//				"258500 Order08 1 companyB",
//				"547429 Order09 2 companyB",
//				"048423 Order10 1 companyB",
//				"238859 Order11 1 companyB",
//				 "188021 Order12 1 companyB",
//				 "159921 Order13 1 companyB",
//				 "189673 Order11 1 company_C",
//				 "068897 Order12 1 company_C",
//				 "738726 Order13 1 company_C",
//				 "218700 Order14 1 company_C",
//				 "198713 Order15 1 company_C",
//				 "218700 Order16 1 company_C",
//				 "198713 Order17 1 company_C",
//				 "389458 Order01 1 company_C",
//				 "278986 Order02 1 company_C",
//				 "431011 Order03 1 company_C",
//				 "460102 Order04 1 company_C",
//				 "408561 Order05 1 company_C",
//				 "689575 Order06 1 company_C",
//				 "560326 Order01 1 company_C",
//				 "738728 Order01 2 company_C",
//				 "159921 Order03 2 company_C",

			];

    for(i = 0; i < postal_pair.length; i++){
        postal_list = postal_pair[i];
        $postalSequence.append(postal_list, '\n');
    }
}

// Once the page load,
// function will run immediately:

dummyPostalCode();

