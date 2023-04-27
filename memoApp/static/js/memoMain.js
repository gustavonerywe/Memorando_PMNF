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

const inputContainer = document.getElementById('input-container');
const addInputButton = document.getElementById('addInput');

addInputButton.addEventListener('click', () => {
    const newInput = document.createElement('input');
    newInput.type = 'file';
    newInput.name = 'file';
    newInput.id = 'id_file'; 
    inputContainer.appendChild(document.createElement('br'));
    inputContainer.appendChild(newInput);

});

