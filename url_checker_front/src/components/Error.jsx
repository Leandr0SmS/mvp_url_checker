import '../styles/main.css'

function Errors({ error }) {
    return (
        <div id="error--div">
            <p id="erro--status">
                {
                    error.status == 422
                        ? "Erro no formato de url... Inicie com 'https://'"
                        : error.status  
                }
            </p>
        </div>
    )
}

export default Errors