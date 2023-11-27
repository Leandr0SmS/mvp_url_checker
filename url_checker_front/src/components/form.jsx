import '../styles/main.css'

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

export default UrlCheck