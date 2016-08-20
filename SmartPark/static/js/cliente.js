$(function(){

	

	$('#frmMul').on("submit",function(){
		event.preventDefault();
		console.log('pasa');
		$.ajax({
			type:"POST",
			url: "/misitio/ccliente/save/",
			dataType: 'json',
			data:$(this).serialize(),
			success: function(response){
				$.notify("Guardado Correctamente","success");
			},

			error: function(){
				$.notify("Error","error");
			}
		});

	});

	/*
	$.getTable = function(response){

		var elementos = "";
		$.each(response.datos,function(key,value){
			elementos+= "<tr id="+key+">"+
					"<td>"+value.cli_ced+"</td>"+
					"<td>"+value.cli_nom+"</td>"+
					"<td>"+value.cli_ape+"</td>"+
					"<td>"+value.cli_dir+"</td>"+
					"<td>"+value.cli_tel+"</td>"+
					"<td>"+value.cli_eml+"</td>"+
					"<td><button type='button' class='btn btn-primary' data-target='#modalCliente' data-toggle='modal' onclick='$.editarModal($(this).parent());' id='btnEditar'>Editar</button></td>"+
					"<td><button type='button' class='btn btn-danger' onclick='$.eliminar($(this).parent());' id='btnEliminar'>Eliminar</button></td>"+
					"</tr>";
		});
		$('#tblBody').append(elementos);
	};
*/
	var btnsOpTblModels = "<button style='border: 0; background: transparent' data-target='#modalCliente' data-toggle='modal' onclick='$.editarModal($(this).parent())'>"+
							"<img src='/sich/static/img/edit.png' title='Editar'>"+
						  "</button>"+
						  "<button style='border: 0; background: transparent' onclick='$.eliminar($(this).parent())'>"+
							"<img src='/sich/static/img/delete.png' title='Eliminar'>"+
						  "</button>";

	$.renderizeRow = function( nRow, aData, iDataIndex ) {
	   $(nRow).append("<td class='text-center'>"+btnsOpTblModels+"</td>");
	   $(nRow).attr('id',aData['cli_cod']); // 
	};
	
	//Llenar tabla de datos
	//Funcion que carga los datos
	$.fnTbl('#tbClients',
			"/misitio/ccliente/get/",
			[{data:"cli_ced"},{data:"cli_nom"},{data:"cli_ape"},{data:"cli_dir"},{data:"cli_tel"},{data:"cli_eml"}],
			$.renderizeRow);
	
	$("#ltClient").click(function(){
			event.preventDefault();
			$('#tbClients').DataTable().ajax.reload();
	});

	
	$.eliminar = function(td){
		var cedula = $(td).parent().children()[0].textContent; //cedula
		$.ajax({
			type: "POST",
			url: "/misitio/ccliente/delete/", 
			data: {"id":cedula},
			dataType: 'json',
			success: function(response){
				$.notify("Eliminado con exito","success");
				$(td).parent().remove(); // remove a tr				
			},

			error: function(response){
				$.notify("Error al eliminar","error");
			}

		});
	};

	$.editarModal = function(td)
	{
		var tr = $(td).parent().children();
		var ced = tr[0].textContent;
		var nom = tr[1].textContent;
		var ape = tr[2].textContent;
		var dir = tr[3].textContent;
		var tel = tr[4].textContent;
		var eml = tr[5].textContent;
		$('#myModalLabel').html("Editar");
		$('#nom').val(nom);
		$('#ape').val(ape);
		$('#dir').val(dir);
		$('#tel').val(tel);
		$('#eml').val(eml);
		$('#txtId').val(ced);
	};

	$('#btnModalGuardar').click(function(){
		event.preventDefault();
		$.ajax({
			type: "POST",
			data: {
					"cedula":$('#txtId').val() , 
					"nombre":$('#nom').val() , 
					"apellido": $('#ape').val() , 
					"direccion":$('#dir').val(),
					"telefono":$('#tel').val() , 
					"email": $('#eml').val()
				},
			url: "/misitio/ccliente/update/",
			dataType: 'json',
			
			success: function(response){
				$('#modalCliente').modal('hide');
				$.notify("Cliente editado con exito","success");
				$('#tbClients').DataTable().ajax.reload();
			},

			error: function(response){
				$.notify("Error al editar","error");
			}

		});
	});
			
	$('#modalCliente').bind('shown.bs.modal' , function(){
		nom.focus();
	});
	
});