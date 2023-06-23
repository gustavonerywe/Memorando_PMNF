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


// buttonNoModal.addEventListener('click', function () {
//     meuModal.style.display = "none";
//   })
  
//   buttonYesModalMemorando.addEventListener('click', function () {
//     modalAssunto.style.display = 'none';
//     form.submit()
//   });

// botao.addEventListener('click', function (event) {
//     event.preventDefault()
//     meuModalMemorando.style.display = "block";
//     if (assunto.value.trim() === '') {
//       meuModalMemorando.style.display = 'none';
//       modalAssunto.style.display = 'block';
//       pegarLugarTexto.innerHTML = " 'Assunto'";
//     }
//     else if (valorSelect.value.trim() === '-- Selecione um grupo --') {
//       meuModalMemorando.style.display = 'none';
//       modalAssunto.style.display = 'block';
//       pegarLugarTexto.innerHTML = " 'Para'";
//     }
  
//     console.log(corpoMemo)
//     // if (campoSelect.value.trim() !== valorSelect.value.trim() && assunto.value.trim() !== '') {
//     //   return;
//     // }
//     // else if (assunto.value.trim() === '' || valorSelect.value.trim() === '-- Selecione um grupo --') {
//     //   meuModalMemorando.style.display = 'none';
//     //   modalAssunto.style.display = 'block';
//     //   pegarLugarTexto.innerHTML = " 'Assunto' ";
//     //   pegarLugarTextoPara.innerHTML = " 'Para' "
//     //   return;
//     // }
//     // else if()
//   })