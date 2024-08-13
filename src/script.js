
document.getElementById('eventForm').addEventListener('submit', function(event) {
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

    // Prepara os dados para envio
    const data = {
        link: link,
        email: email
    };

    // Faz a requisição POST para a rota /notify
    fetch('http://localhost:3000/notify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            console.log(data)
            return response.json();
            

        } else {
            throw new Error('Erro ao enviar o formulário');
        }
    })
    .then(data => {
        console.log('Success:', data);
        // Você pode adicionar uma lógica aqui para notificar o usuário
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('errorMessage').textContent = 'Ocorreu um erro. Por favor, tente novamente.';
    });
});

function validateEmail(email) {
    // Regex mais robusto para validar e-mail
    var re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(email);
}

