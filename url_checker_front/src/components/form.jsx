import '../styles/main.css'

function UrlCheck({ onSubmitHandle, inputChangeHandler, inputValue, error }) {
    
    const inputClass = error.error
        ? "url_input url_input_error"
        : "url_input url_input_norm"
    
    return (
        <form 
            id="url_form"
            onSubmit={onSubmitHandle}
        >
            <input 
                className={inputClass} 
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