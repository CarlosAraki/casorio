var csrf = $('[name=csrfmiddlewaretoken]')[0].value



var intervalId = window.setInterval(function(){
    dia_antigo = $("#dia")[0].innerText
    hora_antigo = $("#hora")[0].innerText
    minuto_antigo = $("#minuto")[0].innerText
    segundo_antigo = $("#segundo")[0].innerText




    $.ajax({
        type: "GET",
        url: 'update_clock',
        data: {'csrfmiddlewaretoken':csrf},
        success: function(data) {
            $("#dia")[0].innerText = data['dias']
            $("#hora")[0].innerText = data['horas']
            $("#minuto")[0].innerText = data['minutos']
            $("#segundo")[0].innerText = data['segundos']
                    
        }
    });
}, 1000)