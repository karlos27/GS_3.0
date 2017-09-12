//function surt(){ 
	//var caixa = document.createElement("div");
	//var dins = document.createTextNode("");
	//caixa.appendChild(dins);
	//document.getElementById("sortida").appendChild(caixa);

//}

function resposta(){
	alert('El teu missatge s\'ha enviat correctament.');
}

function perfil(){
	alert('S\'han modificat les dades del teu perfil correctament.');
}

function surt(){
	alert('Heu sortit correctament. Fins a la pròxima!');
}

$(document).ready(function() {
		
		$('.up').click(function() {
			$('body, html').animate( {
				scrollTop:'0px'
			}, 500);
		});

		$(window).scroll(function() {
			if( $(this).scrollTop() > 0) {
				$('.up').slideDown(500);
			}
			else {
				$('.up').slideUp(500);
			}

		});
});

