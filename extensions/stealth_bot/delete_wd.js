console.log("Working")
window.eval("Object.defineProperty(window.navigator, 'webdriver', {\
					enumerable: true,\
					value:      false,\
					configurable: true,\
					writable: true});")

console.log(window.navigator.webdriver)
console.log(window.eval("window.navigator.webdriver"))


/*script = document.createElement("script");
script.setAttribute("type", "text/javascript");
script.setAttribute("id", "stealth_bot_script");
script.textContent = '// Pass the Webdriver test\
										Object.defineProperty(navigator, "webdriver", {\
										  get: () => false,\
										});';c 
document.documentElement.appendChild(script);

var script = document.getElementById("stealth_bot_script");
if (script) script.parentNode.removeChild(script);




//window.eval("Object.defineProperty(navigator, 'webdriver', {get: () => false});");
/*
console.log("Is enumerable?: " + navigator.webdriver.propertyIsEnumerable());
console.log("Content script: " + navigator.webdriver);
console.log("Page script: " + navigator.wrappedJSObject.webdriver);

window.eval("Object.defineProperty(window.navigator, 'webdriver', {\
					enumerable: false,\
					value:      false});\
					");


console.log("Content script: " + navigator.webdriver);
console.log("Page script: " + navigator.wrappedJSObject.webdriver);
*/
/*window.eval("Object.defineProperties(navigator, {webdriver: {value:false,enumerable: true,configurable: true,writable: true}});");
window.eval("Object.defineProperty(navigator, 'userAgent', {\
    get: function() {\
        return 'WalshBot';\
    }\
});")
//window.eval("navigator.userAgent='BBoysBot'")
//window.eval("navigator.webdriver=false")
console.log(navigator)

//XPCNativeWrapper(window.wrappedJSObject.foo);

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



//window.eval("Object.defineProperty(navigator, 'webdriver', {get: () => false});");
/*window.eval("Object.defineProperty(navigator, 'webdriver', {
    get: () => false,
});
");*/
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