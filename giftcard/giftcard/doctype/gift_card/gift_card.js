// Copyright (c) 2018, ahmad ragheb and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gift Card', {
	refresh: function(frm) {

	}

});

cur_frm.cscript.validate = function(doc, dt, dn) { 
		var ww = $("[data-fieldname=card_number]");
		var svg = ww.find('svg')[0];
		JsBarcode(svg, makeid()  , {height: 40});

		cur_frm.doc.refresh("card_number");
	 }


function makeid() {
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < 9 ; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

  return text;
}

