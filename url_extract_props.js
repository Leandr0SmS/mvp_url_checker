const dataJson = require('./dataset_phishing_json');

const urlLenCount = url => url.length;

const urlLenHostname = url => url.hostname.length;

const urlNbCountChar = (url, char, scape) => {
    let regExp;
    scape
        ? regExp = new RegExp("\\" + `${char}`, "g")
        : regExp = new RegExp(`${char}`, "g")
    const found = url.match(regExp);
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
        const urlTestObj = new URL(data.url)
        const urlTest = data.url

        check.url = urlTest

        urlLenCount(urlTest) == data.length_url
            ? check.length_url = true
            : check.length_url = false
        
        urlLenHostname(urlTestObj) == data.length_hostname
            ? check.length_hostname = true
            : check.length_hostname = false

        urlNbCountChar(urlTest, "$", true) == data.nb_dollar
            ? check.nb_dollar = true
            : check.nb_dollar = false

        urlNbCountChar(urlTest, ".", true) == data.nb_dots
            ? check.nb_dots = true
            : check.nb_dots = false

        urlNbCountChar(urlTest, "-", true) == data.nb_hyphens
            ? check.nb_hyphens = true
            : check.nb_hyphens = false
        
        urlNbCountChar(urlTest, "_", true) == data.nb_underscore
            ? check.nb_underscore = true
            : check.nb_underscore = false

        urlNbCountChar(urlTest, "~", true) == data.nb_tilde
            ? check.nb_tilde = true
            : check.nb_tilde = false
        
        urlNbCountChar(urlTest, "%", true) == data.nb_percent
            ? check.nb_percent = true
            : check.nb_percent = false
        
        urlNbCountChar(urlTest, "/", true) == data.nb_slash
            ? check.nb_slash = true
            : check.nb_slash = false

        urlNbCountChar(urlTest, ":", true) == data.nb_colon
            ? check.nb_colon = true
            : check.nb_colon = false
        
        urlNbCountChar(urlTest, ",", true) == data.nb_comma
            ? check.nb_comma = true
            : check.nb_comma = false
        
        urlNbCountChar(urlTest, ";", true) == data.nb_semicolumn
            ? check.nb_semicolumn = true
            : check.nb_semicolumn = false

        urlNbCountChar(urlTest, "www", false) == data.nb_www
            ? check.nb_www = true
            : check.nb_www = false

        const urlOriginLen = urlTestObj.origin.length;
        const path = urlTest.substring(urlOriginLen);
        urlNbCountChar(path, "http", false) == data.http_in_path
            ? check.http_in_path = true
            : check.http_in_path = false

        result.push(check)
    }
    return result.map(d => {
        if (Object.values(d).some(value => value === false)) {
            return d
        } else {
            return true
        }
    })
}

console.log(url_checker(dataJson));