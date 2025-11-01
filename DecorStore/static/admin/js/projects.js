$(document).ready(function () {
    if ($('#id_type_of_work_1').is(':checked')) {
        var disable_installation = $('.form-group.row.form-row.field-installation_status').parent().siblings().parent()
        disable_installation.hide()
        console.log(('chck', disable_installation))
    }
    $('#id_type_of_work_1').change(function () {
        if (this.checked) {
            console.log("CHECK CALL")
            var chck = $('.form-group.row.form-row.field-installation_status').parent().siblings().parent()
            chck.hide()
            // $('.form-group.row.form-row.field-installation_staff').hide();
        }
        else{
            var chck = $('.form-group.row.form-row.field-installation_status').parent().siblings().parent()
            chck.show()
        }
    })
    
    });