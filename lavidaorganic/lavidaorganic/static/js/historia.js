$(document).ready(function(){
	$('#id_peso_sino_0').click(function(){
		$('#explique').removeClass("hidden");
		$('#id_desea_rebajar').val("");		
	});

	$('#id_peso_sino_1').click(function(){
		$('#explique').addClass("hidden");
		$('#id_desea_rebajar').val("No");
	 });
	$('#id_levanta_noche_sino_0').click(function(){
		$('#explique2').removeClass("hidden");
		$('#id_levanta_noche').val("");
 	});

	$('#id_levanta_noche_sino_1').click(function(){
		$('#explique2').addClass("hidden");
		$('#id_levanta_noche').val("No");
	 });
	$('#id_dolor_inflamacion_sino_0').click(function(){
		$('#explique3').removeClass("hidden");
		$('#id_dolor_inflamacion').val("");
 	});

	$('#id_dolor_inflamacion_sino_1').click(function(){
		$('#explique3').addClass("hidden");
		$('#id_dolor_inflamacion').val("No");
	 });

	$('#id_estrenimiento_sino_0').click(function(){
		$('#explique4').removeClass("hidden");
		$('#id_estrenimiento').val("");
 	});

	$('#id_estrenimiento_sino_1').click(function(){
		$('#explique4').addClass("hidden");
		$('#id_estrenimiento').val("No");
	 });	
	$('#id_alergia_sino_0').click(function(){
		$('#explique5').removeClass("hidden");
		$('#id_alergia').val("");
 	});

	$('#id_alergia_sino_1').click(function(){
		$('#explique5').addClass("hidden");
		$('#id_alergia').val("No");
	 });
	$('#id_dolorperiodo_sino_0').click(function(){
		$('#explique6').removeClass("hidden");
		$('#id_sintomas_periodo').val("");
 	});

	$('#id_dolorperiodo_sino_1').click(function(){
		$('#explique6').addClass("hidden");
		$('#id_sintomas_periodo').val("No");
	 });
	$('#id_pastillas_sino_0').click(function(){
		$('#explique7').removeClass("hidden");
		$('#id_pastillas_anticonceptivas').val("");
 	});

	$('#id_pastillas_sino_1').click(function(){
		$('#explique7').addClass("hidden");
		$('#id_pastillas_anticonceptivas').val("No");
	 });
	$('#id_infecciones_sino_0').click(function(){
		$('#explique8').removeClass("hidden");
		$('#id_infecciones_vaginales').val("");
 	});

	$('#id_infecciones_sino_1').click(function(){
		$('#explique8').addClass("hidden");
		$('#id_infecciones_vaginales').val("No");
	 });
	$('#id_suplementos_sino_0').click(function(){
		$('#explique9').removeClass("hidden");
		$('#id_suplementos').val("");
 	});

	$('#id_suplementos_sino_1').click(function(){
		$('#explique9').addClass("hidden");
		$('#id_suplementos').val("No");
	 });	

	 /*Get genero */

	$('#id_genero').change(function() {
   		 if($(this).find('option:selected').text() == "Femenino"){
   		 	$('#periodoseccion').removeClass('nodisplay');
   		 }
	}); 
	$('#id_genero').change(function() {
   		 if($(this).find('option:selected').text() == "Masculino"){
   		 	$('#periodoseccion').addClass('nodisplay');
   		 }
	}); 
   	/*Inicializar*/
   	if($('#id_genero').find('option:selected').text() == "Femenino"){
   		 	$('#periodoseccion').removeClass('nodisplay');
   		 }	

	if(jQuery('input[name=peso_sino]:checked').val() == 'si'){
		$('#explique').removeClass("hidden");
	}
	if(jQuery('input[name=levanta_noche_sino]:checked').val() == 'si'){
		$('#explique2').removeClass("hidden");
	}
	if(jQuery('input[name=dolor_inflamacion_sino]:checked').val() == 'si'){
		$('#explique3').removeClass("hidden");
	}
	if(jQuery('input[name=estrenimiento_sino]:checked').val() == 'si'){
		$('#explique4').removeClass("hidden");
	}
	if(jQuery('input[name=alergia_sino]:checked').val() == 'si'){
		$('#explique5').removeClass("hidden");
	}
	if(jQuery('input[name=dolorperiodo_sino]:checked').val() == 'si'){
		$('#explique6').removeClass("hidden");
	}	
	if(jQuery('input[name=pastillas_sino]:checked').val() == 'si'){
		$('#explique7').removeClass("hidden");
	}	
	if(jQuery('input[name=infecciones_sino]:checked').val() == 'si'){
		$('#explique8').removeClass("hidden");
	}	
	if(jQuery('input[name=suplementos_sino]:checked').val() == 'si'){
		$('#explique9').removeClass("hidden");
	}	
	 if($(this).find('option:selected').text() == "Femenino"){
   	 	$('#periodoseccion').removeClass('nodisplay');
   	 }	

   	 /* CONCATENAR */
   	 $('#formulario').submit(function(){
   	 	var p1_s = "1. Por favor escriba lo que le está molestando:\n ";
   	 	var t1_s = $('#id_molestias').text();
   	 	var p2_s = "\n 2. ¿Cual es su meta? \n"
   	 	var t2_s = $('#id_meta').text();
   	 	var p3_s = " \n3. ¿En que punto de su vida se ha sentido mejor?\n ";
   	 	var t3_s = $('#id_punto_vida').text();
   	 	var p4_s = " \n4. ¿Alguna enfermedad/hospitalización/tratamiento serio el que yo deba saber?\n ";
   	 	var t4_s = $('#id_enfermedad').text();
   	 	var p5_s = " \n5. ¿Cómo es/era la salud de su madre y padre? \n";
   	 	var t5_s = $('#id_salud_madre').text();
   	 	var info_salud = p1_s + t1_s + p2_s + t2_s + p3_s + t3_s + p4_s + t4_s + p5_s + t5_s;
   	 	$('#id_informacion_salud').val(info_salud);
   	 	var p1_a = " \n1. ¿Tendrá el soporte de amigos y familiares para hacer los cambios necesarios? \n";
   	 	var t1_a = $('#id_soporte_amigos').text();
   	 	var p2_a = " \n2. ¿Que comida/alimento le cae absolutamente mal?\n ";
   	 	var t2_a = $('#id_comidas_mal').text();
   	 	var p3_a = " \n3. ¿Que considera usted descansar?\n ";
   	 	var t3_a = $('#id_descansar_definicion').text();
   	 	var p4_a = " \n4. ¿Tiene ansiedad al azúcar, cafe, cigarros o alguna adicción?\n ";
   	 	var t4_a = $('#id_adicciones').text();
   	 	var p5_a = " \n5. Lo mas importante que tengo que cambiar de mi dieta es:\n ";
   	 	var t5_a =$('#id_cambiar_dieta').text();
   	 	var p6_a = " \n6. ¿Alguna otra cosa que quiera compartir?\n ";
   		var t6_a = $('#id_algo_mas').text();
   		var info_alimentacion = p1_a + t1_a + p2_a + t2_a + p3_a + t3_a + p4_a + t4_a + p5_a + t5_a + p6_a + t6_a;
   		$('#id_informacion_alimentacion').val(info_alimentacion);
   		var p1_i ="\n Desayuno \n";
   		var t1_i = $('#id_desayuno_infancia').text();
   		var p2_i ="\n Almuerzo \n";
   		var t2_i = $('#id_almuerzo_infancia').text();
   		var p3_i ="\nCena\n";
   		var t3_i = $('#id_cena_infancia').text();
   		var p4_i ="\nMeriendas\n";
   		var t4_i = $('#id_merienda_infancia').text();
   		var p5_i ="\nLíquidos\n";
   		var t5_i = $('#id_liquido_infancia').text();
   		var alimentacion_infancia = p1_i + t1_i + p2_i + t2_i + p3_i + t4_i + p5_i + t5_i;
   	 	$('#id_alimentacion_infancia').val(alimentacion_infancia);
   		var p1_n ="\n Desayuno \n";
   		var t1_n = $('#id_desayuno_actual').text();
   		var p2_n ="\n Almuerzo \n";
   		var t2_n = $('#id_almuerzo_actual').text();
   		var p3_n ="\nCena\n";
   		var t3_n = $('#id_cena_actual').text();
   		var p4_n ="\nMeriendas\n";
   		var t4_n = $('#id_merienda_actual').text();
   		var p5_n ="\nLíquidos\n";
   		var t5_n = $('#id_liquido_actual').text();
   		var alimentacion_actual = p1_n + t1_n + p2_n +t2_n+ p3_n + t4_n + p5_n + t5_n;
   	 	$('#id_alimentacion_actual').val(alimentacion_actual);   	
   	 });
   	 
   	 /*Validación sólo números */
function onlynumber (e) {
                var keyCode = e.which; // Capture the event
                //190 is the key code of decimal if you dont want decimals remove this condition keyCode != 190
                if (keyCode != 8 && keyCode != 9 && keyCode != 13 && keyCode != 37 && keyCode != 38 && keyCode != 39 && keyCode != 40 && keyCode != 46 && keyCode != 110 && keyCode != 190) {
                    if (keyCode < 48) {
                        e.preventDefault();
                    }
                    else if (keyCode > 57 && keyCode < 96) {
                        e.preventDefault();
                    }
                    else if (keyCode > 105) { 
                        e.preventDefault();
                    }
                }
            }           
$('input[name="estatura"]').keydown(onlynumber);
$('input[name="peso_actual"]').keydown(onlynumber);
$('input[name="peso_seismeses"]').keydown(onlynumber);
$('input[name="peso_lastyear"]').keydown(onlynumber);
$('input[name="horas_semana"]').keydown(onlynumber);
$('input[name="horas_duerme"]').keydown(onlynumber);
$('input[name="dias_periodo"]').keydown(onlynumber);	 				 	 	
});