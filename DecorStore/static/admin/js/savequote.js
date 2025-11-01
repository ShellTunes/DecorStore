// $(function () {

//   function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//       const cookies = document.cookie.split(';');
//       for (let i = 0; i < cookies.length; i++) {
//         const cookie = cookies[i].trim();
//         // Does this cookie string begin with the name we want?
//         if (cookie.substring(0, name.length + 1) === (name + '=')) {
//           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//           break;
//         }
//       }
//     }
//     return cookieValue;
//   }
  
//   function ClickRefresh() {
//     var formData = $('#quote_form');
//   formData.submit( function (e) {
//     e.preventDefault();
    
//     console.log("SUBMIT SERIALISED", $(this).serialize())
//     var data = $(this).serialize();
//     $.ajax({
//       type: "post",
//       url: `/DecorStoreApp/quote/add/`,
//       // dataType: 'json',
//       method: 'POST',
//       data: data,
//       // processData: false,
//       // contentType: false,
//       headers: {
//         "X-CSRFToken": getCookie("csrftoken")
//       },
//       success: function (data) {
//         e.preventDefault();
//         console.log("AJAX GOIT ", data)
//         // alert(data);
 
//         // window.location = "/print/quotepdf/"+data;
//       },
//       failure: function (data) {
//         console.log('Got an error dude');
//       }
//     });
//   });
//   }
//   function createRefreshButton() {
//     var $btn = $('<input />', {
//       type: 'submit',
//       text: 'Save and Pdf Download',
//       value: 'Save and Pdf Download',
//       name: '_download',
//       id: 'download'
//     }).click(ClickRefresh);
//     return $btn;
//   }
//   $(".submit-row").append(createRefreshButton());
//   $(createRefreshButton).submit();
// });
