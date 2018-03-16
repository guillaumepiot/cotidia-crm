'use strict';

(function () {

  function send (elm, data) {
    setLoading(elm)

    var xhr = new XMLHttpRequest()

    xhr.onerror = function (e) {
      console.error('Error sending.')
    }

    xhr.onload = function () {
      unsetLoading(elm)

      if(xhr.status === 400) {
        var errorData = JSON.parse(xhr.responseText)
        clearFormError(elm)
        for (var key in errorData) {
          if (errorData.hasOwnProperty(key)) {
              displayFieldError(elm, key, errorData[key])
          }
        }
      }

      if(xhr.status >= 200 && xhr.status < 300) {
        elm.reset()
        clearFormError(elm)
        var successData = JSON.parse(xhr.responseText)
        var successNode = document.createElement("div")
        successNode.className = 'alert alert--success'
        successNode.innerHTML = successData['message']
        elm.prepend(successNode)
      }

    };

    xhr.open('POST', elm.dataset.url)
    xhr.send(data)
  }

  function clearFormError (elm) {
    elm.querySelectorAll('.form__group--error').forEach(function (group) {
      group.classList.remove('form__group--error')
      var errorNode = group.querySelector(".form__help")
      // Save original help text
      errorNode.innerHTML = errorNode.dataset.help
    })
  }

  function displayFieldError (elm, field, error_message){
    var formField = elm.querySelector('[name=' + field + ']')
    // Add error class
    while (!formField.classList.contains('form__group')) {
      formField = formField.parentNode
    }
    formField.classList.add('form__group--error')
    // Display error
    var errorNode = formField.querySelector(".form__help")
    // Save original help text
    errorNode.dataset.help = errorNode.innerHTML
    errorNode.innerHTML = error_message[0]
    formField.appendChild(errorNode)
  }

  function setLoading (elm) {
    elm.querySelector('[type=submit]').classList.add('btn--loading')
  }

  function unsetLoading (elm) {
    elm.querySelector('[type=submit]').classList.remove('btn--loading')
  }

  /////////////////////////////////////////////////////////////////////////////

  // Bootstrap any file uploaders

  function documentReady () {
    return (document.readyState === 'interactive' || document.readyState === 'complete')
  }

  function bootstrap () {
    document.removeEventListener('readystatechange', bootstrap)

    document.querySelectorAll("form.enquiry-form").forEach(function (elm) {
      elm.addEventListener("submit", function (e) {
        e.preventDefault()
        var formData = new FormData(elm)
        send(elm, formData)
      })
    })

  }

  if (documentReady()) {
    bootstrap()
  } else {
    document.addEventListener('readystatechange', bootstrap)
  }
})()
