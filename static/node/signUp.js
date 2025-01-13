document.querySelectorAll(".invalid-feedback").forEach(function(spans) {
    if (spans.innerHTML.trim()) {
        if (spans.parentElement.querySelector("input")) {
            spans.parentElement.querySelector("input").classList.add("is-invalid")
        }
    }
    else {
        spans.parentElement.querySelector("input").classList.remove("is-invalid")
    }
})

document.querySelector("form").addEventListener("submit", function (events) {
    events.preventDefault();
    events.stopPropagation();
    document.querySelectorAll("input").forEach(function(inputs) {
        if (inputs.type === "checkbox") {
            if (inputs.checked) {
                inputs.classList.remove("is-invalid")
                inputs.parentElement.querySelector(".invalid-feedback") ? inputs.parentElement.querySelector(".invalid-feedback").innerHTML = null : null
            }
            else {
                inputs.classList.add("is-invalid")
                inputs.parentElement.querySelector(".invalid-feedback") ? inputs.parentElement.querySelector(".invalid-feedback").innerHTML = `You must agree before submitting.` : null
            }
        }
        else {
            if (!inputs.value.trim()) {
              inputs.classList.add("is-invalid")
              
              if (inputs.parentElement.querySelector(".invalid-feedback")) {
                  inputs.parentElement.querySelector(".invalid-feedback").innerHTML = `This ${inputs.name} is null.`
              }
        }
            else if (!inputs.checkValidity()) {
                inputs.classList.add("is-invalid")
                if (inputs.parentElement.querySelector(".invalid-feedback")) {
                    inputs.parentElement.querySelector(".invalid-feedback").innerHTML = `This ${inputs.name} is invalid.`
                }
        }
            else {
                inputs.classList.remove("is-invalid")
                if (inputs.parentElement.querySelector(".invalid-feedback")) {
                    inputs.parentElement.querySelector(".invalid-feedback").innerHTML = null
                }
        }
        }
    })
    this.checkValidity() ? this.submit() : null
})