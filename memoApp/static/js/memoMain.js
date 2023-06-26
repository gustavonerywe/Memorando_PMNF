const fileInput = document.querySelector('#id_file');
const dropArea = document.getElementById('drop-area');
const inputContainer = document.getElementById('container-file');
const addInputButton = document.getElementById('addInput');
const fechar = document.querySelector('.fechar');
const removeDiv = document.querySelector('.input-row');
let fileInputs = [];

dropArea.addEventListener('dragover', handleDragOver);
dropArea.addEventListener('drop', handleFileDrop);

function handleDragOver(event) {
  event.preventDefault();
  console.log('File drop event');
  dropArea.classList.remove('drag-over');
  const files = event.dataTransfer.files;
  console.log('Dropped files:', files);
}

function handleFileDrop(event) {
  event.preventDefault();
  dropArea.classList.remove('drag-over');
  const files = event.dataTransfer.files;
  if (fileInputs.length > 0) {
    const lastFileInput = fileInputs[fileInputs.length - 1];
    lastFileInput.files = files;
  } else {
    fileInput.files = files;
  }
}

let selectCounterCopia = 1;

document.addEventListener('DOMContentLoaded', function () {

  function removeLastSelectCopia(){
    if(selectCounterCopia>1){
      let elementRemovido = document.getElementById('select-container-copia-'+selectCounterCopia);
      let removeBotao = document.getElementById('removeSelectCopia');

      console.log(elementRemovido);
      elementRemovido.remove();
      selectCounterCopia--;
            
      if(selectCounterCopia == 1){
        removeBotao.remove();
      }
    }
  }

  function createNewSelectCopia() {
    let selectOriginal = document.getElementById('select-secretaria-copia-para');
    let selectClone = selectOriginal.cloneNode(true);
    let novoWrapper = document.createElement('div');
    let selectTable = document.getElementById('select-table-copia');

    if(selectCounterCopia == 1){
      let removeSelect = document.createElement('button');
      let icone = document.createElement('i');
      icone.classList.add('bi' , 'bi-dash');
      removeSelect.appendChild(icone);
      let container = document.getElementById('container_and_button-copia');

      container.appendChild(removeSelect);
      removeSelect.id = 'removeSelectCopia';
      removeSelect.innerHTML = "REMOVER";
      removeSelect.type = 'button';

      removeSelect.addEventListener('click', function(){
        removeLastSelectCopia();
      })
    }

    selectCounterCopia++;
    novoWrapper.setAttribute('class', 'select-wrapper-copia');
    novoWrapper.id = 'select-container-copia-' + selectCounterCopia;
    selectTable.appendChild(novoWrapper)


    selectClone.id = 'select-secretaria-copia-' + selectCounterCopia;
    selectClone.setAttribute('data-select2-id', selectClone.id);
    selectClone.style.width = '100%';

    novoWrapper.appendChild(selectClone);
    $(selectClone).select2();
  }
  const addSelectButtonCopia = document.getElementById('addSelectCopia')

  addSelectButtonCopia.addEventListener('click', () => {
    createNewSelectCopia()
  })
})
let selectCounter = 1;

document.addEventListener('DOMContentLoaded', function () {

  function removeLastSelect(){
    if(selectCounter>1){
      let elementRemovido = document.getElementById('select-container-'+selectCounter);
      let removeBotao = document.getElementById('removeSelect');

      elementRemovido.remove();
      selectCounter--;
            
      if(selectCounter == 1){
        removeBotao.remove();
      }
      
    }
  }

  function createNewSelect() {
    let selectOriginal = document.getElementById('select-secretaria');
    let selectClone = selectOriginal.cloneNode(true);
    let novoWrapper = document.createElement('div');
    let selectTable = document.getElementById('select-table');

    if(selectCounter == 1){
      let removeSelect = document.createElement('button');
      let container = document.getElementById('container_and_button');

      container.appendChild(removeSelect);
      removeSelect.id = 'removeSelect';
      removeSelect.innerHTML = "REMOVER";
      removeSelect.type = 'button';

      removeSelect.addEventListener('click', function(){
        removeLastSelect();
      })
    }

    selectCounter++;

    novoWrapper.setAttribute('class', 'select-wrapper');
    novoWrapper.id = 'select-container-' + selectCounter;
    selectTable.appendChild(novoWrapper)

    selectClone.id = 'select-secretaria-' + selectCounter;
    selectClone.setAttribute('data-select2-id', selectClone.id);
    selectClone.style.width = '100%';

    novoWrapper.appendChild(selectClone);
    $(selectClone).select2();
    $(selectClone).val(null);
    selectClone.selectedIndex = 0;
  }


  const addSelectButton = document.getElementById('addSelect');
  addSelectButton.addEventListener('click', function () {
    createNewSelect();
    // const newSelect = createNewSelect()
    // console.log(document.getElementById('selectFather').innerHTML = newSelect)
  });
})

function createNewInput() {
  const inputRow = document.createElement('div');
  const cancelButton = document.createElement('button');
  const newFileInput = document.createElement('input');
  let imgRemove = document.createElement('img');
  let widthInput = document.getElementById('id_file').width;

  inputRow.classList.add('input-row');
  cancelButton.classList.add('cancel-button');
  cancelButton.type = 'button';
  cancelButton.id = 'cancel-button-dynamic'
  imgRemove.setAttribute('class', 'img-remove');
  imgRemove.src = '/static/img/lixo.png';
  imgRemove.alt = 'remove';
  newFileInput.type = 'file';
  newFileInput.name = 'file';
  // newFileInput.style.margin = '15px'
  // newFileInput.style.width = '100%';
  newFileInput.classList.add('form-control', 'form-control-sm');
  newFileInput.classList.add('file-input');
  newFileInput.multiple = true;
  newFileInput.required = false;


  cancelButton.appendChild(imgRemove);
  inputRow.appendChild(cancelButton);
  inputRow.appendChild(newFileInput);
  inputContainer.appendChild(inputRow);

  fileInputs.push(newFileInput)

  cancelButton.addEventListener('click', function () {
    if (fileInput != null) {
      meuModal.style.display = "block";
    }
  });

  fechar.addEventListener("click", function () {
    meuModal.style.display = "none";
  });

  window.addEventListener("click", function (event) {
    if (event.target == meuModal) {
      meuModal.style.display = "none";
    }
  });
}

function addCancelButtonEvent(cancelButton) {
  cancelButton.type = 'button';
  cancelButton.addEventListener('click', function () {
    console.log(fileInput.value)
    if (cancelButton.parentNode == document.getElementById('div-anexo-orig')) {
      if (fileInput.value != '') {
        meuModal.style.display = "block";
        buttonYesModal.addEventListener('click', function () {
          setTimeout(function () {
            fileInput.value = '';
          }, 100);
          meuModal.style.display = 'none';
        }
        )
      }
      return;
    } else {
      meuModal.style.display = "block";
      buttonYesModal.addEventListener('click', function () {
        const correspondingInput = cancelButton.nextSibling;
        setTimeout(function () {
          correspondingInput.parentNode.remove();
        }, 100);
        // correspondingInput.value = '';
        // meuModal.style.display = "none";
        // setTimeout(function () {
        //   correspondingInput.remove()
        //   document.getElementById('cancel-button-dynamic').remove()
        // }, 100)
        spanMessage.textContent = "Arquivo removido com sucesso!";
        setTimeout(function () {
          spanMessage.textContent = '';
        }, 2500)
      })
    }
  });

  fechar.addEventListener("click", function () {
    meuModal.style.display = "none";
  });

  window.addEventListener("click", function (event) {
    if (event.target == meuModal) {
      meuModal.style.display = "none";
    }
  });
}

addInputButton.addEventListener('click', function () {
  createNewInput();
  const cancelButtons = document.querySelectorAll('.cancel-button');
  cancelButtons.forEach(function (cancelButton) {
    addCancelButtonEvent(cancelButton);
  });
});

const firstCancelButton = document.querySelector('.cancel-button');
addCancelButtonEvent(firstCancelButton);


// function pdfReader(dados) {
//   const pdfUrl = dados;
//   const canvas = document.getElementById('pdf-canvas');
//   const ctx = canvas.getContext('2d');

//   pdfjsLib.getDocument(pdfUrl).promise
//     .then((pdf) => {
//       return pdf.getPage(1);
//     })
//     .then((page) => {
//       const viewport = page.getViewport({ scale: 1 });
//       canvas.width = viewport.width;
//       canvas.height = viewport.height;

//       const renderContext = {
//         canvasContext: ctx,
//         viewport: viewport,
//       };
//       return page.render(renderContext);
//     })
//     .catch((error) => {
//       console.error('Erro ao carregar o arquivo PDF:', error);
//     });

// }

// fetch('/digital_view/')
//   .then((response) => {
//     return response.json()
//   })
//   .then((dados) => {
//     pdfReader(dados)
//   })


let fecharMemorando = document.querySelector(".fecharMemorando")
let meuModalMemorando = document.querySelector('#meuModalMemorando')
const btn = document.querySelector('#botao')
let corpoMemo = document.getElementById('corpo');
const valorSelect = document.getElementById('select-secretaria')

botao.addEventListener('click', function (event) {
  event.preventDefault()
  meuModalMemorando.style.display = "block";
  if (assunto.value.trim() === '') {
    meuModalMemorando.style.display = 'none';
    modalAssunto.style.display = 'block';
    pegarLugarTexto.innerHTML = " 'Assunto'";
  }
  else if (valorSelect.value.trim() === '-- Selecione um grupo --') {
    meuModalMemorando.style.display = 'none';
    modalAssunto.style.display = 'block';
    pegarLugarTexto.innerHTML = " 'Para'";
  }


  console.log(corpoMemo)
  // if (campoSelect.value.trim() !== valorSelect.value.trim() && assunto.value.trim() !== '') {
  //   return;
  // }
  // else if (assunto.value.trim() === '' || valorSelect.value.trim() === '-- Selecione um grupo --') {
  //   meuModalMemorando.style.display = 'none';
  //   modalAssunto.style.display = 'block';
  //   pegarLugarTexto.innerHTML = " 'Assunto' ";
  //   pegarLugarTextoPara.innerHTML = " 'Para' "
  //   return;
  // }
  // else if()
})

fecharMemorando.addEventListener('click', function () {
  meuModalMemorando.style.display = "none";
})

window.addEventListener("click", function (event) {
  if (event.target == meuModalMemorando) {
    meuModalMemorando.style.display = "none";
  }
});


const buttonYesModal = document.querySelector('#buttonYesModal')
const buttonNoModal = document.querySelector('#buttonNoModal')
const buttonYesModalMemorando = document.querySelector('#buttonYesModalMemorando')
const buttonNoModalMemorando = document.querySelector('#buttonNoModalMemorando')
const spanMessage = document.querySelector('#spanMessage')
const form = document.querySelector('#form-main')
const assunto = document.querySelector('#id_name')
const modalAssunto = document.querySelector('#meuModalAssunto')
const fecharModalAssunto = document.querySelector('#ok-modal')
const fecharModalAsssunto2 = document.getElementById('botaoFechar');
const campoSelect = document.getElementById('select-secretaria');
const pegarLugarTexto = document.getElementById('texto-colocar')
const pegarLugarTextoPara = document.getElementById('texto-colocar-para')
const grupoSelected = document.getElementById('grupo_selected')

buttonYesModal.addEventListener('click', function () {
  document.querySelector('.file-input').value = '';
  meuModal.style.display = "none";
  spanMessage.textContent = "Arquivo removido com sucesso!"
  setTimeout(function () {
    spanMessage.textContent = ''
  }, 2500)
})

buttonNoModal.addEventListener('click', function () {
  meuModal.style.display = "none";
})

buttonYesModalMemorando.addEventListener('click', function () {
  modalAssunto.style.display = 'none';
  form.submit()
});

buttonNoModalMemorando.addEventListener('click', function () {
  meuModalMemorando.style.display = "none";
})
/*$(document).ready(function() {
  $('.meu-js').select2();
});*/

fecharModalAssunto.addEventListener('click', function () {
  modalAssunto.style.display = 'none';
})
fecharModalAsssunto2.addEventListener('click', function () {
  modalAssunto.style.display = 'none';
})