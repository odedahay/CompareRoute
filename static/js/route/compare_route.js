$(function() {

// validation for onload
if (typeof jQuery === "undefined") {
    throw new Error("jQuery progress timer requires jQuery");
}

// scroll up and down
function scrollToAnchor(aid){
    var aTag = $("a[name='"+ aid +"']");
    $('html,body').animate({scrollTop: aTag.offset().top}, 1000);
}


// validation for Route by Trucks:
var errorBox = $('#message-errors');


//buttons
var btn_generateRoute = $("#routeBtn");

//forms
////var startingPoint = $('#starting_postal').val();
//var postal_sequence = $('#postal_sequence').val();


// Validate HQ point
// Route by Truck
function checkStarting_Point(starting_postal){

    var errorInput = $('.startingPoint');
    var errorMessage;

    // create regex to validate if numbers onlyåå
    var reg = /^[0-9]+$/;

    if(starting_postal === 'undefined'  || starting_postal === ''){

        errorMessage = "*Postal Code required!";
        errorInput.fadeIn();
        errorInput.html(errorMessage);

        return false;

    }else if( (starting_postal.length) < 5 || (starting_postal.length) > 6 ){

        //console.log(errorMessage);
        errorMessage = "*Postal Code should only be 6 digits";
        errorInput.fadeIn();
        errorInput.html(errorMessage);

        return false;

    }else if (!reg.test(starting_postal)){

        errorMessage = "*Postal Code should be numbers only";
        errorInput.fadeIn();
        errorInput.html(errorMessage);

        return false;

    }else{

        errorInput.hide();
        return true;

    }
} // end

// validation function for Postal Sequence
function postalSequence_area(postal_sequence){
    var errorInput = $('.postalSeq');
    var errorMessage;

    if(postal_sequence === ''){

        errorMessage = "*Please, Enter your Delivery Location Details!";
        errorInput.fadeIn();
        errorInput.html(errorMessage);

        return

    }else{

        errorInput.hide();
        return true;
    }
}

// validation for truck capacity
function truck_capacity_area(type_of_truck, truck_capacity, num_of_truck){

    var errorInput1 = $('.typeTruck');
    var errorInput2 = $('.truckCapacity');
    var errorInput3 = $('.numTruck');

    var errorMessage;
     // create regex to validate if numbers onlyåå
    var reg = /^[0-9]+$/;

    errorInput1.hide();
    errorInput2.hide();
    errorInput3.hide();

    //check the fields if empty
    if(type_of_truck === ''){

        errorMessage = "*Please Enter Types of Truck!";
        errorInput1.fadeIn();
        errorInput1.html(errorMessage);

        return false;

    }
    else if( truck_capacity === '' || parseInt(truck_capacity) <= 0 || !reg.test(truck_capacity) ){

        errorMessage = "*Please Enter Valid Truck Capacity";
        errorInput2.fadeIn();
        errorInput2.html(errorMessage);

        return false;
    }
    else if( num_of_truck === '' || parseInt(num_of_truck) <= 0  || !reg.test(num_of_truck) ){

        errorMessage = "*Please Enter Valid Number of Truck";
        errorInput3.fadeIn();
        errorInput3.html(errorMessage);

        return false;
    }
    else{

        errorInput1.hide();
        errorInput2.hide();
        errorInput3.hide();
        return true;
    }

}

// validation for truck capacity second field
function truck_capacity_area_1(type_of_truck_1, truck_capacity_1, num_of_truck_1){

    var errorInput1 = $('.typeTruck_1');
    var errorInput2 = $('.truckCapacity_1');
    var errorInput3 = $('.numTruck_1');

    var errorMessage;
    var reg = /^[0-9]+$/;

     errorInput1.hide();
     errorInput2.hide();
     errorInput3.hide();

    //check the fields if empty
    if(type_of_truck_1 === ''){

        errorMessage = "*Please Enter Types of Truck!";
        errorInput1.fadeIn();
        errorInput1.html(errorMessage);

        return false;

    }
    else if( truck_capacity_1 === '' || parseInt(truck_capacity_1) <= 0 || !reg.test(truck_capacity_1) ){

        errorMessage = "*Please Enter Valid Truck Capacity ";
        errorInput2.fadeIn();
        errorInput2.html(errorMessage);

        return false;
    }
    else if( num_of_truck_1 === '' || parseInt(num_of_truck_1) <= 0 || !reg.test(num_of_truck_1) ){

        errorMessage = "*Please Enter valid Number of Truck";
        errorInput3.fadeIn();
        errorInput3.html(errorMessage);

        return false;
    }
    else{
        errorInput1.hide();
        errorInput2.hide();
        errorInput3.hide();
        return true;
    }
}

// validation for truck capacity third field
function truck_capacity_area_2(type_of_truck_2, truck_capacity_2, num_of_truck_2){

    var errorInput1 = $('.typeTruck_2');
    var errorInput2 = $('.truckCapacity_2');
    var errorInput3 = $('.numTruck_2');

    var errorMessage;
    var reg = /^[0-9]+$/;

     errorInput1.hide();
     errorInput2.hide();
     errorInput3.hide();

    //check the fields if empty
    if(type_of_truck_2 === ''){

        errorMessage = "*Please Enter Types of Truck!";
        errorInput1.fadeIn();
        errorInput1.html(errorMessage);

        return false;

    }
    else if( truck_capacity_2 === '' || parseInt(truck_capacity_2) <= 0 || !reg.test(truck_capacity_2) ){

        errorMessage = "*Please Enter Valid Truck Capacity ";
        errorInput2.fadeIn();
        errorInput2.html(errorMessage);

        return false;
    }
    else if( num_of_truck_2 === '' || parseInt(num_of_truck_2) <= 0 || !reg.test(num_of_truck_2) ){

        errorMessage = "*Please Enter valid Number of Truck";
        errorInput3.fadeIn();
        errorInput3.html(errorMessage);

        return false;
    }
    else{
        errorInput1.hide();
        errorInput2.hide();
        errorInput3.hide();
        return true;
    }
}


// Click --> Generate Button
$('#routeBtn').click(function () {

    //route by truck
    var starting_postal = $("#starting_postal").val();
    var vehicle_quantity = $("#vehicle_quantity").val();

    //route by capacity
    // 1
    var starting_postal_cap = $("#starting_postal_cap").val();
    var type_of_truck = $("#type_of_truck").val();
    var truck_capacity = $("#truck_capacity").val();
    var num_of_truck = $("#num_of_truck").val();

    // 2
    var type_of_truck_1 = $("#type_of_truck_1").val();
    var truck_capacity_1 = $("#truck_capacity_1").val();
    var num_of_truck_1 = $("#num_of_truck_1").val();

    // 3
    var type_of_truck_2 = $("#type_of_truck_2").val();
    var truck_capacity_2 = $("#truck_capacity_2").val();
    var num_of_truck_2 = $("#num_of_truck_2").val();

    //route by companies
    var starting_postal_1 = $("#starting_postal_1").val();
    var starting_postal_2 = $("#starting_postal_2").val();
    var starting_postal_3 = $("#starting_postal_3").val();
    var starting_postal_4 = $("#starting_postal_4").val();
    var starting_postal_5 = $("#starting_postal_5").val();
    var starting_postal_6 = $("#starting_postal_6").val();

    var vehicle_quantity_1 = $("#vehicle_quantity_1").val();
    var vehicle_quantity_2 = $("#vehicle_quantity_2").val();
    var vehicle_quantity_3 = $("#vehicle_quantity_3").val();
    var vehicle_quantity_4 = $("#vehicle_quantity_4").val();
    var vehicle_quantity_5 = $("#vehicle_quantity_5").val();
    var vehicle_quantity_6 = $("#vehicle_quantity_6").val();

    //route by companies - companies
    var type_of_truck_c1 = $("#type_of_truck_c1").val();
    var type_of_truck_c2 = $("#type_of_truck_c2").val();
    var type_of_truck_c3 = $("#type_of_truck_c3").val();
    var type_of_truck_c4 = $("#type_of_truck_c4").val();
    var type_of_truck_c5 = $("#type_of_truck_c5").val();
    var type_of_truck_c6 = $("#type_of_truck_c6").val();

    var truck_capacity_c1 = $("#truck_capacity_c1").val();
    var truck_capacity_c2 = $("#truck_capacity_c2").val();
    var truck_capacity_c3 = $("#truck_capacity_c3").val();
    var truck_capacity_c4 = $("#truck_capacity_c4").val();
    var truck_capacity_c5 = $("#truck_capacity_c5").val();
    var truck_capacity_c6 = $("#truck_capacity_c6").val();

    var num_of_truck_c1 = $("#num_of_truck_c1").val();
    var num_of_truck_c2 = $("#num_of_truck_c2").val();
    var num_of_truck_c3 = $("#num_of_truck_c3").val();
    var num_of_truck_c4 = $("#num_of_truck_c4").val();
    var num_of_truck_c5 = $("#num_of_truck_c5").val();
    var num_of_truck_c6 = $("#num_of_truck_c6").val();

    // sub fields 1
    var type_of_truck_cc1 = $("#type_of_truck_cc1").val();
    var type_of_truck_cc2 = $("#type_of_truck_cc2").val();
    var type_of_truck_cc3 = $("#type_of_truck_cc3").val();

    var truck_capacity_cc1 = $("#truck_capacity_cc1").val();
    var truck_capacity_cc2 = $("#truck_capacity_cc2").val();
    var truck_capacity_cc3 = $("#truck_capacity_cc3").val();

    var num_of_truck_cc1 = $("#num_of_truck_cc1").val();
    var num_of_truck_cc2 = $("#num_of_truck_cc2").val();
    var num_of_truck_cc3 = $("#num_of_truck_cc3").val();

    // sub fields 2
    var type_of_truck_cc21 = $("#type_of_truck_cc21").val();
    var type_of_truck_cc22 = $("#type_of_truck_cc22").val();
    var type_of_truck_cc23 = $("#type_of_truck_cc23").val();

    var truck_capacity_cc21 = $("#truck_capacity_cc21").val();
    var truck_capacity_cc22 = $("#truck_capacity_cc22").val();
    var truck_capacity_cc23 = $("#truck_capacity_cc23").val();

    var num_of_truck_cc21 = $("#num_of_truck_cc21").val();
    var num_of_truck_cc22 = $("#num_of_truck_cc22").val();
    var num_of_truck_cc23 = $("#num_of_truck_cc23").val();

    // Event Counter
    var add_truck_cc1 = $("#add_truck_cc1").val();
    var add_truck_cc2 = $("#add_truck_cc2").val();
    var add_truck_cc3 = $("#add_truck_cc3").val();

    var count_truck1 = $("#add_truck_capacity_1").val();
    var count_truck2 = $("#add_truck_capacity_2").val();

    var postal_sequence = $("#postal_sequence").val();
    var email = $("[name=email_value]").val();
    var has_return = $("#return_startpoint")[0].checked;

    var optionsTruck = $("#optionsTruck")[0].checked;
    var priority_capacity = $("#priority_capacity")[0].checked;
    var priority_capacity_comp = $("#priority_capacity_comp")[0].checked;

    var sort_company = $("#sort_company")[0].checked;
    var num_comp_val = $("#num_comp_val").val();

    $('#prog').progressbar({ value: 0 });


    // Declare variable will for event
    var generate_route = false;
    var truckCapacity_false = false;

    // Route by Truck
    if(optionsTruck === true){

        var startingValue = checkStarting_Point(starting_postal);
        var postalSeqValue = postalSequence_area(postal_sequence);

        // if all true, generate_route = true
        if(startingValue === true && postalSeqValue === true){

            generate_route = true;
        }

        //console.log(startingValue);
    }
    // Check if Priority Capacity only
    if (priority_capacity === true){

        //if not exist
        if(!count_truck2){
            count_truck2 = 0;
        }

        // Create Variable to generate events
        var truckCount = ( parseInt(count_truck1) + parseInt(count_truck2) );

        var startingValue = checkStarting_Point(starting_postal_cap);
        var postalSeqValue = postalSequence_area(postal_sequence);

        // I set num_truck for event to know if they additional fields
       // if( parseInt(count_truck1) === truckCount ){
        if( parseInt(truckCount) === 1 ){

             // Validate the two Truck forms
            var truckCapacity = truck_capacity_area(type_of_truck, truck_capacity, num_of_truck);
            var truckCapacity1 = truck_capacity_area_1(type_of_truck_1, truck_capacity_1, num_of_truck_1);

            // check truckCapacity1 if true
            if(truckCapacity1 !== false ){
                truckCapacity_false = true;
            }

        }
        else if ( parseInt(truckCount) === 3 ){

            // Validate the two Truck forms
            var truckCapacity = truck_capacity_area(type_of_truck, truck_capacity, num_of_truck);
            var truckCapacity1 = truck_capacity_area_1(type_of_truck_1, truck_capacity_1, num_of_truck_1);
            var truckCapacity2 = truck_capacity_area_2(type_of_truck_2, truck_capacity_2, num_of_truck_2);

            // check truckCapacity1
            if(truckCapacity2 !== false ){
                truckCapacity_false = true;
            }

        }else{

            // validate One Truck forms
            var truckCapacity0 = truck_capacity_area(type_of_truck, truck_capacity, num_of_truck);
            truckCapacity_false = truckCapacity0;

             console.log('HELLO3', truckCapacity0);

        }
        console.log('HELLO', truckCapacity_false);
        // Initiate the value
        truckCapacity = truckCapacity_false;

        // if all true, generate_route = true
        if(startingValue === true && postalSeqValue === true && truckCapacity === true){
            generate_route = true;
        }
    }

   // Check first value of inputs before it process
   //if(startingValue === true && postalSeqValue === true){
   if(generate_route === true){

        $.ajax({
            type: "POST",
            url: "/sorting",
            dataType: 'json',
            data: {
                starting_postal: starting_postal,
                vehicle_quantity: vehicle_quantity,

                // 1
                starting_postal_cap: starting_postal_cap,
                type_of_truck: type_of_truck,
                truck_capacity: truck_capacity,
                num_of_truck: num_of_truck,

                // 2
                type_of_truck_1: type_of_truck_1,
                truck_capacity_1: truck_capacity_1,
                num_of_truck_1: num_of_truck_1,

                // 3
                type_of_truck_2: type_of_truck_2,
                truck_capacity_2: truck_capacity_2,
                num_of_truck_2: num_of_truck_2,

                //Route by Companies
                starting_postal_1: starting_postal_1,
                starting_postal_2: starting_postal_2,
                starting_postal_3: starting_postal_3,
                starting_postal_4: starting_postal_4,
                starting_postal_5: starting_postal_5,
                starting_postal_6: starting_postal_6,

                vehicle_quantity_1: vehicle_quantity_1,
                vehicle_quantity_2: vehicle_quantity_2,
                vehicle_quantity_3: vehicle_quantity_3,
                vehicle_quantity_4: vehicle_quantity_4,
                vehicle_quantity_5: vehicle_quantity_5,
                vehicle_quantity_6: vehicle_quantity_6,

                //route by companies - companies
                type_of_truck_c1: type_of_truck_c1,
                type_of_truck_c2: type_of_truck_c2,
                type_of_truck_c3: type_of_truck_c3,
                type_of_truck_c4: type_of_truck_c4,
                type_of_truck_c5: type_of_truck_c5,
                type_of_truck_c6: type_of_truck_c6,

                truck_capacity_c1: truck_capacity_c1,
                truck_capacity_c2: truck_capacity_c2,
                truck_capacity_c3: truck_capacity_c3,
                truck_capacity_c4: truck_capacity_c4,
                truck_capacity_c5: truck_capacity_c5,
                truck_capacity_c6: truck_capacity_c6,

                num_of_truck_c1: num_of_truck_c1,
                num_of_truck_c2: num_of_truck_c2,
                num_of_truck_c3: num_of_truck_c3,
                num_of_truck_c4: num_of_truck_c4,
                num_of_truck_c5: num_of_truck_c5,
                num_of_truck_c6: num_of_truck_c6,

                // sub fields:1
                type_of_truck_cc1: type_of_truck_cc1,
                type_of_truck_cc2: type_of_truck_cc2,
                type_of_truck_cc3: type_of_truck_cc3,

                truck_capacity_cc1: truck_capacity_cc1,
                truck_capacity_cc2: truck_capacity_cc2,
                truck_capacity_cc3: truck_capacity_cc3,

                num_of_truck_cc1: num_of_truck_cc1,
                num_of_truck_cc2: num_of_truck_cc2,
                num_of_truck_cc3: num_of_truck_cc3,

                 // sub fields:2
                type_of_truck_cc21: type_of_truck_cc21,
                type_of_truck_cc22: type_of_truck_cc22,
                type_of_truck_cc23: type_of_truck_cc23,

                truck_capacity_cc21: truck_capacity_cc21,
                truck_capacity_cc22: truck_capacity_cc22,
                truck_capacity_cc23: truck_capacity_cc23,

                num_of_truck_cc21: num_of_truck_cc21,
                num_of_truck_cc22: num_of_truck_cc22,
                num_of_truck_cc23: num_of_truck_cc23,

                add_truck_cc1: add_truck_cc1,
                add_truck_cc2: add_truck_cc2,
                add_truck_cc3: add_truck_cc3,
                postal_sequence: postal_sequence,
                email: email,
                has_return: has_return,

                optionsTruck: optionsTruck,
                priority_capacity: priority_capacity,
                priority_capacity_comp: priority_capacity_comp,
                sort_company: sort_company,

                num_comp_val: num_comp_val
            },
            beforeSend:function(){
                var errorBox = $('#message-errors');

                // this is where we append a loading image
                $('#progressbar').html('<div class="loading">Loading...<br /><img src="/img/ajax-loader.gif" alt="Loading..." /></div>');

                $("#sorted_sequence").hide();
                $("#sorted_sequence0").hide();

                $("#sorted_sequence0_ul").hide();
                $("#sorted_sequence0_ul_02").hide();
                //$("#sorted_sequence1").hide();

                $("#proposedTable_company").hide();

                $("#visualization").hide();
                $("#visualization_tab_comp").hide();
                $("#visualization_table").hide();
                $(".hidden_field_legend").hide();

                errorBox.hide();
                //$("#routeBtn").prop('disabled', true);
             },
            success: function (response) {

                // Main Variable for Layout
                var $sorted_sequence = $("#sorted_sequence0");
                var $sorted_sequenceTable = $("#sorted_sequence");
                var errorBox = $('#message-errors');

                $sorted_sequence.empty();
                $sorted_sequenceTable.empty();

                $('#progressbar').empty();

                $("#sorted_sequence0_ul").empty();
                $("#sorted_sequence0_ul_02").empty();
                //$("#sorted_sequence1").empty();
                $("#proposedTable_company").empty();
                $("#visualization_tab_comp").empty();

                $("#map_legend").empty();


                //$("#routeBtn").prop('disabled', false);

                var status = response.status;
                var sort_company = response.sort_company;

                if (status === "ok"){

                    // HTML Tags Reference:
                    var $h2_success = $("<h2 style='font-weight:normal'></h2>");
                    var $download_div = $('<div id="download_button" style="margin:20px 0;"></div>');
                    var $download_button = $('<button id="btn_export" class="btn btn-success btn-xs">Export to excel</button>'); //<a id="btn_export" class="btn btn-success btn-xs">Export to excel</a>

                    var $ul_sequence = $('<ul class="list-group" style="list-style-type:none; font-size:16px;"></ul>');
                    var $ul_result = $('<ul class="list-group" style="list-style-type:none; font-size:16px;"></ul>');

                    var $p_note = $("<p style='font-weight:normal; font-size:16px;'></p>");
                    var $p_note1 = $("<p style='font-weight:normal; font-size:16px;'></p>");

                    // Details Table
                    var $ParentTable = $('<table class="tableL table-bordered"></table>');

                    // Route by Trucks
                    var $tableThead0 = $('<thead><tr><th>Summary Details </th><th></th></tr></thead>');

                    // Route by Capacity
                    var $tableThead1 = $('<thead><tr><th>Summary Details </th><th></th><th></th></tr></thead>');
                    var $tableTbody = $('<tbody></tbody>');
                    var $tableTd = $('<tr></tr>'); // min -4 td
                    var $tableTd1 = $('<td></td>');
                    var $tableTd2 = $('<td></td>');
                    var $tableTd3 = $('<td></td>');
                    var $ul_table = $('<ul class="list-group" style="list-style-type:none; font-size:16px;"></ul>');
                    var $ul_table1 = $('<ul class="list-group" style="list-style-type:none; font-size:16px;"></ul>');

                    //Companies
                    var $tableThead_comp = $('<thead><tr><th>Summary Details </th><th></th></tr></thead>');
                    var $ul_table_truck = $('<ul class="list-group" style="list-style-type:none; font-size:16px;"></ul>');
                    var $ul_table_name = $('<ul class="list-group" style="list-style-type:none; font-size:16px;"></ul>');
                    var $ul_table_delivery = $('<ul class="list-group" style="list-style-type:none; font-size:16px;"></ul>');

                    // Summary Table
                    var $proposedTable = $('<table id="proposedTable" class="tableL table-bordered"></table>');
                    var $p_dlBtn = $('');
                    var $p_note2 = $('<p style="font-weight:normal; font-size:16px;"></p>');

                    //Status and Download
                    $download_div.append($download_button)
                    $sorted_sequence.append($h2_success);
                    $sorted_sequence.append($download_div);

                    //List of Data Entry
                    $sorted_sequence.append($ul_sequence);
                    $sorted_sequence.append($ul_result);
                    $sorted_sequence.append($p_note1);
                    $sorted_sequence.append($p_note);

                    // Div for Table for Postal Code list
                    $sorted_sequenceTable.append($p_dlBtn);
                    $sorted_sequenceTable.append($p_note2);
                    $sorted_sequenceTable.append($proposedTable);

                    // Global Function //

                    // Addition
                    function add(a, b) {return a + b;}

                    if (sort_company === "true"){

                        //required fields:
                        var starting = response.data_result[0].required_fields.starting_postal;

                        var postal_sequence_company = response.data_result[0].required_fields.postal_sequence;
                        var result_list = response.data_result[0].required_fields.propose_result;
                        var result_list_list = response.data_result[0].required_fields.propose_results;
                        var name_of_company = response.data_result[0].required_fields.name_of_companies;
                        var has_return = response.data_result[0].required_fields.has_return;

                        //GeoCode for LatLng
                        var latlng_array_list = response.data_result[0].geo_code_latlng.latlng_array;

                        //total_summary_saving
                        var total_savings = response.data_result[0].total_summary_saving.total_savings;

                        // Counter to check for repeated postal codes
                        function unique(originalArray){
                            var ar = originalArray.slice(0); //Make a copy of the array and store it in ar
                            var i = ar.length;
                            while(i--){  //Iterate through the array
                                if(ar.indexOf(ar[i],i+1)> -1){  //If the array has a duplicate
                                    ar.splice(i,1);  //Remove that element!
                                }
                            }
                            return ar; //Return the new, more unique array
                        }

                        // Counter for PostalCode Sorted;
                        var counter =1;
                        var split = postal_sequence.split("\n")

                        for(var i=0;i < split.length;i++){
                            postalSorted = counter++
                        }

                        /*$("#sorted_sequence0_ul").show();
                        $("#sorted_sequence0_ul_02").show();*/
                        //$("#sorted_sequence1").show();

                        $("#proposedTable").show();
                        $("#proposedTable_company").show();

                        $sorted_sequence.show();
                        $sorted_sequenceTable.show();
                        //- - - - - - - - Info Box - - - - - - - - - -//

                        $(".hidden_field_legend").show();
                        $("#priority_capacity_comp").show();

                        $sorted_sequence.append($ParentTable);
                        $ParentTable.append($tableThead_comp);
                        $tableThead_comp.appendTo($ParentTable);
                        $tableTbody.appendTo($ParentTable);

                        $tableTbody.append($tableTd);
                        $tableTd1.append($ul_table_truck); //$ul_table
                        //$tableTd2.append($ul_table_name);
                        $tableTd2.append($ul_table_delivery);
                        $tableTd1.appendTo($tableTd);
                        $tableTd2.appendTo($tableTd);
                        $tableTd3.appendTo($tableTd);

                        $h2_success.text('Successful!')

                        $("#download_button").show();

                        // Sequence Entered
                        //$ul_sequence.append('<li>Starting Postal Code : '+num_comp_val+'</li>');
                        //$ul_sequence.append('<li>Starting Postal Code : '+postalSorted+'</li>');

    //                    for (i=0; i < name_of_company.length; i++){
    //                        var company_name = name_of_company[i];
    //                         $ul_table_name.append("<li> "+ (i + 1) + " : " +company_name+ "</li>");
    //                    }

                        for (var hq = 0; hq < starting.length; hq++){
                            var hq_startingPoint = starting[hq];
                            var company_name = name_of_company[hq];
                                company_name = company_name.toLowerCase().replace(/\b[a-z]/g, function(letter) {return letter.toUpperCase(); });

                            $ul_table_truck.append("<li>Company "+(hq + 1) +" - " +company_name+  " w/ Starting Postal Code : "+hq_startingPoint+ " </li>");
                        }


                        // - - - - - - Global Message - - - - - - - //
                        // Message Layout
                        $p_note2.text('Breakdown of Proposed Postal Code Routes');

                        // Table Layout
                        $proposedTable.append("<tr><th colspan='2'>Postal Code</th> <th>Order ID</th><th>Truck Capacity</th><th>Company Name</th></tr>");

                        var new_postal_code;
                        var counter_nums;
                        var counter_num_array = [];

                        // Loop the Postal Sequence
                        for(i = 0; i < postal_sequence_company.length; i++){
                            var postal_seq_vehicle = postal_sequence_company[i];

                            // Truck Counter
                            $("#map_legend").append("<li><i class='fa fa-arrow-circle-o-right' aria-hidden='true'></i> Company " + (i + 1 ) + " <i class='marker_map marker_img"+ (i + 1) +"'></i></li>");

                            for(x = 0; x < postal_seq_vehicle.length; x++ ){
                                var company_set = postal_seq_vehicle[x];
                                var postal_code_arr = [];

                                $proposedTable.append("<tr><td colspan='5'><b>Company " + (i + 1) + " - <span class='label label-info'>Truck "+(x + 1)+ "</span></b> : </td></td></tr>" );

                                var counter_num = x + 1;

                                for (z = 0; z < company_set.length; z++){
                                     var company_details = company_set[z];

                                     var postal_code = company_details[0];
                                     var order_id = company_details[1];
                                     var capacity_load = company_details[2];
                                     var company_id = company_details[3];
                                         company_id = company_id.toLowerCase().replace(/\b[a-z]/g, function(letter) {return letter.toUpperCase(); });

                                    // Counter to check for repeated postal codes
                                    postal_code_arr.push(postal_code);
                                    var new_postal_code = unique(postal_code_arr);

                                    for (c = 0; c < new_postal_code.length; c++){
                                        var counter_num = c + 1;
                                    }
                                    $proposedTable.append("<tr><td>"+ counter_num +"</td><td>"+postal_code+"</td><td>"+order_id+"</td><td>"+capacity_load+"</td><td>"+company_id+"</td></tr>");
                                }
                                // Summary Table
                                counter_num_array.push(counter_num);
                                $ul_table_delivery.append('<li>Company '+(i+1)+' : '+counter_num+' Proposed Delivery Routes </li>');
                            }

                        }
                        var sum = counter_num_array.reduce(add, 0);

                        //$ul_sequence.append('Total Number of Proposed Routes: '+sum+ '  Postal Codes  <br />');
                        //$ul_sequence.append('Summary Details :<br />');

                        // - - - - - - End of Table fo Sorted Results - - - - - - - //

                        // - - - - - - Start Map Results - - - - - - - //
                        var postal_seq = postal_sequence;
                        var postal_seq_arr = postal_seq.split("\n");

                        // Storing the order ID and postal pairs  // current route
                        var order_postal_arr = [];

                        for(i = 0; i < postal_seq_arr.length; i ++){
                            var order_postal = postal_seq_arr[i];
                            order_postal = order_postal.replace(/\s+/g, " ");
                            order_postal = order_postal.replace("\t", " ");
                            order_postal = order_postal.trim();

                            var order_postal_split = order_postal.split(" ");
                            order_postal_arr.push(order_postal_split)
                        }

                        // - - - - -  Callback Function for map - - - - - - //

                       // generateGMap_company(starting_postal, result_list, order_postal_arr, latlng_array, sort_company);
                        generateGMap_company(starting, result_list, result_list_list, order_postal_arr, latlng_array_list, sort_company);

                        // Table below map - Summary-Value
                        $('#visualization_tab_comp').show()

                        //Summary Report for
                        //generateSummaryReport_comp(total_savings)

                        // Loop the Summary Saving
                        for(i = 0; i < total_savings.length; i++){
                            var route_savings = total_savings[i];
                            console.log('route_savings', route_savings);

                            var current = route_savings[0];
                            var proposed = route_savings[1];
                            var savings = route_savings[2];

                            $("#visualization_tab_comp").append("<div class='col-md-4'> <strong>Company "+(i +1)+"</strong><table class='summary_Table'><tr><th>Current Total Distance</th><th>Proposed Total Distance</th><th>Total Savings</tr><tr><td>"+current+" km"+"</td><td>"+proposed+" km"+"</td><td>"+savings+" %"+"</td></tr></table></div>");
                        }
                        // $('.modal-body').html(response['html']);
                        // $('#register-button').css('display', 'none');

                        //send email section
                        $.post('/email_info',  {
                            'starting_postal': $('#starting_postal').val(),
                            'original': $("#postal_sequence").val(),
                            'generated': $('#sorted_sequence').val()
                        });

                    } //End of sort_company

                    else{

                        //required fields:
                        var starting = response.data_result[0].required_fields.starting_postal;

                        var postal_sequence_new = response.data_result[0].required_fields.postal_sequence;
                        var result_list = response.data_result[0].required_fields.propose_result;
                        var has_return = response.data_result[0].required_fields.has_return;

                        //GeoCode for LatLng
                        var latlng_array = response.data_result[0].geo_code_latlng.latlng_array;

                        //Truck Options-1:
                        var vehicle_priority = response.data_result[0].vehicle_priority.vehicle_num;

                        //Truck Options-2
                        var capacity_priority = response.data_result[0].capacity_priority.priority_capacity;
                        var vehicle_type = response.data_result[0].capacity_priority.vehicle_type;

                        //total_summary_saving
                        var propose_route_value = response.data_result[0].total_summary_saving.propose_distance;
                        var current_route_value = response.data_result[0].total_summary_saving.current_distance;
                        var total_savings = response.data_result[0].total_summary_saving.total_savings;

                        // Get the value from unsorted Postal Code
                        // var postal_seq = $("#postal_sequence").val();
                        var postal_seq = postal_sequence;
                        var postal_seq_arr = postal_seq.split("\n");

                        // Storing the order ID and postal pairs  // current route
                        var order_postal_arr = [];

                        // postal_seq_arr.replace(/\s+/g, " ")
                        for(i = 0; i < postal_seq_arr.length; i ++){
                            var order_postal = postal_seq_arr[i];
                            order_postal = order_postal.replace(/\s+/g, " ")
                            order_postal = order_postal.replace("\t", " ");
                            order_postal = order_postal.trim();

                            var order_postal_split = order_postal.split(" ");
                            order_postal_arr.push(order_postal_split)
                        }

                        //console.log('capacity_priority-1', capacity_priority);
                        //console.log('vehicle_type-1', vehicle_type);

                        //- - - - - - export btn - - - - -  - - - - -//
                        $("#download_button").show();
                        // - - - - - - Start of Table fo Sorted Results - - - - - - - //

                        $sorted_sequence.show();
                        $sorted_sequenceTable.show();

                        //$("#sorted_sequence1").show();
                        $(".hidden_field_legend").show();

                        // Counter for Postal Code Sorted;
                        var counter = 0;
                        var split = postal_sequence.split("\n")

                        for( var i=0; i < split.length; i++ ){
                            var postalSorted = counter++;
                        }

                        $h2_success.text('Successful!')

                        // Sequence Entered
                        //$ul_sequence.append('<li>Starting Postal Code : '+starting+'</li>');
                        //$ul_sequence.append('<li>No. of Postal Sequence Entered : '+postalSorted+'</li>');
                        //$ul_sequence.append('<li>No. of Truck Entered : '+vehicle_priority+'</li>');

                        // Condition for Route by Truck:
                        if(optionsTruck === true){

                            //$p_note.append('Summary Details : <br />');

                            // Summary Table
                            $sorted_sequence.append($ParentTable);

                            // if the Truck is more than 1:
                            if(parseInt(vehicle_priority) > 1){
                                // Summary Table
                                $sorted_sequence.append($ParentTable);

                                // Append the Thead (title of each col)
                                $ParentTable.append($tableThead0);
                                $ParentTable.append($tableTbody);

                                $tableTbody.append($tableTd)

                                // Col 1
                                $tableTd.append($tableTd1);
                                $tableTd1.append('Starting Postal Code : '+starting);
                                // Col 2
                                $tableTd.append($tableTd2);
                                $tableTd2.append($ul_table);

                                var new_postal_code;
                                var counter_nums;
                                var counter_num_array = [];

                                for(i = 0; i < postal_sequence_new.length; i++){
                                    var postal_seq_vehicle = postal_sequence_new[i];
                                    var postal_code_arr = [];

                                    // counts the postal code
                                    for(k = 0; k < postal_seq_vehicle.length; k++){
                                        var postal_seq_new = postal_seq_vehicle[k]
                                        var postal_code = postal_seq_new[0];

                                        var counter_num = k + 1;

                                        // Counter to check for repeated postal codes
                                        postal_code_arr.push(postal_code);

                                        var new_postal_code = unique_postal(postal_code_arr);
                                        for (c = 0; c < new_postal_code.length; c++){
                                                var counter_num = c + 1;
                                            }
                                    }
                                    counter_num_array.push(counter_num);
                                    $ul_table.append('<li> Truck '+(i+1)+' : '+counter_num+' Propose Delivery Routes </li>');

                                }
                                var sum = counter_num_array.reduce(add, 0);

                            }
                            else{

                                // Append the Thead (title of each col)
                                $ParentTable.append($tableThead0);
                                $ParentTable.append($tableTbody);

                                $tableTbody.append($tableTd)

                                // Col 1
                                $tableTd.append($tableTd1);
                                // Col 2
                                $tableTd.append($tableTd2);


                                var total_num_result;
                                var total_truck;
                                for (var a=0; a < latlng_array.length; a++){
                                    var result_sortedPostal = latlng_array[a];
                                           total_num_result = result_sortedPostal.length;

                                }

                                // Result
                                $tableTd1.append('Starting Postal Code : '+starting);
                                $tableTd2.append('Delivery Truck '+vehicle_priority+' : '+total_num_result+' Proposed Delivery Routes');

                            }

                        } // end of if condition - Route by Truck

                        // Condition for Route by Capacity:
                        if (priority_capacity === true){

                            // Summary Table
                            $sorted_sequence.append($ParentTable);

                            // Append the Thead (title of each col)
                            $ParentTable.append($tableThead1);
                            $ParentTable.append($tableTbody);

                            $tableTbody.append($tableTd)

                            // Col 1
                            $tableTd.append($tableTd1);
                            $tableTd1.append('Starting Postal Code : '+starting);
                            // Col 2
                            $tableTd.append($tableTd2);
                            $tableTd2.append($ul_table);

                            // Col 3
                            $tableTd.append($tableTd3);
                            $tableTd3.append($ul_table1);

                            var new_postal_code;
                            var counter_nums;
                            var counter_num_array = [];

                            /*if (parseInt(vehicle_type.length) > 1){

                                for (var x=0; x < vehicle_type.length; x ++){
                                   var vehicle_types = vehicle_type[x];

                                    var truck_type = vehicle_types[0];
                                    var max_type = vehicle_types[1];
                                    var available_type = vehicle_types[2];

                                    $ul_table_truck.append('<li>Delivery Truck '+(x+1)+' : '+truck_type+'</li>');
                                }

                                }else{

                                        for (var i=0; i < vehicle_type.length; i ++){
                                            var truck_detail = vehicle_type[i];
                                            truck_type = truck_detail[0];

                                             $ul_table_truck.append('<li>Truck : '+truck_type+'</li>');
                                        }
                                }
                                // Truck Loop details
                                $.each(postal_sequence_new.concat(vehicle_type), function(i, item) {
                                    console.log(item);
                                });*/

                                //console.log(truck_name);
                                 var truck_name = [];

                                    for (var x=0; x < vehicle_type.length; x ++){
                                        var vehicle_types = vehicle_type[x];
                                        var truck_type = vehicle_types[0];
                                        var num_truck = vehicle_types[2];

                                        //$ul_table_truck.append('<li>Delivery Truck '+(x+1)+' : '+truck_type+'</li>');
                                        //truck_name.push(truck_type);
                                        $ul_table.append('<li>Delivery Truck Type '+(x+1)+' :  ' +truck_type+' </li>');
                                    }

                                for(i = 0; i < postal_sequence_new.length; i++){
                                    var postal_seq_vehicle = postal_sequence_new[i];
    //                                var truck_type = truck_name[i];
    //                                var truck_type1 = vehicle_type[i];

                                    var postal_code_arr = [];
                                    // Sum of Total Load per Trucks
                                    var loadsCount = postal_seq_vehicle.reduce(function(sum, current){
                                            return sum + current[2];
                                        }, 0 );

                                    // counts the postal code
                                    for(k = 0; k < postal_seq_vehicle.length; k++){
                                        var postal_seq_new = postal_seq_vehicle[k]
                                        var postal_code = postal_seq_new[0];

                                        //console.log('postal_seq_new-1' ,postal_seq_new);
                                        var counter_num = k + 1;

                                        // Counter to check for repeated postal codes
                                        postal_code_arr.push(postal_code);
                                        var new_postal_code = unique_postal(postal_code_arr);

                                        for (c = 0; c < new_postal_code.length; c++){
                                            var counter_num = c + 1;
                                        }
                                     }

                                     $ul_table1.append('<li>Delivery Truck '+(i+1)+' :  ' +counter_num+' Proposed Delivery Routes </li>');

                                 }

                                // Sum all Delivery Postal Code
                                var sum = counter_num_array.reduce(add, 0);

                                // Total Number
                                //$p_note.append('Summary Truck Details : <br />');
                                //$tableTd.append('<td>'+sum+ ' Proposed Sorted Postal Code</td>');
                                //$tableTd.append('<td>'+vehicle_priority+'</td>');

                        } // end of if condition - Route by Capacity

                        // - - - - - - Global Message - - - - - - - //
                        // Message Layout
                        $p_note2.text('Breakdown of Proposed Delivery Routes');

                        // Table Layout
                        $proposedTable.append("<tr><th>#</th><th>Postal Code</th> <th>Order ID</th><th>Truck Capacity</th></tr>");

                        // Counter to check for repeated postal codes
                        function unique_postal(originalArray){
                            var ar = originalArray.slice(0); //Make a copy of the array and store it in ar
                            var i = ar.length;
                            while(i--){  //Iterate through the array
                                if(ar.indexOf(ar[i],i+1)> -1){  //If the array has a duplicate
                                    ar.splice(i,1);  //Remove that element!
                                }
                            }
                            return ar; //Return the new, more unique array
                        }

                        // Loop the Postal Sequence
                        for(i = 0; i < postal_sequence_new.length; i++){
                            var postal_seq_vehicle = postal_sequence_new[i];
                            var postal_code_arr = [];

                            // Marker Truck Counter
                            $("#map_legend").append("<li><i class='fa fa-arrow-circle-o-right' aria-hidden='true'></i> Delivery Truck " + (i + 1 ) + " <i class='marker_map marker_img"+ (i+ 1) +"'></i></li>");

                            // Summary Table Truck Counter
                            $proposedTable.append("<tr><td><i class='fa fa-truck' aria-hidden='true'></i></td><td colspan='3'><b>Delivery Truck  " + (i + 1) + "</b>: </td></td>" );

                            for(k = 0; k < postal_seq_vehicle.length; k++){
                                var postal_seq_new = postal_seq_vehicle[k]

                                var postal_code = postal_seq_new[0];
                                var order_id = postal_seq_new[1];
                                var capacity_load = postal_seq_new[2];

                                var counter_num = k + 1;

                                // Counter to check for repeated postal codes
                                postal_code_arr.push(postal_code);

                                var new_postal_code = unique_postal(postal_code_arr);
                                for (c = 0; c < new_postal_code.length; c++){
                                        var counter_num = c + 1;
                                    }
                               $proposedTable.append("<tr><td class='postal_num'>"+ counter_num +"</td><td>"+postal_code+"</td><td>"+order_id+"</td><td>"+capacity_load+"</td></tr>");

                            }

                        }
                        // - - - - - - End of Table fo Sorted Results - - - - - - - //

                        // - - - - - - Start Map Results - - - - - - - //

                        //Visual Map Function
                        generateGMap(starting, result_list, order_postal_arr, latlng_array);

                        //Summary Report for
                        //generateSummaryReport(propose_route_val, current_route_val, numOfPostalCode)

                        //visualization_table(current_route_value, propose_route_value);
                        //Table below map - Summary-Value
                        $('#visualization_table').show()
                        $('#currentTotalDist').html(current_route_value.toFixed(2) + ' km');
                        $('#proposedTotalDist').html(propose_route_value.toFixed(2) + ' km');
                        $('#totalSavings').html(total_savings.toFixed(2) + '%');

                        // $('.modal-body').html(response['html']);
                        // $('#register-button').css('display', 'none');

                        //send email section
                        $.post('/email_info',  {
                            'starting_postal': $('#starting_postal').val(),
                            'original': $("#postal_sequence").val(),
                            'generated': $('#sorted_sequence').val()
                        });

                    } // end of else her:

                } // end Status == ok
                else{

                    var errors = response.errors;

                    // if there is an error in process, validation error will show
                    if(response.errors){

                       errorBox.fadeIn();
                       errorBox.find('p').html(errors);

                    }else{
                       errorBox.hide();
                    }
                }
            },
            error: function (response) {
                // failed request; give feedback to user
                $('#progressbar').html('<p class="error"><strong>Oops!</strong> Try that again in a few moments.</p>');

                // Errors validation
                var errorBox = $('#message-errors');

                if (response.responseJSON) {
                    var title = response.responseJSON['title'];
                    var message = response.responseJSON['message'];

                    errorBox.css('display', 'block');
                    errorBox.find('strong').html(title);
                    errorBox.find('span').html(message);
                }
            },
            complete: function () {

                // register_button.html('Register');
                // register_button_icon.removeClass('fa-cog fa-spin').addClass('fa-arrow-right');
            }
        });
   } //end of validation

}); //end of function


// Generate Google Map according to the sorted postal sequence
function generateGMap(starting_postal, result_list, order_postal_arr, latlng_array, sort_company){

    // Clear all "Visualization" child elements(i.e. header and google maps)
    $("#visualization").empty();
    $("#visualization").show();

    // Create "Visualization" header
    $("<h3>").attr("id", "header_visualization").append("Visualization".bold()).appendTo("#visualization");

    // Array containing lat and lng for plotting on Google Maps
    //var latlng_array = []

    // Format the postal codes (split by "," and removal of whitespaces) for calling Geocoding API
    var vehicle_postal_list_full = [];

    // Start of formatting:
    for(i = 0; i < result_list.length; i++){

        var vehicle_postal_list = result_list[i];

        for(j = 0; j < vehicle_postal_list.length; j++){
            vehicle_postal_list[j] = vehicle_postal_list[j].trim();
        }
        // Push into a full list for plotting Markers later
        vehicle_postal_list_full.push(vehicle_postal_list);
    } // End of postal code formatting

    // Create the div for Google Map
    $("<div>").attr("id", "map-canvas").appendTo("#visualization");

    // Setting map zoom and center coordinates
    var mapOptions = {
        zoom: 12,
        center: new google.maps.LatLng(1.362600, 103.830000)
    };

    // Generate the map
    var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

    // Setting the polygon coordinates
    polygon_array = [] // for assigning info window to polygon

    // Colors to differentiate the polygons
    //["red", "blue", "green", "yellow", "black", "orchid", "indigo", "darkcyan", "deeppink", "orange", "lawngreen", "azure", "rose", "magenta", "white"];
    // red - 1, blue - 2, green -3, yellow- 4
    var colors = ["#ff0033", "#0267fe", "#02cc35",
                  "#fecc02", "#999999", "#ff00cc",
                  "#cc00ff", "#029967", "#cccc67",  // #cc00cc
                  "#fe6702", "#02fe35", "#67ccfe",
                  "#fe6767", "#ff33ff", "#ccfefe",
                  "#670202", "#c6641d"];

    // Push into a full list for plotting Markers later
    polygon_coord_full = [];

    for(i = 0; i < latlng_array.length; i++){
        vehicle_latlng = latlng_array[i];

        // console.log('vehicle_latlng', vehicle_latlng);
        // Store lat and lng for constructing the polygon
        polygon_coord = []

        // Extract out the lat and lng per postal code to create LatLng object
        for(j = 0; j < vehicle_latlng.length; j++){
            latlng = vehicle_latlng[j];
            lat = latlng[0];
            lng = latlng[1];
            polygon_coord.push(new google.maps.LatLng(lat, lng));
        }

        polygon_coord_full.push(polygon_coord);

        // Construct the polygon
        // [i] the numbers of vehicle // colors[i]
        var polygon_line;

        polygon_line = new google.maps.Polygon({
            paths: polygon_coord,
            strokeColor: colors[i],
            strokeOpacity: 0.6,
            strokeWeight: 2, //3
            fillColor: colors[i],
            fillOpacity: 0.2
        });

        // Plot the polygon on the map
        addLine(polygon_line, map);
        //polygon_line.setMap(map);

        // Store the polygon for infowindow binding
        polygon_array.push(polygon_line);

        //addLine(polygon_line);

    } // End of latlng array forEach


    // Create the infowindow instance
    info_window = new google.maps.InfoWindow();

    for(i = 0; i < polygon_array.length; i++){

        // Set the content
        var content = "<b>Delivery Truck No. " + (i + 1) + "</b></br>";

        // Iterate through the postal codes to find the relevant order ID
        var postal_arr = result_list[i];

        for(j = 0; j < postal_arr.length; j++){

            var postal = postal_arr[j].trim();

            for(k = 0; k < order_postal_arr.length; k++){
                var order_postal = order_postal_arr[k];
                var order_id = order_postal[0];
                var postal2 = order_postal[1];

                if(postal == postal2){
                    if(j == 0){
                        content += order_id;
                    }else{
                        content += ", " + order_id;
                    }
                }
            }
        }

        // Postal codes for the content
        var postal_str = "";
        for(j = 0; j < postal_arr.length; j++){
            var postal = postal_arr[j];

            // Counter to check for repeated postal codes
            var counter = 0;

            for(k = 0; k < order_postal_arr.length; k++){
                var order_postal = order_postal_arr[k];
                var postal2 = order_postal[0];

                if(postal == postal2){
                    counter++;
                }
            }

            for(k = 0; k < counter; k++){
                if(j == 0 && k == 0){
                    postal_str += postal;
                    //console.log('counter-0: ', postal_str);
                }else{
                    postal_str += ", " + postal;
                }
            }
            //console.log('order_id: ', postal_str);
        }
        content += "</br>" + postal_str;

        //console.log('order_id-1: ', content);
        // Bind polygons to mouseover events
        createAndBindPolygon(polygon_array[i], content, map);
    }

    // Get lat lng of starting postal code and plot a marker
    $.ajax({
        url: "https://maps.googleapis.com/maps/api/geocode/json?address=" + starting_postal,
        type: "GET",
        async: false,
        success: function(result){
            var lat = result.results[0].geometry.location.lat
            var lng = result.results[0].geometry.location.lng

            var latlng = new google.maps.LatLng(lat, lng);
            var marker = new google.maps.Marker({
                position: latlng,
                animation: google.maps.Animation.Drop,
                map: map,
               // icon: "img/gmap_marker/marker-blue.png"
                icon: "img/gmap_marker/marker-blue_2.png",
                zIndex:100,
            });
            google.maps.event.addListener(marker, 'click', function(event){
                    info_window.setContent("Starting Postal Code: " + starting_postal);
                    info_window.setPosition(event.latLng);
                    info_window.open(map);
                });
        }
    }); // End of GET

    // Generate Markers
    for(i = 0; i < vehicle_postal_list_full.length; i++){
        veh_postal = vehicle_postal_list_full[i];
        ven_latlng = polygon_coord_full[i];

        for(j = 0; j < veh_postal.length; j++){
            var postal = veh_postal[j];
            var latlng = ven_latlng[j];

            // var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
            // Colors to differentiate the polygons
            var images = ["img/gmap_marker/red/marker" + (j + 1) + ".png",
                          "img/gmap_marker/blue/marker" + (j + 1) + ".png",
                          "img/gmap_marker/green/marker" + (j + 1) + ".png",
                          "img/gmap_marker/yellow/marker" + (j + 1) + ".png",
                          "img/gmap_marker/black/marker" + (j + 1) + ".png",
                          "img/gmap_marker/orchid/marker" + (j + 1) + ".png",
                          "img/gmap_marker/indigo/marker" + (j + 1) + ".png",
                          "img/gmap_marker/darkcyan/marker" + (j + 1) + ".png",
                          "img/gmap_marker/nine/marker" + (j + 1) + ".png",
                          "img/gmap_marker/orange/marker" + (j + 1) + ".png",
                          "img/gmap_marker/lawngreen/marker" + (j + 1) + ".png",
                          "img/gmap_marker/azure/marker" + (j + 1) + ".png",
                          "img/gmap_marker/rose/marker" + (j + 1) + ".png",
                          "img/gmap_marker/magenta/marker" + (j + 1) + ".png",
                          "img/gmap_marker/fifteen/marker" + (j + 1) + ".png",
                          "img/gmap_marker/sixteen/marker" + (j + 1) + ".png",
                          "img/gmap_marker/seventeen/marker" + (j + 1) + ".png",
                          ];

            var marker = new google.maps.Marker({
                position: latlng,
                map: map,
                icon: images[i],
                zIndex:10,
            });

            var content = "";

            // Find the relevant order ID for the content
            for(k = 0; k < order_postal_arr.length; k++){
                var order_postal = order_postal_arr[k];
                var order_id = order_postal[0];
                var postal2 = order_postal[1];

                if(postal == postal2){
                    content += "[" + postal + "]";
                }
            }
            content += "</br>" + postal;
            createAndBindMarker(marker, content, map);
        }
    }

} // End of generateGMap

function removeLine(polygon_line) {
        polygon_line.setMap(null);
      }

// Linking infowindow to the polygons and binding it to a click//mouseover event
function createAndBindPolygon(poly, content, map){
    $('#loading_map').show();

    google.maps.event.addListener(poly, 'click', function(event){
            info_window.setContent(content);
            info_window.setPosition(event.latLng);
            info_window.open(map);
        });
}
// Link infowindow to the Markers and binding it to a click event
function createAndBindMarker(marker, content, map){
google.maps.event.addListener(marker, 'click', function(event){
        info_window.setContent(content);
        info_window.setPosition(event.latLng);
        info_window.open(map);
    });
}

// Generate Google Map according to the sorted postal sequence
function generateGMap_company(starting, result_list, result_list_list, order_postal_arr, latlng_array_list, sort_company){

    // Clear all "Visualization" child elements(i.e. header and google maps)
    $("#visualization").empty();
    $("#visualization").show();

    // Create "Visualization" header
    $("<h3>").attr("id", "header_visualization").append("Visualization".bold()).appendTo("#visualization");

    // Array containing lat and lng for plotting on Google Maps
    //var latlng_array = []

    // Format the postal codes (split by "," and removal of whitespaces) for calling Geocoding API
    var vehicle_postal_list_full = [];

    // Start of formatting:

    for(i = 0; i < result_list_list.length; i++){
        var vehicle_postal_list = result_list_list[i];
        
        // Push into a full list for plotting Markers later
        vehicle_postal_list_full.push(vehicle_postal_list);
    } // End of postal code formatting

    // Map Object start below:
    // Create the div for Google Map
    $("<div>").attr("id", "map-canvas").appendTo("#visualization");

    // Setting map zoom and center coordinates //singapore maps
    var mapOptions = {
        zoom: 12,
        center: new google.maps.LatLng(1.362600, 103.830000)
    };

    // Generate the map
    var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

    // Setting the polygon coordinates
    polygon_array = [] // for assigning info window to polygon
    polygon_array2 = [] 
    // Colors to differentiate the polygons for 15 vehicles 
    var colors = ["#ff0033", 
                  "#0267fe", 
                  "#02cc35", 
                  "#fecc02", 
                  "#999999", 
                  "#ff00cc", 
                  "#cc00ff", 
                  "#029967", 
                  "#cccc67", // # cc00cc
                  "#fe6702", 
                  "#02fe35", 
                  "#67ccfe", 
                  "#fe6767", 
                  "#ff33ff", 
                  "#ffffff"];

    // Push into a full list for plotting Markers later
    polygon_coord_full = [];

    // Implement the Postal Code - Lat Long value here:
    for (s = 0; s < latlng_array_list.length; s++){
            var latlng_array = latlng_array_list[s];

        for(i = 0; i < latlng_array.length; i++){
            vehicle_latlng = latlng_array[i];

            // Store lat and lng for constructing the polygon
            polygon_coord = []

            // Extract out the lat and lng per postal code to create LatLng object
            for(j = 0; j < vehicle_latlng.length; j++){
                latlng = vehicle_latlng[j];
                lat = latlng[0];
                lng = latlng[1];

                polygon_coord.push(new google.maps.LatLng(lat, lng));
            }

            polygon_coord_full.push(polygon_coord);

            var polygon_line;
            // Construct the polygon
            // [i] the numbers of vehicle // colors[i]

            polygon_line = new google.maps.Polygon({
                paths: polygon_coord,
                strokeColor: colors[s],
                strokeOpacity: 0.6,
                strokeWeight: 2, //3
                fillColor: colors[s],
                fillOpacity: 0.2

            });

            // Plot the polygon on the map singapore
            addLine(polygon_line, map);
            //polygon.setMap(map);

            // Store the polygon for infowindow binding
             polygon_array.push(polygon_line);
        } // End of latlng array forEach
       polygon_array2.push(polygon_array);

    }// End of latlng_array
    
    // Create the info_window instance
    info_window = new google.maps.InfoWindow();
    var company_count = 0
    for(s = 0; s < result_list_list.length; s++){
        var result_list2 = result_list_list[s];

        console.log('result_list2', result_list2);

        company_count++;

        for(i = 0; i < polygon_array.length; i++){
            console.log('count: ',company_count);

            var content = "Truck " + (i + 1) + "</b></br>";
            // Iterate through the postal codes to find the relevant order ID
            var postal_arr = result_list[i];
          
            for(j = 0; j < postal_arr.length; j++){
                  // Set the content

                var postal = postal_arr[j].trim();

                for(k = 0; k < order_postal_arr.length; k++){
                    var order_postal = order_postal_arr[k];
                    var order_id = order_postal[0];
                    var postal2 = order_postal[1];

                    if(postal == postal2){
                        if(j == 0){
                            content += order_id;
                        }else{
                            content += ", " + order_id;
                        }
                    }
                }
            }

            // Postal codes for the content
            var postal_str = "";

            for(j = 0; j < postal_arr.length; j++){
                var postal = postal_arr[j];

                // Counter to check for repeated postal codes
                var counter = 0;
                for(k = 0; k < order_postal_arr.length; k++){
                    var order_postal = order_postal_arr[k];
                    var postal2 = order_postal[0];
                    if(postal == postal2){
                        counter++;
                    }
                }

                for(k = 0; k < counter; k++){
                    if(j == 0 && k == 0){
                        postal_str += postal;
                    }else{
                        postal_str += ", " + postal;
                    }
                }
            }
            content += "</br>" + postal_str;
            // console.log('kulit', content);
            // Bind polygons to mouseover events
           createAndBindPolygon(polygon_array[i], content, map);
        } //polygon_array


    }//results
    // - - - - - - - //

    var counter = 1;
    for (j = 0; j < starting.length; j++){
       
        var postal_hq = starting[j];
        var company_counter = counter++;

        //Get lat lng of starting postal code and plot a marker
        $.ajax({
            url: "https://maps.googleapis.com/maps/api/geocode/json?address=" + postal_hq,
            type: "GET",
            async: false,
            success: function(result){
                var lat = result.results[0].geometry.location.lat
                var lng = result.results[0].geometry.location.lng

                var latlng = new google.maps.LatLng(lat, lng);
                var marker = new google.maps.Marker({
                    position: latlng,
                    animation: google.maps.Animation.Drop,
                    map: map,
                    icon: "img/gmap_marker/marker"+(j +1)+".png",
                    zIndex:100,
                });

                //callback function to read HQ postal code array
                hqpoints(marker, postal_hq, map, company_counter);
            }
        }); // End of GET

    } // end loop for starting point

    // Generate Markers
    for(s = 0; s < vehicle_postal_list_full.length; s++){  
        var result_list = vehicle_postal_list_full[s];
        var polygon_coord_list = latlng_array_list[s];

        for(i = 0; i < result_list.length; i++){

            var veh_postal = result_list[i]
 
            for(j = 0; j < veh_postal.length; j++){
                var postal = veh_postal[j];
                // var latlng = polygon_coord2[j]; 
                // console.log('postal', postal);

                 for (l = 0; l < polygon_coord_list.length; l++){ 
                    var ven_latlng2 = polygon_coord_list[l];

                    for(k = 0; k < ven_latlng2.length; k++){
                        latlng2 = ven_latlng2[k];
                        lat = latlng2[0];
                        lng = latlng2[1];

                        var latlng = new google.maps.LatLng(lat, lng);
                        //polygon_coord2.push(new google.maps.LatLng(lat, lng));
                        var images = ["img/gmap_marker/red/marker" + (k + 1) + ".png",
                              "img/gmap_marker/blue/marker" + (k + 1) + ".png",
                              "img/gmap_marker/green/marker" + (k + 1) + ".png",
                              "img/gmap_marker/yellow/marker" + (k + 1) + ".png",
                              "img/gmap_marker/black/marker" + (k + 1) + ".png",
                              "img/gmap_marker/orchid/marker" + (k + 1) + ".png",
                              "img/gmap_marker/indigo/marker" + (k + 1) + ".png",
                              "img/gmap_marker/darkcyan/marker" + (k + 1) + ".png",
                              //"img/gmap_marker/deeppink/marker" + (k + 1) + ".png",
                              "img/gmap_marker/nine/marker" + (k + 1) + ".png",
                              "img/gmap_marker/orange/marker" + (k + 1) + ".png",
                              "img/gmap_marker/lawngreen/marker" + (k + 1) + ".png",
                              "img/gmap_marker/azure/marker" + (k + 1) + ".png",
                              "img/gmap_marker/rose/marker" + (k + 1) + ".png",
                              "img/gmap_marker/magenta/marker" + (k + 1) + ".png",
                              "img/gmap_marker/white/marker" + (k + 1) + ".png"
                              ];

                        var marker = new google.maps.Marker({
                            position: latlng,
                            map: map,
                            icon: images[s],
                            zIndex:10,
                        });

                    }
                }
            
                // var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
                // Colors to differentiate the polygons
                var content = "";

                // Find the relevant order ID for the content
                for(k = 0; k < order_postal_arr.length; k++){
                    var order_postal = order_postal_arr[k];

                    var postal2 = order_postal[0];
                    var order_id = order_postal[1];         
                    var company_id = order_postal[3];         

                    if(postal == postal2){
                        content += "[" + company_id + "]";
                    }
                }
                content += "</br>" + postal;
                createAndBindMarker(marker, content, map);
            }
        }    
       
    }// End of vehicle_postal_list_full
} // End of generateGMap

// Linking infowindow to the polygons and binding it to a mouseover //click event
function createAndBindPolygon(polygon, content, map){
    $('#loading_map').show();

    google.maps.event.addListener(polygon, 'click', function(event){
                            info_window.setContent(content);
                            info_window.setPosition(event.latLng);
                            info_window.open(map);
    });
}
// Link infowindow to the Markers and binding it to a mouseover //click event
function createAndBindMarker(marker, content, map, postal){
    google.maps.event.addListener(marker, 'click', function(event){ 
                                info_window.setContent(content);
                                info_window.setPosition(event.latLng);
                                info_window.open(map);
    });
}

// Infowindow for Starting Point Postal Code
function hqpoints(marker, postal_hq, map, company_counter){
    google.maps.event.addListener(marker, 'click', function(event){
            info_window.setContent("Company "+company_counter+" <br /> Starting Point: " + postal_hq);
            info_window.setPosition(event.latLng);
            info_window.open(map);
    });
}


function addLine(polygon_line, map) {
    //polygon_line.setMap(map);
//    $('#addLinesss').click(function() {
//      var clicks = $(this).data('clicks');
//
//      if (clicks) {
//         // odd clicks
//         polygon_line.setMap(null);
//      } else {
//         // even clicks
//          polygon_line.setMap(map);
//      }
//      $(this).data("clicks", !clicks);
//    });

    polygon_line.setMap(map);

    $("#addLines").click(function() {
        // Option Truck
        if($(this).data('clicked', true)){
           // alert('Test');
            polygon_line.setMap(null);

        }

    });

    $("#backagain").click(function() {
        // Option Truck
        if($(this).data('clicked', true)){
           // alert('Test');
           polygon_line.setMap(map);

        }

    });
}


});