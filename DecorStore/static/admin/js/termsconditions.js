$(document).ready(function () {
    $('.form-group.row.form-row.field-terms').hide();
    $('.form-group.row.form-row.field-header').hide();
    if ($('#id_choose_terms').is(':checked')) {
        var terms = $('.form-group.row.form-row.field-terms')
        terms.show()
    }

    if ($('#id_choose_header').is(':checked')) {
        var header = $('.form-group.row.form-row.field-header')
        header.show()
    }

    $('#id_choose_terms').change(function () {
        if (this.checked) {
            var chck = $('.form-group.row.form-row.field-terms')
            chck.show()
        }
        else{
            var chck = $('.form-group.row.form-row.field-terms')
            chck.hide()
        }
    })
    $('#id_choose_header').change(function () {
        if (this.checked) {
            console.log("CHECK CALL")
            var headers = $('.form-group.row.form-row.field-header')
            headers.show()
        }
        else{
            var headers = $('.form-group.row.form-row.field-header')
            headers.hide()
        }
    })
    
    });