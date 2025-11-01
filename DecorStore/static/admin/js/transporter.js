$(document).ready(function () {
    console.log('hello');
    
    $('#id_transporter').on('change', function () {
        const transporterId = $(this).val(); // Get the selected transporter ID
        if (transporterId) {
            // Make AJAX call to fetch contact number
            $.ajax({
                url: '/get_transporter_contact/', // URL to fetch data
                data: { id: transporterId },
                success: function (response) {
                    if (response.contactnumber) {
                        // Update the contact number field
                        $('#id_contactnumber').val(response.contactnumber);
                    } else {
                        alert('Contact number not found for the selected transporter.');
                        $('#id_contactnumber').val(''); // Clear the field
                    }
                },
                error: function () {
                    alert('Error fetching contact number.');
                    $('#id_contactnumber').val(''); // Clear the field
                }
            });
        } else {
            $('#id_contactnumber').val(''); // Clear the field if no transporter is selected
        }
    });
    $('#id_transporter').select2({
        matcher: function (params, data) {
            if ($.trim(params.term) === '') {
                return data;
            }

            keywords=(params.term).split(" ");

            for (var i = 0; i < keywords.length; i++) {
                if (((data.text).toUpperCase()).indexOf((keywords[i]).toUpperCase()) == -1) 
                return null;
            }
            return data;
        }
    });
});