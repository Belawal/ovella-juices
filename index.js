const { PythonShell } = require('python-shell');
const static = require('node-static');
const http = require('http');
const fs = require('fs');

// Serve static files from ./static
const static_serve = new static.Server('./static');

// Create HTTP server
const server = http.createServer(function (req, res) {
    console.log(`Received request: ${req.method} ${req.url}`);
    static_serve.serve(req, res, function (err, result) {
        if (err) {
            console.error('Error serving file:', err);
            res.writeHead(err.status || 500, { 'Content-Type': 'text/plain' });
            res.end(err.message || 'Internal Server Error');
        }
    });
});

// Setup socket.io with the server (force WebSocket)
const io = require('socket.io')(server, {
    cors: {
        origin: "*", // Optional: Set to your domain for production
    },
    transports: ['websocket'], // Force WebSocket only (no polling)
});

io.on('connection', (socket) => {
    console.log("✅ Socket connected");

    function run_python_script() {
        try {
            const pyshell = new PythonShell('run.py');

            socket.on('disconnect', () => {
                console.log(" Socket disconnected");
                try {
                    pyshell.kill();
                } catch (e) {
                    console.log('Error killing Python shell:', e);
                }
            });

            socket.on('command_entered', (command) => {
                console.log(" Command received:", command);
                try {
                    pyshell.send(command);
                } catch (e) {
                    console.log('Error sending to Python shell:', e);
                }
            });

            pyshell.on('message', (message) => {
                console.log(' Python Output:', message);
                socket.emit("console_output", message);
            });

            pyshell.on('close', () => {
                console.log('🔚 Python process ended');
            });

            pyshell.on('error', (error) => {
                console.log(' Python error:', error);
                socket.emit("console_output", `Error: ${error}`);
            });
        } catch (e) {
            console.error(" Exception starting Python script:", e);
        }
    }

    // Optional: Save credentials if provided via ENV
    if (process.env.CREDS != null) {
        fs.writeFile('creds.json', process.env.CREDS, 'utf8', function (err) {
            if (err) {
                console.log('Error writing creds:', err);
                socket.emit("console_output", "Error saving credentials.");
            } else {
                run_python_script();
            }
        });
    } else {
        run_python_script();
    }
});

// Start server on assigned port
const port = process.env.PORT || 8000;
server.listen(port, () => {
    console.log(` Server listening on port ${port}`);
});
