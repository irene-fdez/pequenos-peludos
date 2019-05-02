
/*Funcion para validar si en el campo file está vacio*/
function validar_file(campo) {
    var id_val = campo.id.concat("Val");
    var id_campo = document.getElementById(campo.id);
    document.getElementById(id_val).style = "display:none";

    if ( id_campo.value === "") {
        activar_div_val("Este campo no puede estar vacio", campo, id_val);
        return false;
    } else {
        document.getElementById(campo.id).style.backgroundColor = "transparent";
        return true;
    }
}


/*Funcion para validar si en el campo date está vacio*/
function validar_date(campo) {
    var id_val = campo.id.concat("Val");
    var id_campo = document.getElementById(campo.id);
    document.getElementById(id_val).style = "display:none";

    if ( id_campo.value === "") {
        activar_div_val("Este campo no puede estar vacio", campo, id_val);
        return false;
    } else {

        fech_format = new Date(); //Almacena en formatFecha un formato fecha
		fecha_input = campo.value.split("-"); //divide la fecha introducida por /
		fech_format.setFullYear(fecha_input[0],fecha_input[1]-1,fecha_input[2]); //construye la fecha introducida en formatFecha a partir del dia, mes y año

        if (fech_format > new Date()){
            activar_div_val("La fecha no puede ser mayor que el día de hoy", campo, id_val);
            return false;
        } else{
            document.getElementById(campo.id).style.backgroundColor = "transparent";
            return true;
        }

    }
}


/*Funcion para validar si el campo de texto esta vacio o es incorrecto*/
function validar_texto(campo) {

    var id_campo = document.getElementById(campo.id);
    var id_val = campo.id.concat("Val");
    document.getElementById(id_val).style = "display:none";

    var expr_reg = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ!,"'_.\-\s]+$/; //expresion regular para ltexto

    if (campo.value === "") { //si el campo está vacio
        activar_div_val("Este campo no puede estar vacio", campo, id_val);
        return false;
    } else { //si el campo no está vacio

        if (expr_reg.test(id_campo.value) === false) { //si no se corresponde con la expresión regular
            activar_div_val("El formato del campo es incorrecto", campo, id_val);
            return false;
        } else { // si se corresponde con la expresión regular
            document.getElementById(campo.id).style.backgroundColor = "transparent";
            return true;

        }
    }
}


/*Funcion para validar si el campo de tipo select es correcto*/
function validar_opcion(campo) {
    var id_val = campo.id.concat("Val");
    var id_campo = document.getElementById(campo.id);
    document.getElementById(id_val).style = "display:none";

    if (id_campo.value === "") {
        activar_div_val("Debe elegir una opción", campo, id_val);
        return false;
    } else {
        document.getElementById(campo.id).style.backgroundColor = "transparent";
        return true;
    }
}


/* Funcion para validar todos los campos*/
function validar_edit(formulario){
    var form =  document.forms[formulario];
    var alerts = [false,false,false,false,false,false,false,false];

    if (!validar_texto(form.nombre)){ alerts[0] = form.nombre;}
    if (!validar_texto(form.raza)){ alerts[1] = form.raza;}
    if (!validar_date(form.nacimiento)){ alerts[2] = form.nacimiento;}
    if (!validar_opcion(form.tamanho)){ alerts[3] = form.tamanho;}
    if (!validar_opcion(form.sexo)){ alerts[4] = form.sexo;}
    if (!validar_texto(form.color)){ alerts[5] = form.color;}
    if (!validar_opcion(form.adoptado)){ alerts[6] = form.adoptado;}
    if (!validar_texto(form.descripcion)){ alerts[7] = form.descripcion;}

	for ( var i = 0; i < alerts.length; i++) {
	    if(alerts[i] !== false) { // si hay algun campo incorrecto
	        activar_div_val("No se ha podido enviar la solicitud.<br>Compruebe que todos los campos son correctos", comprobar_todo, "comprobar_todo");
	        document.getElementById(alerts[i].id).focus();
	    	return false;
	    }
	}
    document.edit.submit();
    return true;
}


/* Funcion para validar todos los campos*/
function validar_add(formulario) {
    var form = document.forms[formulario];
    var alerts = [false,false,false,false,false,false,false,false];


     if (!validar_texto(form.nombre)){ alerts[0] = form.nombre;}
     if (!validar_texto(form.raza)){ alerts[1] = form.raza;}
     if (!validar_date(form.nacimiento)){ alerts[2] = form.nacimiento;}
     if (!validar_opcion(form.tamanho)){ alerts[3] = form.tamanho;}
     if (!validar_opcion(form.sexo)){ alerts[4] = form.sexo;}
     if (!validar_texto(form.color)){ alerts[5] = form.color;}
     if (!validar_file(form.foto)){ alerts[6] = form.foto;}
     if (!validar_texto(form.descripcion)){ alerts[7] = form.descripcion;}

    for (var i = 0; i < alerts.length; i++) {
        if (alerts[i] !== false) { // si hay algun campo incorrecto
            activar_div_val("No se ha podido enviar la solicitud.<br>Compruebe que todos los campos son correctos", comprobar_todo, "comprobar_todo");
             document.getElementById(alerts[i].id).focus();
            return false;
        }
    }
    document.add.submit();
    return true;
}


/*Funcion que activa el div de error*/
function activar_div_val(msj, campo, id_val) {
    document.getElementById(id_val).innerHTML = msj;
    document.getElementById(id_val).style = "display:inline-block";
    if(id_val !== 'comprobar_todo') {
        document.getElementById(campo.id).style.backgroundColor = "rgba(206,132,131,0.5)";
    }
    else{
        document.getElementById(campo.id).style.textAlign = "center";
    }

}