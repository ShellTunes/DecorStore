(function ($) {
    $(document).ready(function (e) {
        $(`.submit-row input.default`).attr('value', 'Save and Pdf Download');
        $(`label[for^=id_Quote_id-][for$=-remarks]`).css({"marginLeft": "-43px"});
        $(`label[for*=-Total]`).css({"marginLeft": "-17px"});
        $(`label[for*=-Rate]`).css({"marginLeft": "-15px"});
        $(`label[for^=id_QuoteId][for$=-Quantity]`).css({"marginLeft": "-10px"});
        $(`label[for^=id_QuoteId][for$=-UnitOfMeasurement]`).css({"marginLeft": "-7px"});
        $(`label[for^=id_Quote_id][for$=-Quantity]`).css({"marginLeft": "-10px"});

        var elements = 0;
        $('.module').find("h2:contains('Glasses')").parent().each(function (i, obj) {
            elements = $(obj).children('.inline-related.has_original').length
        });

        $(".card-body").find(".field-ItemMasterId").parent().css({"display": "grid",
        "grid-template-columns": "repeat(7, minmax(50px, 1fr))",
        // "grid-row": "auto auto",
        "grid-column-gap": "20px",
        "grid-row-gap": "20px",
        "grid-auto-flow": "column",
        })

        $(".form-group.row.form-row").css({"grid-column": "1"})

        $(".field-ItemMasterId").css({"grid-column": "1"})
        $('.field-UnitOfMeasurement').css({"grid-column": "2"})
        $('.field-Length').css({"grid-column": "3"})
        $('.field-billedlength').css({"grid-column": "3"})
        $(".field-Width").css({"grid-column": "4"})
        $('.field-billedwidth').css({"grid-column": "4  "})
        $('.field-Quantity').css({"grid-column": "5"})
        $('.field-Rate').css({"grid-column": "6"})
        $('.field-Total').css({"grid-column": "7"})


        $(".card-body").find(".field-Polish").parent().css({"display": "grid", 'padding-top': '0', 'padding-bottom': '0',
        "grid-template-columns": "repeat(8, minmax(50px, 1fr))",
        "grid-row": "auto auto",
        "grid-column-gap": "20px",
        "grid-row-gap": "20px",
        "grid-auto-flow": "column",})

        // $(".form-group.row.form-row").css({"grid-column": "1"})

        $(".field-crystal").css({"grid-column": "1"})

        $('.field-crystalRate').css({"grid-column": "1"})

        $(".field-Beveling1").css({"grid-column": "1"})

        $('.field-Beveling1Rate').css({"grid-column": "1"})

        $('.field-remarks').css({"grid-column": "1"})

        $(".field-hole").css({"grid-column": "1"})

        $('.field-holeRate').css({"grid-column": "1", "grid-row":"6"})

        $(".field-Beveling2").css({"grid-column": "2"})

        $('.field-Beveling2Rate').css({"grid-column": "2"})

        $(".field-holeQty").css({"grid-column": "2", "grid-row":"6"})

        $(".field-Beveling3").css({"grid-column": "2"})

        $('.field-Beveling3Rate').css({"grid-column": "2"})

        $(".field-Beveling4").css({"grid-column": "3"})

        $('.field-Beveling4Rate').css({"grid-column": "3"})

        $(".field-Beveling5").css({"grid-column": "3"})

        $('.field-Beveling5Rate').css({"grid-column": "3"})

        $(".field-cutout").css({"grid-column": "3"})

        $('.field-cutoutRate').css({"grid-column": "3", "grid-row": "6"})

        $(".field-Beveling6").css({"grid-column": "4"})

        $('.field-Beveling6Rate').css({"grid-column": "4"})

        $(".field-frosting").css({"grid-column": "4"})

        $('.field-frostingRate').css({"grid-column": "4"})

        $(".field-cutoutQty").css({"grid-column": "4", "grid-row": "6"})

        $(".field-spacer_hole").css({"grid-column": "5"})

        $('.field-spacerholeRate').css({"grid-column": "5", "grid-row":"6"})

        $(".field-digital_printing").css({"grid-column": "5"})

        $('.field-printingRate').css({"grid-column": "5"})

        $(".field-etching").css({"grid-column": "5"})

        $('.field-etchingRate').css({"grid-column": "5"})

        $(".field-double_stroke").css({"grid-column": "6"})

        $('.field-strokeRate').css({"grid-column": "6"})

        $(".field-lacquered").css({"grid-column": "6"})

        $('.field-lacqueredRate').css({"grid-column": "6"})

        $(".field-spacerholeQty").css({"grid-column": "6", "grid-row":"6"})

        $(".field-Polish").css({"grid-column": "7"})

        $('.field-PolishRate').css({"grid-column": "7"})

        $('.field-Polishfeet').css({"grid-column": "7"})

        $(".field-screw_hole").css({"grid-column": "7", "grid-row":"5"})

        $('.field-screwholeRate').css({"grid-column": "7", "grid-row":"6"})

        $(".field-screwholeQty").css({"grid-column": "8", "grid-row":"6"})

        $('.field-igst').hide();
        $('.field-cgst').hide();
        if ($('#id_gst').is(':checked')) {
            //$(this).prop('checked',false);
            $('.field-igst').show();
            $('.field-cgst').show();
        }
        else{
            $('.field-igst').hide();
            $('.field-cgst').hide();
        }
        
        for (edit_id = 0; edit_id < elements; edit_id++) {
            if ($(`#id_QuoteId-${edit_id}-Polish`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-PolishRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-PolishRate]`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Polishfeet]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Polishfeet`).css("display", "flex");
            }
            else {
                $(`#id_QuoteId-${edit_id}-PolishRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-PolishRate]`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Polishfeet]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-Polishfeet`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-Beveling1`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-Beveling1Rate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Beveling1Rate]`).css("display", "flex");

            }
            else {
                $(`#id_QuoteId-${edit_id}-Beveling1Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling1Rate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-Beveling2`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-Beveling2Rate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Beveling2Rate]`).css("display", "flex");

            }
            else {
                $(`#id_QuoteId-${edit_id}-Beveling2Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling2Rate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-Beveling3`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-Beveling3Rate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Beveling3Rate]`).css("display", "flex");

            }
            else {
                $(`#id_QuoteId-${edit_id}-Beveling3Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling3Rate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-Beveling4`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-Beveling4Rate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Beveling4Rate]`).css("display", "flex");

            }
            else {
                $(`#id_QuoteId-${edit_id}-Beveling4Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling4Rate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-Beveling5`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-Beveling5Rate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Beveling5Rate]`).css("display", "flex");

            }
            else {
                $(`#id_QuoteId-${edit_id}-Beveling5Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling5Rate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-Beveling6`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-Beveling6Rate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Beveling6Rate]`).css("display", "flex");

            }
            else {
                $(`#id_QuoteId-${edit_id}-Beveling6Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling6Rate]`).css("display", "none");
            }
            
        }


    })
    $(document).on("click", function (e) {
        
        $("input[id$='Total']").addClass('disabled');
        var current_id = e.target.id;
        var split_id = current_id.split("-")

        var edit_id = split_id[1]
        var change_element_id = 0
        $('.module').find("h2:contains('Glasses')").parent().each(function (i, obj) {
            change_element_id = $(obj).children('.inline-related.dynamic-QuoteId').length
            // console.log("CHECK ID for on click OBJ IS ",change_element_id)
        });
        elements = $(e.target).parent().siblings('.inline-related.last-related.dynamic-QuoteId').length
        console.log("element", elements)
        var element_edit_id = elements - 1

        $(".card-body").find(".field-ItemMasterId").parent().css({"display": "grid",
        "grid-template-columns": "repeat(7, minmax(50px, 1fr))",
        // "grid-row": "auto auto",
        "grid-column-gap": "20px",
        "grid-row-gap": "20px",
        "grid-auto-flow": "column",
        })

        $(".form-group.row.form-row").css({"grid-column": "1"})

        $(".field-ItemMasterId").css({"grid-column": "1"})
        $('.field-UnitOfMeasurement').css({"grid-column": "2"})
        $('.field-Length').css({"grid-column": "3"})
        $('.field-billedlength').css({"grid-column": "3"})
        $(".field-Width").css({"grid-column": "4"})
        $('.field-billedwidth').css({"grid-column": "4  "})
        $('.field-Quantity').css({"grid-column": "5"})
        $('.field-Rate').css({"grid-column": "6"})
        $('.field-Total').css({"grid-column": "7"})

        $(".card-body").find(".field-Polish").parent().css({"display": "grid",
        "grid-template-columns": "repeat(8, minmax(50px, 1fr))",
        "grid-row": "auto auto",
        "grid-column-gap": "20px",
        "grid-row-gap": "20px",
        "grid-auto-flow": "column",})

        // $(".form-group.row.form-row").css({"grid-column": "1"})
        $(".field-crystal").css({"grid-column": "1"})

        $('.field-crystalRate').css({"grid-column": "1"})

        $(".field-Beveling1").css({"grid-column": "1"})

        $('.field-Beveling1Rate').css({"grid-column": "1"})

        $('.field-remarks').css({"grid-column": "1"})

        $(".field-hole").css({"grid-column": "1"})

        $('.field-holeRate').css({"grid-column": "1", "grid-row":"6"})

        $(".field-Beveling2").css({"grid-column": "2"})

        $('.field-Beveling2Rate').css({"grid-column": "2"})

        $(".field-holeQty").css({"grid-column": "2", "grid-row":"6"})

        $(".field-Beveling3").css({"grid-column": "2"})

        $('.field-Beveling3Rate').css({"grid-column": "2"})

        $(".field-Beveling4").css({"grid-column": "3"})

        $('.field-Beveling4Rate').css({"grid-column": "3"})

        $(".field-Beveling5").css({"grid-column": "3"})

        $('.field-Beveling5Rate').css({"grid-column": "3"})

        $(".field-cutout").css({"grid-column": "3"})

        $('.field-cutoutRate').css({"grid-column": "3", "grid-row": "6"})

        $(".field-Beveling6").css({"grid-column": "4"})

        $('.field-Beveling6Rate').css({"grid-column": "4"})

        $(".field-frosting").css({"grid-column": "4"})

        $('.field-frostingRate').css({"grid-column": "4"})

        $(".field-cutoutQty").css({"grid-column": "4", "grid-row": "6"})

        $(".field-spacer_hole").css({"grid-column": "5"})

        $('.field-spacerholeRate').css({"grid-column": "5", "grid-row":"6"})

        $(".field-digital_printing").css({"grid-column": "5"})

        $('.field-printingRate').css({"grid-column": "5"})

        $(".field-etching").css({"grid-column": "5"})

        $('.field-etchingRate').css({"grid-column": "5"})

        $(".field-double_stroke").css({"grid-column": "6"})

        $('.field-strokeRate').css({"grid-column": "6"})

        $(".field-lacquered").css({"grid-column": "6"})

        $('.field-lacqueredRate').css({"grid-column": "6"})

        $(".field-spacerholeQty").css({"grid-column": "6", "grid-row":"6"})

        $(".field-Polish").css({"grid-column": "7"})

        $('.field-PolishRate').css({"grid-column": "7"})

        $('.field-Polishfeet').css({"grid-column": "7"})

        $(".field-screw_hole").css({"grid-column": "7", "grid-row":"5"})

        $('.field-screwholeRate').css({"grid-column": "7", "grid-row":"6"})

        $(".field-screwholeQty").css({"grid-column": "8", "grid-row":"6"})

        
        if (e.target.text == "Add another Line Items Glass") {
            $(`#id_QuoteId-${change_element_id - 1}-PolishRate`).css("display", "none")
            $(`label[for=id_QuoteId-${change_element_id - 1}-PolishRate]`).css("display", "none");
            $(`label[for=id_QuoteId-${change_element_id - 1}-Polishfeet]`).css("display", "none");
            $(`#id_QuoteId-${change_element_id - 1}-Polishfeet`).css("display", "none");

            $(`#id_QuoteId-${change_element_id - 1}-Beveling1Rate`).css("display", "none") 
            $(`label[for=id_QuoteId-${change_element_id - 1}-Beveling1Rate]`).css("display", "none");

            $(`#id_QuoteId-${change_element_id - 1}-Beveling2Rate`).css("display", "none")
            $(`label[for=id_QuoteId-${change_element_id - 1}-Beveling2Rate]`).css("display", "none");

            $(`#id_QuoteId-${change_element_id - 1}-Beveling3Rate`).css("display", "none")
            $(`label[for=id_QuoteId-${change_element_id - 1}-Beveling3Rate]`).css("display", "none");

            $(`#id_QuoteId-${change_element_id - 1}-Beveling4Rate`).css("display", "none")
            $(`label[for=id_QuoteId-${change_element_id - 1}-Beveling4Rate]`).css("display", "none");

            $(`#id_QuoteId-${change_element_id - 1}-Beveling5Rate`).css("display", "none")
            $(`label[for=id_QuoteId-${change_element_id - 1}-Beveling5Rate]`).css("display", "none");

            $(`#id_QuoteId-${change_element_id - 1}-Beveling6Rate`).css("display", "none")
            $(`label[for=id_QuoteId-${change_element_id - 1}-Beveling6Rate]`).css("display", "none");

            
        }

        $(`#id_gst`).change(function () {
            if (this.checked) {
                //$(this).prop('checked',false);
                $('.field-igst').show();
                $('.field-cgst').show();
            }
            else{
                $('.field-igst').hide();
                $('.field-cgst').hide();
            }
        });


        $(`#id_QuoteId-${edit_id}-Polish`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-PolishRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-PolishRate]`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-Polishfeet]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Polishfeet`).css("display", "flex");
                value = $(`#id_QuoteId-${edit_id}-ItemMasterId`).find("option:selected").text() 
                console.log('value', value.split(' '))
                firstvalue = value.split(' ')
                firstvalue = firstvalue[0]
                firstvalue = firstvalue.toLowerCase();
                console.log(firstvalue)
                if (firstvalue == '10mm' || firstvalue == '8mm' || firstvalue == '5mm' || firstvalue == '6mm' || value == '4MM BROWN GLASS'){
                    $(`#id_QuoteId-${edit_id}-PolishRate`).val('10')
                }
                else if (firstvalue == '12mm'){
                    $(`#id_QuoteId-${edit_id}-PolishRate`).val('15')
                }
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-PolishRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-PolishRate]`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Polishfeet]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-Polishfeet`).css("display", "none");
            }
        });

    
        $(`#id_QuoteId-${edit_id}-Beveling1`).change(function () {
            if (this.checked) {
                console.log("CHECK CALL")
                //Do stuff
                $(`#id_QuoteId-${edit_id}-Beveling1Rate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Beveling1Rate`).val('30')
                $(`label[for=id_QuoteId-${edit_id}-Beveling1Rate]`).css("display", "flex");
                
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-Beveling1Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling1Rate]`).css("display", "none");
                
            }
        });

        $(`#id_QuoteId-${edit_id}-Beveling2`).change(function () {
            if (this.checked) {
                console.log("CHECK CALL")
                //Do stuff
                $(`#id_QuoteId-${edit_id}-Beveling2Rate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Beveling2Rate`).val('30')
                $(`label[for=id_QuoteId-${edit_id}-Beveling2Rate]`).css("display", "flex");
                
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-Beveling2Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling2Rate]`).css("display", "none");
                
            }
        });
        $(`#id_QuoteId-${edit_id}-Beveling3`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-Beveling3Rate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Beveling3Rate`).val('30')
                $(`label[for=id_QuoteId-${edit_id}-Beveling3Rate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-Beveling3Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling3Rate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-Beveling4`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-Beveling4Rate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Beveling4Rate`).val('50')
                $(`label[for=id_QuoteId-${edit_id}-Beveling4Rate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-Beveling4Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling4Rate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-Beveling5`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-Beveling5Rate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Beveling5Rate`).val('50')
                $(`label[for=id_QuoteId-${edit_id}-Beveling5Rate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-Beveling5Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling5Rate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-Beveling6`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-Beveling6Rate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-Beveling6Rate`).val('50')
                $(`label[for=id_QuoteId-${edit_id}-Beveling6Rate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-Beveling6Rate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-Beveling6Rate]`).css("display", "none");
            }
        });

    })




})(django.jQuery);