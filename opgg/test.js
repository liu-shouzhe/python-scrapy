a = function() {
    if (!Object(r.a)(i))
        return i;
    return ["hash", "host", "hostname", "href", "origin", "pathname", "port", "protocol", "search"].forEach((function(t) {
        i[t] = window.location[t]
    }
    )),
    i.search ? "?" === i.search[0] ? i.searchParam = Object(o.parseSearch)(i.search.substring(1)) : i.searchParam = Object(o.parseSearch)(i.search) : i.searchParam = {},
    i.hash ? "#" === i.hash.charAt(0) ? i.hashParam = Object(o.parseSearch)(i.hash.substring(1)) : i.hashParam = Object(o.parseSearch)(i.hash) : i.hashParam = {},
    i.getParamFromHref = function(t) {
        if (t)
            return void 0 !== i.searchParam[t] ? i.searchParam[t] : void 0 !== i.hashParam[t] ? i.hashParam[t] : void 0
    }
    ,
    i
}
function Oe() {
    return Object(a)().searchParam.mixKey
}
