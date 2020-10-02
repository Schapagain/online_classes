/*
 * Implement all your JavaScript in this file!
 */

var operationCodes = new Set([42,43,45,247]);

 $('button').click( function(ev) {
     
    var currentButton = $(this).html();
    if (currentButton === '=') {
        handleEquals();
    }else if(currentButton === "C") {
        handleClear();
    }else if(operationCodes.has(currentButton.charCodeAt(0))) {
        handleOperation(currentButton);
    }else {
        handleNumber(currentButton);
    }
 });

 function handleClear(){
    $('#display').val(''); 
 }

 function handleOperation(operation) {
 }

 function handleNumber(numberPressed){
    var prevDisplay = $('#display').val();
    var newDisplay = prevDisplay.concat(numberPressed);
    $('#display').val(newDisplay);
 }

 function handleEquals(){
 }