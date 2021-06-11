// $(".cf-form").onsubmit = function (e) {
//     e.preventDefault();
//     var dataString = $(this).serialize();
//     $.ajax("/contact/", {
//         type: "POST",
//         data: dataString,
//         success: function (data) {
//             console.log('yes')
//             $(".form-response").text(data.message).removeClass("d-none");
//         },
//         error: function (data, textStatus, errorThrown) {
//             console.log(data, textStatus, errorThrown);
//         },
//     });
//     return false;
// };
