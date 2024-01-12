const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    password: /^.{4,12}$/, // 4 a 12 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = {
    usuario: false,
    nombre: false,
    password: false,
    correo: false,
    telefono: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "usuario":
            validarCampo(expresiones.usuario, e.target, 'usuario');
            break;
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;
        case "password":
            validarCampo(expresiones.password, e.target, 'password');
            validarPassword2();
            break;
        case "password2":
            validarPassword2();
            break;
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
            break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target, 'telefono');
            break;
    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    } else {
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('password');
    const inputPassword2 = document.getElementById('password2');

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['password'] = false;
    } else {
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['password'] = true;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});
/*
formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    const terminos = document.getElementById('terminos');
    if (campos.usuario && campos.nombre && campos.password && campos.correo && campos.telefono && terminos.checked) {
        formulario.reset();

        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);

        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }
});
*/
$('.navbar-collapse a').click(function() {
    $(".navbar-collapse").collapse('hide');
});


function validarContacto() {
    var consulta = document.getElementById("contacto").value;
    if (consulta.length == 0) {


        document.getElementById("errorConsulta").innerHTML = "La consulta no debe estar vacía";
        event.preventDefault();
    }


}
$(document).ready(function() {
    $("#error").hide();
});

$("#usuarioini").blur(function() {

    $("#error").hide();
    /**validarr */
    var mensaje = "";

    if ($("#usuarioini").val().trim().length == 0) {

        mensaje = "El usuario está en blanco";
    }

    if ($("#usuarioini").val().trim().length > 12 || $("#usuarioini").val().trim().length < 3) {
        mensaje = "El nombre de usuario debe estar entre 4 y 12 caracteres";
    }


    if (mensaje != "") {

        $("#error").html(mensaje); //almacena el mensaje en el div
        $("#error").show(); //muestra el div
        event.preventDefault(); //evita que se envie
    }


});

$("#contrasenaini").blur(function() {

    $("#error").hide();
    /**validarr */
    var mensaje = "";

    if ($("#contrasenaini").val().trim().length == 0) {

        mensaje = "Ingrese su contraseña!";
    }

    if ($("#contrasenaini").val().trim().length > 13) {
        mensaje = "La contraseña no puede tener mas de 13 caracteres";
    }


    if (mensaje != "") {

        $("#error").html(mensaje); //almacena el mensaje en el div
        $("#error").show(); //muestra el div
        event.preventDefault(); //evita que se envie
    }

});

$(document).ready(function() {
    console.log("hola")
    var d = new Date().getDate();
    var m = document.querySelectorAll("#contain_moon div");
    var a = new XMLHttpRequest();
    var url = "https://www.icalendar37.net/lunar/api/?lang=es&month=" + (new Date().getMonth() + 1) + "&year=" + (new Date().getFullYear()) + "&size=100&lightColor=rgb(245,245,245)&shadeColor=rgb(17,17,17)&LDZ=" + new Date(new Date().getFullYear(), new Date().getMonth(), 1) / 1000 + "";
    m[1].style.height = "100px";
    a.onreadystatechange = function() {
        if (a.readyState == 4 && a.status == 200) {
            var b = JSON.parse(a.responseText);
            m[1].innerHTML = b.phase[d].svg;
            if (typeof moon_widget_loaded == "function") moon_widget_loaded(b);
            m[2].innerHTML = b.phase[d].npWidget;
            m[3].innerHTML = "Próxima luna llena<br>" + b.nextFullMoon
        }
    };
    a.open("GET", url, true);
    a.send()
});

$(document).on('click', '.confirmareliminar', function() {
    return confirm('Estás seguro que quieres eliminar este servicio?');
});