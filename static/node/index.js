var formSearch = document.querySelector("form")
var InputSearch = document.querySelector("input")
var BtnClose = document.querySelectorAll(".close")
var MediaQuery = window.matchMedia("(max-width: 768px)")
var NavbarNav = document.querySelector("#navbarNavDropdown")

console.log(BtnClose)

function mediaQuery() {
    if (mediaQuery.matches) {
      NavbarNav.classList.add('h-all');
      NavbarNav.classList.add("position-absolute")
    } else {
      NavbarNav.classList.remove('h-all');
    }
}

MediaQuery.addEventListener("change", mediaQuery)

InputSearch.addEventListener("input", () => {
    if (!InputSearch.value) {
        BtnClose[0].classList.add("invisible")
    }
    else {
        BtnClose[0].classList.remove("invisible")
    }
})

formSearch.addEventListener("submit", (event) => {
    event.preventDefault()
    if (InputSearch.value.trim()) {
        formSearch.submit()
    }
})

BtnClose[0].addEventListener("click", () => {
    InputSearch.value = null
    BtnClose[0].classList.add("invisible")
})