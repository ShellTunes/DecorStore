(function ($) {
    $(document).ready(function () {
        // console.log("My Model HAS LOADED ")

        /// Filter Multi Select /////
        // var r = $('<input id="multifilterbtn" type="button" value="Filter"/>');
        // $("#changelist-filter").append(r);
        // console.log("JS SCRIPT HAS LOADED ")
        // // $("a").removeAttr("href");
        // // window.onbeforeunload = function(e) {
        // //     console.log("ON REFRESH ", e)
        // //     e.preventDefault()
        // //     return "Dude, are you sure you want to leave? Think of the kittens!";
        // //     // e.returnValue = ''
        // // }

        // $("#multifilterbtn").on('click', function (e) {
        //     console.log("Filtering ")

        //     var queryString = multiSelectFilters.join("&")

        //     console.log("QUERY FOR ", queryString)

        //     let url = window.location.href;
        //     if (url.indexOf('?') > -1) {
        //         url += `&${queryString}`
        //     } else {
        //         url += `?${queryString}`
        //     }
        //     window.location.href = url;
        // })
        // var multiSelectFilters = []
        // const onFilterSelected = (e) => {
        //     console.log("CLICKEDDD ", e.target.id)
        //     var target = (e.target.id).substring(1);
        //     multiSelectFilters.push(target)

        //     console.log("SELECTED FILTERS ", multiSelectFilters)
        // }

        // $("#changelist-filter ul > li > a").each(function (index) {
        //     console.log("puchu ", index + ": " + $(this).attr('href'));
        //     var id = $(this).attr('href')
        //     $(this).removeAttr("href");
        //     // $(this).attr("href", "#");
        //     $(this).attr('id', id);
        //     $(this).on('click', onFilterSelected);
        // });










        $('.field-diagram_file').hide();
        $('.field-diagram_file_1').hide();
        $('.field-diagram_file_2').hide();
        $('.field-invoice_file').hide();
        if ($('#id_diagram_status').is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-diagram_file').show();
            $('.field-diagram_file_1').show();
            $('.field-diagram_file_2').show();
        }
        else {

            $('.field-diagram_file').hide();
            $('.field-diagram_file_1').hide();
            $('.field-diagram_file_2').hide();
        }

        if ($('#id_invoice_status').is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-invoice_file').show();
        }
        else {

            $('.field-invoice_file').hide();
        }
        // $('.field-diagram_file').hide();
        // $('#id_diagram_file').hide();
    });
    $(document).on('click', '#id_diagram_status', function (e) {

        if ($(this).is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-diagram_file').show();
            $('.field-diagram_file_1').show();
            $('.field-diagram_file_2').show();
        }
        else {
            //$(this).prop('checked',true);
            $('.field-diagram_file').hide();
            $('.field-diagram_file_1').hide();
            $('.field-diagram_file_2').hide();
        }

    });



    $(document).on('click', '#id_invoice_status', function (e) {

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