const buttonConsulta = document.querySelector("#submit-consulta");
const consultaBody = document.querySelector("#consulta-body");
buttonConsulta.addEventListener("click", function(){
    consultaBody.style.height = "auto";
});

const backPage = document.getElementById('backPage');

backPage.addEventListener('click', () =>{
    window.history.back()
})

