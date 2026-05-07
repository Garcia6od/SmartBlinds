const ip_esp = "http://192.168.0.122";

const enviar = (accion) => {
    console.log("Enviando: " + accion);
    fetch(`${ip_esp}/${accion}`)
        .catch(err => console.log("Error al enviar: ", err));
};

const subir = document.getElementById("open");
const bajar = document.getElementById("close");
const estado = document.getElementById("estado");
const auto = document.getElementById("automatic");
const modo1=document.getElementById("mode1");
const modo2=document.getElementById("mode2");
const modo3=document.getElementById("mode3")


subir.addEventListener("pointerdown", () => {
    estado.textContent = "ESTADO: ABRIENDO";
    enviar("abrir");
});

subir.addEventListener("pointerup", () => {
    estado.textContent = "ESTADO: DETENIDO";
    enviar("detener");
});

bajar.addEventListener("pointerdown", () => {
    estado.textContent = "ESTADO: CERRANDO";
    enviar("cerrar");
});

bajar.addEventListener("pointerup", () => {
    estado.textContent = "ESTADO: DETENIDO";
    enviar("detener");
});

auto.addEventListener("change", () => {
    if (auto.checked) {
        estado.textContent = "ESTADO: MODO AUTOMATICO ACTIVADO";
        enviar("modo_auto");
    } else {
        estado.textContent = "ESTADO: MODO MANUAL ACTIVADO";
        enviar("modo_manual");
    }
});

auto.addEventListener("change", () => {
    const botones = document.querySelectorAll(".control button");

    if (auto.checked) {
        estado.textContent = "ESTADO: MODO AUTOMÁTICO ACTIVADO";
        enviar("modo_auto");
        botones.forEach(btn => btn.disabled = true);
    } else {
        estado.textContent = "ESTADO: MODO MANUAL ACTIVADO";
        enviar("modo_manual");
        botones.forEach(btn => btn.disabled = false);
    }
});

modo1.addEventListener("pointerdown", ()=>{
estado.textContent="ESTADO: EJECUTANDO MODO 1...";
enviar("25");
});

modo2.addEventListener("pointerdown", ()=>{
estado.textContent="ESTADO: EJECUTANDO MODO 2...";
enviar("50");
});

modo3.addEventListener("pointerdown", ()=>{
estado.textContent="ESTADO: EJECUTANDO MODO 3...";
enviar("75");
});

