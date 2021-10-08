import React, { useState, useEffect } from "react";
import { Rating, RatingView } from 'react-simple-star-rating'
import axios from "axios";
const baseURL = 'http://localhost:5000'

// antiguo CONEX, ahora es VER
//ward: la cosa que puse para rankear se comparte entre todas las imágenes, no es única

function VerMeme() {

  const [selectedFile, setSelectedFile] = useState();
  const [memeName, setMemeName] = useState()
  const [memeRanking, setMemeRanking] = useState()
  const [memeStory, setMemeStory] = useState()
  const [memeId, setMemeId] = useState()


  const handleMemeNameChange = (event) => {
    console.log(event)
    setMemeName(event)
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
////////////////////////////////////////////////

  const [data, setData] = useState([]);
  useEffect(() => {
    fetch("/ver")
      .then((res) => res.json())
      .then((res) => {
        // console.log(res);
        setData(res);
      });
  }, []);
  // console.log(data);
////////////////////////////////////////////////////////////

const [rating, setRating] = useState();

const handleRating = (rate) => {
  setRating(rate)
}

const handleSub2 = () => {
  const formData = new FormData();
  
  formData.append('rating', rating);
  formData.append('meme_name',memeName);
  formData.append('meme_id', memeId)
  axios.post(`${baseURL}/update_ranking`, formData)
    .then((response) => response.json())
    .then((result) => {
      console.log('Success:', result);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


////////////////////////////////////////////////////////////
  return (
    <div className="centered">
      <h1 className="memename"> Mostrando memes </h1>
      { data.length === 0 ? (
        <p>Loading ...</p>
      ) : (
      data.map((meme) =>
      <div className="meme">
        <h1 className="memename" id="meme_name">{meme.meme_name}</h1>
        <br/>
        <img key={meme.meme_id} src={`data:image/;base64, ${meme.meme_image}`} className="img2"/>
        <RatingView ratingValue ={meme.meme_ranking} stars={10}  />
        <text className="navegador"> autor: </text>
        <span className="navegador" key={meme.meme_id}>{meme.meme_ranking}</span>
        <text className="navegador">/10 </text>
        <br/>
        <h2 className="wrapper">{meme.meme_story}</h2>
        <div className="flex">
        <form className="flex-item" action="" method="POST"><button className="button" name="meme_name" value={meme.meme_name}>Delete this</button></form>
        
        <form className="flex-item" action="/update_meme"  method="POST" ><button className="button"  name="meme_name" value={meme.meme_name}>Update meme</button></form>
      </div>
      </div>
 )
      )}
    </div>
  );
}

export default VerMeme;
