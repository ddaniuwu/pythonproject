

google.charts.load('current', {'packages':['table']});
google.charts.setOnLoadCallback(drawTable);
function drawTable() {


  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Residuo');
  data.addColumn('number', 'Piezas');
  data.addColumn('boolean', 'Status');
  data.addRows([
    ['Cajas',  {v: 4}, true],
    ['Botellas',   {v:2},  false],
    ['Otros', {v: 1}, true],
  ]);

  var table = new google.visualization.Table(document.getElementById('table_div'));

  table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
}



var id =0;
function agregarFila(){
  
var CONTADOR_BOTELLAS = 1;
id = id +1
  
document.getElementById("tablaprueba").insertRow(-1).innerHTML = `
  <td>${id}</td>
  <td>Botella</td>
  <td>${CONTADOR_BOTELLAS}</td>
`;
}


function agregarFilaCajas(){
  let CONTADOR_CAJAS =1
  id = id +1

  document.getElementById("tablaprueba").insertRow(-1).innerHTML = `
  <td>${id}</td>
  <td>Caja</td>
  <td>${CONTADOR_CAJAS}</td>
  `;
}