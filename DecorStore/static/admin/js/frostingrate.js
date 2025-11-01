(function ($) {
    $(document).ready(function (e) {
        var elements = 0;
        $('.module').find("h2:contains('Glasses')").parent().each(function (i, obj) {
            elements = $(obj).children('.inline-related.has_original').length
            console.log("CHECK ID OBJ IS ", $(obj).children('.inline-related.has_original'))
        });
        for (edit_id = 0; edit_id < elements; edit_id++) {
            if ($(`#id_QuoteId-${edit_id}-frosting`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-frostingRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-frostingRate]`).css("display", "flex");

            }
            else {
                $(`#id_QuoteId-${edit_id}-frostingRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-frostingRate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-digital_printing`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-printingRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-printingRate]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-printingRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-printingRate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-etching`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-etchingRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-etchingRate]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-etchingRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-etchingRate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-double_stroke`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-strokeRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-strokeRate]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-strokeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-strokeRate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-crystal`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-crystalRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-crystalRate]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-crystalRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-crystalRate]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-lacquered`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-lacqueredRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-lacqueredRate]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-lacqueredRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-lacqueredRate]`).css("display", "none");
            }
            
            if ($(`#id_QuoteId-${edit_id}-hole`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-holeRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-holeRate]`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-holeQty]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-holeQty`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-holeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-holeRate]`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-holeQty]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-holeQty`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-cutout`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-cutoutRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-cutoutRate]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-cutoutQty`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-cutoutQty]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-cutoutRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-cutoutRate]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-cutoutQty`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-cutoutQty]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-spacer_hole`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-spacerholeRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeRate]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-spacerholeQty`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeQty]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-spacerholeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeRate]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-spacerholeQty`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeQty]`).css("display", "none");
            }
            if ($(`#id_QuoteId-${edit_id}-screw_hole`).is(':checked')) {
                $(`#id_QuoteId-${edit_id}-screwholeRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-screwholeRate]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-screwholeQty`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-screwholeQty]`).css("display", "flex");

            }
            else {
                console.log("CHECK ID not checked")
                $(`#id_QuoteId-${edit_id}-screwholeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-screwholeRate]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-screwholeQty`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-screwholeQty]`).css("display", "none");
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
        
        if (e.target.text == "Add another Line Items Glass") {
                $(`#id_QuoteId-${change_element_id - 1}-frostingRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-frostingRate]`).css("display", "none");
                // $(`label[for="PolishRate"]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-printingRate`).css("display", "none") 
                $(`label[for=id_QuoteId-${change_element_id - 1}-printingRate]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-etchingRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-etchingRate]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-strokeRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-strokeRate]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-crystalRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-crystalRate]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-lacqueredRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-lacqueredRate]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-holeRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-holeRate]`).css("display", "none");
                $(`#id_QuoteId-${change_element_id - 1}-holeQty`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-holeQty]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-cutoutRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-cutoutRate]`).css("display", "none");
                $(`#id_QuoteId-${change_element_id - 1}-cutoutQty`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-cutoutQty]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-spacerholeRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-spacerholeRate]`).css("display", "none");
                $(`#id_QuoteId-${change_element_id - 1}-spacerholeQty`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-spacerholeQty]`).css("display", "none");

                $(`#id_QuoteId-${change_element_id - 1}-screwholeRate`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-screwholeRate]`).css("display", "none");
                $(`#id_QuoteId-${change_element_id - 1}-screwholeQty`).css("display", "none")
                $(`label[for=id_QuoteId-${change_element_id - 1}-screwholeQty]`).css("display", "none");

            
        }





        $(`#id_QuoteId-${edit_id}-frosting`).change(function () {
            if (this.checked) {
                //Do stuff
                // $(".field-Polish").insertAfter(".field-PolishRate" );
                $(`#id_QuoteId-${edit_id}-frostingRate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-frostingRate`).val('50')
                $(`label[for=id_QuoteId-${edit_id}-frostingRate]`).css("display", "flex");

                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-frostingRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-frostingRate]`).css("display", "none");
            }
        });

    
        $(`#id_QuoteId-${edit_id}-digital_printing`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-printingRate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-printingRate`).val('300')
                $(`label[for=id_QuoteId-${edit_id}-printingRate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-printingRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-printingRate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-etching`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-etchingRate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-etchingRate`).val('200')
                $(`label[for=id_QuoteId-${edit_id}-etchingRate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-etchingRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-etchingRate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-double_stroke`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-strokeRate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-strokeRate`).val('250')
                $(`label[for=id_QuoteId-${edit_id}-strokeRate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-strokeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-strokeRate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-crystal`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-crystalRate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-crystalRate`).val('300')
                $(`label[for=id_QuoteId-${edit_id}-crystalRate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-crystalRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-crystalRate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-lacquered`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-lacqueredRate`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-lacqueredRate`).val('180');
                $(`label[for=id_QuoteId-${edit_id}-lacqueredRate]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-lacqueredRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-lacqueredRate]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-hole`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-holeRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-holeRate]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-holeQty`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-holeQty]`).css("display", "flex");
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-holeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-holeRate]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-holeQty`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-holeQty]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-cutout`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-cutoutRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-cutoutRate]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-cutoutQty`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-cutoutQty]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-cutoutRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-cutoutRate]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-cutoutQty`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-cutoutQty]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-spacer_hole`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-spacerholeRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeRate]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-spacerholeQty`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeQty]`).css("display", "flex");
                
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-spacerholeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeRate]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-spacerholeQty`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-spacerholeQty]`).css("display", "none");
            }
        });
        $(`#id_QuoteId-${edit_id}-screw_hole`).change(function () {
            if (this.checked) {
                //Do stuff
                $(`#id_QuoteId-${edit_id}-screwholeRate`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-screwholeRate]`).css("display", "flex");
                $(`#id_QuoteId-${edit_id}-screwholeQty`).css("display", "flex");
                $(`label[for=id_QuoteId-${edit_id}-screwholeQty]`).css("display", "flex");
            }
            
            else {
                $(`#id_QuoteId-${edit_id}-screwholeRate`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-screwholeRate]`).css("display", "none");
                $(`#id_QuoteId-${edit_id}-screwholeQty`).css("display", "none");
                $(`label[for=id_QuoteId-${edit_id}-screwholeQty]`).css("display", "none");
            }
        });

    })




})(django.jQuery);