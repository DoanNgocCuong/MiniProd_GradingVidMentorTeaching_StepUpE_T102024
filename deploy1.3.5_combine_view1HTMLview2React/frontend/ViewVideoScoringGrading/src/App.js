import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Navigation from './components/Navigation';

const App = () => {
  return (
    <Router basename="/grading">
      <div>
        <Navigation />
        {/* Các routes khác của ứng dụng */}
      </div>
    </Router>
  );
};

export default App; 