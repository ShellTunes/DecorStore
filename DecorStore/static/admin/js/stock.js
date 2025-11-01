if (window.location.href.includes("add")){
    $(document).ready(function () {
        const today = new Date();
        const yyyy = today.getFullYear();
        let mm = today.getMonth() + 1; // Months start at 0!
        let dd = today.getDate();

        if (dd < 10) dd = '0' + dd;
        if (mm < 10) mm = '0' + mm;

        const formattedToday =  yyyy + "-" + mm + "-" + dd

            $('#id_date').val(formattedToday)
            console.log('date')
        });
    }
$(document).ready(function(){
    var stock = $(`#id_fittingsStock`).select2({
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
    var stock = $(`#id_quote`).select2({
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
})