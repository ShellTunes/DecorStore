$(document).ready(function () {
    console.log('first')
    $('#id_project').select2({
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
    
    const actionsChildren = $('.actions.col-sm-6.col-md-6').children();
    if (actionsChildren.length > 0) {
        console.log('Check:', actionsChildren);
    } else {
        console.warn('No children found for .actions.col-sm-6.col-md-6');
    }
    $('input[name="materials"]').each(function () {
        if ($(this).val() === "") {
            $(this).closest('li').css('display', 'none'); // Hide the parent <li> element
        }
    });
})
