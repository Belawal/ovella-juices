// server.js
const static = require('node-static');
const http = require('http');
const pty = require('node-pty');
const WebSocket = require('ws');

const file = new static.Server('.');
const server = http.createServer(function (req, res) {
  file.serve(req, res);
});

const wss = new WebSocket.Server({ server });

wss.on('connection', function (ws) {
  const shell = pty.spawn('python3', ['run.py'], {
    name: 'xterm-color',
    cols: 80,
    rows: 24,
    cwd: process.env.HOME,
    env: process.env
  });

  shell.on('data', function (data) {
    ws.send(data);
  });

  ws.on('message', function (msg) {
    shell.write(msg);
  });

  ws.on('close', function () {
    shell.kill();
  });
});

server.listen(process.env.PORT || 5000);
