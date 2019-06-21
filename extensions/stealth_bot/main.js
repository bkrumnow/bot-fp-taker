function rewrite(obj, property, value_in){
	/** Rewrites on a single property of an object
		*	@type property is a string 
	 */
	let value = value_in != undefined ? value_in : eval(obj+"."+property) 
	let marks = typeof eval(obj+"."+property) == "string" ? "'"  : "";
	let value_string = marks + value + marks
	
	command = "Object.defineProperty(" + obj + ", '" + property + "', {\
		enumerable: true,\
		value: "+ value_string +"});";
	console.log(command)
	window.eval(command);
}

rewrite("navigator","webdriver",false);

