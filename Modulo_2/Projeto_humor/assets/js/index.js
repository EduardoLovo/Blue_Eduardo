const elementoSituacao = document.querySelector('#situacao');
const elementoImg =document.querySelector('#imagem');
let elementoBtn = document.querySelector('#alterar');


elementoBtn.addEventListener('click', () =>{
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './assets/img/bebado400.png'
        elementoSituacao.innerText = 'Rick chapadão'
        elementoBtn.value = 'segundo'
    }
    
    else if(elementoBtn.value == 'segundo'){
        elementoImg.src = './assets/img/toxico400.png'
        elementoSituacao.innerText = 'Rick toxico'
        elementoBtn.value = 'terceiro'
    }
    
    else if(elementoBtn.value == 'terceiro'){
        elementoImg.src = './assets/img/ri400.png'
        elementoSituacao.innerText = 'PICKLE RICK!'
        elementoBtn.value = 'quarto'
    }

    else{
        elementoImg.src = './assets/img/dançando400.png'
        elementoSituacao.innerText = 'Rick bom de dança'
        elementoBtn.value = 'primeiro'
    }
})