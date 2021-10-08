import './App.css';
import React from 'react'
import Componente0 from './Navegador.js'
import VerMeme from './VerMeme.js'
import SubirArchivo from './SubirArchivo.js'
import Update from './Update';


import { BrowserRouter as Router, Route, Redirect, Link, useHistory } from "react-router-dom";
import Navegador from './Navegador.js';
function App() {

  return (
    <div className="App">
      <Router>
        <Route path="/ver">
          <VerMeme/>
        </Route>
        <Route path="/subir">
          <SubirArchivo/>
        </Route>
        <Route path="/update">
          <Update/>
        </Route>
        <Route path="/">
          <Navegador/>
        </Route>

      </Router>
    </div>
  );
}

export default App;
