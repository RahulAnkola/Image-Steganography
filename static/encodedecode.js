const encodecard = document.querySelector('.display-imagestego-card');
const encode = document.querySelector('.encode-txt');
const decode = document.querySelector('.decode-txt');
const decodecard = document.querySelector('.display-decodecard');

encode.addEventListener('click', (evt) => {
    evt.preventDefault();
    encodecard.classList.toggle("display-imagestego-card");
})

decode.addEventListener('click', (evt) =>{
    evt.preventDefault();
    decodecard.classList.toggle("display-decodecard");
    
})