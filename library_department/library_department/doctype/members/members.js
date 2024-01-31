// Copyright (c) 2023, NEW INDIA and contributors
// For license information, please see license.txt

frappe.ui.form.on('Members', {

    first_name:function(frm) {
        let firstValid = /^[A-Za-z]+$/;
        if ((!frm.doc.first_name) || !firstValid.test(frm.doc.first_name)) {
            frappe.msgprint("Please enter a valid first name with alphabets only");
            frappe.validated = false;
        }
    },

    //*****************************************************************************************************

    last_name:function(frm){
        let firstValid = /^[A-Za-z]+$/;
        if ((!frm.doc.last_name) || !firstValid.test(frm.doc.last_name))  {
            frappe.msgprint("Please enter a valid last name with alphabets only");
            frappe.validated = false;
        }
    },

    //*****************************************************************************************************

    date_of_birth:function(frm) {
        if (frm.doc.date_of_birth === null){
			frappe.throw("Please Enter Date of Birth");
        }else {
            frm.call({
                doc:frm.doc,
                method:'validate_dob',
            })
        }
    },

    //*****************************************************************************************************

    full_address:function(frm) {
        if (frm.doc.full_address === null){
            frappe.throw("Please Enter Full Address");
        } else {
            frm.call( {
                doc:frm.doc,
                method:'validate_address',
            })
        }
    },

    //*****************************************************************************************************

    phone:function(frm) {
        let nums = /^[0-9]+$/;
        if ((!frm.doc.phone) || !nums.test(frm.doc.phone)){
            frappe.msgprint("Please Enter Numbers only");
        }
        else {
            frm.call({
                doc:frm.doc,
                method:'validate_phone',
            })
        }
    },

    //*****************************************************************************************************

    email:function(frm) {
        if (!frm.doc.email === null) {
            frappe.msgprint("Please Enter the Email Address ");
        }else {
            frm.call( {
                doc:frm.doc,
                method:'validate_email',
            })
        }
    },

    //*****************************************************************************************************

    photo:function(frm) {
        if (frm.doc.photo){
            frm.call( {
                doc:frm.doc,
                method:'validate_photo_format',
            })
        }
    },
});











//     // ********************************************************************************************
//     // **************************************************************************************************
        














//         // function validateEmail() {
//         //     var emailValue = frm.doc.email;
//         //     var emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b/;

//         //     if (emailValue && !emailPattern.test(emailValue)) {
//         //         frappe.msgprint(__("Please enter a valid email address."));
//         //         frappe.validated = false;
//         //     }
//         // }
//         // frm.fields_dict.email.$input.on('change', function() {
//         //     validateEmail();
//         // });

//     }

     
        // if (!frm.doc.photo) {
        //     frappe.msgprint("Please upload a photo");
        //     frappe.validated = false;
        // } else {
        //     var path = frm.doc.photo.split('.');
        //     var pathFormat = path[path.length - 1].toLowerCase();
        //     var allowedFormats = ['jpg', 'jpeg', 'pdf', 'png'];

        //     if (!allowedFormats.includes(pathFormat)) {
        //         frappe.msgprint("Enter a valid format including (jpg, jpeg, pdf, png) only");
        //         frappe.validated = false;
        //     }
        // }


// function validateNames() {

        //     function validateFirstNames() {
        //         if (!frm.doc.first_name) {
        //             frappe.msgprint("Please enter Valid first name with alphabets only");
        //             frappe.validated = false; 
        //         } else {
        //             frm.doc.first_name = frm.doc.first_name;
        //         }
        //     }
        //     frm.fields_dict.first_name.$input.on('input', function() {
        //         validateFirstNames();
        //     });
    
        //     function validateLastNames() {
        //         if (!frm.doc.last_name) {
        //             frappe.msgprint("Please enter Valid last name with alphabets only");
        //             frappe.validated = false; 
        //         } else {
        //             frm.doc.last_name = frm.doc.last_name;
        //         }
        //     }
    
        //     frm.fields_dict.last_name.$input.on('input', function() {
        //         validateLastNames();
        //     });
    
        //     frm.doc.last_name = frm.doc.first_name + " " + frm.doc.last_name
        // }

        // validateNames();

    

        // function validateDate() {
        //     if (frm.doc.date_of_birth == None) {
		// 	    frappe.msgprint("Please Enter Date of Birth");
        //     }
		//     var dob = frappe.datetime.strptime(frm.doc.date_of_birth, '%Y-%m-%d').date();
		//     var cur_date = frappe.datetime.now().date();

		//     var age = cur_date.year - dob.year - ((cur_date.month,cur_date.day) < (dob.month,dob.day));

        //     if (dob == cur_date) {
        //         frappe.msgprint("Dob is Same as Current Date");
        //     }
        //     else if (dob > cur_date) {
        //         frappe.msgprint("Date Of birth can't be furture date");
        //     }
        //     else if (age == 0) {
        //         frappe.msgprint("Enter Valid Age (Greater than 1 year)");
        //     }
        //     else {
        //         frm.doc.age = age;
        //     }
        // }
        // validateDate();