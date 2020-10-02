/*
 * Implement all your JavaScript in this file!
 */
var _prevResult;
var _prevResultExists;
var _currentOperator;
var _currentOperatorExists;
var _prevOperation;
var _prevOperationExists;
var _currentNumber;
var _currentNumberExists;

function setGlobalValues(prevResult,currentOperator,prevOperation,currentNumber) {
    _prevResult = prevResult;
    _currentOperator = currentOperator;
    _prevOperation = prevOperation;
    _currentNumber = currentNumber;
}

function setGlobalStates(prevResultExists,currentOperatorExists,prevOperationExists,currentNumberExists){
    _prevResultExists = prevResultExists;
    _currentOperatorExists = currentOperatorExists;
    _prevOperationExists = prevOperationExists;
    _currentNumberExists = currentNumberExists;
}

function setInitialState(){
    setGlobalStates(false,false,false,false);
}

 $('button').click( function(ev) {
    
    var currentButton = $(this).html();
    if (currentButton === '=') {
        handleEquals();
    }else if(currentButton === "C") {
        handleClear();
    }else if($.isNumeric(currentButton)) {
        handleNumber(currentButton);
    }else {
        handleOperation(currentButton);
    }
 });

 function updateDisplay(newVal) {
    $('#display').val(newVal);
    setGlobalValues(_prevResult,_currentOperator,_prevOperation,newVal);
    setGlobalStates(_prevResultExists,_currentOperatorExists,_prevOperationExists,newVal!='');
 }

 function handleClear(){
   updateDisplay(''); 
   setInitialState();
 }

 function handleNumber(numberPressed){
    resetPrevOperation();
    if (_currentNumberExists){
        var prevNumber = $('#display').val();
        numberPressed = prevNumber.concat(numberPressed);
    }
    updateDisplay(numberPressed);
 }

 function handleOperation(operand) {
    resetPrevOperation();
     var result = doOperationAndUpdateDisplay();
     if(result){
        setGlobalStates(true,_currentOperatorExists,_prevOperationExists,_currentNumber);
        setGlobalValues(result,_currentOperator,_prevOperation,_currentNumber); 
     }
     updateOperand(operand);
     setGlobalStates(_prevResultExists,_currentOperatorExists,_prevOperationExists,false); 
 }

 function updateOperand(operand) {
     setGlobalValues(_prevResult,operand,_prevOperation,_currentNumber);
     setGlobalStates(_prevResultExists,true,_prevOperationExists,_currentNumberExists);
 }

 function doOperationAndUpdateDisplay() {
     var result;
     if (_currentNumberExists && _currentOperatorExists && _prevResultExists) {
        result = applyOperator(_prevResult,_currentNumber,_currentOperator).toString();
        updateDisplay(result);
     }else{
        result = _currentNumber;
     }
     return result;
 }

 function applyOperator(a,b,operator){
     a = parseInt(a);
     b = parseInt(b);
     switch (operator) {
        case '+':
            return a + b;
            break;
        case '-':
            return a - b;
            break;
        case '*':
            return a * b;
            break;
        default:
            return a / b;
     }
 }

 function handleEquals(){
    if (_prevOperationExists) {
        var result = applyOperator(_prevResult,_prevOperation[1],_prevOperation[0]);
        updateDisplay(result);
        _prevResult = result;
    }else if (_currentNumberExists){
        var prevOperation = [_currentOperator,_currentNumber];
        var result = doOperationAndUpdateDisplay();
        if (result) {
            setResultAndPrevOperation(result,prevOperation);
        }
    }
 }

 function setResultAndPrevOperation(result,prevOperation) {
     setGlobalStates(true,false,true,false);
     setGlobalValues(result,_currentOperator,prevOperation,_currentNumber);
 }

 function resetPrevOperation(){
   _prevOperationExists = false;
 }