function appendToResult(value) {
    var result = document.getElementById("result");
    result.value += value;
  }
  
  function clearResult() {
    var result = document.getElementById("result");
    result.value = "";
  }
  
  function deleteLastChar() {
    var result = document.getElementById("result");
    result.value = result.value.slice(0, -1);
  }
  
  function evaluateExpression() {
    var result = document.getElementById("result");
    try {
      result.value = eval(result.value);
    } catch (error) {
      result.value = "Error";
    }
  }