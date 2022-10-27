#!/usr/bin/node
/**
  * updates the text of the <header> to New Heade!!! when the user clicks on DIV#update_header
  */
const $ = window.$;
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
