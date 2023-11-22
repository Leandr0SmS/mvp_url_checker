const { useState, useEffect } = React;
const { createRoot } = ReactDOM;

const UrlCheck = ({onClickHandle, inputChangeHandler, inputValue}) => {
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

const App = () => {

    const [urlToCheck, setUrlToCheck] = useState("");
    const [urlStatus, setUrlStatus] = useState("");

    const handleInputChange = (e) => {
        setUrlToCheck(e.target.value);
    }

    const handleCheckClick = () => {
        if (urlToCheck) {
            const result = checkerURL(urlToCheck);
            setUrlStatus(result);
            console.log(`URL Checked: ${result.url}`)
        } else {
            console.log(`URL Checked: Fail`)
        }
    }

    return (
        <React.Fragment>
            <h1 id="title">URL CHECK</h1>
            <UrlCheck
                inputChangeHandler={handleInputChange}
                inputValue={urlToCheck}
                onClickHandle={handleCheckClick}
            />
            <h2>{urlStatus}</h2>
        </React.Fragment>
    )
}

//Render
const app = document.getElementById('root');
const root = createRoot(app);
root.render(<App/>);