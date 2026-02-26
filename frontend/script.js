// Simple script to handle basic interactions for the prototype

document.addEventListener('DOMContentLoaded', () => {
    // Current page highlight
    const path = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        if (link.getAttribute('href') && path.endsWith(link.getAttribute('href'))) {
            link.classList.add('active');
        }
    });

    // Handle "Details" button clicks in inventory
    const detailButtons = document.querySelectorAll('.btn-details');
    detailButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const row = e.target.closest('tr');
            const name = row.cells[0].innerText;
            const qtd = row.cells[2].innerText;
            alert(`Detalhes do Item:\n\nNome: ${name}\nQuantidade: ${qtd}\n\nDescrição detalhada seria mostrada aqui.`);
        });
    });

    // Tag filtering mock
    const tags = document.querySelectorAll('.tag');
    tags.forEach(tag => {
        tag.addEventListener('click', () => {
            tag.classList.toggle('active');
        });
    });

    // Form submission mock
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Item criado com sucesso! (Simulação)');
            window.location.href = 'inventory.html';
        });
    }
});
