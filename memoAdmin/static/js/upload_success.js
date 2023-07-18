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
