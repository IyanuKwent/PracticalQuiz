import logo from './logo.svg';
import axios from 'axios'
import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [post, setPost] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/v1/api/posts/').then(response => {setPost(response.data)})
  })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      {
        post.map((obj,index) => <div key={index}>{obj.title}</div>)
      }
    </div>
  );
}

export default App;
