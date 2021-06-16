google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawMultSeries);

function drawMultSeries() {
      var data = google.visualization.arrayToDataTable([
        ['Fecha de separación', 'Numero de piezas Junio', 'Piezas en Julio'],
        [', 12-06-21', 2, 4],
        ['10-07-21,', 3, 2],
        ['11-07-21', 10, 5],
        ['1-06-21', 3, 5],
        ['2-06-21', 14, 34]
      ]);

      var options = {
        title: 'Piezas separadas',
        chartArea: {width: '50%'},
        hAxis: {
          title: 'Total de piezas',
          minValue: 0
        },
        vAxis: {
          title: 'Fecha'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('chart_bar_div'));
      chart.draw(data, options);
    }