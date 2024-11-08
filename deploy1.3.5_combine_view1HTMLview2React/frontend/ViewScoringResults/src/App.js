import { BrowserRouter as Router } from 'react-router-dom';
import Navigation from './components/Navigation';

function App() {
  return (
    <Router basename="/scoring">
      <div>
        <Navigation />
        {/* Các routes khác của ứng dụng */}
      </div>
    </Router>
  );
}

export default App;