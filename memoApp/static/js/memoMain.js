const fileInput = document.querySelector('#id_file');
const dropArea = document.getElementById('drop-area');
const inputContainer = document.getElementById('container-file');
const addInputButton = document.getElementById('addInput');
let fileInputs = []; 

dropArea.addEventListener('dragover', handleDragOver);
dropArea.addEventListener('drop', handleFileDrop);

function handleDragOver(event) {
  event.preventDefault();
  dropArea.classList.add('drag-over');
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

  inputRow.classList.add('input-row');
  cancelButton.classList.add('cancel-button');
  cancelButton.type = 'button';
  cancelButton.textContent = 'x';
  newFileInput.type = 'file';
  newFileInput.name = 'file';
  newFileInput.classList.add('file-input');
  newFileInput.multiple = true;
  newFileInput.required = true;

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


function pdfReader(dados) {
  const pdfUrl = dados;
  const canvas = document.getElementById('pdf-canvas');
  const ctx = canvas.getContext('2d');

  pdfjsLib.getDocument(pdfUrl).promise
    .then((pdf) => {
      return pdf.getPage(1);
    })
    .then((page) => {
      const viewport = page.getViewport({ scale: 1 });
      canvas.width = viewport.width;
      canvas.height = viewport.height;

      const renderContext = {
        canvasContext: ctx,
        viewport: viewport,
      };
      return page.render(renderContext);
    })
    .catch((error) => {
      console.error('Erro ao carregar o arquivo PDF:', error);
    });

}

fetch('/digital_view/')
  .then((response) => {
    return response.json()
  })
  .then((dados) => {
    pdfReader(dados)
  })


var fecharMemorando = document.querySelector(".fecharMemorando")
var meuModalmemorando = document.querySelector('#meuModalMemorando')
const btn = document.querySelector('#botao')

botao.addEventListener('click', function (event) {
  event.preventDefault()
  meuModalMemorando.style.display = "block";
})

fecharMemorando.addEventListener('click', function () {
  meuModalmemorando.style.display = "none";
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
  meuModal.style.display = "none";
  form.submit()
})

buttonNoModalMemorando.addEventListener('click', function () {
  meuModalMemorando.style.display = "none";
})