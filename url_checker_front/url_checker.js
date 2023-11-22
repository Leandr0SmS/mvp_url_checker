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

export const checkerURL = (url) => {
    const result = {}
    const urlObj = new URL(url)

    result.url = url;
    result.length_url = urlLenCount(url);
    result.length_hostname = urlLenHostname(urlObj);
    result.nb_dots = urlNbCountChar(url, ".", true);
    result.nb_hyphens = urlNbCountChar(url, "-", true);
    result.nb_underscore = urlNbCountChar(url, "_", true);
    result.nb_tilde = urlNbCountChar(url, "~", true);
    result.nb_percent = urlNbCountChar(url, "%", true);
    result.nb_slash = urlNbCountChar(url, "/", true);
    result.nb_colon = urlNbCountChar(url, ":", true);
    result.nb_comma = urlNbCountChar(url, ",", true);
    result.nb_semicolum = urlNbCountChar(url, ";", true);
    result.nb_dollar  = urlNbCountChar(url, "$", true);
    result.nb_www = urlNbCountChar(url, "www", false);

    const urlOriginLen = urlObj.origin.length;
    const path = url.substring(urlOriginLen);
    result.http_in_path = urlNbCountChar(path, "http", false);

    return result
}
