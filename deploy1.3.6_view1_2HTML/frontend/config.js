const config = {
  development: {
    frontendUrl: 'http://localhost:25036',
    backendUrl: 'http://localhost:25035',
    liveDevelopment: 'http://127.0.0.1:5502/frontend'
  },
  production: {
    frontendUrl: 'http://103.253.20.13:25036',
    backendUrl: 'http://103.253.20.13:25035'
  }
};

// Determine environment based on hostname
const getEnvironment = () => {
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    return 'development';
  }
  return 'production';
};

export const getConfig = () => {
  const env = getEnvironment();
  return config[env];
};