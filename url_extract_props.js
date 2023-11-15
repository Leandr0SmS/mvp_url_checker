const dataJson = require('./dataset_phishing_json');

const urlLenCount = url => url.href.length;

const urlLenHostname = url => url.hostname.length;

const urlNbCountChar = (url, char) => {
    const urlString = url.href;
    const regExp = new RegExp("\\" + `${char}`, "g");
    const found = urlString.match(regExp);
    if (found) {
        return found.length
    } else {
        return 0
    }
}

const url_checker = (dataSet) => {
    const result = [];
    for (let data of dataSet) {
        const check = {};
        const urlTest = new URL(data.url)

        data.url.length == data.length_url
            ? check.length_url = true
            : check.length_url = false
        
        urlLenHostname(urlTest) == data.length_hostname
            ? check.length_hostname = true
            : check.length_hostname = false

        urlNbCountChar(urlTest, "$") == data.nb_dollar
            ? check.nb_dollar = true
            : check.nb_dollar = false

        urlNbCountChar(urlTest, ".") == data.nb_dots
            ? check.nb_dots = true
            : check.nb_dots = false

        urlNbCountChar(urlTest, "-") == data.nb_hyphens
            ? check.nb_hyphens = true
            : check.nb_hyphens = false
        
        urlNbCountChar(urlTest, "_") == data.nb_underscore
            ? check.nb_underscore = true
            : check.nb_underscore = false

        urlNbCountChar(urlTest, "~") == data.nb_tilde
            ? check.nb_tilde = true
            : check.nb_tilde = false
        
        urlNbCountChar(urlTest, "%") == data.nb_percent
            ? check.nb_percent = true
            : check.nb_percent = false
        
        urlNbCountChar(urlTest, "/") == data.nb_slash
            ? check.nb_slash = true
            : check.nb_slash = false

        urlNbCountChar(urlTest, ":") == data.nb_colon
            ? check.nb_colon = true
            : check.nb_colon = false
        
        urlNbCountChar(urlTest, ",") == data.nb_comma
            ? check.nb_comma = true
            : check.nb_comma = false
        
        urlNbCountChar(urlTest, ";") == data.nb_semicolumn
            ? check.nb_semicolumn = true
            : check.nb_semicolumn = false

        urlNbCountChar(urlTest, "\s") == data.nb_space
            ? check.nb_space = true
            : check.nb_space = false

        result.push(check)
    }
    return result.map(d => {
        if (Object.values(d).some(value => value === false)) {
            return d
        }
    })
}

console.log(url_checker(dataJson));