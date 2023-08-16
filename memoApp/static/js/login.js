const cadastroLogin = document.getElementById('cadastro-login');
const modalLogin = document.getElementById('modal-login');
const fechar = document.querySelector(".fechar");
const okModal = document.querySelector('#ok-modal')
const alterarSenha = document.querySelector('#alterar_senha')
const modalSenha = document.getElementById('modal-senha')
const confirmaSenha = document.getElementById('confirma-senha')
const fecharSenha = document.querySelector('#fechar-senha')
const mensagemSucesso = document.querySelector('#mensagem_sucesso')
const erroAcontecido = document.querySelector('#erro_acontecido')
const formSenha = document.querySelector('#form-senha')
const errorBox = document.querySelector('#error_box')


try {

    alterarSenha.addEventListener('click', function(e){
        e.preventDefault();
        modalSenha.style.display = "block"
    })
    
    confirmaSenha.addEventListener('click', function(){
        e.preventDefault();
        setTimeout(() => {
            modalSenha.style.display = "none";    
        }, 5000);
        
    })
    
    fecharSenha.addEventListener('click', function(){
        modalSenha.style.display = "none";
    })

    setTimeout(() => {
       errorBox.style.display = "none"; 
    }, 10000);

} catch (error) {
    
}


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

setTimeout(() => {
    mensagemSucesso.style.display = 'none';
}, 10000);

console.log(errorList)
