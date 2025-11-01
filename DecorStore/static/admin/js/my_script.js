// A $( document ).ready() block.

target_id = null
// global rate value setter 
 var current_rate = 0


if (window.location.href.includes("add")){
    $(document).on('click', function (e) {
    $(document).on('change', 'select[id^=id_QuoteId][id$=-ItemMasterId]' ,  function(event) {
        var ratevalue = event.target.id
        console.log('Working rate new', ratevalue)
        ratevalue = ratevalue.split("-")[1]
        console.log('Working rate new', ratevalue)
        var this_rate = $(`#id_QuoteId-${ratevalue}-Rate`).val()
        console.log("WORKING GLASS VAL : ", this_rate)
        current_rate =this_rate
    })
    })

    $(document).on('change' , 'input[id^=id_QuoteId][id$=-Rate]' , function(event) {
        current_rate =event.target.value
        console.log("WORKING RAte" , event.target.value)

    })


    $(document).on('change', 'input[id^=id_QuoteId][id$=-Length], input[id^=id_QuoteId][id$=-Width], input[id^=id_QuoteId][id$=-Quantity],input[id^=id_QuoteId][id$=-billedwidth], input[id^=id_QuoteId][id$=-billedlength]', function (event) {
        var input_id = event.target.id
        
        input_id = input_id.split("-")[1]
        console.log('WORKING rate val', $(`#id_QuoteId-${input_id}-Rate`).val())
        value = (Number($(`#id_QuoteId-${input_id}-Total`).val()) / Number($(`#id_QuoteId-${input_id}-Quantity`).val()))
        if (value >= Number('50')){
            console.log('WORKING reslt', current_rate)
            totalsum2 = ((current_rate * 0.1) + Number(current_rate))
            console.log('WORKING rate', totalsum2)
            $(`#id_QuoteId-${input_id}-Rate`).val(totalsum2)
        }
        if (value <= Number('50')){
            console.log('WORKING reslt', current_rate)
            totalsum2 = ((current_rate))
            console.log('WORKING rate', totalsum2)
            $(`#id_QuoteId-${input_id}-Rate`).val(totalsum2)
        }

    });
}
// A $( document ).ready() block.
$(document).on("click",  function(e){
     var current_id =  $(e.target).closest('a').attr('id');
        console.log("id",current_id)
        if (current_id != null){
            var split_id = current_id.split("-")
            console.log("CHANGING INPUT2 : ", split_id)
            target = split_id[1]
            console.log("CLICKED EVENT",target)
            $(window).focus(function() {
                if (split_id[2] == "ItemMasterId" || split_id[2] == "ItemMasterid" || split_id[2] == "ItemMasterIdMisc"){

                    if(split_id[2] === "ItemMasterId") {
                        var conceptName = $(`#id_QuoteId-${target}-ItemMasterId`).find(":selected").text();
                        console.log('CHNAGESDDDD Focus', conceptName);
                
                        $(`#id_QuoteId-${target}-ItemMasterId`).change();
                    }
                    if(split_id[2] === "ItemMasterid") {
                        var conceptName = $(`#id_Quoteid-${target}-ItemMasterid`).find(":selected").text();
                        console.log('CHNAGESDDDD Focus', conceptName);
                
                        $(`#id_Quoteid-${target}-ItemMasterid`).change();
                    }
                    if(split_id[2] === "ItemMasterIdMisc") {
                        var conceptName = $(`#id_Quote_id-${target}-ItemMasterIdMisc`).find(":selected").text();
                        console.log('CHNAGESDDDD Focus', conceptName);
                
                        $(`#id_Quote_id-${target}-ItemMasterIdMisc`).change();
                    }
                }
            });
        }
            
   


    $('select').change(function(event) {
        var current_id = event.target.id;
        var split_id = current_id.split("-")
        // console.log("CHANGING INPUT : ", split_id)
        var edit_id = split_id[1]
        if (split_id[2] == "ItemMasterId" || split_id[2] == "ItemMasterid" || split_id[2] == "ItemMasterIdMisc"){

            if(split_id[2] === "ItemMasterId") {
                        // do what ever you want
            var itemType = $(`#id_QuoteId-${edit_id}-ItemMasterId`).find(":selected").val();
            console.log("DOPING WHATEVRI WANT", itemType)
            $.ajax({
                type: "get",
                url:`/getItemRate/${itemType}`,
                success: function(data) {
                    console.log("AJAX GOIT ", data)
                    $(`#id_QuoteId-${edit_id}-Rate`).val(data);
                    current_rate = data
                    // alert(data);
                },
                failure: function(data) { 
                    console.log('Got an error dude');
                }
            });
            }

            if (split_id[2] === "ItemMasterid") {
                                        // do what ever you want
                var itemType = $(`#id_Quoteid-${edit_id}-ItemMasterid`).find(":selected").val();
                console.log("CHNAGESDDDD  WANT", itemType)
                $.ajax({
                    type: "get",
                    url:`/getItemRate/${itemType}`,
                    success: function(data) {
                        console.log("AJAX GOIT ", data)
                        $(`#id_Quoteid-${edit_id}-Rate`).val(data);
                        current_rate = data
                        // alert(data);
                    },
                    failure: function(data) { 
                        console.log('Got an error dude');
                    }
                });
            }

            if (split_id[2] === "ItemMasterIdMisc") {
                // do what ever you want
                var itemType = $(`#id_Quote_id-${edit_id}-ItemMasterIdMisc`).find(":selected").val();
                console.log("CHNAGESDDDD  WANT", itemType)
                $.ajax({
                type: "get",
                url:`/getItemRate/${itemType}`,
                success: function(data) {
                console.log("AJAX GOIT ", data)
                $(`#id_Quote_id-${edit_id}-Rate`).val(data);
                current_rate = data
                // alert(data);
                },
                failure: function(data) { 
                console.log('Got an error dude');
                }
                });
                
            }

}

});
});

$(document).ready(function () {
    $('#id_preparedBy').select2({
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