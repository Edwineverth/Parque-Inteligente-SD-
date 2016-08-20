$(function(){

	$('#frmMed').on("submit",function(){
		event.preventDefault();
		$.ajax({
			type:"POST",
			url: "/sgcm/cmedico/save/",
			dataType: 'json',
			data:$(this).serialize(),
			
			success: function(response){
				$.notify("Guardado Correctamente","success");
				$('#med_ced').val("");
				$('#med_nom').val("");
				$('#med_ape').val("");
				$('#med_dir').val("");
				$('#med_tel').val("");
				$('#med_eml').val("");
			},

			error: function(){
				$.notify("Error","error");
			}
		});

	});
	
	var btnsOpTblModels = "<button style='border: 0; background: transparent' data-target='#modalMedico' data-toggle='modal' onclick='$.editarModal($(this).parent())'>"+
							"<img src='/sich/static/img/edit.png' title='Editar'>"+
						  "</button>"+
						  "<button style='border: 0; background: transparent' onclick='$.eliminar($(this).parent())'>"+
							"<img src='/sich/static/img/delete.png' title='Eliminar'>"+
						  "</button>";

	$.renderizeRow = function( nRow, aData, iDataIndex ) {
	   $(nRow).append("<td class='text-center'>"+btnsOpTblModels+"</td>");
	   $(nRow).attr('id',aData['med_cod']); // 
	};
	
	//Llenar tabla de datos
	//Funcion que carga los datos
	$.fnTbl('#tbMedico',
			"/sgcm/cmedico/get/",
			[	{data:"med_ced"},
				{data:"med_nom"},
				{data:"med_ape"},
				{data:"med_dir"},
				{data:"med_tel"},
				{data:"med_eml"}
			],
			$.renderizeRow);
	
	$("#ltMedico").click(function(){
			event.preventDefault();
			$('#tbMedico').DataTable().ajax.reload();
	});

	$.eliminar = function(td){
		var tr = $(td).parent().children();
		var med_ced = tr[0].textContent;
		var med_e = 'FALSE';
		$.ajax({
			type: "POST",
			data: {"med_ced":med_ced,"med_e":med_e},
			url: "/sgcm/cmedico/delete/", 
			dataType: 'json',
			success: function(response){
				event.preventDefault();
				$.notify("Eliminado con exito","success");

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
		$('#mmed_nom').val(nom);
		$('#mmed_ape').val(ape);
		$('#mmed_dir').val(dir);
		$('#mmed_tel').val(tel);
		$('#mmed_eml').val(eml);
		$('#txtId').val(ced);
	};

	$('#btnModalGuardar').click(function(){
		event.preventDefault();
		$.ajax({
			type: "POST",
			data: { 
					"med_ced": $('#txtId').val(),
					"med_nom": $('#mmed_nom').val(), 
					"med_ape": $('#mmed_ape').val(), 
					"med_dir": $('#mmed_dir').val(),
					"med_tel": $('#mmed_tel').val(),
					"med_eml": $('#mmed_eml').val()
					},
			url: "/sgcm/cmedico/update/",
			dataType: 'json',			
			
			success: function(response){
				$('#modalMedico').modal('hide');				
				$.notify("Medico editado con exito","success");
				$('#tbMedico').DataTable().ajax.reload();
			},

			error: function(response){
				$.notify("Error al editar","error");
			}

		});
	});
			
	$('#modalMedico').bind('shown.bs.modal' , function(){
		med_nom.focus();
	});
	
	
});

