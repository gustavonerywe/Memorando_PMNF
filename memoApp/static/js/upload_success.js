const linkUpload = document.getElementById('link-upload');
const uploadModal = document.getElementById('modal-upload');
const enviaModal = document.getElementById('envia-modal');
const naoEnviaModal = document.getElementById('nao-envia-modal');
const fechar = document.querySelector(".fechar");

linkUpload.addEventListener('click', function(e){
    e.preventDefault();
    uploadModal.style.display = "block";
})

naoEnviaModal.addEventListener('click', function(){
    uploadModal.style.display = "none";
})

enviaModal.addEventListener('click', function(){
    uploadModal.style.display = "none";
    window.location.href = "/";
})

fechar.addEventListener('click', function(){
    uploadModal.style.display = "none";
})

const linkUploadPdf = document.getElementById('link-upload-pdf')
const ModalPdf = document.getElementById('modal-pdf')
const okPdf = document.querySelector('#ok-modal-pdf')
const fecharPdf = document.querySelector('.fechar-pdf')
const dotContainer = document.querySelector('#dot-container')
const imgCheck = document.querySelector('#check-img')

linkUploadPdf.addEventListener('click', function(e){
    ModalPdf.style.display = 'block'
    console.log(ModalPdf)
    setInterval(() => {
        dotContainer.style.display = "none";
    }, 7300);
    setTimeout(() => {
        imgCheck.style.display = "flex";
    }, 7300);
})

fecharPdf.addEventListener('click', function(){
    imgCheck.style.display = "none";
    dotContainer.style.display = "flex";
    ModalPdf.style.display = 'none'
})

okPdf.addEventListener('click', function(){
    imgCheck.style.display = "none";
    dotContainer.style.display = "flex";
    ModalPdf.style.display = 'none'
})

const buttonYesSair = document.querySelector('#buttonYesSair')
const buttonNoSair = document.querySelector('#buttonNoSair')
const modalSair = document.querySelector('#modal-sair')
const btnTrueSair = document.querySelector('#link-upload-sair')
const fecharSair = document.querySelector('.fechar-sair')

modalSair.style.display = 'none';

btnTrueSair.addEventListener('click', function (e) {
  e.preventDefault();
  modalSair.style.display = 'block';
})  

buttonNoSair.addEventListener('click', function(){
  modalSair.style.display = 'none';
})

buttonYesSair.addEventListener('click', function(){
    window.location.href = '/encerrar-sessao/'
})

fecharSair.addEventListener('click', function(){
  modalSair.style.display = 'none';
})