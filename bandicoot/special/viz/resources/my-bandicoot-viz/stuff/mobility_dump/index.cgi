#!/usr/bin/env python

import cgi
import string

print "Content-Type: text/html"
print ""


page_str = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link href="base.css" rel="stylesheet" type="text/css" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script type="text/javascript">
    function get_file_id(){
      return document.getElementById("fid").value
    }
  </script>
</head>
<body>
  <form>
    <input type="hidden" id="fid" name="fid" value="$file_id" />
  </form>
  <div id='map'>
  </div>

  <script type="text/javascript" src="../bower_components/d3/d3.min.js"></script> 
  <script type="text/javascript" src="../bower_components/simple-statistics/src/simple_statistics.js"></script>
  <script type="text/javascript" src="../bower_components/colorbrewer/colorbrewer.js"></script>
  <script type="text/javascript" src="../bower_components/jquery/dist/jquery.min.js"></script> 
  
  <script src='https://api.tiles.mapbox.com/mapbox.js/v2.1.7/mapbox.js'></script>
  <link href='https://api.tiles.mapbox.com/mapbox.js/v2.1.7/mapbox.css' rel='stylesheet' />
  

  <script type="text/javascript" src="voronoi_map.js"></script>
  <script>
	L.mapbox.accessToken = 'pk.eyJ1IjoiYmphcmtlIiwiYSI6ImUxYWVkZmE4ZTcxZTI1NTU5ZjQ2MDZhNzI1MGQ0OWRhIn0.UmrE6Fv2XigzVQbSn8TgMA';

	var tileLayer = L.mapbox.tileLayer('bjarke.c66cb2ac');

	var map = L.mapbox.map('map', null, {
		minZoom: 5,
		maxZoom: 16,
		'center': [0, 0],
		'zoom': 1,
	 	'layers': [tileLayer],
		attributionControl: false,
		zoomControl:false 
	});
	
	map.maxZoom = 16;
	map.minZoom = 11;

	 var layerControl = L.control.layers(null, {
		'Background': tileLayer
	}).addTo(map);
	
	  
    link_antenna = get_file_id().concat('antenna.csv');
	link_transition = get_file_id().concat('transitions.csv');
    voronoiMap(map, link_antenna, link_transition, layerControl);
  </script>
</body>
</html>
"""

form = cgi.FieldStorage()
if "fid" in form:
    file_id = form["fid"].value
else:
    file_id = ""
out = string.Template(page_str).substitute(file_id=file_id)
print out
