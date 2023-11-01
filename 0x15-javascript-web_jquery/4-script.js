$('DIV#toggle_header').click(function () {
  if ($('header').attr('class') === 'red') {
    $('header').removeAttr('class');
    $('header').addClass('green');
  } else if ($('header').attr('class') === 'green') {
    $('header').removeAttr('class');
    $('header').addClass('red');
  }
});
