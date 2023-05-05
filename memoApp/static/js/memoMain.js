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

function pdfReader(dados) {
    // Seu código JavaScript
    const pdfUrl = dados;
    const canvas = document.getElementById('pdf-canvas');
    const ctx = canvas.getContext('2d');

    // Carrega o arquivo PDF
    pdfjsLib.getDocument(pdfUrl).promise
        .then((pdf) => {
            // Carrega a primeira página do PDF
            return pdf.getPage(1);
        })
        .then((page) => {
            // Calcula as dimensões do canvas para caber a página inteira do PDF
            const viewport = page.getViewport({ scale: 1 });
            canvas.width = viewport.width;
            canvas.height = viewport.height;

            // Renderiza a página do PDF no canvas
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

botao.addEventListener('click', function(event){
    event.preventDefault()

    let confirmed = confirm('Deseja mesmo enviar o formulário?')
    if(confirmed){
        event.target.closest('form').submit()
    } 
})