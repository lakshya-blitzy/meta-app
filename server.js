/**
 * @fileOverview Simple HTTP server for Meta App Repository
 * @description Minimal Node.js HTTP server that responds to all requests with "Hello, World!" message.
 * This server binds only to localhost (127.0.0.1) on port 3000 for security. It uses the built-in
 * http module with no external dependencies, making it lightweight and easy to deploy.
 * The server handles ALL HTTP methods (GET, POST, PUT, DELETE, etc.) and ALL paths with the same
 * static response.
 * 
 * @requires module:http - Node.js built-in HTTP module
 * @example
 * // Start the server
 * node server.js
 * // Access the endpoint
 * // Navigate to http://127.0.0.1:3000 in your browser
 * // Or use curl: curl http://127.0.0.1:3000
 * @version 1.0.0
 */
const http = require('http');

/**
 * Server hostname configuration.
 * The server binds only to localhost (127.0.0.1), preventing external network access for security.
 * This means the server is only accessible from the same machine it's running on.
 * For production deployment allowing external access, change to '0.0.0.0' to bind to all network
 * interfaces, or specify a particular IP address.
 * 
 * @constant
 * @type {string}
 * @default '127.0.0.1'
 * @see README.md Configuration section for production deployment details
 */
const hostname = '127.0.0.1';

/**
 * Server port number configuration.
 * Port 3000 is commonly used for Node.js development servers. If this port is already in use
 * by another application, modify this value to an available port (e.g., 3001, 8080, 8000).
 * Consider using environment variables (process.env.PORT) for flexible configuration across
 * different deployment environments.
 * 
 * @constant
 * @type {number}
 * @default 3000
 * @see README.md Configuration section for details on changing the port
 */
const port = 3000;

/**
 * HTTP request handler that processes all incoming requests.
 * This callback function handles ALL HTTP methods (GET, POST, PUT, DELETE, PATCH, etc.) and
 * ALL URL paths with the same static response. No request parsing, routing, or method filtering
 * is implemented. Every request receives a 200 OK status with "Hello, World!" in plain text.
 * 
 * @param {http.IncomingMessage} req - The incoming HTTP request object containing request details
 *                                      (method, URL, headers, etc.)
 * @param {http.ServerResponse} res - The server response object used to send the HTTP response
 *                                     back to the client
 * @see README.md API Reference section for endpoint documentation and examples
 */
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

/**
 * Start the HTTP server and bind it to the specified hostname and port.
 * The callback function is executed when the server successfully starts and is ready to
 * accept incoming connections. It logs the server URL to the console for confirmation.
 */
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
