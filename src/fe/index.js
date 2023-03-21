// turnOn light function
function turnOn() {
  // post the /api/vi/turn_on endpoint
  fetch('/api/v1/turn_on', {
    method: 'POST'
  }).then(function(response) {
    // get the response span
    var responseSpan = document.getElementById(
      'turn-on-response'
    );
    // set the response span text to the response text content
    // don't forget to get the result of the promise
    response.text().then(function(text) {
      responseSpan.textContent = text;
    })

  })
}

// get status function, from /api/v1/status
function getStatus() {
  // post the /api/vi/turn_on endpoint
  fetch('/api/v1/status', {
    method: 'GET'
  }).then(function(response) {
    // get the response span
    var responseSpan = document.getElementById(
      'status-response'
    );
    // set the response span text to the response text content
    // don't forget to get the result of the promise
    response.json().then(function(obj) {
      responseSpan.textContent = obj.colour;

    })

  })
}

// turnOff light function
function turnOff() {
  // post the /api/vi/turn_on endpoint
  fetch('/api/v1/turn_off', {
    method: 'POST'
  }).then(function(response) {
    // get the response span
    var responseSpan = document.getElementById(
      'turn-off-response'
    );
    // set the response span text to the response text content
    // don't forget to get the result of the promise
    response.text().then(function(text) {
      responseSpan.textContent = text;
    })

  })
}
