
// Main Navigation
var url = window.location;
// Will only work if string in href matches with location
$('#loggedNav li a[href="'+ url +'"]').parent().addClass('active');

// relative and absolute HREF URL
$('#loggedNav li a').filter(function() {
    return this.href == url;
}).parent().addClass('active');

// relative and absolute HREF URL
$('#admin_nav li a').filter(function() {
    return this.href == url;
}).parent().addClass('active');

$('#admin_nav li a[href="'+ url +'"]').parent().addClass('active');



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


// Global Variable of CompareRoute landing page
// TextArea input
var postalSequence = $('#postal_sequence');
var template_byTruck = $('.textbox_truck');
var template_byCapacity = $('.textbox_capacity');
var template_byCompanies = $('.textbox_companies');

// radio button event:
var routeFields = $(".box");
var tableDisplay = $('.tableDisplay');

// input fields
var cr_truck = $('.cr_truck');
var cr_capacity = $('.cr_capacity');
var cr_companies = $('.cr_companies');

// Template Companies:
var refreshBtn_companies = $('.refreshBtn');

// error variables:
var errorInput = $('.js_error');
var errorMainBox = $('#message-errors');

$(function() {

    // Default Open for Optimizing Truck
    if($('#optionsTruck').prop('checked', true)){ $(".cr_truck").show();}

    // close Btn:
    $("#closeBtn").on('click', function(){
        $(this).parent().remove();
    })
    // When it click
    template_byTruck.on('click', function(event){
        $(this).hide();
        postalSequence.css("display", "inline-block");
    });

   postalSequence.hide();

    $('input[type="radio"]').click(function(){

        if($(this).attr("value")==="by_truck"){

            // default
            routeFields.not(cr_truck).hide();

            // TextBox display
            tableDisplay.not(cr_truck).hide();
            cr_truck.show();

            // TextBox Template:
            template_byTruck.show();
            postalSequence.hide();

            // When it click the textarea field:
            template_byTruck.on('click', function(event){
                $(this).hide();
                postalSequence.css("display", "inline-block");
            });

            //main error validation
            errorMainBox.hide();

        }

        if($(this).attr("value")==="by_capacity"){

            routeFields.not(cr_capacity).hide();

            // TextBox display
            tableDisplay.not(cr_capacity).hide();

            cr_capacity.show();
            refreshBtn_companies.hide();

            // TextBox Template:
            template_byCapacity.show();

            // Hide Route by Truck
            template_byTruck.hide();
            postalSequence.hide();

            // When it click the textArea field:
            template_byCapacity.on('click', function(event){
                $(this).hide();
                postalSequence.css("display", "inline-block");

            });
             //main error validation
            errorMainBox.hide();
        }
        if($(this).attr("value")==="by_companies"){

             routeFields.not(cr_companies).hide();

             // TextBox display
             tableDisplay.not(cr_companies).hide();
             cr_companies.show();
             refreshBtn_companies.show();

             // TextBox Template:
             template_byCompanies.show();
             postalSequence.hide();

             // When it click the textarea field:
             template_byCompanies.on('click', function(event){

                $(this).hide();
                postalSequence.css("display", "inline-block");

            });

            //main error validation
            errorMainBox.hide();

            // Always uncheck if the checkbox is checked when switching
            $('#priority_capacity_comp').prop('checked', false);

            //$("#vehicle_quantity_1").val('1'); // Option to reset the value
        }

        // hide the error message
        // if switching tab
        errorInput.hide();


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

         //$('.hidden_field1').fadeIn();
    }
});

// - - - - - Consider Truck Capacity, For Company Sorting- - - - - //  vehicle_qty_div
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
     //$("#vehicle_qty_div_info").hide();

     if(this.checked){

       $(".vehicle_qty_div").hide();
       $(".hidden_field1").fadeIn();
       // $("#vehicle_qty_div_info").show();

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
        //$("#vehicle_qty_div_info").hide();
        $(".vehicle_qty_div").show();
        $(".hidden_field1").hide();

        //$(".hidden_field_master").hide();
       // $(".hidden_field2").hide();
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

// Route by Companies by Refreshing Btn:

$( '#refresh_btn' ).on( 'click', function() {
        // call the ajax
        //alert('hello');
        //location.reload();
         $('#priority_capacity_comp').prop('checked', false);
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


    });

$(function() {

    var $sortCompanies = $("#sort_company");
    //var $priority_capacity_comp = $("#priority_capacity_comp")[0].checked;

    $sortCompanies.change(function() {
         $("#vehicle_qty_div_info").hide();

        // checked the checkbox field
        if(this.checked) {

            $("#vehicle_qty_div_info").show();
            var postal_sequence = $("#postal_sequence").val();

            $.ajax({
                type: "POST",
                url: "/sorting_comp",
                data: {
                    postal_sequence: postal_sequence,
                   // priority_capacity_comp: priority_capacity_comp,
                },
                beforeSend:function(){

                     $('#progressbar').html('<div class="loading">Loading...<br /><img src="/img/ajax-loader.gif" alt="Loading..." /></div>');
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
                        //additional Truck Btn
                        //generateFields_add_truck(name_of_company);

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
    var $fields_company_add = $('#fields_company_add');


    var $fields_column7 = $('<div class ="hidden_field1"></div>');

    $fields_parent.empty();
    $fields_parent.show();

    $fields_parent.append($fields_parent_sub);

    // Add fields
    $fields_company_add.append($fields_column7);

    for (i=0; i < name_of_company.length; i++){
        var company_name = name_of_company[i];

        //newHTML.push('<span>' + name_of_company[i] + '</span>');
        // Postal Code

        var $fields_parent_sub = $('<div class ="row"></div>');

        var $fields_column1 = $('<div class ="col-xs-2"></div>');
        var $fields_column2 = $('<div class ="col-xs-2 vehicle_qty_div"></div>');
        // priority capacity
        var $fields_column3 = $('<div class ="col-xs-2 hidden_field1"></div>');
        var $fields_column4 = $('<div class ="col-xs-2 hidden_field1"></div>');
        var $fields_column5 = $('<div class ="col-xs-2 hidden_field1"></div>');
        var $fields_column6 = $('<div class ="hidden_field1"></div>'); // btn Add

        var $fields_label01 = $('<label class="control-label font_11" for="starting_postal_'+(i+1)+'"> <span class="name_companies"> Starting Postal: '+company_name +' * </span></label>')
        var $fields_input01 = $('<input type="text" class="form-control input down_15" id="starting_postal_'+(i+1)+'" name="starting_postal_'+(i+1)+'" placeholder="461051" value="461051">')

        var $fields_label02 = $('<label class="control-label font_11" for="vehicle_quantity_'+(i+1)+'">Enter No. of Truck * </label>')
        var $fields_input02 = $('<input type="number" class="form-control input down_15" id="vehicle_quantity_'+(i+1)+'" name="vehicle_quantity_'+(i+1)+'" placeholder="1" value="1">')

        var $fields_label03 = $('<label class="control-label font_11" for="type_of_truck_c'+(i+1)+'"> Enter Types of Truck</label>');
        var $fields_input03 = $('<input type="text" class="form-control input down_15" id="type_of_truck_c'+(i+1)+'" name="type_of_truck_c'+(i+1)+'" placeholder="e.g. M3 Truck" value="Truck">');

        var $fields_label04 = $('<label class="control-label font_11" for="truck_capacity_c'+(i+1)+'"> Enter Max Truck Capacity * </label>');
        var $fields_input04 = $('<input type="number" class="form-control input down_15" id="truck_capacity_c'+(i+1)+'" name="truck_capacity_c'+(i+1)+'" placeholder="e.g. 10" value="10">');

        var $fields_label05 = $('<label class="control-label font_11" for="num_of_truck_c'+(i+1)+'"> No. of Truck </label>');
        var $fields_input05 = $('<input type="number" class="form-control input down_15" id="num_of_truck_c'+(i+1)+'" name="num_of_truck_c'+(i+1)+'" placeholder="e.g. 5" value="1">');

        var $fields_button_add = $('<button id="add_button_c'+(i+1)+'" class="btn btn-link btn-sm customBtn_comp" >+ Add New Truck (3 of 1)</button>');

        var $fields_parent_addBTn = $('<div class="row" id="btn_item_'+(i+1)+'" style="margin-bottom:15px; margin-top:-24px"></div>');

        $fields_parent_sub.append($fields_column1);
        $fields_parent_sub.append($fields_column2);
        $fields_parent_sub.append($fields_column3);
        $fields_parent_sub.append($fields_column4);
        $fields_parent_sub.append($fields_column5);
        $fields_parent_sub.append($fields_column6);

        // Priority Truck
        $fields_column1.append($fields_label01);
        $fields_column1.append($fields_input01);

        $fields_column2.append($fields_label02);
        $fields_column2.append($fields_input02);

        // Priority Capacity
        $fields_column3.append($fields_label03);
        $fields_column3.append($fields_input03);

        $fields_column4.append($fields_label04);
        $fields_column4.append($fields_input04);

        $fields_column5.append($fields_label05);
        $fields_column5.append($fields_input05);

        // The button Add
        $fields_column6.append($fields_button_add);

        // append <row>
        $fields_parent.append($fields_parent_sub);
        $fields_parent.append($fields_parent_addBTn);

    }//end of loop



// function of the button:
function generateFields_add_truck(){ }

//Btn 1
$(function() {
    var counter = 1;
    var limitTruck = 2;

    $('#add_button_c1').click(function(event){

        if (counter <= limitTruck){

            event.preventDefault();
            var $inputField_span = $('<span></span>');
            var $inputField_row = $('<div class="row"></div>');
            var $inputFields_col = $('<div class="col-xs-2"><label style="font-size: 12px; padding-top:15px; padding-left:20px; ">Additional Truck : '+(counter + 1)+'</label></div><div class="col-xs-2"><input type="text" class="form-control input" id="type_of_truck_cc'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="truck_capacity_cc'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="num_of_truck_cc'+counter+'" /><input type="hidden" id="add_truck_cc1" value="true"/></div><button class="btn btn-info btn-sm" id="delete_comp_c1" style="margin-top:5px;" title="Delete"> Remove </button>');

            $inputField_span.append($inputField_row);
            $inputField_row.append($inputFields_col);

            $('#add_button_c1').text("+ Add New Truck (3 of "+ (counter + 1)+" )");
            $('#btn_item_1').append($inputField_span);
            counter ++;

        }else{

            alert("You have reached the limit of adding Truck of " + counter + " inputs");
        }
       return false
    });

    $('#btn_item_1').on('click', '#delete_comp_c1', function(){
        $('#add_button_c1').text("+ Add New Truck (3 of "+ (counter - 1)+" )");
        $(this).parents('span').remove();
        counter --;
        return false;
    });
});

// Btn 2
$(function() {
    var counter = 1;
    var limitTruck = 2;

    $('#add_button_c2').click(function(event){

        if (counter <= limitTruck){

            event.preventDefault();
            var $inputField_span = $('<span></span>');
            var $inputField_row = $('<div class="row"></div>');
            var $inputFields_col = $('<div class="col-xs-2"><label style="font-size: 12px; padding-top:15px; padding-left:20px; ">Additional Truck : '+(counter + 1)+'</label></div><div class="col-xs-2"><input type="text" class="form-control input" id="type_of_truck_cc2'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="truck_capacity_cc2'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="num_of_truck_cc2'+counter+'" /><input type="hidden" id="add_truck_cc2" value="true"/></div><button class="btn btn-info btn-sm" id="delete_comp_c2" style="margin-top:5px;" title="Delete"> Remove </button>');

            $inputField_span.append($inputField_row);
            $inputField_row.append($inputFields_col);

            $('#add_button_c2').text("+ Add New Truck (3 of "+ (counter + 1)+" )");
            $('#btn_item_2').append($inputField_span);
            counter ++;

        }else{

            alert("You have reached the limit of adding Truck of " + counter + " inputs");
        }
       return false
    });

    $('#btn_item_2').on('click', '#delete_comp_c2', function(){
        $('#add_button_c2').text("+ Add New Truck (3 of "+ (counter - 1)+" )");
        $(this).parents('span').remove();
        counter --;
        return false;
    });
});


// Btn 3
$(function() {
    var counter = 1;
    var limitTruck = 2;

    $('#add_button_c3').click(function(event){

        if (counter <= limitTruck){

            event.preventDefault();
            var $inputField_span = $('<span></span>');
            var $inputField_row = $('<div class="row"></div>');
            var $inputFields_col = $('<div class="col-xs-2"><label style="font-size: 12px; padding-top:15px; padding-left:20px; ">Additional Truck : '+(counter + 1)+'</label></div><div class="col-xs-2"><input type="text" class="form-control input" id="type_of_truck_cc3'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="truck_capacity_cc3'+counter+'" /></div><div class="col-xs-2 down_15"><input type="number" class="form-control input" id="num_of_truck_cc3'+counter+'" /><input type="hidden" id="add_truck_cc3" value="true"/></div><button class="btn btn-info btn-sm" id="delete_comp_c3" style="margin-top:5px;" title="Delete"> Remove </button>');

            $inputField_span.append($inputField_row);
            $inputField_row.append($inputFields_col);

            $('#add_button_c3').text("+ Add New Truck (3 of "+ (counter + 1)+" )");
            $('#btn_item_3').append($inputField_span);
            counter ++;

        }else{

            alert("You have reached the limit of adding Truck of " + counter + " inputs");
        }
       return false
    });

    $('#btn_item_3').on('click', '#delete_comp_c3', function(){
        $('#add_button_c3').text("+ Add New Truck (3 of "+ (counter - 1)+" )");
        $(this).parents('span').remove();
        counter --;
        return false;
    });
});


} // end of function

// - - - - - Download Button- - - - - //

$('body').on('click', '#btn_export', function() {
   //alert('test');
   $("#proposedTable").btechco_excelexport({
        containerid: "proposedTable",
        datatype: $datatype.Table,
        filename: 'compareroute_xls'
    });

});

// undefined function
$("#mark_botton").click(function(e){
    // alert('Hello');
    e.preventDefault()
    $( "#changeColor" ).append( "- <span class='addedStyle'>added!</span>" );
})

// undefined function
$('#myTabs a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})


// - - Route Log page table - - - - - -//
/* Make the table row click-able */
$(".clickable-row").click(function() {
    window.document.location = $(this).data("href");
});


// - - API page for the page - - - - - -//
// Hide after 3sec the error message box
//Display error message for 3 seconds and then fades out
//$('.hideThis').delay(3000).fadeOut();


// Make Credit button disabled
$('#api_credits').on('keyup', function () {
    $('#creditAccess_Btn').removeAttr('disabled')
});


// - - Back to Top Function- - - - - -//
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


// - - By Route Truck Capacity Function by Adding input fields - - - - - -//

$(function() {
    var counter = 1;
    var limitForms = 2;


    $('#addBtn').click(function(event){

        if (counter <= limitForms){

            event.preventDefault()
            var $inputFields_span = $('<span></span>');
            var $inputFields_row = $('<div class="row" id="group"></div>');

            var $inputFields_div1 = $('<div class="col-xs-2 down_15"></div>');
            var $inputFields_div2 = $('<div class="col-xs-2 down_15"></div>');
            var $inputFields_div3 = $('<div class="col-xs-2 down_15"></div>');
            var $inputFields_div4 = $('<div class="col-xs-2"></div>');

            var $inputFields1 = $('<input type="text" class="form-control input" id="type_of_truck_'+counter+'" /><p class="js_error typeTruck_'+counter+'"></p>');
            var $inputFields2 = $('<input type="text" class="form-control input" id="truck_capacity_'+counter+'" /><p class="js_error truckCapacity_'+counter+'"></p>');
            var $inputFields3 = $('<input type="text" class="form-control input" id="num_of_truck_'+counter+'" /><p class="js_error numTruck_'+counter+'"></p><input type="hidden" id="add_truck_capacity_'+counter+'" value="'+counter+'"/>');
            var $button = $('<button class="btn btn-info btn-sm" id="delete" style="margin-top:5px;" title="Delete"> Remove </button>');

            // append in span:
            var parentNode = $inputFields_span.append($inputFields_row)

            // append in row:
            $inputFields_row.append($inputFields_div1, $inputFields_div2, $inputFields_div2, $inputFields_div3, $inputFields_div4);

            // append in div:
            $inputFields_div1.append($inputFields1);
            $inputFields_div2.append($inputFields2);
            $inputFields_div3.append($inputFields3);
            $inputFields_div4.append($button);

            $('#counter_fields').text(" ("+(counter+ 1)+" of 3)");
            $('#items').append(parentNode);
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