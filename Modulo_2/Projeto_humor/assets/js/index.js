const elementoSituação = document.querySelector('#situação');
const elementoImg =document.querySelector('#imagem');
let elementoBtn = document.querySelector('#alterar');


elementoBtn.addEventListener('click', () =>{
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './assets/img/bebado400.png'
        elementoSituação.innerText = 'Rick chapadão'
        elementoBtn.value = 'segundo'
    }else if(elementoBtn.value == 'segundo'){
        elementoImg.src = './assets/img/toxico400.png'
        elementoSituação.innerText = 'Rick toxico'
        elementoBtn.value = 'terceiro'
    }else if(elementoBtn.value == 'terceiro'){
        elementoImg.src = './assets/img/picle400.png'
        elementoSituação.innerText = 'PICKLE RICK!'
        elementoBtn.value = 'primeiro'
    }       
})