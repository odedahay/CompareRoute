// Pre-load the textarea with data so
// that it can show the demo when the page renders //

function dummyPostalCode(){
    var $postalSequence = $("#postal_sequence");

    var postal_pair = [
                "469001 Order01 1 company_A",
				"760450 Order02 1 company_A",
				"596937 Order03 1 company_A",
				"596740 Order04 1 company_A",
				"098585 Order05 1 company_A",
				"109680 Order06 1 company_A",
				"189637 Order06 1 company_A",
				"258500 Order07 1 company_A",
				"547429 Order04 2 company_A",
				"048423 Order08 1 company_A",
				"238859 Order09 1 company_A",
				"188021 Order10 1 company_B",
				"188021 Order11 1 company_B",
				"189673 Order11 1 company_B",
				"068897 Order12 1 company_B",
				"738726 Order13 1 company_B",
				"218700 Order14 1 company_B",
				"198713 Order15 1 company_B",
				"218700 Order16 1 company_B",
				"198713 Order17 1 company_B",
				"389458 Order01 1 company_B",
				"278986 Order02 1 company_C",
				"431011 Order03 1 company_C",
				"460102 Order04 1 company_C",
				"408561 Order05 1 company_C",
				"689575 Order06 1 company_C",
				"560326 Order01 1 company_C",
				"738728 Order01 2 company_C",
				"159921 Order03 2 company_C",
//
			];

    for(i = 0; i < postal_pair.length; i++){
        postal_list = postal_pair[i];
        $postalSequence.append(postal_list, '\n');
    }
}

// Once the page load,
// function will run immediately:

dummyPostalCode();

