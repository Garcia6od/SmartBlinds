const subir= document.getElementById("open");
const bajar= document.getElementById("close");
const estado= document.getElementById("estado");
const automatico= document.getElementById("auto");

subir.addEventListener("mouseup",()=>{
estado.textContent="ESTADO: DETENIDO";
});

subir.addEventListener("mousedown",()=>{
estado.textContent="ESTADO: ABRIENDO";
});

bajar.addEventListener("mouseup",()=>{
estado.textContent=" ESTADO: DETENIDO";
});

bajar.addEventListener("mousedown",()=>{
estado.textContent="ESTADO: CERRANDO";
});
