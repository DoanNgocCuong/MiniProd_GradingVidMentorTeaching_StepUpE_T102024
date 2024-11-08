/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#0066cc',
          foreground: '#ffffff',
        },
        accent: {
          DEFAULT: '#f0f0f0',
          foreground: '#000000',
        },
        input: '#e2e8f0',
        background: '#ffffff',
        ring: '#0066cc',
        'muted-foreground': '#6b7280',
      },
    },
  },
  plugins: [],
} 