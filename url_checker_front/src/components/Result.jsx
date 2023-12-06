import '../styles/main.css'

function Result({ status }) {

    const predict = status.url_predic;

    const resultClass = predict
                ? "result--status bad"
                : "result--status good"

    const resultDivClass = predict
                ? "result--div div-bad"
                : "result--div div-good"
    
    return (
        <div className={resultDivClass}>
            <h1 className={resultClass}>
                {
                    predict
                        ? "Phishing"
                        : "Legítimo"
                }
            </h1>
        </div>
    )
}

export default Result