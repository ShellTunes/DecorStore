(function ($) {
  $(document).ready(function () {
    console.log("Global HAS LOADED ");
    /// Filter Multi Select /////
    var r = $(
      '<input id="multifilterbtn" class = "btn btn-success" type="button" value="Filter"/>'
    );
    $("#changelist-filter").append(r);

    $("#multifilterbtn").on("click", function (e) {
      console.log("Filtering ");
      e.preventDefault()
      for (i= 0; i < multiSelectFilters.length; i++){
        multiSelectFilters[i] = (multiSelectFilters[i]).replace("-","=")
        console.log("replc", multiSelectFilters)
      }
      console.log('multiselect', multiSelectFilters)
      var queryString = multiSelectFilters.join("&");

      console.log("QUERY FOR ", queryString);
      console.log("url", `&${queryString}`);
      let url = window.location.href;
      if (url.indexOf("?") > -1) {
        url = url.slice(0, url.indexOf("?"));
        url += `?${queryString}`;
      } else {
        url += `?${queryString}`;
      }
      window.location.href = url;
    });
    var BreakException = {};

    var multiSelectFilters = [];
    const onFilterSelected = (e) => {
      var target = e.target.id;
      var key = target.split("-")[0];

      // console.log("This id", $(`#${target}`))
      // if ($(`#${target}`).parent().hasClass('selected')){
      //     console.log('parent', )
      //     $(`#${target}`).parent().removeClass('selected')
      // }
      // else{
      //     console.log('parent select',)
      //     $(`#${target}`).parent().addClass('selected')
      // }
      // $(`#${target}`).parent().removeClass('selected')
      // $(`#${target}`).parent().each(function(){
      //     $(`#${target}`).parent().addClass('selected')
      // })

      console.log("key", key);

      // $("#changelist-filter ul > li > a").each(function (index) {
      //     var id = $(this).attr('href')
      //     $(this).parent().removeClass('selected')
      // });

      var targetElement = multiSelectFilters.find((el) => el.includes(key));
      console.log("target element", targetElement);
      if (targetElement) {
        var indexOf = multiSelectFilters.indexOf(targetElement);
        console.log("index", indexOf);
        multiSelectFilters.splice(indexOf, 1);
        console.log("if choose target", target);
        multiSelectFilters.push(target);
        console.log("target removed", target);
      } else {
        multiSelectFilters.push(target);
        console.log("target added", target);
        console.log("else choose target", (target));
      }

      console.log("Targeted ", targetElement);
      $("#changelist-filter ul > li > a").each(function (index) {
        var id = $(this).attr("href");
        $(this).parent().removeClass("selected");
      });

      for (i= 0; i < multiSelectFilters.length; i++){
        $(`#${multiSelectFilters[i]}`).parent().addClass('selected')
      }
      console.log("SELECTED FILTERS ", multiSelectFilters);
    };

    $("#changelist-filter ul > li > a").each(function (index) {
      var id = $(this).attr("href");
      $(this).removeAttr("href");
      // $(this).attr("href", "#");
      console.log("Setting Id ", id.substring(1).replace("=", "-"));
      $(this).attr("id", id.substring(1).replace("=", "-"));
      $(this).on("click", onFilterSelected);
    });
  });
})(django.jQuery);
