/**
 * Created by Cliente on 27/02/2018.
 */
$( "#id_fornecedor" ).last().addClass( "form-control form-control-sm" );
$( "#id_processoconcluido" ).last().addClass( "form-control form-control-sm" );
$( "#id_comprador" ).last().addClass( "form-control form-control-sm" );

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});
$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').focus()
});
