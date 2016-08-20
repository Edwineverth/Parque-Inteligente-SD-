$(function(){

	$('#frmUsu_save').on("submit",function(){
		event.preventDefault();
		//console.log('pasa');
		$.ajax({
			type:"POST",
			url: "/sgcm/cregistro_usuario/save/",
			dataType: 'json',
			data:$(this).serialize(),

			success: function(response){
				$.notify("Guardado Correctamente","success");
				$(window).attr('location', 'http://localhost/sgcm/');
				jQuery(window).attr('location', 'http://localhost/sgcm/');
			},

			error: function(){
				$.notify("Error","error");
			}
		});

	});
});