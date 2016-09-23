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

$(document).ready(function () {
if($('#optionsTruck').is(":checked")==true){
         $(".cr_truck").show();
    }
});

// --- Radio Btn Logic when it click --- //

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


// Remove the multiple space in text area: #postal_sequence
//tr = str.replace(/ +(?= )/g,'');  
// $(function() {
//     $('#postal_sequence').click(function(){
//         // $(this).replace(/\s\s+/g, ' ');
//         $(this).split(' ').join('');
//     });
// });

// $(document).click(function(){
//     $('#deleteMe').show();
//     $('#postal_sequence').css("display", "none");
// });


// $('a').click(function(){
//     $('html, body').animate({
//         scrollTop: $( $.attr(this, 'href') ).offset().top
//     }, 500);
//     return false;
// });
// 	

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

// - - - - - Consider Truck Capacity, Option 2- - - - - //

$("#priority_capacity_comp").change(function() {
     $("#vehicle_qty_div_info").hide();

     if(this.checked){

        $("#vehicle_qty_div").hide();
        $("#vehicle_qty_div_info").show();
        //$(".hidden_field_master").show();

        if($('#num_comp_val').val() == '2')  {
            //alert('hello');

            $(".hidden_field1").fadeIn();
       	    $(".hidden_field2").fadeIn();

       	    // generateFields_companies();
        }
        else if($('#num_comp_val').val() == '3') {
            //alert('hello');

            $(".hidden_field1").fadeIn();
       	    $(".hidden_field2").fadeIn();
       	    $(".hidden_field3").fadeIn();

        }else if($('#num_comp_val').val() == '4') {
            //alert('hello');

            $(".hidden_field1").fadeIn();
       	    $(".hidden_field2").fadeIn();
       	    $(".hidden_field3").fadeIn();
       	    $(".hidden_field4").fadeIn();

        }else if($('#num_comp_val').val() == '5') {
            //alert('hello');

            $(".hidden_field1").fadeIn();
       	    $(".hidden_field2").fadeIn();
       	    $(".hidden_field3").fadeIn();
       	    $(".hidden_field4").fadeIn();
       	    $(".hidden_field5").fadeIn();

        }else if($('#num_comp_val').val() == '6') {
            //alert('hello');

            $(".hidden_field1").fadeIn();
       	    $(".hidden_field2").fadeIn();
       	    $(".hidden_field3").fadeIn();
       	    $(".hidden_field4").fadeIn();
       	    $(".hidden_field5").fadeIn();
       	    $(".hidden_field6").fadeIn();
        }
        else{
            $(".hidden_field1").show();
       	    $(".hidden_field2").show();
            $(".hidden_field3").hide();
       	    $(".hidden_field4").hide();
       	    $(".hidden_field5").hide();
       	    $(".hidden_field6").hide();
        }
     }
     else{
        $("#vehicle_qty_div_info").hide();
        $("#vehicle_qty_div").show();

        //$(".hidden_field_master").hide();
        $(".hidden_field1").hide();
        $(".hidden_field2").hide();
        $(".hidden_field3").hide();
        $(".hidden_field4").hide();
        $(".hidden_field5").hide();
        $(".hidden_field6").hide();
     }

}); //end of function

function generateFields_companies(){
    //$('#vehicle_bigTruck_1').hide();
    $('#vehicle_type_1').change(function(){
        if($('#vehicle_type_1').val() == 'truck_2'){
            $('#vehicle_bigTruck_1').show();
            //$('#vehicle_m3_1').hide();

        }else {
           //$('#vehicle_bigTruck_1').hide();
           //$('#vehicle_m3_1').show();
        }
    });
    //2nd set
   //$('#vehicle_bigTruck_2').hide();
    $('#vehicle_type_2').change(function(){
        if($('#vehicle_type_2').val() == 'truck_2'){
            $('#vehicle_bigTruck_2').show();
            //$('#vehicle_m3_2').hide();

        }else {
          // $('#vehicle_bigTruck_2').hide();
          // $('#vehicle_m3_2').show();
        }
    });
}

// - - - - -  End for Sorting by Company - - - - //
// Normal states
$(function() {

    $('#vehicle_quantity_2').hide();
    $('#starting_postal_2').hide();
    $('#vehicle_label_2').hide();
    $('#starting_label_2').hide();

    $('#starting_postal_3').hide();
    $('#vehicle_label_3').hide();
    $('#starting_label_3').hide();
    $('#vehicle_quantity_3').hide();

    $('#starting_postal_4').hide();
    $('#vehicle_label_4').hide();
    $('#starting_label_4').hide();
    $('#vehicle_quantity_4').hide();

    $('#starting_postal_5').hide();
    $('#vehicle_label_5').hide();
    $('#starting_label_5').hide();
    $('#vehicle_quantity_5').hide();

    $('#starting_postal_6').hide();
    $('#vehicle_label_6').hide();
    $('#starting_label_6').hide();
    $('#vehicle_quantity_6').hide();

});

$("#sort_company").change(function() {

    // checked the checkbox field
    if(this.checked) {

        $("#vehicle_qty_div_info").hide();
        var postal_sequence = $("#postal_sequence").val();

        $.ajax({
            type: "POST",
            url: "/sorting_comp",
            data: {
                postal_sequence: postal_sequence,
            },
            beforeSend:function(){
                 $('#progressbar').html('<div class="loading">Loading...<br /><img src="/img/ajax-loader.gif" alt="Loading..." /></div>');
            },
            success: function (response) {
                console.log('response-company', response);
                var num_comp_val = response.data_valid_company[0].required_fields.num_comp_val;
                $('#progressbar').empty();
                $('#ajax_errors').empty();
                $('#ajax_errors').hide();

                var status = response.status;
                if (status == "ok"){
                     // Print the number of companies
                    $('#num_comp_val').val(num_comp_val);

                    // Generate the fields
                    generateFields();

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

        generateFields();
    }

}); //end of function


function generateFields(){

    if($('#num_comp_val').val() == '2')  {
        $('#vehicle_quantity_2').show();
        $('#starting_postal_2').show();
        $('#vehicle_label_2').show();
        $('#starting_label_2').show();

        $('#starting_postal_3').hide();
        $('#vehicle_label_3').hide();
        $('#starting_label_3').hide();
        $('#vehicle_quantity_3').hide();

        $('#input_num1').show();
        $('#label_num1').show();

    }else if ($('#num_comp_val').val() == '3'){
            $('#starting_postal_3').show();
            $('#vehicle_label_3').show();
            $('#starting_label_3').show();
            $('#vehicle_quantity_3').show();

            $('#vehicle_quantity_2').show();
            $('#starting_postal_2').show();
            $('#vehicle_label_2').show();
            $('#starting_label_2').show();

            $('#input_num1').show();
            $('#label_num1').show();

    }else if ($('#num_comp_val').val() == '4'){

            $('#starting_postal_4').show();
            $('#vehicle_label_4').show();
            $('#starting_label_4').show();
            $('#vehicle_quantity_4').show();

            $('#starting_postal_3').show();
            $('#vehicle_label_3').show();
            $('#starting_label_3').show();
            $('#vehicle_quantity_3').show();

            $('#vehicle_quantity_2').show();
            $('#starting_postal_2').show();
            $('#vehicle_label_2').show();
            $('#starting_label_2').show();

            $('#input_num1').show();
            $('#label_num1').show();

    }else if ($('#num_comp_val').val() == '5'){

            $('#starting_postal_5').show();
            $('#vehicle_label_5').show();
            $('#starting_label_5').show();
            $('#vehicle_quantity_5').show();

            $('#starting_postal_4').show();
            $('#vehicle_label_4').show();
            $('#starting_label_4').show();
            $('#vehicle_quantity_4').show();

            $('#starting_postal_3').show();
            $('#vehicle_label_3').show();
            $('#starting_label_3').show();
            $('#vehicle_quantity_3').show();

            $('#vehicle_quantity_2').show();
            $('#starting_postal_2').show();
            $('#vehicle_label_2').show();
            $('#starting_label_2').show();

            $('#input_num1').show();
            $('#label_num1').show();

    }else if ($('#num_comp_val').val() == '6'){

            $('#starting_postal_6').show();
            $('#vehicle_label_6').show();
            $('#starting_label_6').show();
            $('#vehicle_quantity_6').show();

            $('#starting_postal_5').show();
            $('#vehicle_label_5').show();
            $('#starting_label_5').show();
            $('#vehicle_quantity_5').show();

            $('#starting_postal_4').show();
            $('#vehicle_label_4').show();
            $('#starting_label_4').show();
            $('#vehicle_quantity_4').show();

            $('#starting_postal_3').show();
            $('#vehicle_label_3').show();
            $('#starting_label_3').show();
            $('#vehicle_quantity_3').show();

            $('#vehicle_quantity_2').show();
            $('#starting_postal_2').show();
            $('#vehicle_label_2').show();
            $('#starting_label_2').show();

            $('#input_num1').show();
            $('#label_num1').show();
    }else {

        $('#vehicle_quantity_2').hide();
        $('#starting_postal_2').hide();
        $('#vehicle_label_2').hide();
        $('#starting_label_2').hide();

        $('#starting_postal_3').hide();
        $('#vehicle_label_3').hide();
        $('#starting_label_3').hide();
        $('#vehicle_quantity_3').hide();

        $('#starting_postal_4').hide();
        $('#vehicle_label_4').hide();
        $('#starting_label_4').hide();
        $('#vehicle_quantity_4').hide();

        $('#starting_postal_5').hide();
        $('#vehicle_label_5').hide();
        $('#starting_label_5').hide();
        $('#vehicle_quantity_5').hide();

        $('#starting_postal_6').hide();
        $('#vehicle_label_6').hide();
        $('#starting_label_6').hide();
        $('#vehicle_quantity_6').hide();

        $('#input_num1').hide();
        $('#label_num1').hide();
    }

}

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

var counter = 1;
var limitForms = 2;

$('#addBtn').click(function(e){
    if (counter <= limitForms){

        event.preventDefault()
        $('#items').append('<span><div class="row" id="group"><div class="col-xs-2 down_15"><input type="text" class="form-control input" id="type_of_truck_'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="truck_capacity_'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="num_of_truck_'+counter+'" /></div>'+' <div class="col-xs-2" style="margin-top:10px;"><input type="button" value="-" id="delete" /></div></div></span>' );
        counter++;

    }else{

        alert("You have reached the limit of adding Truck " + counter + " inputs");
    }
});
// Delete Input fields
$('#items').on('click', '#delete', function(){
    $('#group').parent().remove();
    counter--;
});


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

