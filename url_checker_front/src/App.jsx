import { useState, Fragment } from 'react'
import UrlCheck from './components/Form'
import Result from './components/Result'
import Errors from './components/Error'
import './styles/main.css'

const baseUrl = 'http://127.0.0.1:5000/'

function App() {

    const initError = { error: false, status: "" }

    const [urlToCheck, setUrlToCheck] = useState("");
    const [urlStatus, setUrlStatus] = useState("");
    const [error, setError] = useState(initError);

    const postData = async () => {

        const formData = new FormData();
        formData.append('url_str', urlToCheck);

        try {
            const response = await fetch(`${baseUrl}/url_check`, {
                                        method: 'post',
                                        body: formData
                                    });
    
            if (!response.ok) {
                // Checkar error status
                throw new Error(`Error! Status: ${response.status}`);
            }
    
            const result = await response.json();
            setError(initError)
            setUrlStatus(result);
        } catch (error) {
            setError(() => ({
                error: true,
                status: "Formato Url não suportado. Adicione 'https://'"
            }));
        }
      };

    const handleSubmit = (e) => {

        e.preventDefault()

        if (urlToCheck == "") {
            setError({
                error: true,
                status: "Url deve ser preenchido"
            })
        } else if (Number(urlToCheck)) {
            setError({
                error: true,
                status: "Url não pode ser um numero"
            })
        } else {
            postData()
        }
    };

    function handleInputChange(e) {
        setUrlStatus("")
        setError(initError)
        setUrlToCheck(e.target.value);
    }

    return (
        <Fragment>
            <h1 id="title">URL CHECK</h1>
            <UrlCheck
                inputChangeHandler={handleInputChange}
                inputValue={urlToCheck}
                onSubmitHandle={handleSubmit}
                error={error}
            />
            {
                error.error
                    ? <Errors 
                        error={error}
                      />
                    : urlStatus
                        ? <Result
                            status={urlStatus}
                          />
                        : undefined
            }
        </Fragment>
    )
}

export default App
