
console.log('Hello! ----')
//var $ = jQuery;
//jQuery(document).ready(function($){
$(document).ready(function(){

    var searchBtn  = $('#search-btn');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function(){
        searchForm.submit();
        console.log('Foi!!!')

    })

});



function MessagesDjango(id){

    let confirmation = confirm('[Alerta!] - Deseja realmente deletar esse template?');
    
    if (confirmation == true){
        setTimeout(function() {
            window.location.href = `delete/${id}`
        }, 1000); 

    }
    else{
        alert("Ok, o template não será deletado.");
    }
}


function MessageCriaTemplate(){
    console.log('entrou!')
    let confirmation = confirm('[Alerta!] - Deseja Carregar Templates?');
    
    if (confirmation == true){
        alert("Ok, o template serão carregados");

    }
    else{
        alert("Ok, os template não serõ carregados.");
    }
}