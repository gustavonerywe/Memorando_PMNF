const fileInput = document.querySelector('#id_file')
const dropArea = document.getElementById('drop-area');

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
    fileInput.files = files;
}

// const inputContainer = document.getElementById('input-container');
// const addInputButton = document.getElementById('addInput');

// addInputButton.addEventListener('click', () => {
//     const newInput = document.createElement('input');
//     newInput.type = 'file';
//     newInput.name = 'file';
//     newInput.id = 'id_file';
//     inputContainer.appendChild(document.createElement('br'));
//     inputContainer.appendChild(newInput);

// });

const inputContainer = document.getElementById('container-file');
const addInputButton = document.getElementById('addInput');

function createNewInput() {
  const inputRow = document.createElement('div');
  inputRow.classList.add('input-row');

  const cancelButton = document.createElement('button');
  cancelButton.classList.add('cancel-button');
  cancelButton.textContent = 'x';

  const fileInput = document.createElement('input');
  fileInput.type = 'file';
  fileInput.name = 'file';
  fileInput.classList.add('file-input');
  fileInput.multiple = true;
  fileInput.required = true;

  inputRow.appendChild(cancelButton);
  inputRow.appendChild(fileInput);
  inputContainer.insertBefore(inputRow, addInputButton.parentNode);

  cancelButton.addEventListener('click', function() {
    let conf = confirm('Deseja cancelar o arquivo?');
    if (conf) {
      fileInput.value = '';
    }
  });
}

function addCancelButtonEvent(cancelButton) {
  cancelButton.addEventListener('click', function() {
    let conf = confirm('Deseja cancelar o arquivo?');
    if (conf) {
      const fileInput = cancelButton.nextElementSibling;
      fileInput.value = '';
    }
  });
}

addInputButton.addEventListener('click', function() {
  createNewInput();
  const cancelButtons = document.querySelectorAll('.cancel-button');
  cancelButtons.forEach(function(cancelButton) {
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

const btn = document.querySelector('#botao')

botao.addEventListener('click', function (event) {
    event.preventDefault()

    let confirmed = confirm('Deseja mesmo enviar o formulário?')
    if (confirmed) {
        event.target.closest('form').submit()
    }
})

// let cancelElement = document.querySelector('#cancel-button')

// fileInput.parentNode.insertBefore(cancelElement, fileInput.nextSibling)

// cancelElement.addEventListener('click', function(){
//     let conf = confirm('Deseja cancelar o arquivo?')
//     if(conf){
//         fileInput.value = ''
//     }
// })