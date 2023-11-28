import '../styles/main.css'

function Result({ status }) {
    return (
        <div id="result--div">
            <h1 class="result--status">
                {
                    status == 1
                        ? "Phishing"
                        : "Good"
                }
            </h1>
        </div>
    )
}

export default Result