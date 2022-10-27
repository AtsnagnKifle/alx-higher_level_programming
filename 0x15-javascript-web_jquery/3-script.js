#!/usr/bin/node
/**
  * adds the class red <header> when the user clicks on the tag DIV#red_header
  */
const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').addClass('red');
});
