import { useState } from "react";
import axios from "axios";
import "./App.css";
import logo from "./logo.svg";

function App() {
  // new line start
  const [profileData, setProfileData] = useState(null);

  function getData() {
    axios({
      method: "GET",
      url: "http://127.0.0.1:8000/",
    })
      .then((response) => {
        const res = response.data;
        console.log(res);
        setProfileData({
          profile_name: res.name,
          about_me: res.about,
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

        {/* new line start*/}
        <p>To get your profile details: </p>
        <button onClick={getData}>Click me</button>
        {profileData && (
          <div>
            <p>Profile name: {profileData.profile_name}</p>
            <p>About me: {profileData.about_me}</p>
          </div>
        )}
        {/* end of new line */}
      </header>
    </div>
  );
}

export default App;

// function App() {
//   return (
//     <div className="Overall-app">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <h1 className="App-title">SussanahAI</h1>
//         <p className="App-description">
//           Enter any text below and have Sussannah analyze it for you! She can
//           analyze it either for sentiment, spam, or summary. <br></br>
//           <b>Sentiment</b>: Sussanah analyzes the emotion in the text and
//           displays a pie chart of emotions shown. <br></br>
//           <b>Spam</b>: Sussanah analyzes the text and indicates how much is
//           considered spam. <br></br>
//           <b>Summary</b>: Sussanah condenses the text into a brief overview
//           capturing the main points.
//         </p>
//       </header>
//       <body className="App-body">
//         <div className="App-input">
//           <textarea
//             className="App-text"
//             placeholder="Enter text here"
//           ></textarea>
//         </div>
//         <div className="App-buttons">
//           <button className="App-button">Sentiment</button>
//           <button className="App-button">Spam</button>
//           <button className="App-button">Summary</button>
//         </div>
//         <div className="App-output">
//           <div className="App-pie"></div>
//           <div className="App-spam"></div>
//           <div className="App-summary"></div>
//         </div>
//       </body>
//       <footer className="App-footer"></footer>
//     </div>
//   );
// }

// export default App;
