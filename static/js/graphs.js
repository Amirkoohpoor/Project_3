function buildGraphs(properties){
    // enter d3 code to plot graphs here, properties is the output of the users search result in json format
    console.log("buildGraphs", properties);
//     // Create a map object
//     var myMap = L.map("map", {
//         center: [37.09, -95.71],
//         zoom: 5
//         });
  
//   // Add a tile layer
//     L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//         attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//         maxZoom: 18,
//         id: "mapbox.streets",
//         accessToken: API_KEY
//         }).addTo(myMap);
//         properties.forEach(function(unit) {
//             L.marker([unit.Lat, unit.Long],{
//                 title: unit.MLS_Number
//             })
//             .addTo(myMap)
//     });
    var selection = d3.selectAll("tbody").selectAll("tr").data(properties)
    selection.enter()
        .append("tr")
        .html(d => `<td>${d.Mls_Number}</td><td>${d.Lat}</td><td>${d.Long}</td><td>${d.Street}</td><td>${d.City}</td><td>${d.Postal_Code}</td><td>${d.Walk_Score}</td><td>${d.Price}</td><td>${d.Photo_url}</td>`)
}