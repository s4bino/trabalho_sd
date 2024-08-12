// script.js
document.getElementById('eventForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Limpar mensagens de erro
    document.getElementById('errorMessage').innerText = '';

    // Validações básicas
    var link = document.getElementById('link').value.trim();
    var email = document.getElementById('email').value.trim();
    var errorMessage = '';

    if (link === '') {
        errorMessage += 'O link é obrigatório.\n';
    }

    if (email === '') {
        errorMessage += 'Email é obrigatório.\n';
    } else if (!validateEmail(email)) {
        errorMessage += 'Por favor, insira um e-mail válido.\n';
    }

    if (errorMessage !== '') {
        document.getElementById('errorMessage').innerText = errorMessage;
        return; // Impede o envio do formulário se houver erros
    }
});

function validateEmail(email) {
    // Regex mais robusto para validar e-mail
    var re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(email);
}
