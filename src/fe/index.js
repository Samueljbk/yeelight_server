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
      responseSpan.textContent = obj;

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

// setColour light function
function setColour() {
  // get the rgb colour values from the 3 input fields
  var red = document.getElementById('red').value;
  var green = document.getElementById('green').value;
  var blue = document.getElementById('blue').value;

  var colour = [red, green, blue];

  // post the /api/vi/set_colour endpoint
  fetch('/api/v1/set_colour', {
    method: 'POST',
    body: JSON.stringify(colour)
  }).then(function(response) {
    // get the response span
    var responseSpan = document.getElementById(
      'set-colour-response'
    );
    // set the response span text to the response text content
    // don't forget to get the result of the promise
    response.text().then(function(text) {
      responseSpan.textContent = text;
    })

  })
}

// setBrightness light function
function setBrightness() {
  // get the brightness value from the input field
  var brightness = document.getElementById('brightness').value;

  // post the /api/vi/set_brightness endpoint
  fetch('/api/v1/set_brightness', {
    method: 'POST',
    body: JSON.stringify(brightness)
  }).then(function(response) {
    // get the response span
    var responseSpan = document.getElementById(
      'set-brightness-response'
    );
    // set the response span text to the response text content
    // don't forget to get the result of the promise
    response.text().then(function(text) {
      responseSpan.textContent = text;
    })

  })
}
