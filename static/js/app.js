function load_house(){
    
    fetch(`/api/house-full-list`)
    .then(response => response.json())
    .then(response => house_data(response.posting))
    .catch(err=> console.error(err.stack));

}
//var h_data 
var houseMarkers = [];

function house_data(h_data)
{
        //h_data = JSON.stringify(h_data)
        // Loop through the house lat long array
        for (var index = 0; index < h_data.length; index++) {

          //var houseMarker = [h_data[index]['Lat'], h_data[index]['Long']]
          var houseMarker = L.marker([h_data[index]['Lat'], h_data[index]['Long']])
          .bindPopup("<h3>" + h_data.Mls_Number + "<h3><h3>Price: " + h_data.Price + "<h3>");
    
        
          // Add the marker to the bikeMarkers array
          houseMarkers.push(houseMarker);
        }


  // Create a layer group made from the bike markers array, pass it into the createMap function
  //createMap(L.layerGroup(houseMarkers));   
    //d3.json(data, createMarkers);
    
var geoJSONurl = 'static/data/Data.geojson'


var mapConfig = {
    center: [43.65, -79.38],
    zoom: 10
}

var tileURL = "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}"

var tileConfig = {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}

var map = L.map("map", mapConfig)
var mapLayer = L.tileLayer(tileURL, tileConfig).addTo(map)
d3.json(geoJSONurl, function(data) {
    L.geoJSON(data, {
        style: function(feature) {
            return {
                color: "blue",
                fillColor: "salmon",
                fillOpacity: 0.5,
                weight: 1.5
              };
        }, 
        onEachFeature : function (feature, layer) {
                layer.on({
                    mouseover: function(event) {
                        layer = event.target, 
                        layer.setStyle({
                            fillOpacity: 0.75
                        });
                    }, 
                    doubleclick: function(event) {
                        //map.fitBounds(event.target.getBounds());
                        map.zoomOut();
                    },
                    click: function (event) {
                        map.zoomIn();
                    },
                    mouseout: function(event) {
                        layer = event.target, 
                        layer.setStyle({
                            fillOpacity: 0.5
                        })
                    }
                });
                layer.bindPopup("<h1>" + feature.properties.AREA_DESC + "</h1><hr><h2>" + feature.properties.AREA_TYPE + "</h2>");
        }
    }).addTo(map);
})



}

if(window.addEventListener) {
    window.addEventListener('load', load_house,false); //W3C
} else {
    window.attachEvent('onload',load_house); //IE
}

