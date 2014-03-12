$(document).on("ready", inicio);
		
	function inicio(){
		$(".ContTitSecciones div").on("click", MuestraSeccion);
	}

	function MuestraSeccion(evento) {
		var SecAct = evento.currentTarget.id;
		//var NumSec = NvaSec.substr(6,1);
		//console.log("Seccion: " + NumSec);

		$(".ContTitSecciones div").attr('class', 'Seccion');
		$("#" + SecAct).attr('class', 'SeccionActivo');

		$(".InfSeccion").css('display', 'none');
		$("#C" + SecAct).css('display', 'block');
	}