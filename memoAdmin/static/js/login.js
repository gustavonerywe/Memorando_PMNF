const cadastroLogin = document.getElementById('cadastro-login');
const modalLogin = document.getElementById('modal-login');
const fechar = document.querySelector(".fechar");
const okModal = document.querySelector('#ok-modal')


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
