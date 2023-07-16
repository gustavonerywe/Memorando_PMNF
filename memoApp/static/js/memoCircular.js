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

  function removeLastSelectCopia() {
    if (selectCounterCopia > 1) {
      let elementRemovido = document.getElementById('select-container-copia-' + selectCounterCopia);
      let removeBotao = document.getElementById('removeSelectCopia');

      elementRemovido.remove();
      selectCounterCopia--;

      if (selectCounterCopia == 1) {
        removeBotao.remove();
      }
    }
  }

  function createNewSelectCopia() {
    let selectOriginal = document.getElementById('select-secretaria-copia-para');
    let novoWrapper = document.createElement('div');
    let selectTable = document.getElementById('select-table-copia');

    if (selectCounterCopia == 1) {
      let removeSelect = document.createElement('button');
      removeSelect.setAttribute('class', 'cancel-button-select');
      let tagIcone = document.createElement('i');
      tagIcone.setAttribute('class', 'bi bi-dash');
      removeSelect.appendChild(tagIcone);
      let container = document.getElementById('container_and_button-copia');
      container.appendChild(removeSelect);

      removeSelect.id = 'removeSelectCopia';
      removeSelect.type = 'button';

      removeSelect.addEventListener('click', function () {
        removeLastSelectCopia();
      });
    }

    selectCounterCopia++;

    let novoSelect = document.createElement('select');
    novoSelect.name = 'destinatarios_copia';
    novoSelect.id = 'select-secretaria-copia-' + selectCounterCopia;
    novoSelect.style.width = '100%';

    // Adicionar classes do Bootstrap ao novo select
    novoSelect.classList.add('form-control');

    novoWrapper.setAttribute('class', 'select-wrapper-copia');
    novoWrapper.id = 'select-container-copia-' + selectCounterCopia;
    novoWrapper.appendChild(novoSelect);
    selectTable.appendChild(novoWrapper);

    // Clone as opções do select original para o novo select
    let options = selectOriginal.options;
    for (let i = 0; i < options.length; i++) {
      let option = document.createElement('option');
      option.value = options[i].value;
      option.text = options[i].text;
      novoSelect.appendChild(option);
    }
    $(novoSelect).select2();
  }


  let selectCounterCopia = 1;

  document.addEventListener('DOMContentLoaded', function () {
    const addSelectButtonCopia = document.getElementById('addSelectCopia');
    addSelectButtonCopia.addEventListener('click', createNewSelectCopia);
  });

  const addSelectButtonCopia = document.getElementById('addSelectCopia')

  addSelectButtonCopia.addEventListener('click', () => {
    createNewSelectCopia()
  })
})
let selectCounter = 1;

document.addEventListener('DOMContentLoaded', function () {

  function removeLastSelect() {
    if (selectCounter > 1) {
      let elementRemovido = document.getElementById('select-container-' + selectCounter);
      let removeBotao = document.getElementById('removeSelect');

      elementRemovido.remove();
      selectCounter--;

      if (selectCounter == 1) {
        removeBotao.remove();
      }

    }
  }

  function createNewSelect() {
    let selectOriginal = document.getElementById('select-secretaria');
    let novoWrapper = document.createElement('div');
    let selectTable = document.getElementById('select-table');

    if (selectCounter == 1) {
      let removeSelect = document.createElement('button');
      let container = document.getElementById('container_and_button');
      removeSelect.setAttribute('class', 'cancel-button-select')
      let tagIcone = document.createElement('i');
      tagIcone.setAttribute('class', 'bi bi-dash');
      removeSelect.appendChild(tagIcone);

      container.appendChild(removeSelect);
      removeSelect.id = 'removeSelect';
      //removeSelect.innerHTML = "REMOVER";
      removeSelect.type = 'button';

      removeSelect.addEventListener('click', function () {
        removeLastSelect();
      })
    }

    selectCounter++;

    let novoSelect = document.createElement('select');
    novoSelect.name = 'destinatarios_copia';
    novoSelect.id = 'select-secretaria-copia-' + selectCounter;
    novoSelect.style.width = '100%';

    novoSelect.classList.add('form-control');

    novoWrapper.setAttribute('class', 'select-wrapper-copia');
    novoWrapper.id = 'select-container-copia-' + selectCounter;
    novoWrapper.appendChild(novoSelect);
    selectTable.appendChild(novoWrapper);

    // Clone as opções do select original para o novo select
    let options = selectOriginal.options;
    for (let i = 0; i < options.length; i++) {
      let option = document.createElement('option');
      option.value = options[i].value;
      option.text = options[i].text;
      novoSelect.appendChild(option);
    }
    $(novoSelect).select2();
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
  // let widthInput = document.getElementById('id_file').width;
  newFileInput.setAttribute('id', 'id_file');

  inputRow.classList.add('input-row');
  cancelButton.classList.add('cancel-button');
  cancelButton.type = 'button';
  cancelButton.id = 'cancel-button-dynamic'
  cancelButton.setAttribute('class', 'bi bi-dash cancel-button')
  newFileInput.type = 'file';
  newFileInput.name = 'file';
  // newFileInput.style.margin = '15px'
  // newFileInput.style.width = '100%';
  newFileInput.setAttribute('id', 'id_file');
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
        meuModal.style.display = "none";
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
const buttonYesSair = document.querySelector('#buttonYesSair')
const buttonNoSair = document.querySelector('#buttonNoSair')
const modalSair = document.querySelector('#modal-sair')
const btnTrueSair = document.querySelector('#btnTrueSair')
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


// buttonYesModal.addEventListener('click', function () {
//   document.querySelector('.file-input').value = '';
//   meuModal.style.display = "none";
//   spanMessage.textContent = "Arquivo removido com sucesso!"
//   setTimeout(function () {
//     spanMessage.textContent = ''
//   }, 2500)
// })

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

const btnTroca = document.querySelector('#btnTroca')
const modalTrocar = document.getElementById('modal-trocar')
const fecharTroca = document.querySelector('.fechar-trocar')
const memorandoComum = document.getElementById('memorandoComum')
const memorandoCircular = document.getElementById('memorandoCircular')
const oficio = document.getElementById('oficio')
const messageAviso = document.getElementById('message-aviso')

btnTroca.addEventListener('click', function(e){
  e.preventDefault();
  modalTrocar.style.display = 'block';
  messageAviso.style.display = 'none';
})

fecharTroca.addEventListener('click', function(){
  modalTrocar.style.display = 'none'
})

memorandoComum.addEventListener('click', function(){
  messageAviso.style.display = 'block'
  messageAviso.innerHTML = "Carregando..."
  setTimeout(function(){
    modalTrocar.style.display = 'none';
  }, 1500)
})

memorandoCircular.addEventListener('click', function(){
  messageAviso.style.display = 'block'
  messageAviso.innerHTML = "Carregando..."
  setTimeout(() => {
    window.location.href = '/memorando_circular'
  }, 1500);
})