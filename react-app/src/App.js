import { useState } from "react";
import axios from "axios";
import "./App.css";
import PieChart from "./PieChart";
import InfoCard from "./InfoCard";
import {
  Chart,
  ArcElement,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
Chart.register(
  ArcElement,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);



function App() {
  // new line start
  const scanOption = ["Sentiment", "Spam", "Summary"];
  const [checkedState, setCheckedState] = useState(
    new Array(scanOption.length).fill(false)
  );

  const [result, setResultData] = useState(null);
  const [sentimentData, setSentimentData] = useState(null);
  const [spamData, setSpamData] = useState(null);

  let initialState = {
    name: "Enter your text here",
    options: [],
  };
  const [analysisForm, setAnalysisForm] = useState(initialState);

  function getData(e) {
    e.preventDefault();
    axios({
      method: "post",
      url: "http://localhost:5000/spam",
      data: JSON.stringify(analysisForm),
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => {
        const res = response.data;
        console.log(res);
        setResultData({
          paragraph: res.summary ? res.summary : null,
          options: [
            res.sentiment ? res.sentiment : null,
            res.spam ? res.spam : null,
          ],
          sentimentValue: res.sentimentValue,
        });
        if (res.sentimentValue)
          setSentimentData({
            labels: ["Negative", "Positive", "Neutral"],
            datasets: [
              {
                label: "Sentiment analysis",
                data: res.sentimentValue,
                backgroundColor: ["#ecf0f1", "#50AF95", "#f3ba2f"],
                borderColor: "black",
                borderWidth: 2,
              },
            ],
          });
        else setSentimentData(null);
        if (res.spamValue)
          setSpamData({
            labels: ["Spam", "Not spam"],
            datasets: [
              {
                label: "Spam analysis",
                data: res.spamValue,
                backgroundColor: ["#ecf0f1", "#50AF95", "#f3ba2f"],
                borderColor: "black",
                borderWidth: 2,
              },
            ],
          });
        else setSpamData(null);
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
    setAnalysisForm((prev) => {
      return { ...prev, [name]: value };
    });
  };

  const handleOnChange = (position) => {
    const updatedCheckedState = checkedState.map((item, index) =>
      index === position ? !item : item
    );

    setCheckedState(updatedCheckedState);

    setAnalysisForm((prev) => {
      let choices = [];

      for (let i = 0; i < checkedState.length; i++) {
        if (updatedCheckedState[i]) {
          choices.push(scanOption[i].toLowerCase());
        }
      }

      return { ...prev, options: choices };
    });
  };

  return (
    <div className="Overall-app">
      <header className="App-header">
        <img src="sss_logo.png" className="App-logo" alt="logo" />
        <h1 className="App-title">SUSSANAH</h1>
      </header>

      <div className="App-info">
        <InfoCard
          title="Sentiment Analysis"
          children={"Enter any text below and have Sussannah analyze it for you! She can analyze it either for sentiment, spam, or summary."}
        />

        <InfoCard
          title="Spam Detection"
          children={"Sussanah analyzes the emotion in the text and displays a pie chart of emotions shown"}
        />

        <InfoCard
          title="Text Summary"
          children={"Sussanah condenses the text into a brief overview capturing the main points."}
        />
      </div>

      <div className="App-description">
        <form onSubmit={getData}>
          <textarea
            class="text-input"
            type="text"
            name="paragraph"
            value={analysisForm.paragraph}
            onChange={(e) => onChangeHandler(e.target)}
            rows="3"
            placeholder="Start your first message with Sussannah"
          />
        </form>
      </div>

      {/*newline*/}
      <br></br>
      <form className="form" onSubmit={getData}>
        {scanOption.map((name, index) => {
          return (
            <div className="App-buttons-outer">
              <div className="App-buttons">
                <li className="checkbox-container" id="Buttons-list" key={index}>
                  <input
                    type="checkbox"
                    id={`custom-checkbox-${index}`}
                    name={name}
                    value={name}
                    checked={checkedState[index]}
                    onChange={() => handleOnChange(index)}
                    className="checkbox-input"
                  />
                  <label
                    htmlFor={`custom-checkbox-${index}`}
                    className="checkbox-label">{name}
                  </label>
                </li>
              </div>
            </div>
          );
        })}
        <br />
        <div className="Submit-button color-change">
          <input className="button color-change" type="submit" value="Submit" />
        </div>
      </form>

      {/*newline*/}
      <div className="results-full">
        <h2>Your analysis details: </h2>
        {result && (
          <div className="Results-container">
            <div className="Charts-container">
              {(result.options.spam != null ||
                result.options.sentiment != null) && (
                  <p>Result: {result.options}</p>
                )}
              {spamData && (
                <div id="spam_chart">
                  <p>Spam analysis</p>
                  <PieChart chartData={spamData} />
                </div>
              )}
              {sentimentData && (
                <div id="sentiment_chart" class="chart">
                  <p>Sentiment analysis</p>
                  <PieChart chartData={sentimentData} />
                </div>
              )}
            </div>
            <div className="summary-container">
              {result.paragraph && <p className="summary-result">Summary: {result.paragraph}</p>}
            </div>
          </div>
        )}
      </div>
      {/*end*/}
    </div>
  );
}

export default App;