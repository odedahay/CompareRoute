$(document).ready(function () {
    $('#btnExport').click(download_excel);

});

var table_example = $('#deleteMe');
	table_example.click(function(){
	event.stopPropagation(); 

	$(this).hide();

    $('#postal_sequence').css("display", "inline-block");
    // $('#postal_sequence').val().replace(/\s\s+/g, ' ');
})

// Password validation for confirmation:
$('#btn_profile').prop('disabled', true);

$('#cfm_new_password').on('keyup', function () {
    if ($(this).val() == $('#new_password').val()) {

        $('#message_validation').html('Matching').css('color', 'green');
        $('#btn_profile').prop('disabled', false);
    } else{
        $('#message_validation').html('Not matching').css('color', 'red');
        $('#btn_profile').prop('disabled', true);
    }
});


// --- Radio Btn Logic --- //

$(function() {

    if($('#optionsTruck').prop('checked', true)){
        $(".cr_truck").show();
    }

    $('input[type="radio"]').click(function(){

        if($(this).attr("value")=="by_truck"){
            $(".box").not(".cr_truck").hide();
            $(".cr_truck").show();

            //$("#vehicle_quantity").val('1');  // Option to reset the value
        }
        if($(this).attr("value")=="by_capacity"){
            $(".box").not(".cr_capacity").hide();
            $(".cr_capacity").show();

            //$("#truck_capacity").val('');  // Option to reset the value
        }
        if($(this).attr("value")=="by_companies"){
            $(".box").not(".cr_companies").hide();
            $(".cr_companies").show();

            //$("#vehicle_quantity_1").val('1'); // Option to reset the value
        }

    });

    $( '#refresh_btn' ).on( 'click', function() {
        // call the ajax
        //alert('hello');

    });
});


// - - - - - Consider Truck Capacity, Option 1- - - - - //
$("#priority_capacity").change(function() {

    if(this.checked){
        $( "#vehicle_type" ).change(function() {
            if($(this).val() !== "truck_1" || $(this).val() !== "truck_2"){
                $('#truck_capacity').val('');
            }
         });
    }
});

// - - - - - Consider Truck Capacity, For Company Sorting- - - - - //
$("#priority_capacity_comp").change(function() {
    if(this.checked){
        $( "#vehicle_type_1" ).change(function() {
            if($(this).val() !== "truck_1" || $(this).val() !== "truck_2"){
                $('#truck_capacity_1').val('');
            }
         });
    }
    if(this.checked){
        $( "#vehicle_type_2" ).change(function() {
            if($(this).val() !== "truck_1" || $(this).val() !== "truck_2"){
                $('#truck_capacity_2').val('');
            }
         });
    }
    if(this.checked){
        $( "#vehicle_type_3" ).change(function() {
            if($(this).val() !== "truck_1" || $(this).val() !== "truck_2"){
                $('#truck_capacity_3').val('');
            }
         });
    }
    if(this.checked){
        $( "#vehicle_type_4" ).change(function() {
            if($(this).val() !== "truck_1" || $(this).val() !== "truck_2"){
                $('#truck_capacity_4').val('');
            }
         });
    }
});

//// - - - - - Consider Truck Capacity, Option 2- - - - - //
//
$("#priority_capacity_comp").change(function() {
     $("#vehicle_qty_div_info").hide();

     if(this.checked){

        $("#vehicle_qty_div").hide();
        $("#vehicle_qty_div_info").show();

        $(".hidden_field1").fadeIn();
        //$(".hidden_field_master").show();

//        if($('#num_comp_val').val() == '2')  {
//            //alert('hello');
//
//            $(".hidden_field1").fadeIn();
//       	    $(".hidden_field2").fadeIn();
//
//       	    // generateFields_companies();
//        }
//        else if($('#num_comp_val').val() == '3') {
//            //alert('hello');
//
//            $(".hidden_field1").fadeIn();
//       	    $(".hidden_field2").fadeIn();
//       	    $(".hidden_field3").fadeIn();
//
//        }else if($('#num_comp_val').val() == '4') {
//            //alert('hello');
//
//            $(".hidden_field1").fadeIn();
//       	    $(".hidden_field2").fadeIn();
//       	    $(".hidden_field3").fadeIn();
//       	    $(".hidden_field4").fadeIn();
//
//        }else if($('#num_comp_val').val() == '5') {
//            //alert('hello');
//
//            $(".hidden_field1").fadeIn();
//       	    $(".hidden_field2").fadeIn();
//       	    $(".hidden_field3").fadeIn();
//       	    $(".hidden_field4").fadeIn();
//       	    $(".hidden_field5").fadeIn();
//
//        }else if($('#num_comp_val').val() == '6') {
//            //alert('hello');
//
//            $(".hidden_field1").fadeIn();
//       	    $(".hidden_field2").fadeIn();
//       	    $(".hidden_field3").fadeIn();
//       	    $(".hidden_field4").fadeIn();
//       	    $(".hidden_field5").fadeIn();
//       	    $(".hidden_field6").fadeIn();
//        }
//        else{
//            $(".hidden_field1").show();
//       	    $(".hidden_field2").show();
//              $(".hidden_field3").hide();
//       	    $(".hidden_field4").hide();
//       	    $(".hidden_field5").hide();
//       	    $(".hidden_field6").hide();
//        }
     }
     else{
        $("#vehicle_qty_div_info").hide();
        $("#vehicle_qty_div").show();

        //$(".hidden_field_master").hide();
        $(".hidden_field1").hide();
//        $(".hidden_field2").hide();
//        $(".hidden_field3").hide();
//        $(".hidden_field4").hide();
//        $(".hidden_field5").hide();
//        $(".hidden_field6").hide();
     }

}); //end of function

//function generateFields_companies(){
//
//    //$('#vehicle_bigTruck_1').hide();
//    $('#vehicle_type_1').change(function(){
//
//        if($('#vehicle_type_1').val() == 'truck_2'){
//            $('#vehicle_bigTruck_1').show();
//            //$('#vehicle_m3_1').hide();
//
//        }else {
//           //$('#vehicle_bigTruck_1').hide();
//           //$('#vehicle_m3_1').show();
//        }
//    });
//    //2nd set
//   //$('#vehicle_bigTruck_2').hide();
//    $('#vehicle_type_2').change(function(){
//        if($('#vehicle_type_2').val() == 'truck_2'){
//            $('#vehicle_bigTruck_2').show();
//            //$('#vehicle_m3_2').hide();
//
//        }else {
//          // $('#vehicle_bigTruck_2').hide();
//          // $('#vehicle_m3_2').show();
//        }
//    });
//}

// - - - - -  End for Sorting by Company - - - - //
// Normal states
//$(function() {
//
//    $('#vehicle_quantity_2').hide();
//    $('#starting_postal_2').hide();
//    $('#vehicle_label_2').hide();
//    $('#starting_label_2').hide();
//
//    $('#starting_postal_3').hide();
//    $('#vehicle_label_3').hide();
//    $('#starting_label_3').hide();
//    $('#vehicle_quantity_3').hide();
//
//    $('#starting_postal_4').hide();
//    $('#vehicle_label_4').hide();
//    $('#starting_label_4').hide();
//    $('#vehicle_quantity_4').hide();
//
//    $('#starting_postal_5').hide();
//    $('#vehicle_label_5').hide();
//    $('#starting_label_5').hide();
//    $('#vehicle_quantity_5').hide();
//
//    $('#starting_postal_6').hide();
//    $('#vehicle_label_6').hide();
//    $('#starting_label_6').hide();
//    $('#vehicle_quantity_6').hide();
//
//});

// Route by Companies

$(function() {

    var $sortCompanies = $("#sort_company");
    var priority_capacity_comp = $("#priority_capacity_comp")[0].checked;

    $sortCompanies.change(function() {

        // checked the checkbox field
        if(this.checked) {

            $("#vehicle_qty_div_info").hide();

            var postal_sequence = $("#postal_sequence").val();

            $.ajax({
                type: "POST",
                url: "/sorting_comp",
                data: {
                    postal_sequence: postal_sequence,
                    priority_capacity_comp: priority_capacity_comp,
                },
                beforeSend:function(){

                     $('#progressbar').text('<div class="loading">Loading...<br /><img src="/img/ajax-loader.gif" alt="Loading..." /></div>');
                },
                success: function (response) {

                    var num_comp_val = response.data_valid_company[0].required_fields.num_comp_val;
                    var name_of_company = response.data_valid_company[0].required_fields.name_of_companies;

                    //console.log('Name of the companies', name_of_company);

                    $('#progressbar').empty();
                    $('#ajax_errors').empty();
                    $('#ajax_errors').hide();

                    var status = response.status;

                    if (status == "ok"){
                         // Print the number of companies
                        $('#num_comp_val').val(num_comp_val);

                        // Generate the fields
                        generateFields(name_of_company);

                        // show the input field
                        $(".hidden_1").fadeIn();

                    }
                    else{
                        var errors = response.errors;
                        $('#ajax_errors').show();
                        $('#ajax_errors').html(errors);
                    }
                },
                error: function (response) {
                    $('#progressbar').html('<p class="error"><strong>Oops!</strong> Try that again in a few moments.</p>');
                },
            })

        }// end of if statement

        else{

            $("#vehicle_qty_div_info").show();
            $('#num_comp_val').val('');
            $(".hidden_1").hide();

           generateFields(name_of_company);
        }

    }); //end of function

});

function generateFields(name_of_company){


    var $name_companies = $('.name_companies');
    var $priority_capacity_company = $('#priority_capacity_comp');
    var $fields_parent = $('#fields_company');

    // avoid duplicate
    $fields_parent.empty();
    $fields_parent.show();

    var $fields_column1 = $('<div class ="col-xs-2"></div>');
    var $fields_column2 = $('<div class ="col-xs-2" id="vehicle_qty_div"></div>');
    var $fields_column3 = $('<div class ="col-xs-2 hidden_field1"></div>');
    var $fields_column4 = $('<div class ="col-xs-2 hidden_field1"></div>');
    var $fields_column5 = $('<div class ="col-xs-2 hidden_field1"></div>');


    $fields_parent.append($fields_column1);
    $fields_parent.append($fields_column2);
    $fields_parent.append($fields_column3);
    $fields_parent.append($fields_column4);
    $fields_parent.append($fields_column5);

    //$fields_parent.append($labels)
    //$fields_parent.append($inputs)
    //console.log($fields_column);


//    $priority_capacity_company.change(function() {
//        $("#vehicle_qty_div_info").hide();
//
////        $fields_column3.hide();
////        $fields_column4.hide();
////        $fields_column5.hide();
//
//         //if(this.checked){
//         if($('#priority_capacity_comp').is(":checked")===true){
//            //alert('test');
//
//         }
//
////        if($('#priority_capacity_comp').is(':checked')== true){
////         alert('test');
////        }
//
//     }); // end of Function


    //var newHTML = [];

    for (i=0; i < name_of_company.length; i++){
        company_name = name_of_company[i];

        //newHTML.push('<span>' + name_of_company[i] + '</span>');
        // Postal Code
        $fields_column1.append('<label class="control-label font_11" for="starting_postal_'+(i+1)+'"> <span class="name_companies"> Starting Postal: '+company_name +' * </span></label>')
        $fields_column1.append('<input type="text" class="form-control input down_15" id="starting_postal_'+(i+1)+'" name="starting_postal_'+(i+1)+'" placeholder="461051" value="461051">')

        // Truck Inputs
        $fields_column2.append('<label class="control-label font_11" for="vehicle_quantity_'+(i+1)+'">Enter No. of Truck * </label>')
        $fields_column2.append('<input type="number" class="form-control input down_15" id="vehicle_quantity_'+(i+1)+'" name="vehicle_quantity_'+(i+1)+'" placeholder="1" value="1">')

        // Truck Capacity
        $fields_column3.append('<label class="control-label font_11" for="type_of_truck_c'+(i+1)+'"> Enter Type of Truck</label>');
        $fields_column3.append('<input type="text" class="form-control input down_15" id="type_of_truck_c'+(i+1)+'" name="type_of_truck_c'+(i+1)+'" placeholder="e.g. M3 Truck" value="Big Truck">');

        $fields_column4.append('<label class="control-label font_11" for="truck_capacity_c'+(i+1)+'"> Enter Max Truck Capacity * </label>');
        $fields_column4.append('<input type="number" class="form-control input down_15" id="truck_capacity_c'+(i+1)+'" name="truck_capacity_c'+(i+1)+'" placeholder="e.g. 10" value="10">');

        $fields_column5.append('<label class="control-label font_11" for="num_of_truck_c'+(i+1)+'"> No. of Truck </label>');
        $fields_column5.append('<input type="number" class="form-control input down_15" id="num_of_truck_c'+(i+1)+'" name="num_of_truck_c'+(i+1)+'" placeholder="e.g. 5" value="3">');


    }//end of loop


     //$(".element").text(newHTML.join(""));

    //$name_companies.text(newHTML.join(""));



//        if($('#num_comp_val').val() == '2')  {
//            $('#vehicle_quantity_2').show();
//            $('#starting_postal_2').show();
//            $('#vehicle_label_2').show();
//            $('#starting_label_2').show();
//
//            $('#starting_postal_3').hide();
//            $('#vehicle_label_3').hide();
//            $('#starting_label_3').hide();
//            $('#vehicle_quantity_3').hide();
//
//            $('#input_num1').show();
//            $('#label_num1').show();
//
//        }else if ($('#num_comp_val').val() == '3'){
//                $('#starting_postal_3').show();
//                $('#vehicle_label_3').show();
//                $('#starting_label_3').show();
//                $('#vehicle_quantity_3').show();
//
//                $('#vehicle_quantity_2').show();
//                $('#starting_postal_2').show();
//                $('#vehicle_label_2').show();
//                $('#starting_label_2').show();
//
//                $('#input_num1').show();
//                $('#label_num1').show();
//
//        }else if ($('#num_comp_val').val() == '4'){
//
//                $('#starting_postal_4').show();
//                $('#vehicle_label_4').show();
//                $('#starting_label_4').show();
//                $('#vehicle_quantity_4').show();
//
//                $('#starting_postal_3').show();
//                $('#vehicle_label_3').show();
//                $('#starting_label_3').show();
//                $('#vehicle_quantity_3').show();
//
//                $('#vehicle_quantity_2').show();
//                $('#starting_postal_2').show();
//                $('#vehicle_label_2').show();
//                $('#starting_label_2').show();
//
//                $('#input_num1').show();
//                $('#label_num1').show();
//
//        }else if ($('#num_comp_val').val() == '5'){
//
//                $('#starting_postal_5').show();
//                $('#vehicle_label_5').show();
//                $('#starting_label_5').show();
//                $('#vehicle_quantity_5').show();
//
//                $('#starting_postal_4').show();
//                $('#vehicle_label_4').show();
//                $('#starting_label_4').show();
//                $('#vehicle_quantity_4').show();
//
//                $('#starting_postal_3').show();
//                $('#vehicle_label_3').show();
//                $('#starting_label_3').show();
//                $('#vehicle_quantity_3').show();
//
//                $('#vehicle_quantity_2').show();
//                $('#starting_postal_2').show();
//                $('#vehicle_label_2').show();
//                $('#starting_label_2').show();
//
//                $('#input_num1').show();
//                $('#label_num1').show();
//
//        }else if ($('#num_comp_val').val() == '6'){
//
//                $('#starting_postal_6').show();
//                $('#vehicle_label_6').show();
//                $('#starting_label_6').show();
//                $('#vehicle_quantity_6').show();
//
//                $('#starting_postal_5').show();
//                $('#vehicle_label_5').show();
//                $('#starting_label_5').show();
//                $('#vehicle_quantity_5').show();
//
//                $('#starting_postal_4').show();
//                $('#vehicle_label_4').show();
//                $('#starting_label_4').show();
//                $('#vehicle_quantity_4').show();
//
//                $('#starting_postal_3').show();
//                $('#vehicle_label_3').show();
//                $('#starting_label_3').show();
//                $('#vehicle_quantity_3').show();
//
//                $('#vehicle_quantity_2').show();
//                $('#starting_postal_2').show();
//                $('#vehicle_label_2').show();
//                $('#starting_label_2').show();
//
//                $('#input_num1').show();
//                $('#label_num1').show();
//        }else {
//
//            $('#vehicle_quantity_2').hide();
//            $('#starting_postal_2').hide();
//            $('#vehicle_label_2').hide();
//            $('#starting_label_2').hide();
//
//            $('#starting_postal_3').hide();
//            $('#vehicle_label_3').hide();
//            $('#starting_label_3').hide();
//            $('#vehicle_quantity_3').hide();
//
//            $('#starting_postal_4').hide();
//            $('#vehicle_label_4').hide();
//            $('#starting_label_4').hide();
//            $('#vehicle_quantity_4').hide();
//
//            $('#starting_postal_5').hide();
//            $('#vehicle_label_5').hide();
//            $('#starting_label_5').hide();
//            $('#vehicle_quantity_5').hide();
//
//            $('#starting_postal_6').hide();
//            $('#vehicle_label_6').hide();
//            $('#starting_label_6').hide();
//            $('#vehicle_quantity_6').hide();
//
//            $('#input_num1').hide();
//            $('#label_num1').hide();
//        }


} // end of function

// - - - - - Sorting by Company Option 2- - - - - //


function download_excel(){
  $("#proposedTable").btechco_excelexport({
            containerid: "proposedTable",
            datatype: $datatype.Table,
            filename: 'compareroute'
        });
}

$("#mark_botton").click(function(e){
    // alert('Hello');
    e.preventDefault()
    $( "#changeColor" ).append( "- <span class='addedStyle'>added!</span>" );
})


$('#myTabs a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})


/* Make the table row click-able */

$(".clickable-row").click(function() {
    window.document.location = $(this).data("href");
});

//Display error message for 3 seconds and then fades out
$('.hideThis').delay(3000).fadeOut();


// Make Credit button disabled
$('#api_credits').on('keyup', function () {
    $('#creditAccess_Btn').removeAttr('disabled')
});


// - - - - - Back to Top - - - - - -//
//$(document).ready(function(){

//Check to see if the window is top if not then display button
$(window).scroll(function(){
    if ($(this).scrollTop() > 400) {
        $('.scrollToTop').fadeIn();
    } else {
        $('.scrollToTop').fadeOut();
    }
});

//Click event to scroll to top
$('.scrollToTop').click(function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
});


// By Route Truck Function by Adding input fields
$(function() {
    var counter = 1;
    var limitForms = 2;


    $('#addBtn').click(function(event){
        if (counter <= limitForms){

            event.preventDefault()
            var $inputFields = $('<span><div class="row" id="group"><div class="col-xs-2"><input type="text" class="form-control input" id="type_of_truck_'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="truck_capacity_'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="num_of_truck_'+counter+'" /></div>'+' <div class="col-xs-2"><button class="btn btn-info btn-sm" id="delete" style="margin-top:5px;" title="Delete"> Remove </button></div></div></span>');

            $('#counter_fields').text("(3 of "+ (counter + 1)+" )");
            $('#items').append($inputFields);
            counter++;

        }else{
            alert("You have reached the limit of adding Truck " + counter + " inputs");
        }

        return false;
    });

    // Delete Input fields
    $('#items').on('click', '#delete', function(){
        $('#counter_fields').html("(3 of "+ (counter - 1)+" )");
        $(this).parents('span').remove();
        counter--;

        return false;
    });

}); // end of function

//});

// - - - - -End Back to Top - - - - - -//


//Validation for Postal Sequence:

// - - - - - Sorting by Company - - - - - //
//  function route_by_Company(){
//    if($('#sort_company').is(":checked")){
//        var postal_sequence = $('textarea#postal_sequence').val().split('\n');
////        console.log('this is message', postal_sequence);
////        for(i = 0; i < postal_sequence.length; i++){
////            var postal_seq = postal_sequence[i].trim();
////            console.log('this is postal_seq', postal_seq);
////        }
//        postal_seq_array = []
//        $.each(postal_sequence, function(index, item){
//            var postal_seq = item.trim();
//            postal_seq_array.push(postal_seq);
//        });
//        for(i = 0; i < postal_seq_array.length; i++){
//            var items = postal_seq_array[i];
//            console.log('test',items);
//        }
//    }// end click
//}

