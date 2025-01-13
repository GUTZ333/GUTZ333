document.querySelector(".error-db").innerHTML.trim() ? document.querySelector(".alert").classList.remove("d-none") : null
document.querySelector("form").addEventListener("submit", function(events) {
    events.preventDefault();
    events.stopPropagation();
    document.querySelectorAll("input").forEach(function(inputs) {
        !inputs.value.trim() ? inputs.classList.add("is-invalid") : inputs.classList.remove("is-invalid")
    })
    this.checkValidity() ? this.submit() : null
})