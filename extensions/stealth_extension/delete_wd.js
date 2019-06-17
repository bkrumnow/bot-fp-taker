console.log("I AM WORKING");
Object.defineProperties(window.navigator, {
	webdriver: {
		value:false,
		enumerable: false,
		configurable: false,
		writable: false
	}
});  
/*console.log("Window 1: window.navigator.webdriver")
console.log(window.navigator.webdriver)
Object.defineProperties(window.navigator, {webdriver: {value:false}});
*/