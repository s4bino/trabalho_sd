const cors = require('cors');
const express = require('express');
const path = require('path');
const nodemailer = require('nodemailer');

const app = express();
const port = 3000;

let produtos = [];
let alerts = [];
let linkGlobal;

// Middleware para parsear JSON
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'front-end')));

// Rota para receber dados do produto
app.post('/api/produtos', (req, res) => {
    const produto = req.body;
    console.log(`Produto Atual: ${produto.price_usd_min}`);

    if (produto.title) {
        // Adiciona o produto ao histórico com timestamp
        produtos.push({ 
            time: new Date().toLocaleTimeString(), 
            title: produto.title,
            price: produto.price_usd_min
        });
        res.status(200).json({
            message: 'Dados recebidos com sucesso.'
        });

        // Verifica os alertas após adicionar o novo produto
        checkAlerts(produto);
    }
    // console.log(`Lista de produtos:`, produtos);
});

// Rota para obter o histórico de produtos
app.get('/api/produtos', (req, res) => {
    res.json(produtos);
});

// Rota para configurar notificações de preço
app.post('/notify', (req, res) => {
    const { link, email, valor } = req.body;

    // Armazena a preferência de alerta
    alerts.push({ link, email, valor });

    console.log('Link:', link);
    console.log('Email:', email);
    console.log('Valor desejado:', valor);

    linkGlobal = link

    res.status(200).json({ message: 'Alerta configurado com sucesso!' });
});

// Rota para enviar a página de gráfico
app.get('/notify', (req, res) => {
    res.sendFile(path.join(__dirname, 'front-end', 'index.html'));
});

// Rota para enviar a página de gráfico
app.get('/chart', (req, res) => {
    res.sendFile(path.join(__dirname, 'front-end', 'chart.html'));
});

// Configuração do serviço de email
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'ranulfomascarineto@gmail.com',  // substitua com seu email
        pass: 'xiei zcyq vjeb nvlz'           // substitua com sua senha
    }
});

// Função para verificar e enviar alertas
function checkAlerts(produto) {
    console.log("Verificando alertas:");
    alerts.forEach(alert => {
        console.log('Alerta:', alert);
        const { link, email, valor } = alert;

        const valorAtual = parseFloat(produto.price_usd_min.replace('US$ ', '').replace('.', '').replace(',', '.'));
        const valorDesejado = parseFloat(valor);
        console.log(`Valor atual: ${valorAtual}`);
        console.log(`Valor desejado: ${valorDesejado}`);

        // Verifica se o preço atual do produto é menor ou igual ao valor do alerta
        if (valorAtual <= valorDesejado) {
            // Configura as opções de email
            const mailOptions = {
                from: 'ranulfomascarineto@gmail.com', // substitua com seu email
                to: email,
                subject: 'Product Alert',
                text: `O produto no link ${link} está disponível por ${produto.price_usd_min} USD, que é menor ou igual ao valor de ${valor} USD que você definiu.`
            };

            // Envia o email
            transporter.sendMail(mailOptions, (error, info) => {
                if (error) {
                    console.error('Erro ao enviar email:', error);
                } else {
                    console.log('Email enviado:', info.response);
                }
            });

            console.log("Produto mais barato encontrado.");
            // Remove o alerta após o envio do email
            alerts = alerts.filter(a => a !== alert);
        } else {
            console.log("O preço atual do produto ainda não atingiu o valor desejado.");
        }
    });
}

app.get('/pedeLink', (req, res) => {
    res.send(linkGlobal);
});

// Inicia o servidor
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
