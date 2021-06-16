
google.charts.load('current', {'packages':['table']});
google.charts.setOnLoadCallback(drawTable);
function drawTable() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Reciduo');
  data.addColumn('number', 'Piezas');
  data.addColumn('boolean', 'Status');
  data.addRows([
    ['Botella',  {v: 10000, f: '$10,000'}, true],
    ['Botella',   {v:8000,   f: '$8,000'},  false],
    ['Botella', {v: 12500, f: '$12,500'}, true],
    ['Botella',   {v: 7000,  f: '$7,000'},  true]
  ]);

  var table = new google.visualization.Table(document.getElementById('table_div'));

  table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
}