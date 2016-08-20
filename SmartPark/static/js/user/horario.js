$(function(){

	$('#frmNewHorario').on("submit",function(){
		event.preventDefault(); // no permite recarga
		$.ajax({
			type: "POST",
			url: "/sgcm/chorario/save/",
			dataType: 'json',
			data: $(this).serialize(),
			success: function(response){
				$.notify("Guardado Correctamente","success");
				$('#hor_des').val("");
				hor_des.focus();
			},

			error: function(){
				$.notify("Error","error");
			}

			});		
	});

	$.editarModal = function(td)
	{
		var tr = $(td).parent().children();
		var hor_des = tr[1].textContent;
		$('#myModalLabel').html("Editar");
		$('#mhor_des').val(hor_des);
		$('#txtId').val($(td).parent().attr('id'));
	};

	$.eliminar = function(td)
	{
		$.ajax({
			type: "POST",
			url: "/sgcm/chorario/delete/", 
			data: {"hor_cod":$(td).parent().attr('id')},
			dataType: 'json',
			success: function(response){
				$.notify("Eliminado con exito","success");
				$(td).parent().remove(); // remove a tr				
			},

			error: function(response){
				$.notify("El horario esta asignado, NO se puede eliminar","error");
			}

		});
	};


	var btnsOpTblModels = "<button style='border: 0; background: transparent' data-target='#modalHorario' data-toggle='modal' onclick='$.editarModal($(this).parent())'>"+
							"<img src='/sgcm/static/img/edit.png' title='Editar'>"+
						  "</button>"+
						  "<button style='border: 0; background: transparent' onclick='$.eliminar($(this).parent())'>"+
							"<img src='/sgcm/static/img/delete.png' title='Eliminar'>"+
						  "</button>";

	$.renderizeRow = function( nRow, aData, iDataIndex ) {
	   $(nRow).append("<td class='text-center'>"+btnsOpTblModels+"</td>");
	   $(nRow).attr('id',aData['hor_cod']); // 
	};
	
	//Llenar tabla de datos
	//Funcion que carga los datos
	$.fnTbl('#tbHorario',
			"/sgcm/chorario/get/",
			[{data:"hor_cod",},
			 {data:"hor_des"}
			 ],
			$.renderizeRow);
	
	$("#ltHorario").click(function(){
			event.preventDefault();
			$('#tbHorario').DataTable().ajax.reload();
	});


	$('#btnModalGuardar').click(function(){
		event.preventDefault();
		$.ajax({
			type: "POST",
			data: {
					"hor_cod":$('#txtId').val() , 
					"hor_des":$('#mhor_des').val()
				},
			url: "/sgcm/chorario/update/",
			dataType: 'json',
			
			success: function(response){
				$('#modalHorario').modal('hide');
				$.notify("Horario editado con exito","success");
				$('#tbHorario').DataTable().ajax.reload();
			},

			error: function(response){
				$.notify("Error al editar","error");
			}

		});
	});

});