var rowNum = 0;
var foodItems = ["Select Food Item", "Idli", "Dosa", "Uppit", "Chapati", "Curry", "Rice", "Salad", "Fruits"];
var Quantity =["Quantity", 1, 2, 3];

function createRow(){
	rowNum = 0;	
	addRow();
	
	//create a Add button
	var btn = document.createElement("BUTTON");
	btn.setAttribute("id", "addBtn");
	btn.onclick = addRow;
	var t = document.createTextNode("Add Row");  
	btn.appendChild(t);                         
	document.getElementById("addButton").appendChild(btn);	
}

function addRow(){
	var foodRow = "row" + rowNum + "food";
	var quantityRow = "row" + rowNum + "quantity";
	rowNum++;
	
	// Create Food Select Element
	var x = document.createElement("SELECT");
	x.setAttribute("id", foodRow);
	document.getElementById("newRow").appendChild(x);
	
	// Add options to Food Select Element
	var i = 0;
	for(i=0; i<foodItems.length; i++){
		var z = document.createElement("option");
		z.setAttribute("value", foodItems[i]);
		var t = document.createTextNode(foodItems[i]);
		z.appendChild(t);
		document.getElementById(foodRow).appendChild(z);
	}

	// Create Quantity Select Element
	var x = document.createElement("SELECT");
	x.setAttribute("id", quantityRow);
	document.getElementById("newRow").appendChild(x);
	
	// Add options to Food Select Element
	var i = 0;
	for(i=0; i<Quantity.length; i++){
		var z = document.createElement("option");
		z.setAttribute("value", Quantity[i]);
		var t = document.createTextNode(Quantity[i]);
		z.appendChild(t);
		document.getElementById(quantityRow).appendChild(z);
	}
	// Add a new line
	var x = document.createElement("BR");
	x.setAttribute("id", "BR");
	document.getElementById("newRow").appendChild(x);

}