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
    window.location.href = "/oficio";
})

fechar.addEventListener('click', function(){
    uploadModal.style.display = "none";
})

const linkUploadPdf = document.getElementById('link-upload-pdf')
const ModalPdf = document.getElementById('modal-pdf')
const okPdf = document.querySelector('#ok-modal-pdf')
const fecharPdf = document.querySelector('.fechar-pdf')

linkUploadPdf.addEventListener('click', function(e){
    ModalPdf.style.display = 'block'
})

fecharPdf.addEventListener('click', function(){
    ModalPdf.style.display = 'none'
})

okPdf.addEventListener('click', function(){
    ModalPdf.style.display = 'none'
})