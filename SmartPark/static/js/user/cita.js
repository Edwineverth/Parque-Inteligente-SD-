$(function(){

	var med_ced_global, esp_cod_global , dmh_cod_global, cit_tur_global ,usuario = [],usu_cod_com = [];
	var usu_cod_global = $('#usu_cod').attr('data-usucod'); 

	// LLENA EL COMBO BOX ESPECIALIDAD
	$.getDataForCmbEsp = function(response)
	{
		var datos = "";
		$.each(response.datos, function(i,value){
			datos+= "<option value="+value.esp_cod+">"+value.esp_des+"</option>";
		});

		$('#cmbEsp').html(datos);
	};

	/*
	$.getDataForHor = function(response){
		
		var datos = "";
		var dmh_cods;
		var contador=0;

		$.ajax({
			type: "POST",
			url: "/sgcm/ccita/getDmhPorDia/", 
			data: {			
					"cit_fec" : $('#cit_fec').val()
				},
			dataType: 'json',
			async: false,

			success: function(r){
					dmh_cods = r.datos;
			},

			error: function(r){
				$.notify("Error obteniendo cmh_cod por dia","error");
			}

		});

		
		 for (var i = 0 ; i < dmh_cods.length ; i++)
		 {
		 	for ( var j = 0 ; j < response.datos.length ; j++)
		 	{
		 		if( response.datos[j] !== null)
		 		{
		 			if((dmh_cods[i]["cit_dmh_cod"] === response.datos[j]["dmh_cod"]))
		 			{
		 				response.datos[j] = null;	
				 	}
		 		}		 		
		 	}
		 }

		 for (var y = 0 ; y < response.datos.length ; y++)
		 {
		 	if(response.datos[y] !== null)
		 	{
		 		datos+= "<tr>"+
				  		"<td>"+response.datos[y]["hor_des"]+"</td>"+ 
				  		"<td> <input type='checkbox' id='check"+contador+"' data-horcod="+response.datos[y]["hor_cod"]+" data-dmhcod="+response.datos[y]["dmh_cod"]+"></td>"+
				  		"</tr>";
				contador++;	
		 	}
		 }

		$('#bodyTbCita').html(datos);
	};*/

	
	// FUNCION QUE SE EJECUTA AL LLAMAR AL MODAL
	$.cita = function(td)
	{
		event.preventDefault();
		esp_cod_global = $('#cmbEsp').val();
		med_ced_global = $(td).parent().children()[0].textContent;
		$('#myModalLabel').html("Horarios Disponibles para "+$(td).parent().children()[1].textContent);
	};


	var btnsOpTblModels = "<button type='button' class='btn btn-primary' data-target='#modalCita' data-toggle='modal' onclick='$.cita($(this).parent());'>"+
						  "<span class='glyphicon glyphicon-list-alt' aria-hidden='true'></span>  Horario"+
						  "</button>";

	var tablaCita = $('#tbCita').dataTable();
///////////////////////////////////////////////////////////////////////	 EVENTO CHANGE DEL COMBO BOX
	
	$('#cmbEsp').change(function(){
		event.preventDefault();
		$.ajax({
				type: "POST",
				url: "/sgcm/ccita/getMedico/",
				dataType: 'json',
				data: {
					"esp_cod" : $(this).val()
				},
				success: function(s){
					tablaCita.fnClearTable();
					for(var i= 0 ; i < s.datos.length ; i++)
					{
						tablaCita.fnAddData([	s.datos[i]["med_ced"], 
												s.datos[i]["medico"],
												"<td>"+btnsOpTblModels+"</td>"
										]);
					}

					
				},
				error: function(response)
				{
					$.notify("error","error");
				}				
			});
	});

	//EVENTO AL CAMBIAR DE FECHA EN EL CONTROL ******************
	$('#cit_fec').on("change",function(){
		$.ajax({
			type: "POST",
			url: "/sgcm/ccita/getHorarioDisponible/", 
			data: {			
					"med_ced" : med_ced_global,
					"esp_cod" : esp_cod_global,
					"cit_fec" : $(this).val()
				},
			dataType: 'json',

			success: function(response){
				var datos ="";
				if(response.datos.length > 0)
				{
					$.each(response.datos, function(i,item){
						datos+= "<tr>"+
				  				"<td>"+item.hor_des+"</td>"+ 
				  				"<td> <input type='checkbox' id='check"+i+"' data-horcod="+item.hor_cod+" data-dmhcod="+item.dmh_cod+"></td>"+
				  				"</tr>";
					});
					$('#bodyTbCita').html(datos);						
				}				
			},
			error: function(response){
				$.notify("Error al cargar Horario Disponible","error");
			}

		});
	});

	//Evento al Cerrar el Modal - borra todas las filas
	$('#modalCita').on('hidden.bs.modal', function(){
		var rows = $('#bodyTbCita >tr');
		for(var i=0 ; i < $(rows).length ; i++)
		{
			$(rows)[i].remove();
		}
	});

	//Controla el evento change en un checkbox
	$(document).on('change', '[type=checkbox]', function (e) {
		
		dmh_cod_global = $(this).attr("data-dmhcod"); //
		var rows = $('#bodyTbCita >tr');

		if($(this).is(":checked"))
		{
			for(var i=0 ; i < $(rows).length ; i++)
			{
				if(!($("#check"+i).is(':checked')))  //unchecked y tiene data-dmhcod
				{
					$("#check"+i).prop("disabled",true);
				}			
			}
		}
		else
		{
			for(var j=0 ; j < $(rows).length ; j++)
			{
				$('#check'+j).prop("disabled",false);			
			}

		}
	});


	$('#btnGuardar').on("click", function(){
		
		$.ajax({
				type: "POST",
				url: "/sgcm/ccita/getTc/", 
				dataType: 'json',
				async: false,				
				success : function(response)
				{
					$('#modalCita').modal('hide');
					if(response.datos.turno !== null)
					{
						cit_tur_global = response.datos.turno;	
					}
					else
					{
						cit_tur_global =1;
					}
					
				},

				error : function(response)
				{
					$('#modalCita').modal('hide');
					$.notify("Error al guardar","error");						
				}
			});//ajax

		//***********************GUARDA LA CITA ********************************************************
		$.ajax({
				type: "POST",
				url: "/sgcm/ccita/save/", 
				dataType: 'json', 
				data:{
						"cit_dmh_cod" 	: dmh_cod_global,
						"cit_est" 		: true,
						"cit_fec" 		: $("#cit_fec").val(),
						"cit_tur"		: cit_tur_global,
						"usu_cod"		: usu_cod_global
					},
				success : function(response)
				{
					$('#modalCita').modal('hide');
					$.notify("Cita Guardada Correctamente","success");
				},

				error : function(response)
				{
					$('#modalCita').modal('hide');
					$.notify("Error al guardar","error");						
				}
			});//
	});

	
	

//***************************************************CARGAR TABLAS*****************************************************************

	$.verCita = function(td){

	};

	var printReport = "<button style='border: 0; background: transparent' data-target='#modalVerCita' data-toggle='modal' onclick='$.verCita($(this).parent())'>"+
						  "<img src='/sgcm/static/img/imprimir.png' title='Imprimir'>"+
						  "</button>";

	$.renderizeRow = function( nRow, aData, iDataIndex ) {
	   $(nRow).append("<td class='text-center'>"+printReport+"</td>");
	   //$(nRow).attr('id',aData['hor_cod']);
	};
	
	var tbCitDet = $('#tbCitDet');

	//DATATABLE CON FILTROS 
	tbCitDet.DataTable({
        ordering : true,
        "ajax": {
        	"type": 'POST',
            "url": "/sgcm/ccita/getCita/",
            "data": {usu_cod: usu_cod_global,
            		 tip_usu: $('#usu_cod').attr('data-usutip')},
            "dataSrc": 'datos'
        },
        "columns": [{data:"cit_tur"} , 
            		{data:"cit_fec"}, 
            		{data:"hor_des"},
            		{data:"usuario"},
            		{data:"medico"},
            		{data:"esp_des"}
            		],
        "fnCreatedRow": $.renderizeRow
        });
	
	$("#ltCita").click(function(){
			event.preventDefault();
			tbCitDet.DataTable().ajax.reload();
	});


	//llamada ComboBox Especialidad
	$.post("/sgcm/cespecialidad/get/",$.getDataForCmbEsp);
	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////// AUTOCOMPLETAR ***********

	$('#usuario').autocomplete({
		source: usuario , 
		select: function(t){
			for(var i = 0 ; i < usuario.length ; i++)
			{
				if(usuario[i] == $(this).val())
				{
					usu_cod_global = usu_cod_com[i];
				}
			}
			
		},
	});

	$.getUser = function(response)
	{
		if(response.datos.length !== 0)
		{
			$.each(response.datos,function(i,value){
				usuario[i] 		= value.usuario;
				usu_cod_com[i]	= value.usu_cod;
			});
			

		}
	};

	$.post("/sgcm/cusuario/getUserByNom/",$.getUser);

});//final