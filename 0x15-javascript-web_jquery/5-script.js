#!/usr/bin/node
/**
  * adds a <li> to a list when the user clicks on the tag DIV#add_item
  */
const $ = window.$;
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
