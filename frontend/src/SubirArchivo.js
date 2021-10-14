import React, { useState } from "react";
import axios from "axios";

const baseURL = 'http://backend:5000'




function SubirArhivo() {
  const [selectedFile, setSelectedFile] = useState();
  const [memeName, setMemeName] = useState()
  const [memeRanking, setMemeRanking] = useState()
  const [memeStory, setMemeStory] = useState()

  const handleMemeNameChange = (event) => {
    console.log(event.target.value)
    setMemeName(event.target.value)
  }
  const handleMemeRankingChange = (event) => {
    setMemeRanking(event.target.value)
  }
  const handleMemeStoryChange = (event) => {
    setMemeStory(event.target.value)
  }
  const handleFileChange = event => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmission = () => {
    const formData = new FormData();

    formData.append('meme_name', memeName);
    formData.append('meme_ranking', memeName);
    formData.append('meme_story', memeName);
    formData.append('meme_image', selectedFile);

    
    axios.post(`${baseURL}/subir`, formData)
    .then((response) => response.json())
    .then((result) => {
      console.log('Success:', result);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }

  return (
    <div>
    <h1 className="memename"> Formulario creacion meme 2.0</h1>
    <br/>
        <form action="/subir" method="POST" id="formulario" onSubmit={handleSubmission} enctype="multipart/form-data">
        <label className="form__label"> 
          <input className="form__input" placeholder="Nombre del meme" type="text" name="meme_name" min="1" max="20" onChange={handleMemeNameChange} required/>
          <br/>
        </label>
        <label className="form__label">
          <input className="form__input" placeholder="Ranking del meme" type="number" name="meme_ranking" min="1" max="10" onChange={handleMemeRankingChange} required/>
          <br/>
        </label>
        <label className="form__label">
          <input  className="form__input" placeholder="Historia del meme" type="text" name="meme_story" min="1" max="200" onChange={handleMemeStoryChange} required/>
          <br/>
        </label>  
        <label className="form__label">
        <input className="form__input" type="file" name="meme_image" id="image" accept="image/png, image/jpeg, image/jpg, image/gif" onChange={handleFileChange} />
        </label>
        <br/>

			  {/* <button onClick={handleSubmission}>Subir</button> */}
        <label className="form__label">
        <input className="form__input" type="submit" value="Enviar"/>
        </label>
        </form>
    </div>
  );
}

export default SubirArhivo;