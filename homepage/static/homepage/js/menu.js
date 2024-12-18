// Función para abrir y cerrar el menú de categorías
function toggleCategories() {
    const menu = document.getElementById('categories-menu');
    menu.classList.toggle('open');
}

// Función para cerrar el menú si se hace clic fuera de él
document.addEventListener('click', function(event) {
    const menu = document.getElementById('categories-menu');
    const menuButton = document.querySelector('.menu-btn');
    
    if (!menu.contains(event.target) && !menuButton.contains(event.target)) {
        if (menu.classList.contains('open')) {
            menu.classList.remove('open');
        }
    }
});

// Función obetener le fecha y la hora acutal
function updateTime() {
    const currentTime = new Date();
    const hours = currentTime.getHours().toString().padStart(2, '0');
    const minutes = currentTime.getMinutes().toString().padStart(2, '0');
    const date = currentTime.toLocaleDateString('en-US');
    const time = `${hours}:${minutes}`;
    document.getElementById('current-time').innerHTML = `${date} - ${time}`;
}

setInterval(updateTime, 1000);
