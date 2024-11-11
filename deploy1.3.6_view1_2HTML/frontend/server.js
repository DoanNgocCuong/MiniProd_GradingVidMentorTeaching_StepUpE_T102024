const http = require('http');
const fs = require('fs');
const path = require('path');

// Add environment configuration
const env = process.env.NODE_ENV || 'development';
const config = {
  development: {
    port: 5000,
    corsOrigin: 'http://localhost:25036'
  },
  production: {
    port: 5000,
    corsOrigin: 'http://103.253.20.13:25036'
  }
};

// Use in your server setup
const currentConfig = config[env];
const port = process.env.PORT || currentConfig.port;

const server = http.createServer((req, res) => {
  let filePath = '.' + req.url.split('?')[0];
  if (filePath === './') {
    filePath = './index.html';
  }

  if (filePath === './index.html' || filePath === './UIBuilder/index.html') {
    filePath = path.join(__dirname, filePath);
  }

  const extname = String(path.extname(filePath)).toLowerCase();
  const contentType = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
  };

  fs.readFile(filePath, (error, content) => {
    if (error) {
      if (error.code === 'ENOENT') {
        fs.readFile(path.join(__dirname, 'index.html'), (err, content) => {
          if (err) {
            res.writeHead(404);
            res.end('File not found');
          } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(content, 'utf-8');
          }
        });
      } else {
        res.writeHead(500);
        res.end('Server error: ' + error.code);
      }
    } else {
      res.writeHead(200, { 'Content-Type': contentType[extname] || 'text/plain' });
      res.end(content, 'utf-8');
    }
  });
});

server.listen(port, () => {
  console.log(`Server running at port ${port}`);
});