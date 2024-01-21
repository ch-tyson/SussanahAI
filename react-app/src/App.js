import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  // new line start
  const [profileData, setProfileData] = useState(null);

  let initialState = {
    name: "Enter your text here",
  };
  const [person, setPerson] = useState(initialState);

  function getData(e) {
    e.preventDefault();
    axios({
      method: "post",
      data: JSON.stringify(person),
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => {
        const res = response.data;
        console.log(res);
        setProfileData({
          profile_name: res.message,
          about_me: res.message,
        });
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  }
  //end of new line

  const onChangeHandler = (event) => {
    const { name, value } = event;
    setPerson((prev) => {
      return { ...prev, [name]: value };
    });
  };

  return (
    <div className="Overall-app">
      <header className="App-header">
        <img src="sss_logo.png" className="App-logo" alt="logo" />
        <h1 className="App-title">SussanahAI</h1>

        <form onSubmit={getData}>
          <label>
            Name:
            <input
              type="text"
              name="name"
              value={person.name}
              onChange={(e) => onChangeHandler(e.target)}
            />
          </label>
          <input type="submit" value="Submit" />
        </form>

        <p className="App-description">
          Enter any text below and have Sussannah analyze it for you! She can
          analyze it either for sentiment, spam, or summary. <br></br>
          <b>Sentiment</b>: Sussanah analyzes the emotion in the text and
          displays a pie chart of emotions shown. <br></br>
          <b>Spam</b>: Sussanah analyzes the text and indicates how much is
          considered spam. <br></br>
          <b>Summary</b>: Sussanah condenses the text into a brief overview
          capturing the main points.
        </p>
      </header>
      <body className="App-body">
        <div className="App-input">
          <textarea
            className="App-text"
            placeholder="Enter text here"
          ></textarea>
        </div>
        <div className="App-buttons">
          <button className="App-button">Sentiment</button>
          <button className="App-button">Spam</button>
          <button className="App-button">Summary</button>
        </div>
        <div className="App-output">
          <div className="App-pie"></div>
          <div className="App-spam"></div>
          <div className="App-summary"></div>
        </div>
      </body>
      <footer className="App-footer"></footer>
    </div>
  );
}

export default App;
