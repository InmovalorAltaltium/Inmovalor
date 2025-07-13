// tiempo.js
let timer;
const logoutTime = 2 * 60 * 1000;

function cerrarSesionPorInactividad() {
  window.location.href = logoutUrl;
}

function resetTimer() {
  clearTimeout(timer);
  timer = setTimeout(cerrarSesionPorInactividad, logoutTime);
}

window.onload = resetTimer;
document.onmousemove = resetTimer;
document.onkeypress = resetTimer;
document.onscroll = resetTimer;