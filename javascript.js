

function calculate() {
	var price = parseFloat(document.getElementById("price").value)
	var multiplier = parseFloat(document.getElementById("service").value)
	var splitBy = parseInt(document.getElementById("splitBetween").value)

	var tip = price * multiplier
	var total =  tip + price
	var payEach = total / splitBy

	var group = [tip, total, payEach]

	for (var element of group) {
		group[group.indexOf(element)] = (Math.round(element*100) / 100).toFixed(2)
		// I don't like this. I miss python loops...
	}

	document.getElementById('outputTip').innerHTML = "Tip: £" + tip.toFixed(2)
	document.getElementById("outputTotal").innerHTML= "Total: £" + total.toFixed(2)
	document.getElementById("outputEach").innerHTML= "Pay Each: £" + payEach.toFixed(2)

	// y loop no work?

	console.log(total)
}