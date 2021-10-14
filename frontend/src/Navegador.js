import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";

// CONEX



function Navegador() {

  
    const history = useHistory();

    const routeChange = () =>{ 
      let path = `ver`; 
      history.push(path);
    }
    const routeChange2 = () =>{ 
        let path = `subir`; 
        history.push(path);
      }
  
    return (
        <div>
            <h1 className="navegador"> Navegacion </h1>

            ...
                <button color="primary" className="px-4"
                  onClick={routeChange}
                    >
                    Ver memes
                  </button>
                <button color="link" className="px-0" onClick={routeChange2}>Subir memes</button>

            ...
        </div>
    );
  }

export default Navegador;
