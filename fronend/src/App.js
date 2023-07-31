import { BrowserRouter, Routes,Route} from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar'
import Subjects from './pages/Subjects'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path='/subjects' Component={Subjects}> </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
