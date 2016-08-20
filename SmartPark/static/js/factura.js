$(function(){

	var keywords= [], keyproducts = []; //declaro un array

	$('#txtCedula').autocomplete({
		source: keywords , 
		select: function(){
			
			$.ajax({
				url: "/misitio/index.php/cfactura/getCliente/",
				type: "POST",
				data: {"cedula":$("#txtCedula").val()},
				dataType : "json",
				success: function(response){
					$("#txtNombre").val(response.cliente.cli_nom);
					$("#txtApellido").val(response.cliente.cli_ape);
					$("#txtDireccion").val(response.cliente.cli_dir);
					$("#txtTelefono").val(response.cliente.cli_tel);
					$("#txtEmail").val(response.cliente.cli_eml);
					$('#txtProductos').focus();
				},
			});

		},
	});

	$('#txtProductos').autocomplete({
		source: keyproducts ,
		select: function(){
			$.ajax({
				url: "/misitio/index.php/cfactura/getProducto/",
				type: "POST",
				data: {"id":$("#txtProductos").val()},
				dataType : "json",
				success: function(response){
					var detalle = "";
					detalle = "<div class='form-group col-sm-6'>"+ 
					"<tr>"+					
					"<td align='center'> <input type='text' class='control-form' value='"+response.producto.pro_des+"'></td>"+
					"<td aling='center'> <input type='text' class='control-form' value='"+response.producto.pro_pvp+"'></td>"+
					"<td aling='center'> <input type='text' class='control-form'></td>"+					
					"<td align='center'> <button type='button' class='btn btn-default'>  <span class='glyphicon glyphicon-remove' aria-hidden='true'></span></button> </td>"+
					"</tr>"+
					"</div>";
					$("#tbodyDetails").html(detalle);	
				},
			});
		},
	});



	$.getId = function(response){
		$.each(response.cedula, function(key, value){
			keywords[key] = value.cli_ced;			
		});
	};

	$.getPro = function(response){
		$.each(response.producto , function(key, value){
			keyproducts[key] = value.pro_des;
		});
	};

	$.post("/misitio/index.php/cfactura/autocompletar_cliente/",$.getId);
	$.post("/misitio/index.php/cfactura/autocompletar_producto/",$.getPro);
});