const fileInput = document.querySelector('#id_file');
const dropArea = document.getElementById('drop-area');
const inputContainer = document.getElementById('container-file');
const addInputButton = document.getElementById('addInput');
const fechar = document.querySelector('.fechar')
const removeDiv = document.querySelector('.input-row')
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

function createNewInput() {
  const inputRow = document.createElement('div');
  const cancelButton = document.createElement('button');
  const newFileInput = document.createElement('input');
  var imgRemove = document.createElement('img')

  inputRow.classList.add('input-row');
  cancelButton.classList.add('cancel-button');
  cancelButton.type = 'button';
  cancelButton.id = 'cancel-button-dynamic'
  imgRemove.id = 'img-remove';
  imgRemove.src = 'https://pedroschuenck.github.io/bin.png';
  imgRemove.alt = 'remove';
  newFileInput.type = 'file';
  newFileInput.name = 'file';
  newFileInput.style.margin = '15px'
  newFileInput.style.width = '105%'
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
    meuModal.style.display = "block";
    buttonYesModal.addEventListener('click', function () {
      const correspondingInput = cancelButton.nextSibling;
      correspondingInput.value = '';
      meuModal.style.display = "none";
      setTimeout(function () {
        correspondingInput.remove()
        document.getElementById('cancel-button-dynamic').remove()
      }, 100)
      spanMessage.textContent = "Arquivo removido com sucesso!";
      setTimeout(function () {
        spanMessage.textContent = '';
      }, 2500)
    })
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


var fecharMemorando = document.querySelector(".fecharMemorando")
var meuModalMemorando = document.querySelector('#meuModalMemorando')
const btn = document.querySelector('#botao')

botao.addEventListener('click', function (event) {
  event.preventDefault()
  meuModalMemorando.style.display = "block";
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

buttonYesModalMemorando.addEventListener('click', function() {
  meuModal.style.display = 'none';
  if (assunto.value.trim() === '') {
    alert('Por favor, preencha o campo assunto.');
    return;
  }
  form.submit();
});

buttonNoModalMemorando.addEventListener('click', function () {
  meuModalMemorando.style.display = "none";
})
/*$(document).ready(function() {
  $('.meu-js').select2();
});*/
