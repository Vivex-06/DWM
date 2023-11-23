const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Welcome to Node.js HTTP Server!\n');
})

server.listen(3000, 'localhost', () => {
    console.log('Detecting Requests');
})