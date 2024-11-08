const config = {
    API_URL: process.env.NODE_ENV === 'production'
        ? 'http://103.253.20.13:25035'
        : 'http://localhost:25035',
    PORT: 25035
};

console.log('Current API_URL:', config.API_URL);

export default config;