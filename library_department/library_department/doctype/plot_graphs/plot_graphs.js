frappe.ui.form.on('Plot Graphs', {
    document: function(frm) {
        frappe.call({
            doc: frm.doc,
            method: 'get_fields_names',
            callback: function(response) {
                var fields = response.message;
                frm.set_df_property('x_axis', 'options', fields);
                frm.set_df_property('y_axis', 'options', fields);
            }
        });
    },

    second_document: function(frm) {
        frappe.call({
            doc: frm.doc,
            method: 'get_fields_names_second',
            callback: function(response) {
                var fields = response.message;
                frm.set_df_property('x_axis_second', 'options', fields);
                frm.set_df_property('y_axis_second', 'options', fields);
            }
        });
    },

    enable_graph_button: function(frm) {
        frm.add_custom_button('Show Graph', function() {
            var userGraph = frm.doc.graph_type;
            var xAxis = frm.doc.x_axis;
            var yAxis = frm.doc.y_axis;
            var xAxis_second = frm.doc.x_axis_second;
            var yAxis_second = frm.doc.y_axis_second;
            var secondDocument = frm.doc.second_document;

            if (userGraph && xAxis || yAxis && xAxis_second || yAxis_second && secondDocument) {
                frappe.call({
                    doc: frm.doc,
                    method: 'generate_graph',
                    args: {
                        selected_graph_type : userGraph
                    },
                    callback: function(response) {
                        console.log(response);
                        if (response.message && response.message.image) {
                            var img = document.createElement('img');
                            img.src = response.message.image; 
                            img.alt = 'Generated Graph';
                            frm.fields_dict['image_wrapper'].wrapper.appendChild(img);
                            var downloadLink = document.createElement('a');
                            downloadLink.href = response.message.image; 
                            downloadLink.download = 'graph_image.png';
                            downloadLink.innerHTML = 'Download Image';
                            frm.fields_dict['image_wrapper'].wrapper.appendChild(downloadLink);
                        }
                    }
                });
            } else {
                frappe.msgprint('Please fill all required fields.');
            }
        });
    }
});





































// // Copyright (c) 2023, NEW INDIA and contributors
// // For license information, please see license.txt

// frappe.ui.form.on('Plot Graphs', {

//     document:function(frm) {
//         frappe.call({
//             doc:frm.doc,
//             method: 'get_fields_names',
//             callback: function(response) {
//                 console.log(response.message); 
//                 frm.set_df_property('x_axis', 'options', response.message);
//                 frm.set_df_property('y_axis', 'options', response.message);
//             }
//         });
//     },

    
//     enable_graph_button: function(frm) {
//         frm.add_custom_button('Show Graph', function() {
//             var user_graph = frm.doc.graph_type; 
//             var Onxaxis = frm.doc.x_axis; 
//             var Onyaxis = frm.doc.y_axis; 
            
//             frappe.call({
//                 method: 'Plot Graphs.generate_graph' + user_graph, 
//                 args: {
//                     x_values: Onxaxis,
//                     y_values: Onyaxis
//                 },
//                 callback: function(response) {
//                     console.log(response);
//                 }
//             });
//         });
//     }
// });



