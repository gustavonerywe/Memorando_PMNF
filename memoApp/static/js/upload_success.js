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
const imgContainer = document.querySelector('#image-container')

linkUploadPdf.addEventListener('click', function(e){
    ModalPdf.style.display = 'block'
    console.log(ModalPdf)
    setInterval(() => {
        dotContainer.remove();
    }, 7300);
    setTimeout(() => {
        imgContainer.style.display = 'block';
        const imgCreate = document.createElement('img')
        imgCreate.src = '/static/img/check.png';
        imgCreate.alt = "check-img";
        imgCreate.width = 30;
        imgCreate.height = 30;
        imgContainer.appendChild(imgCreate)
        console.log(imgCreate)
    }, 7300);
})

fecharPdf.addEventListener('click', function(){
    ModalPdf.style.display = 'none'
})

okPdf.addEventListener('click', function(){
    ModalPdf.style.display = 'none'
})