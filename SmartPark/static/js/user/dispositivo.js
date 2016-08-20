/**
 * Created by Leonardo on 3/8/2016.
 */
$(function(){

	



	

	/**$.renderizeRow = function( nRow, aData, iDataIndex )
	{
		if(aData['usu_est'] == 't')
		{
			$(nRow).append("<td class='text-center'>"+
							"<button type='button' class='btn btn-danger' onclick='$.eliminar($(this).parent());' id='btnEliminar'>"+
						  	"Desactivar"+
						  "</button></td>");
		}
		else
		{
			$(nRow).append("<td class='text-center'>"+
							"<button type='button' class='btn btn-success' onclick='$.activar($(this).parent());' id='btnActivar'>"+
						  	"Activar"+
						  "</button></td>");	
		}
		
		$(nRow).append("<td class='text-center'>"+btnsOpTblModels+"</td>");
		$(nRow).attr('id',aData['usu_cod']); //codigo
		$(nRow).attr('data-usudir',aData['usu_dir']);
		$(nRow).attr('data-tipcod',aData['tip_cod']);
		$(nRow).attr('data-usupas',aData['usu_pas']);
	};*/
	
	/**var lngEsp = {
		"sProcessing":     "Procesando...",
		"sLengthMenu":     "Mostrar _MENU_ registros",
		"sZeroRecords":    "No se encontraron resultados",
		"sEmptyTable":     "Ningún dato disponible en esta tabla",
		"sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
		"sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
		"sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
		"sInfoPostFix":    "",
		"sSearch":         "Buscar:",
		"sUrl":            "",
		"sInfoThousands":  ",",
		"sLoadingRecords": "Cargando...",
		"oPaginate": {
			"sFirst":    "Primero",
			"sLast":     "Último",
			"sNext":     "Siguiente",
			"sPrevious": "Anterior"
		}
	};*/
	
	/**$('#tbUsuario').DataTable({
		ordering: true,
		"ajax":{
			"url": "/sgcm/cusuario/get/",
			"dataSrc": "datos"
		},
		"columns":[{data:"usu_ced"},{data: "usu_nom"}, {data:"usu_ape"},{data:"usu_eml"},{data:"tipo"},{data:"usu_dir"}],
		"columnDefs": [
            {
                "targets": [5],
                "visible": false,
                "searchable": false
            }
        ],
        "fnCreatedRow": $.renderizeRow,
        "language": lngEsp
	});*/
	
	/**$("#ltUsuario").click(function(){
		event.preventDefault();
		$('#tbUsuario').DataTable().ajax.reload();
	});*/

	/**$.eliminar = function(td){
		var cedula = $(td).parent().children()[0].textContent; //cedula
		$.ajax({
			type: "POST",
			url: "/sgcm/cusuario/delete/", 
			data: {"id":cedula},
			dataType: 'json',
			success: function(response){
				$.notify("Eliminado con exito","success");
				$(td).parent().remove(); // remove a tr
				$('#tbUsuario').DataTable().ajax.reload();				
			},

			error: function(response){
				$.notify("Error al eliminar","error");
			}

		});
	};*/

	/**$.activar = function(td){
		event.preventDefault();
		var cedula = $(td).parent().children()[0].textContent; //cedula
		$.ajax({
			type: "POST",
			url: "/sgcm/cusuario/activar/", 
			dataType: 'json',
			data: {"id":cedula},			
			success: function(response){
				$.notify("Activado con exito","success");
				$('#tbUsuario').DataTable().ajax.reload();
			},
			error: function(response){
				$.notify("Error al activar","error");
			}
		});
	};*/
	
	$.editarModal = function(td)
	{
		
		var trChildren 	= $(td).parent().children();
		var id          = trChildren[0].textContent;
        var nom 		= trChildren[1].textContent;
		var mac 		= trChildren[2].textContent;
		var est 		= trChildren[3].textContent;
		var emp 		= trChildren[4].textContent;
		//var tip_user	= $(td).parent().attr('data-tipcod');
        $('#txtId2').val(id)
		$('#txtNombre2').val(nom);
		$('#txtMac2').val(mac);
		$('#selectEstado2').val(est)
		$('#selectParque2').val(emp);
	};

	$('#btnModalActualizar').click(function(){
		alert("entroUP")
		//event.preventDefault();
		$.ajax({
			alert("entroUP2")
			data: {
					"id":$('#txtId2').val(),
					"nombre":$('#txtNombre2').val() , 
					"mac":$('#txtMax2').val() , 
					"est":$('#selectEstado2').val(),
					"parque": $('#selectParque2').val() , 
					},
			type: "POST",
			url: '{% url 'ActualizarDispositivo' %}',
			success: function(response){
				$('#myModalEdit').modal('hide');
				alert("Exito")
				//$.notify("Dispositivo editado con exito","success");
				$('#data-table-simple').DataTable().ajax.reload();
			},
			error: function(response){
				alert("Error")
				//$.notify("Error al editar","error");
			}
		});
	});
   
});