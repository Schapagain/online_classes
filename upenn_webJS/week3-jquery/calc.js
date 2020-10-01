/*
 * Implement all your JavaScript in this file!
 */

 $('.numeric-button').click( function(ev) {
     var prevDisplay = $('#display').val();
     var newDisplay = prevDisplay.concat($(this).val());
     $('#display').val(newDisplay);
 });

 $('#clearButton').click( function(ev) {
    $('#display').val('');
 });