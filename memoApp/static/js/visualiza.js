const linkUploadPdf = document.getElementById('baixa-pdf-visualiza')
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