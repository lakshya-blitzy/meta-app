"# Meta App Repository

A minimal Node.js HTTP server demonstrating basic server implementation using the built-in `http` module. This lightweight server responds to all HTTP requests with a simple "Hello, World!" message, making it perfect for learning Node.js fundamentals, testing network configurations, or serving as a template for more complex applications.

**Key Features:**
- 🚀 Zero external dependencies - uses only Node.js built-in modules
- 🔒 Security-first design with localhost-only binding by default
- 📝 Comprehensive JSDoc documentation for code clarity
- 🧪 Includes Java-based test automation via Git submodules
- ⚡ Lightweight and fast startup

**Technology Stack:**
- Node.js (v14.0+ recommended, tested on v20.19.5)
- Built-in HTTP module for server functionality

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Repository Structure](#repository-structure)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Additional Resources](#additional-resources)

---

## Prerequisites

Before running the Meta App Repository server, ensure you have the following installed:

### Required Software

- **Node.js**: Version 14.0 or higher (tested on v20.19.5)
  - Download from [nodejs.org](https://nodejs.org/)
  - Verify installation: `node --version`
- **npm**: Version 6.0 or higher (bundled with Node.js)
  - Verify installation: `npm --version`
- **Git**: For cloning the repository and managing submodules
  - Download from [git-scm.com](https://git-scm.com/)

### Operating System

- Linux (any modern distribution)
- macOS (10.14+)
- Windows (10/11 with Command Prompt, PowerShell, or WSL)

### Network Requirements

- Available port 3000 (or any alternative port you configure)
- No external network dependencies

---

## Installation

Follow these steps to get the server running on your local machine:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd meta-app
```

### 2. Initialize Git Submodules (Optional)

This repository includes Java-based test automation clients as Git submodules. If you want to use the test clients, initialize them:

```bash
git submodule update --init --recursive
```

**Note:** Submodule initialization is optional and only needed if you plan to run the automated test suite.

### 3. Verify Node.js Installation

Ensure Node.js is properly installed and meets version requirements:

```bash
node --version
```

**Expected output:** `v14.0.0` or higher (e.g., `v20.19.5`)

### 4. No Dependencies to Install

This project has **zero external dependencies**. The server uses only Node.js built-in modules, so no `npm install` is required!

---

## Quick Start

Get the server running in 30 seconds:

### Start the Server

```bash
node server.js
```

**Expected output:**
```
Server running at http://127.0.0.1:3000/
```

### Access the Endpoint

**Option 1: Using a Web Browser**

Open your browser and navigate to:
```
http://127.0.0.1:3000
```

You should see: **Hello, World!**

**Option 2: Using curl (Command Line)**

```bash
curl http://127.0.0.1:3000
```

**Expected output:**
```
Hello, World!
```

### Stop the Server

Press `Ctrl+C` in the terminal where the server is running.

---

## API Reference

The Meta App Repository server exposes a single HTTP endpoint that handles all requests uniformly.

### Endpoint Details

| Property | Value |
|----------|-------|
| **Base URL** | `http://127.0.0.1:3000` |
| **Methods** | ALL (GET, POST, PUT, DELETE, PATCH, OPTIONS, etc.) |
| **Paths** | ALL (wildcard - any path returns the same response) |
| **Authentication** | None |
| **Request Body** | Ignored (not parsed) |
| **Query Parameters** | Ignored (not parsed) |

### Response Specification

**Status Code:** `200 OK`

**Headers:**
```
Content-Type: text/plain
```

**Response Body:**
```
Hello, World!
```

### Example Requests

**Example 1: GET Request**

```bash
curl -X GET http://127.0.0.1:3000/
```

**Response:**
```
Hello, World!
```

**Example 2: POST Request (any path)**

```bash
curl -X POST http://127.0.0.1:3000/api/users -d '{"name":"test"}'
```

**Response:**
```
Hello, World!
```

**Example 3: Different Path**

```bash
curl http://127.0.0.1:3000/any/path/works
```

**Response:**
```
Hello, World!
```

### API Limitations

- ⚠️ **No Routing**: All paths return the same response
- ⚠️ **No Request Parsing**: Request body and query parameters are ignored
- ⚠️ **Static Response**: Response content cannot be modified without changing code
- ⚠️ **No Error Handling**: Server assumes all requests succeed
- ⚠️ **Localhost Only**: By default, accessible only from the same machine

---

## Configuration

The server configuration is defined in `server.js` using hardcoded constants. To modify the server behavior, you'll need to edit the source file.

### Hostname Configuration

**Location:** `server.js:32`

```javascript
const hostname = '127.0.0.1';
```

**Default:** `127.0.0.1` (localhost only)

**Security Consideration:** The server binds only to localhost, preventing external network access. This is a security feature for development environments.

**Production Alternative:** To allow external access, change to:
```javascript
const hostname = '0.0.0.0';  // Binds to all network interfaces
```

**Specific IP:** To bind to a specific network interface:
```javascript
const hostname = '192.168.1.100';  // Replace with your server's IP
```

### Port Configuration

**Location:** `server.js:46`

```javascript
const port = 3000;
```

**Default:** `3000`

**Change Port:** If port 3000 is already in use:
```javascript
const port = 8080;  // Or any available port (e.g., 3001, 8000, 8888)
```

### Environment Variables (Future Enhancement)

Currently, configuration requires editing the source file. For production use, consider implementing environment variable support:

```javascript
const hostname = process.env.HOST || '127.0.0.1';
const port = process.env.PORT || 3000;
```

Then run with:
```bash
HOST=0.0.0.0 PORT=8080 node server.js
```

---

## Repository Structure

```
meta-app/
├── README.md                    # This file - comprehensive project documentation
├── server.js                    # Main Node.js HTTP server with JSDoc comments
├── .gitmodules                  # Git submodule configuration
├── clients/
│   └── ecp-client/              # Git submodule: Java-based Cucumber test automation
│       ├── README.md            # Detailed test automation documentation
│       ├── pom.xml              # Maven project configuration
│       └── src/                 # Java test source code
└── test/
    └── clients/
        └── ecp-client/          # Git submodule: Duplicate test automation reference
            └── (same structure as clients/ecp-client)
```

### File Descriptions

- **README.md**: Complete project documentation including setup, API reference, and deployment guidance
- **server.js**: The main application file containing a minimal HTTP server implementation with comprehensive JSDoc comments
- **.gitmodules**: Configuration file defining Git submodules for test automation
- **clients/ecp-client/**: Java-based test automation using Cucumber BDD framework for API testing
- **test/clients/ecp-client/**: Reference copy of test automation (duplicate submodule)

### Submodules

This repository uses Git submodules to include external test automation repositories. The submodules contain Java-based Cucumber tests for validating the HTTP server.

**Initialize submodules:**
```bash
git submodule update --init --recursive
```

**For more details on the test automation, see:**
- [clients/ecp-client/README.md](clients/ecp-client/README.md)

---

## Deployment

### Development Mode

For local development, run the server directly with Node.js:

```bash
node server.js
```

This is suitable for:
- Local testing and development
- Learning Node.js fundamentals
- Quick prototyping

### Production Considerations

For production deployment, consider the following enhancements:

#### 1. Process Management

Use a process manager to keep the server running and restart it on failures:

**Using PM2:**
```bash
# Install PM2 globally
npm install -g pm2

# Start server with PM2
pm2 start server.js --name meta-app

# View logs
pm2 logs meta-app

# Restart server
pm2 restart meta-app

# Stop server
pm2 stop meta-app
```

**Using systemd (Linux):**

Create `/etc/systemd/system/meta-app.service`:
```ini
[Unit]
Description=Meta App HTTP Server
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/meta-app
ExecStart=/usr/bin/node server.js
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable meta-app
sudo systemctl start meta-app
```

#### 2. Reverse Proxy

Use a reverse proxy for better security and features:

**Nginx Configuration Example:**
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 3. Environment Configuration

- Use environment variables for configuration (hostname, port)
- Set `NODE_ENV=production` for production optimizations
- Implement proper logging (Winston, Bunyan, or Pino)
- Add health check endpoints for monitoring

#### 4. Security Enhancements

- Enable HTTPS with SSL/TLS certificates
- Implement rate limiting
- Add request validation and sanitization
- Use helmet.js for security headers (if migrating to Express)

#### 5. Docker Deployment (Optional)

Create a `Dockerfile`:
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY server.js .
EXPOSE 3000
CMD ["node", "server.js"]
```

Build and run:
```bash
docker build -t meta-app .
docker run -p 3000:3000 meta-app
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Port 3000 Already in Use

**Error Message:**
```
Error: listen EADDRINUSE: address already in use :::3000
```

**Solution:**
- Change the port in `server.js:46` to an available port (e.g., 3001, 8080)
- Or stop the process using port 3000:

```bash
# Find process using port 3000
lsof -i :3000    # macOS/Linux
netstat -ano | findstr :3000    # Windows

# Kill the process (replace PID)
kill -9 <PID>    # macOS/Linux
```

#### Issue 2: Cannot Access Server from Other Machines

**Problem:** Server is running but not accessible from other computers on the network.

**Solution:**
The server binds to `127.0.0.1` (localhost only) by default. To allow external access:
1. Edit `server.js:32`
2. Change `const hostname = '127.0.0.1';` to `const hostname = '0.0.0.0';`
3. Restart the server
4. Access via your machine's IP address: `http://<your-ip>:3000`

#### Issue 3: Server Won't Start

**Error:** Command not found or syntax errors

**Solutions:**
- Verify Node.js is installed: `node --version`
- Ensure Node.js version is v14.0 or higher
- Check for syntax errors in `server.js`
- Verify file permissions (should be readable)

#### Issue 4: Submodules Not Initialized

**Problem:** `clients/ecp-client` directory is empty

**Solution:**
```bash
git submodule update --init --recursive
```

---

## Development

### Setup for Contributors

1. **Fork the repository** on GitHub/GitLab
2. **Clone your fork:**
   ```bash
   git clone <your-fork-url>
   cd meta-app
   ```
3. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** following the code style guidelines
5. **Test your changes** by running the server
6. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
7. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Create a Pull Request** to the main repository

### Code Style Guidelines

- **Follow existing patterns** in `server.js`
- **Add JSDoc comments** for all functions, constants, and significant code blocks
- **Use meaningful variable names**
- **Keep it simple**: This is a minimal server demonstration
- **Test changes locally** before submitting pull requests

---

## Testing

### Manual Testing

**Verify server functionality:**

1. **Start the server:**
   ```bash
   node server.js
   ```

2. **Test with curl:**
   ```bash
   curl http://127.0.0.1:3000
   ```
   Expected: `Hello, World!`

3. **Test in browser:**
   - Open `http://127.0.0.1:3000`
   - Verify "Hello, World!" appears

4. **Test different methods:**
   ```bash
   curl -X POST http://127.0.0.1:3000
   curl -X PUT http://127.0.0.1:3000
   curl -X DELETE http://127.0.0.1:3000
   ```
   All should return: `Hello, World!`

### Automated Testing

The repository includes Java-based Cucumber test automation in the Git submodules:

**Initialize and run tests:**
```bash
# Initialize submodules
git submodule update --init --recursive

# Navigate to test client
cd clients/ecp-client

# Follow test execution instructions in clients/ecp-client/README.md
```

For detailed test automation documentation, see [clients/ecp-client/README.md](clients/ecp-client/README.md).

---

## Contributing

We welcome contributions to the Meta App Repository! Whether you're fixing bugs, improving documentation, or proposing new features, your help is appreciated.

### How to Contribute

1. **Check existing issues** to avoid duplicate work
2. **Fork the repository** and create a feature branch
3. **Make your changes** following code style guidelines
4. **Test thoroughly** to ensure no regressions
5. **Submit a pull request** with a clear description of changes

### Contribution Guidelines

- Maintain the minimalist nature of the server
- Add comprehensive JSDoc comments for any new code
- Update README.md if adding new features
- Ensure backward compatibility
- Write clear commit messages

---

## License

**License information not specified.** This project currently does not include a LICENSE file. Contributors and users should clarify licensing terms with the repository owner before use in commercial or open-source projects.

For guidance on choosing a license, visit [choosealicense.com](https://choosealicense.com/).

---

## Additional Resources

### Official Documentation

- **Node.js Official Website**: [https://nodejs.org/](https://nodejs.org/)
- **Node.js HTTP Module Documentation**: [https://nodejs.org/api/http.html](https://nodejs.org/api/http.html)
- **Git Submodules Guide**: [https://git-scm.com/book/en/v2/Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

### Related Projects

- **Test Automation Client**: [clients/ecp-client/](clients/ecp-client/) - Java-based Cucumber BDD tests

### Learn More

- **Node.js Best Practices**: [https://github.com/goldbergyoni/nodebestpractices](https://github.com/goldbergyoni/nodebestpractices)
- **HTTP Protocol**: [MDN Web Docs - HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- **JSDoc Documentation**: [https://jsdoc.app/](https://jsdoc.app/)

---

**Repository maintained as a minimal Node.js server demonstration and template.**" 
