function scrollToAnchor(aid){
    var aTag = $("a[name='"+ aid +"']");
    $('html,body').animate({scrollTop: aTag.offset().top}, 1000);
}

// Validate Route's Function
$("#routeBtn").click(function() {
   scrollToAnchor('id3');

    // Option Truck
    if($('#optionsTruck').is(":checked")==true){
         //alert('Error!');
        if ($('#starting_postal').val().length === 0){

            //alert('Error!');

            $('#ajax_errors').show();
            $('#ajax_errors').html("No Starting Point");
            $('#starting_postal').css('border-color', 'red');

        }else{

            $('#starting_postal').css('border-color', '');
            $('#ajax_errors').hide();

        }
    }
   // Truck Capacity
//   if($('#priority_capacity').is(":checked")==true){
//
//       if ($('#truck_capacity').val().length === 0){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Please Enter Truck Capacity");
//            $('#truck_capacity').css('border-color', 'red');
//
//       }else if ($('#vehicle_type').val().length <= 1){
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Please Select Type of Truck");
//            $('#vehicle_type').css('border-color', 'red');
//
//       }else if ($('#starting_postal_cap').val().length === 0){
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Enter Starting Postal Code");
//            $('#starting_postal_cap').css('border-color', 'red');
//       }
//       else{
//            $('#truck_capacity').css('border-color', '');
//            $('#starting_postal_cap').css('border-color', '');
//            $('#vehicle_type').css('border-color', '');
//            $('#ajax_errors').hide();
//       }
//   } // end of truck capacity

   // Sort by Company
   if($('#sort_company').is(":checked")==true){
        if ($('#starting_postal_1').val().length === 0){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("No Starting Point");
            $('#starting_postal_1').css('border-color', 'red');

        }else{
            $('#starting_postal_1').css('border-color', '');
            $('#ajax_errors').hide();
        }
        // Set 2
        if ($('#starting_postal_2').val().length === 0 && $('#num_comp_val').val() == '2'){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("No Starting Point");
            $('#starting_postal_2').css('border-color', 'red');

        }else{
            $('#starting_postal_2').css('border-color', '');
            $('#ajax_errors').hide();
        }
        // Set 3
        if ($('#starting_postal_3').val().length === 0 && $('#num_comp_val').val() == '3' ){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("No Starting Point");
            $('#starting_postal_3').css('border-color', 'red');

        }else{
            $('#starting_postal_3').css('border-color', '');
            $('#ajax_errors').hide();
        }
        // Set 4
        if ($('#starting_postal_4').val().length === 0 && $('#num_comp_val').val() == '4'){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("No Starting Point");
            $('#starting_postal_4').css('border-color', 'red');

        }else{
            $('#starting_postal_4').css('border-color', '');
            $('#ajax_errors').hide();
        }
         // Set 5
        if ($('#starting_postal_5').val().length === 0 && $('#num_comp_val').val() == '5' ){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("No Starting Point");
            $('#starting_postal_5').css('border-color', 'red');

        }else{
            $('#starting_postal_5').css('border-color', '');
            $('#ajax_errors').hide();
        }
         // Set 6
        if ($('#starting_postal_6').val().length === 0 && $('#num_comp_val').val() == '6' ){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("No Starting Point");
            $('#starting_postal_6').css('border-color', 'red');

        }else{
            $('#starting_postal_6').css('border-color', '');
            $('#ajax_errors').hide();
        }
    }

    // Sort by Company considering truck capacity
   if($('#priority_capacity_comp').is(":checked")===true){

        // fields 2
        if ($('#vehicle_type_1').val().length <= 1 && $('#num_comp_val').val() == '1'){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("Select Type of Truck");
            $('#vehicle_type_1').css('border-color', 'red');

        }else if ($('#truck_capacity_1').val().length === 0 && $('#num_comp_val').val() == '1'){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("Select Type of Truck");
            $('#truck_capacity_1').css('border-color', 'red');

        }else{
            $('#starting_postal_1').css('border-color', '');
            $('#ajax_errors').hide();
        }

        // field two

        if ($('#vehicle_type_2').val().length <= 1 && $('#num_comp_val').val() == '2'){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("Select Type of Truck");
            $('#vehicle_type_2').css('border-color', 'red');

        }else if ($('#truck_capacity_2').val().length === 0 && $('#num_comp_val').val() == '2'){
            //alert('Error!');
            $('#ajax_errors').show();
            $('#ajax_errors').html("Select Type of Truck");
            $('#truck_capacity_2').css('border-color', 'red');

        }else{
            $('#starting_postal_2').css('border-color', '');
            $('#ajax_errors').hide();
        }
   }else{
//     alert('Heyy!');
     $('#starting_postal_1').css('border-color', '');
     $('#ajax_errors').hide();
   }




        // field three

//        if ($('#vehicle_type_3').val().length <= 1 && $('#num_comp_val').val() == '3'){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Select Type of Truck");
//            $('#vehicle_type_3').css('border-color', 'red');
//
//        }else if ($('#truck_capacity_3').val().length === 0 && $('#num_comp_val').val() == '3'){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Select Type of Truck");
//            $('#truck_capacity_3').css('border-color', 'red');
//
//        }else{
//            $('#starting_postal_3').css('border-color', '');
//            $('#ajax_errors').hide();
//        }
//
//        // field 4th
//        if ($('#truck_capacity_4').val().length === 0 && $('#num_comp_val').val() == '4'){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Select Type of Truck");
//            $('#truck_capacity_4').css('border-color', 'red');
//
//        }else{
//            $('#starting_postal_4').css('border-color', '');
//            $('#ajax_errors').hide();
//        }
//
//        // field 5th
//        if ($('#vehicle_type_5').val().length <= 1 && $('#num_comp_val').val() == '5'){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Select Type of Truck");
//            $('#vehicle_type_5').css('border-color', 'red');
//
//        }else if ($('#truck_capacity_5').val().length === 0){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Select Type of Truck");
//            $('#truck_capacity_5').css('border-color', 'red');
//
//        }else{
//            $('#starting_postal_5').css('border-color', '');
//            $('#ajax_errors').hide();
//        }
//
//        // field 6th
//        if ($('#vehicle_type_6').val().length <= 1 && $('#num_comp_val').val() == '6'){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Select Type of Truck");
//            $('#vehicle_type_6').css('border-color', 'red');
//
//        }else if ($('#truck_capacity_6').val().length === 0){
//            //alert('Error!');
//            $('#ajax_errors').show();
//            $('#ajax_errors').html("Select Type of Truck");
//            $('#truck_capacity_6').css('border-color', 'red');
//
//        }else{
//            $('#starting_postal_6').css('border-color', '');
//            $('#ajax_errors').hide();
//        }
    //} // end of Sort by companys

});

// Click --> Generate Button
$('#routeBtn').click(function () {

    var starting_postal = $("#starting_postal").val();

    var starting_postal_1 = $("#starting_postal_1").val();
    var starting_postal_2 = $("#starting_postal_2").val();
    var starting_postal_3 = $("#starting_postal_3").val();
    var starting_postal_4 = $("#starting_postal_4").val();
    var starting_postal_5 = $("#starting_postal_5").val();
    var starting_postal_6 = $("#starting_postal_6").val();

    // 1
    var starting_postal_cap = $("#starting_postal_cap").val();
    var type_of_truck = $("#type_of_truck").val();
    var truck_capacity = $("#truck_capacity").val();
    var num_of_truck = $("#num_of_truck").val();

    // Additional the reserve Form and limit the number 4 Types of Truck
    // 2
    var type_of_truck_1 = $("#type_of_truck_1").val();
    var truck_capacity_1 = $("#truck_capacity_1").val();
    var num_of_truck_1 = $("#num_of_truck_1").val();

    // 3
    var type_of_truck_2 = $("#type_of_truck_2").val();
    var truck_capacity_2 = $("#truck_capacity_2").val();
    var num_of_truck_2 = $("#num_of_truck_2").val();

    var vehicle_quantity = $("#vehicle_quantity").val();
    var vehicle_quantity_1 = $("#vehicle_quantity_1").val();
    var vehicle_quantity_2 = $("#vehicle_quantity_2").val();
    var vehicle_quantity_3 = $("#vehicle_quantity_3").val();
    var vehicle_quantity_4 = $("#vehicle_quantity_4").val();
    var vehicle_quantity_5 = $("#vehicle_quantity_5").val();
    var vehicle_quantity_6 = $("#vehicle_quantity_6").val();

    var postal_sequence = $("#postal_sequence").val();
    var email = $("[name=email_value]").val();
    var has_return = $("#return_startpoint")[0].checked;

    var truck_capacity_1 = $("#truck_capacity_1").val();
    var truck_capacity_2 = $("#truck_capacity_2").val();
    var truck_capacity_3 = $("#truck_capacity_3").val();
    var truck_capacity_4 = $("#truck_capacity_4").val();
    var truck_capacity_5 = $("#truck_capacity_5").val();
    var truck_capacity_6 = $("#truck_capacity_6").val();

    var vehicle_type = $("#vehicle_type").val();
    var vehicle_type_1 = $("#vehicle_type_1").val();
    var vehicle_type_2 = $("#vehicle_type_2").val();
    var vehicle_type_3 = $("#vehicle_type_3").val();
    var vehicle_type_4 = $("#vehicle_type_4").val();
    var vehicle_type_5 = $("#vehicle_type_5").val();
    var vehicle_type_6 = $("#vehicle_type_6").val();

    var optionsTruck = $("#optionsTruck")[0].checked;
    var priority_capacity = $("#priority_capacity")[0].checked;
    var priority_capacity_comp = $("#priority_capacity_comp")[0].checked;

    var sort_company = $("#sort_company")[0].checked;
    var num_comp_val = $("#num_comp_val").val();

    $('#prog').progressbar({ value: 0 });


    $.ajax({
        type: "POST",
        url: "/sorting",
        dataType: 'json',
        data: {
            starting_postal: starting_postal,

            starting_postal_1: starting_postal_1,
            starting_postal_2: starting_postal_2,
            starting_postal_3: starting_postal_3,
            starting_postal_4: starting_postal_4,
            starting_postal_5: starting_postal_5,
            starting_postal_6: starting_postal_6,

            // 1
            starting_postal_cap: starting_postal_cap,
            type_of_truck: type_of_truck,
            truck_capacity: truck_capacity,
            num_of_truck: num_of_truck,

            // Additional the reserve Form
            // 2
            type_of_truck_1: type_of_truck_1,
            truck_capacity_1: type_of_truck_1,
            num_of_truck_1: num_of_truck_1,

            // 3
            type_of_truck_2: type_of_truck_2,
            truck_capacity_2: truck_capacity_2,
            num_of_truck_2: num_of_truck_2,

            vehicle_quantity: vehicle_quantity,
            vehicle_quantity_1: vehicle_quantity_1,
            vehicle_quantity_2: vehicle_quantity_2,
            vehicle_quantity_3: vehicle_quantity_3,
            vehicle_quantity_4: vehicle_quantity_4,
            vehicle_quantity_5: vehicle_quantity_5,
            vehicle_quantity_6: vehicle_quantity_6,

            postal_sequence: postal_sequence,
            email: email,
            has_return: has_return,

            truck_capacity: truck_capacity,
            truck_capacity_1: truck_capacity_1,
            truck_capacity_2: truck_capacity_2,
            truck_capacity_3: truck_capacity_3,
            truck_capacity_4: truck_capacity_4,
            truck_capacity_5: truck_capacity_5,
            truck_capacity_6: truck_capacity_6,

            vehicle_type: vehicle_type,
            vehicle_type_1: vehicle_type_1,
            vehicle_type_2: vehicle_type_2,
            vehicle_type_3: vehicle_type_3,
            vehicle_type_4: vehicle_type_4,
            vehicle_type_5: vehicle_type_5,
            vehicle_type_6: vehicle_type_6,

            optionsTruck: optionsTruck,
            priority_capacity: priority_capacity,
            priority_capacity_comp: priority_capacity_comp,

            sort_company: sort_company,
            num_comp_val: num_comp_val
        },
        beforeSend:function(){
            // this is where we append a loading image
            $('#progressbar').html('<div class="loading">Loading...<br /><img src="/img/ajax-loader.gif" alt="Loading..." /></div>');
            $("#sorted_sequence0").hide();
            $("#sorted_sequence0_ul").hide();
            $("#sorted_sequence0_ul_02").hide();
            $("#sorted_sequence1").hide();
            $("#proposedTable").hide();
            $("#proposedTable_company").hide();
            $("#download_button").hide();
            $("#visualization").hide();
            $("#visualization_tab_comp").hide();
            $("#visualization_table").hide();
            $(".hidden_field_legend").hide();

            //$("#routeBtn").prop('disabled', true);
         },
        success: function (response) {

            $('#progressbar').empty();
            $('#ajax_errors').empty();
            $("#sorted_sequence0").empty();
            $("#sorted_sequence0_ul").empty();
            $("#sorted_sequence0_ul_02").empty();
            $("#sorted_sequence1").empty();
            $("#proposedTable").empty();
            $("#proposedTable_company").empty();
            $("#visualization_tab_comp").empty();
            $("#map_legend").empty();

            $('#ajax_errors').hide();

            //$("#routeBtn").prop('disabled', false);

            var status = response.status;
            var sort_company = response.sort_company;

            if (status == "ok"){

                if (sort_company == "true"){

                    //required fields:
                    var starting = response.data_result[0].required_fields.starting_postal;

                    var postal_sequence_company = response.data_result[0].required_fields.postal_sequence;
                    var result_list = response.data_result[0].required_fields.propose_result;
                    var result_list_list = response.data_result[0].required_fields.propose_results;

                    var has_return = response.data_result[0].required_fields.has_return;
                    //GeoCode for LatLng
                    var latlng_array_list = response.data_result[0].geo_code_latlng.latlng_array;
        
                    //total_summary_saving
                    var total_savings = response.data_result[0].total_summary_saving.total_savings;

                     // Counter for PostalCode Sorted;
                    var counter =1;
                    var split = postal_sequence.split("\n")

                    for(var i=0;i < split.length;i++){
                        postalSorted = counter++
                    }

                    //- - - - - - export btn - - - - -  - - - - -//
                    $("#download_button").show();
                    //- - - - - -/end export btn - - - -- - - - -//
                    $("#sorted_sequence0").show();
                    $("#sorted_sequence0_ul").show();
                    $("#sorted_sequence0_ul_02").show();
                    $("#sorted_sequence1").show();
                    $("#proposedTable").show();
                    $("#proposedTable_company").show();

                    //- - - - - - - - Info Box - - - - - - - - - -//

                    $(".hidden_field_legend").show();
                    $("#priority_capacity_comp").show();

                    $("#sorted_sequence0").append("<h2 style='font-weight:normal'>Successful!</h2>");
                    
                    for (var hq = 0; hq < starting.length; hq++){
                        var hq_startingPoint = starting[hq];
                        $("#sorted_sequence0_ul").append("<li>Company "+ (hq + 1) +" - Starting Postal Code : "+hq_startingPoint+ "</li>");
                    }

                    $("#sorted_sequence0_ul_02").append("<li>Number of Companies: "+num_comp_val+"</li>");
                    $("#sorted_sequence0_ul_02").append("<li>Total Number of Postal Code: "+postalSorted+"</li>");
                    
                    $("#proposedTable_company").append("<tr><th colspan='2'>Postal Code</th> <th>Order ID</th><th>Truck Volume</th><th>Company ID</th></tr>");

                    //- - - - - - - - /end Info Box - - - - - - -//

                    // Counter to check for repeated postal codes
                    function unique(originalArray){
                        var ar = originalArray.slice(0);//Make a copy of the array and store it in ar
                        var i = ar.length;
                        while(i--){  //Iterate through the array
                            if(ar.indexOf(ar[i],i+1)> -1){  //If the array has a duplicate
                                ar.splice(i,1);  //Remove that element!
                            }
                        }
                        return ar; //Return the new, more unique array
                    }

                    // Loop the Postal Sequence
                    for(i = 0; i < postal_sequence_company.length; i++){
                        var postal_seq_vehicle = postal_sequence_company[i];

                        //console.log('postal_seq_vehicle', postal_seq_vehicle);
                        // Truck Counter
                        $("#map_legend").append("<li><i class='fa fa-arrow-circle-o-right' aria-hidden='true'></i> Company " + (i + 1 ) + " <i class='marker_map marker_img"+ (i + 1) +"'></i></li>");

                        for(x = 0; x < postal_seq_vehicle.length; x++ ){
                            var company_set = postal_seq_vehicle[x];
                            var postal_code_arr = [];

                            $("#proposedTable_company").append("<tr><td colspan='5'><b>Company " + (i + 1) + " - <span class='label label-info'>Truck "+(x + 1)+ "</span></b> : </td></td></tr>" );
                            for (z = 0; z < company_set.length; z++){
                                 var company_details = company_set[z];

                                 var postal_code = company_details[0];
                                 var order_id = company_details[1];
                                 var capacity_load = company_details[2];
                                 var company_id = company_details[3];

                                // Counter to check for repeated postal codes
                                postal_code_arr.push(postal_code);
                                var new_postal_code = unique(postal_code_arr);

                                for (c = 0; c < new_postal_code.length; c++){
                                    var counter_num = c + 1;
                                }

                                $("#proposedTable_company").append("<tr><td>"+ counter_num +"</td><td>"+postal_code+"</td><td>"+order_id+"</td><td>"+capacity_load+"</td><td>"+company_id+"</td></tr>");
                            }
                        }
                    }
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
                    // console.log('latlng_array', latlng_array);
                    //Truck Options-1:
                    var vehicle_priority = response.data_result[0].vehicle_priority.vehicle_num;

                    //Truck Options-2
                    var capacity_priority = response.data_result[0].capacity_priority.priority_capacity;
                    var vehicle_type = response.data_result[0].capacity_priority.vehicle_type;
                    var vehicle_capacity = response.data_result[0].capacity_priority.vehicle_capacity;

                    //total_summary_saving
                    var propose_route_value = response.data_result[0].total_summary_saving.propose_distance;
                    var current_route_value = response.data_result[0].total_summary_saving.current_distance;
                    var total_savings = response.data_result[0].total_summary_saving.total_savings;

                    // Counter for PostalCode Sorted;
                    var counter = 0;
                    var split = postal_sequence.split("\n")

                    for(var i=0;i < split.length;i++){
                        postalSorted = counter++
                    }

                    // Counter to check for repeated postal codes
                    function unique(originalArray){
                        var ar = originalArray.slice(0);//Make a copy of the array and store it in ar
                        var i = ar.length;
                        while(i--){  //Iterate through the array
                            if(ar.indexOf(ar[i],i+1)> -1){  //If the array has a duplicate
                                ar.splice(i,1);  //Remove that element!
                            }
                        }
                        return ar; //Return the new, more unique array
                    }

                    //- - - - - - export btn - - - - -  - - - - -//
                    $("#download_button").show();
                    // - - - - - - Start of Table fo Sorted Results - - - - - - - //

                    $("#sorted_sequence0").show();
                    $("#sorted_sequence1").show();
                    $("#proposedTable").show();
                    $(".hidden_field_legend").show();

                    $("#sorted_sequence0").append("<h2 style='font-weight:normal'>Successful!</h2>");
                    $("#sorted_sequence0").append("<ul class='list-group' style='list-style-type:none; font-size:16px;'><li>Starting Postal Code : "+starting+"</li><li>No. of Postal Sequence Entered : "+postalSorted+"</li><li>No. of Truck Entered : "+vehicle_priority+"</li></ul>");
                    $("#proposedTable").append("<tr><th colspan='2'>Sorted Postal Code</th> <th>Order ID (s)</th><th>Truck Vol.</th></tr>");



                    // Loop the Postal Sequence
                    for(i = 0; i < postal_sequence_new.length; i++){
                        var postal_seq_vehicle = postal_sequence_new[i];
                        var postal_code_arr = [];

                        // Marker Truck Counter
                        $("#map_legend").append("<li><i class='fa fa-arrow-circle-o-right' aria-hidden='true'></i> Truck No. " + (i + 1 ) + " <i class='marker_map marker_img"+ (i+ 1) +"'></i></li>");

                        // Summary Table Truck Counter
                        $("#proposedTable").append("<tr><td colspan='4'><b>Truck No. " + (i + 1) + "</b>: </td></td>" );

                        for(k = 0; k < postal_seq_vehicle.length; k++){
                            var postal_seq_new = postal_seq_vehicle[k]

                            var postal_code = postal_seq_new[0];
                            var order_id = postal_seq_new[1];
                            var capacity_load = postal_seq_new[2];

                            var counter_num = k + 1;

                            // Counter to check for repeated postal codes
                            postal_code_arr.push(postal_code);
                            var new_postal_code = unique(postal_code_arr);

                            for (c = 0; c < new_postal_code.length; c++){
                                var counter_num = c + 1;
                            }
                           // console.log(counter_num );
//                           if (counter_num !== k){
//                            //console.log(postal_code);
//                            $("#proposedTable").append("<tr><td colspan='2'>"+ counter_num +"</td><td>"+postal_code+"</td><td>"+order_id+"</td><td>"+capacity_load+"</td></tr>");
//
//                           }
//                           else{
//                            $("#proposedTable").append("<tr><td >"+ counter_num +"</td><td>"+postal_code+"</td><td>"+order_id+"</td><td>"+capacity_load+"</td></tr>");
//
//                           }

                           $("#proposedTable").append("<tr><td class='postal_num'>"+ counter_num +"</td><td>"+postal_code+"</td><td>"+order_id+"</td><td>"+capacity_load+"</td></tr>");

                        }

                    }
                    // - - - - - - End of Table fo Sorted Results - - - - - - - //

                    // - - - - - - Start Map Results - - - - - - - //
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


                    // - - - - -  Callback Function - - - - - - //
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
                //alert(errors);
                $('#ajax_errors').show();
                $('#ajax_errors').html(errors);
            }
        },
        error: function (response) {
            // failed request; give feedback to user
            $('#progressbar').html('<p class="error"><strong>Oops!</strong> Try that again in a few moments.</p>');

            // Errors validation
            var ajax_errors = $('#ajax-errors');

            if (response.responseJSON) {
                var title = response.responseJSON['title'];
                var message = response.responseJSON['message'];

                ajax_errors.css('display', 'block');
                ajax_errors.find('strong').html(title);
                ajax_errors.find('span').html(message);
            }
        },
        complete: function () {

//            register_button.html('Register');
//            register_button_icon.removeClass('fa-cog fa-spin').addClass('fa-arrow-right');
        }
    })
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

        console.log('vehicle_latlng', vehicle_latlng);
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
        var content = "<b>Truck No. " + (i + 1) + "</b></br>";

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