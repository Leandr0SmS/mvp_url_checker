import { config } from "./config.js";
const { useState } = React;
const { createRoot } = ReactDOM;

function UrlCheck({ onClickHandle, inputChangeHandler, inputValue }) {
    return (
        <form id="url_form">
            <input 
                className="url_input" 
                id="url_Input" 
                type="input"
                onChange={inputChangeHandler}
                value={inputValue}
            />
            <button 
                type="button" 
                id="url_check_btn"
                onClick={onClickHandle}
            >
                Check
            </button>
        </form>
    )
}

function App() {

    const [urlToCheck, setUrlToCheck] = useState("");
    const [urlStatus, setUrlStatus] = useState("");

    const handleCheckClick = async (e) => {
        e.preventDefault();

        const formData = new FormData();
  
        formData.append('url_str', urlToCheck);

        const response = await fetch(`${config.baseUrl}/url_check`, {
            method: 'post',
            body: formData
          })
          if (!response.ok) {
            throw new Error(`${response.status}`);
          }
          const resJson = await response.json();
          setUrlStatus(resJson)
    };

    function handleInputChange(e) {
        setUrlToCheck(e.target.value);
    }

    console.log(urlStatus)

    return (
        <React.Fragment>
            <h1 id="title">URL CHECK</h1>
            <UrlCheck
                inputChangeHandler={handleInputChange}
                inputValue={urlToCheck}
                onClickHandle={handleCheckClick}
            />
            {
                urlStatus
                ? urlStatus.url_predic == 1
                    ? <h2>Phishing</h2>
                    : <h2>Good</h2>
                : undefined
            }
        </React.Fragment>
    )
}

//Render
const app = document.getElementById('root');
const root = createRoot(app);
root.render(<App/>);