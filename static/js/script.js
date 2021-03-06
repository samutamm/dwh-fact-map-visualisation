
google.charts.load('current', {
  'packages':['geochart'],
  // Note: you will need to get a mapsApiKey for your project.
  // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
  'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
  var fact = document.getElementById("myForm").elements.namedItem("fact").value;
  var year = document.getElementById("myForm").elements.namedItem("year").value;
  //fetch server
  var jsonStr = $.ajax({
          url: "countrys/" + year + "/" + fact,
          dataType: "json",
          async: false
          }).responseText;
  var jsonData = JSON.parse(jsonStr)
  console.log(jsonData.data);

  var data = google.visualization.arrayToDataTable(jsonData.data);

  var options = {};

  var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

  chart.draw(data, options);
}
