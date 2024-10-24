# How to Run the Backend API

## Prerequisites
1. Node.js installed on your computer
2. OpenAI API key

## Setup Steps

1. **Install Dependencies**
   ```bash
   cd backend
   npm install
   ```

2. **Configure Environment Variables**
   - Create a `.env` file in the `backend` folder
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Start the Server**
   ```bash
   npm start
   ```
   The server will start on port 3000 (default) or the port specified in your environment variables.

>>> This shows that `npm start` is just running `node app.js` behind the scenes.

The main differences are:

1. **Using `npm start`**:
   - It's the standard way in Node.js projects
   - It will run any pre/post scripts if defined
   - It uses the script defined in package.json

2. **Using `node app.js`**:
   - It's the direct way to run the file
   - It bypasses npm's script system
   - It might miss any environment setup that npm scripts provide

>>> For this simple project, both commands will work exactly the same way. However, it's generally recommended to use `npm start` as it follows Node.js conventions and will work with any additional scripts you might add later.


## Testing the API

You can test the API using Postman or curl:

1. **Endpoint**: `POST http://localhost:3000/api/openai`
2. **Headers**: 
   - Content-Type: application/json
3. **Request Body**:
   ```json
   {
     "systemPrompt": "You are a helpful assistant.",
     "userInputPrompt": "Tell me a joke."
   }
   ```

## Example curl Command



