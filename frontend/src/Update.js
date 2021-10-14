import React, { useState, useEffect } from "react";

import axios from "axios";

const baseURL = 'http://localhost:5000'

function Update() {
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

  const handleSubmission = (event) => {
    event.preventDefault(event);
    const formData = new FormData();

    formData.append('meme_name', memeName);
    formData.append('meme_ranking', memeRanking);
    formData.append('meme_story', memeStory);
    console.log(formData)
    event.preventDefault()
    axios.put(`${baseURL}/update`, formData)
    // .then((response) => response.json())
    // .then((result) => {
    //   console.log('Success:', result);
    // })
    // .catch((error) => {
    //   console.error('Error:', error);
    // });
    window.location.href = "/ver"
  }

  return (
    <div>
    <h1 className="memename"> Formulario Update meme 2.0</h1>
        <form action="/update" id="formulario" method="PUT" onSubmit={(event) =>handleSubmission(event)} encType="multipart/form-data">
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
        <input className="form__input" type="submit" formMethod="PUT" value="Enviar" />
        </label>
        </form>
    </div>
  );
}

export default Update;