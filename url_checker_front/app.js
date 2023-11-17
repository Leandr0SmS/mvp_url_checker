const { useState, useEffect } = React;
const { createRoot } = ReactDOM;

const UrlCheck = () => {
    return (
        <form id="url_form">
            <input className="url_input" id="url_Input" type="input"/>
            <button type="button" id="url_check_btn">Check</button>
        </form>
    )
}

const App = () => {
    return (
        <React.Fragment>
            <h1 id="title">URL CHECK</h1>
            <UrlCheck/>
        </React.Fragment>
    )
}

//Render
const app = document.getElementById('root');
const root = createRoot(app);
root.render(<App/>);