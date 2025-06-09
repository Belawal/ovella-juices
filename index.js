const PythonShell = require('python-shell').PythonShell;
const static = require('node-static');
const http = require('http');
const fs = require('fs');

// Serve files from ./static directory
const static_serve = new static.Server('./static');

// Create HTTP server
const server = http.createServer(function (req, res) {
    static_serve.serve(req, res, function (err, result) {
        if (err) {
            res.writeHead(err.status || 500, {'Content-Type': 'text/plain'});
            res.end(err.message || 'Internal Server Error');
        }
    });
});

// Setup socket.io with the server
const { Server } = require('socket.io');
const io = new Server(server, {
    cors: {
        origin: "*", 
        methods: ["GET", "POST"]
    },
    transports: ['websocket'] 
});

io.on('connection', (socket) => {
    console.log("Socket Connected");

    function run_python_script() {
        try {
            let pyshell = new PythonShell('run.py');

            socket.on('disconnect', () =>  {
                console.log("Socket Disconnected");
                try {
                    pyshell.kill();
                } catch (e) {
                    console.log('Error killing pyshell:', e);
                }
            });

            socket.on('command_entered', (command) =>  {
                console.log("Socket Command:", command);
                try {
                    pyshell.send(command);
                } catch (e) {
                    console.log('Error sending to pyshell:', e);
                }
            });

            pyshell.on('message', (message) => {
                console.log('Process output:', message);
                socket.emit("console_output", message);
            });

            pyshell.on('close', () => {
                console.log('Process ended');
            });

            pyshell.on('error', (err) => {
                console.log('Process error:', err);
                socket.emit("console_output", "Error: " + err.toString());
            });
        } catch (e) {
            console.error("Exception running python script:", e);
        }
    }

    if (process.env.CREDS != null) {
        fs.writeFile('creds.json', process.env.CREDS, 'utf8', function(err) {
            if (err) {
                console.log('Error writing creds file:', err);
                socket.emit("console_output", "Error saving credentials: " + err);
            } else {
                run_python_script();
            }
        });
    } else {
        run_python_script();
    }
});

const port = process.env.PORT || 8000;
server.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
