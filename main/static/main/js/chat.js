$('#check').on('click', function () {
    if ($('.envelope').css('display') == 'none') {
        $('.wrapper').removeClass('d-none');
    } else {
        $('.wrapper').addClass('d-none');
    }
})


alertify.set('notifier', 'position', 'top-right');

$('.chat-form').validate();

var send = function () {
  if (($(".chat-form [name='name']").val() != '') && ($(".chat-form [name='email']").val() != '') && ($(".chat-form [name='message']").val() != '')) {
    if ($('#check').val() == 'on')
      $('#check').click();
    $.ajax({
      url: "/chat/",
      method: 'POST',
      data: {
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
        'name': $(".chat-form [name='name']").val(),
        'email': $(".chat-form [name='email']").val(),
        'message': $(".chat-form [name='message']").val(),
      },
      success: function (data) {
        if (data.ok) {
          alertify.notify(data.message, 'success', 5);
          $(".chat-form [name='name']").val('');
          $(".chat-form [name='email']").val('');
          $(".chat-form [name='message']").val('');
        }
      }
    })
  }
}
