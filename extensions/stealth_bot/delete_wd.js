//window.eval("Object.defineProperty(navigator, 'webdriver', {get: () => false});");
window.eval("navigator.webdriver = false;");
/*
navigator.wrappedJSObject.webdriver = false;

Object.defineProperty(navigator, 'webdriver', {
    get: () => false,
});


Object.defineProperties(window.navigator, {
	webdriver: {
		value:false,
		enumerable: false,
		configurable: false,
		writable: false
	}
});  
*/