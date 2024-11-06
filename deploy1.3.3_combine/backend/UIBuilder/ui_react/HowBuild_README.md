# SUMMARY - Video Scoring UI React

## 1. Cấu trúc Project
```plaintext
ui_react/                  # Thư mục gốc của project
├── node_modules/         # Chứa tất cả các thư viện được cài đặt qua npm
├── public/               # Chứa các file tĩnh, có thể truy cập trực tiếp
│   └── index.html       # File HTML gốc, chứa thẻ root để React render vào
├── src/                 # Chứa mã nguồn chính của ứng dụng
│   ├── components/      # Chứa các components có thể tái sử dụng
│   │   ├── ui/         # Chứa các components UI cơ bản (building blocks)
│   │   │   ├── button.js   # Component button có thể tái sử dụng
│   │   │   └── input.js    # Component input có thể tái sử dụng
│   │   └── VideoScoring.js # Component chính cho tính năng chấm điểm video
│   ├── App.js          # Component gốc của ứng dụng
│   ├── index.js        # Điểm khởi đầu của ứng dụng React
│   └── index.css       # File CSS chính, chứa các styles toàn cục và Tailwind imports
├── postcss.config.js    # Cấu hình PostCSS (để Tailwind hoạt động)
├── tailwind.config.js   # Cấu hình Tailwind CSS
├── Dockerfile          # Cấu hình để build Docker container
├── package-lock.json   # Lock file chứa phiên bản chính xác của các dependencies
└── package.json        # Cấu hình project: dependencies, scripts, thông tin project
```

## 2. Khởi tạo và Cài đặt

### 2.1. Tạo Project React mới
```bash
# Tạo project mới
npx create-react-app ui_react
cd ui_react
```

### 2.2. Tạo và cấu hình các file chính
1. **package.json**
   ```bash
   # Tạo file package.json
   npm init -y
   ```
   Nội dung cơ bản:
   ```json
   {
     "name": "video-scoring-ui",
     "version": "1.0.0",
     "scripts": {
       "start": "react-scripts start",
       "build": "react-scripts build",
       "test": "react-scripts test",
       "eject": "react-scripts eject"
     },
     "dependencies": {
       "react": "^18.2.0",
       "react-dom": "^18.2.0",
       "react-scripts": "5.0.1",
       "lucide-react": "latest"
     }
   }
   ```

2. **Tailwind và PostCSS**
   ```bash
   # Cài đặt Tailwind và các dependencies
   npm install -D tailwindcss postcss autoprefixer
   
   # Tạo file cấu hình Tailwind và PostCSS
   npx tailwindcss init -p
   ```

   **tailwind.config.js**:
   ```javascript
   module.exports = {
     content: [
       "./src/**/*.{js,jsx,ts,tsx}",
     ],
     theme: {
       extend: {},
     },
     plugins: [],
   }
   ```

   **postcss.config.js**:
   ```javascript
   module.exports = {
     plugins: {
       tailwindcss: {},
       autoprefixer: {},
     }
   }
   ```

## 3. Cấu trúc Source Code (src/)

### 3.1. Các file chính trong src/
1. **index.js** - Entry point
```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

2. **index.css** - Global styles
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

3. **App.js** - Root component
```javascript
import VideoScoring from './components/VideoScoring';

function App() {
  return (
    <div className="App">
      <VideoScoring />
    </div>
  );
}

export default App;
```

### 3.2. Components
1. **components/ui/button.js** - Reusable Button component
2. **components/ui/input.js** - Reusable Input component
3. **components/VideoScoring.js** - Main Video Scoring component

## 4. Chạy Project

### 4.1. Cài đặt Dependencies
```bash
# Cài đặt các dependencies trong package.json
npm install

# Cài đặt Tailwind CSS và các tools liên quan
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
```

### 4.2. Khởi chạy Development Server
```bash
npm start
```
Ứng dụng sẽ chạy tại http://localhost:3000

### 4.3. Build Production
```bash
npm run build
```

## 5. Lưu ý quan trọng
1. Đảm bảo Node.js đã được cài đặt trên máy
2. Chạy các lệnh npm từ thư mục gốc của project (ui_react)
3. Kiểm tra file package.json có đầy đủ dependencies cần thiết
4. Cài đặt lại node_modules nếu gặp lỗi: `npm install`
5. Đảm bảo các file cấu hình (postcss.config.js, tailwind.config.js) ở đúng vị trí

## 6. Troubleshooting phổ biến
1. Lỗi "Module not found": Chạy `npm install`
2. Lỗi về Tailwind: Kiểm tra các file cấu hình và cài đặt lại
3. Lỗi khi chạy npm start: Kiểm tra package.json và cài đặt react-scripts