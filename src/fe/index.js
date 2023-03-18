// turnOn light function
function turnOn() {
  // post the /api/vi/turn_on endpoint
  fetch('/api/v1/turn_on', {
    method: 'POST'
  }).then(function(response) {
    // get the response span
    var responseSpan = document.getElementById(
      'response'
    );
    // set the response span text to the response
    responseSpan.innerText = response;
  }
}
