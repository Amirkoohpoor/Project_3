d3.json('/crime')
  .then(function(data){
       console.log(data.features[0].attributes);
   });