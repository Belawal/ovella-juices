const PythonShell = require('python-shell').PythonShell;
const static = require('node-static');
const http = require('http');
const fs = require('fs');

// Serve files from ./static directory
var static_serve = new static.Server('./static');

// Create HTTP server
const server = http.createServer(function (req, res) {
    console.log(`Received request: ${req.method} ${req.url}`);
    static_serve.serve(req, res, function (err, result) {
        if (err) {
            console.error('Error serving file:', err);
            if (err.status === 404) {
                res.writeHead(404, {'Content-Type': 'text/plain'});
                res.end('404 Not Found');
            } else {
                res.writeHead(err.status, {'Content-Type': 'text/plain'});
                res.end(err.message);
            }
        }
    });
});

// Setup socket.io with the server
const io = require('socket.io')(server);

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
                    console.log('Cannot send any more to pyshell', e);
                }
            });

            socket.on('command_entered', (command) =>  {
                console.log("Socket Command: ", command);
                try {
                    pyshell.send(command);
                } catch (e) {
                    console.log('Cannot send any more to pyshell', e);
                }
            });

            pyshell.on('message', (message) => {
                console.log('Process output:', message);
                try {
                    socket.emit("console_output", message);
                } catch (e) {
                    console.log('Cannot write to socket', e);
                }
            });

            pyshell.on('close', () => {
                console.log('Process ended');
            });

            pyshell.on('error', (message) => {
                console.log('Process error:', message);
                try {
                    socket.emit("console_output", message.traceback.replace('\n', '\r\n'));
                } catch (e) {
                    console.log('Cannot write to socket', e);
                }
            });
        } catch (e) {
            console.error("Exception running python script:", e);
        }
    }

    if (process.env.CREDS != null) {
        fs.writeFile('creds.json', process.env.CREDS, 'utf8', function(err) {
            if (err) {
                console.log('Error writing file:', err);
                socket.emit("console_output", "Error saving credentials: " + err);
            } else {
                run_python_script();
            }
        });
    } else {
        run_python_script();
    }
});

// Listen on port from environment variable or default to 8000
const port = process.env.PORT || 8000;
server.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
