import { useState, Fragment } from 'react'
import './styles/main.css'

const baseUrl = 'http://127.0.0.1:5000/'

function UrlCheck({ onSubmitHandle, inputChangeHandler, inputValue }) {
    return (
        <form 
            id="url_form"
            onSubmit={onSubmitHandle}
        >
            <input 
                className="url_input" 
                id="url_Input" 
                type="input"
                onChange={inputChangeHandler}
                value={inputValue}
                placeholder="Adicione um URL..."
            />
            <button 
                type="submit" 
                id="url_check_btn"
            >
                Check
            </button>
        </form>
    )
}

function App() {

    const [urlToCheck, setUrlToCheck] = useState("");
    const [urlStatus, setUrlStatus] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault()

        const formData = new FormData();
  
        formData.append('url_str', urlToCheck);

        const response = await fetch(`${baseUrl}/url_check`, {
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
        <Fragment>
            <h1 id="title">URL CHECK</h1>
            <UrlCheck
                inputChangeHandler={handleInputChange}
                inputValue={urlToCheck}
                //onClickHandle={handleCheckClick}
                onSubmitHandle={handleSubmit}
            />
            {
                urlStatus
                ? urlStatus.url_predic == 1
                    ? <h2>Phishing</h2>
                    : <h2>Good</h2>
                : undefined
            }
        </Fragment>
    )
}

export default App
