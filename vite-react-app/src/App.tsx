import { useState } from 'react'
import reactLogo from './assets/react.svg'
import axios from "axios";
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [profileData, setProfileData] = useState({})
  const [resStat,setResStat] = useState("")
  function getData() {
    axios({
      method: "GET",
      url:"http://127.0.0.1:5000/",
    })
    .then((response) => {
      const res =response.data
      // setProfileData(({
      //   name: res.name,
      //   bio: res.bio}))
      console.log(res);

    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

    function handleSubmit(e:any) {
      e.preventDefault()
      console.log("Running function");
      const input = e.target[0].value;
      axios.post("http://127.0.0.1:8000/create_embedding", {
        body:input
      }).then(function(res){
        console.log(res)
      }).catch(function (error) {
        console.log(error);
      });
    }
  return (
    <div className="App">
     <div className='flex flex-col justify-center items-center'>
      <form className='form-control' onSubmit={handleSubmit}>
        <p className='kbd my-2'>Input text to embed and store </p>
          <input className='input' name='input'>
          </input>
          <button type= "submit">
          Embed
      </button>
      </form>
      <p>{resStat}</p>
     </div>
    </div>
  )
}

export default App
