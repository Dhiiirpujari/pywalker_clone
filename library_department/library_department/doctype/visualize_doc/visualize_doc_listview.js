frappe.listview_settings['Visualize Doc'] = {
    onload: function(listview) {
        // Add a custom button to the list view toolbar
        listview.page.add_menu_item('Button Label', function() {
            // Open the Google Colab notebook in a new tab
            window.open('https://colab.research.google.com/path/to/your/notebook', '_blank');
        });
    }
};

