// Copyright (c) 2023, NEW INDIA and contributors
// For license information, please see license.txt



frappe.ui.form.on('Visualize Doc', {
    refresh: function(frm) {
        // Add a custom button to the form
        frm.add_custom_button('Button Label', function() {
            // Perform the action when the button is clicked
            window.open('https://cocalc.com/features/jupyter-notebook', '_blank');
            // Add your custom logic or function here
        });
    }
});


























// frappe.ui.form.on('Visualize Doc', {
//     refresh: function(frm) {
//         frm.add_custom_button('Doc Analysis', function() {
//             frappe.call({
//                 method: 'library_department.library_department.doctype.visualize_doc.my_template',
//                 callback: function(response) {
//                     var dialog = new frappe.ui.Dialog({
//                         title: 'Doc Analysis',
//                         fields: [
//                             {
//                                 fieldtype: 'HTML',
//                                 label: 'Rendered Content',
//                                 options: response.message 
//                             }
//                         ]
//                     });
//                     dialog.show();
//                 }
//             });
//         });
//     }
// });

