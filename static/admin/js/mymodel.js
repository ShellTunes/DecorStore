(function($) {
    $( document ).ready(function() {
        $('.field-diagram_file').hide();
        $('.field-quote_file').hide();
        $('.field-invoice_file').hide();
        if ($('#id_diagram_status').is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-diagram_file').show();
        }
        else{

            $('.field-diagram_file').hide();
        }
        if ($('#id_quote_status').is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-quote_file').show();
            
        }
        else{

            $('.field-quote_file').hide();
        }

        if ($('#id_invoice_status').is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-invoice_file').show();
        }
        else{

            $('.field-invoice_file').hide();
        }
        // $('.field-diagram_file').hide();
        // $('#id_diagram_file').hide();
    });
    $(document).on('click','#id_diagram_status',function(e) {
       
        if ($(this).is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-diagram_file').show();
        }
        else {
             //$(this).prop('checked',true);
             $('.field-diagram_file').hide();
        }
        
    });

    $(document).on('click','#id_quote_status',function(e) {
       
        if ($(this).is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-quote_file').show();
        }
        else {
             //$(this).prop('checked',true);
             $('.field-quote_file').hide();
        }
        
    });

    $(document).on('click','#id_invoice_status',function(e) {
       
        if ($(this).is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-invoice_file').show();
        }
        else {
             //$(this).prop('checked',true);
             $('.field-invoice_file').hide();
        }
        
    });
   

})(django.jQuery);