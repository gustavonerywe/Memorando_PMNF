const buttonConsulta = document.querySelector("#submit-consulta");
const consultaBody = document.querySelector("#consulta-body");
buttonConsulta.addEventListener("click", function(){
    consultaBody.style.height = "auto";
});

const backPage = document.getElementById('backPage');

backPage.addEventListener('click', () =>{
    console.log('oi')
    window.history.back()
})

document.addEventListener("DOMContentLoaded", function () {
    let inputNumero = document.getElementById("numBusca");
    let clearButton = document.getElementById("clearButton");
    let storedNumero = localStorage.getItem("numBusca");
    if (storedNumero) {
        inputNumero.value = storedNumero;
    }

    clearButton.addEventListener("click", function () {
        inputNumero.value = "";
    });
});

document.querySelector("form").addEventListener("submit", function (event) {
    let inputNumero = document.getElementById("numBusca");
    localStorage.setItem("numBusca", inputNumero.value);
});

document.addEventListener("DOMContentLoaded", function () {
    let termoBusca = document.getElementById("termoBusca");
    let removeBusca = document.getElementById("removeBusca");
    let storedTermo = localStorage.getItem("termoBusca");
    if (storedTermo) {
        termoBusca.value = storedTermo;
    }

    removeBusca.addEventListener("click", function () {
        termoBusca.value = "";
    });
});

document.querySelector("form").addEventListener("submit", function (event) {
    let termoBusca = document.getElementById("termoBusca");
    localStorage.setItem("termoBusca", termoBusca.value);
});
