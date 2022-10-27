#!/usr/bin/node
/**
  * updates the text color of the <header> to red when the user clcks
  * you must use the JQuery API
  */
const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').css('color', 'red');
});
