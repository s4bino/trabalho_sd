const cors = require('cors');
const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

let produtos = {};

let link;

// Middleware to parse JSON bodies
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'src')));

// Route to handle incoming champion data
app.post('/api/produtos', (req, res) => {
    produtos = req.body;
    console.log('Received links data:', produtos);
    res.status(200).json({
        message: 'Data received successfully.'
    });
});


app.post('/notify', (req, res) => {
    const data = req.body;

    // Aqui você pode processar o link e email, salvar em um banco de dados, etc.
    console.log('Link:', data.link);
    console.log('Email:', data.email);
    console.log('Valor:', data.valor);

    link = data.link

    // Resposta de sucesso
    res.status(200).json({ message: 'Produto adicionado com sucesso!' });
});

app.get('/pedeLink', (req, res) => {
    res.send(link);
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});