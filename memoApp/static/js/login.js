const cadastroLogin = document.getElementById('cadastro-login');
const modalLogin = document.getElementById('modal-login');
const fechar = document.querySelector(".fechar");
const okModal = document.querySelector('#ok-modal')
const alterarSenha = document.querySelector('#alterar_senha')
const modalSenha = document.getElementById('modal-senha')
const confirmaSenha = document.getElementById('confirma-senha')
const fecharSenha = document.querySelector('#fechar-senha')

alterarSenha.addEventListener('click', function(e){
    e.preventDefault();
    modalSenha.style.display = "block"
})

confirmaSenha.addEventListener('click', function(){
    modalSenha.style.display = "none"
})

fecharSenha.addEventListener('click', function(){
    modalSenha.style.display = "none";
})

cadastroLogin.addEventListener('click', function (e) {
    e.preventDefault();
    modalLogin.style.display = "block";
})


fechar.addEventListener('click', function () {
    modalLogin.style.display = "none";
})

okModal.addEventListener('click', function () {
    modalLogin.style.display = 'none';
})

