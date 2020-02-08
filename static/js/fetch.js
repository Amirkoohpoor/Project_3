document.getElementById("submit").onclick = () => {
    var minPrice = document.getElementById("minprice").value;
    var maxPrice = document.getElementById("maxprice").value;
    var wScore = document.getElementById("wscore").value;

    fetch(`/api/real-estate-search-results?minprice=${minPrice}&maxprice=${maxPrice}&wscore=${wScore}`)
    .then(response => response.json())
    .then(response => buildGraphs(response.posting))
    // .catch(err=> console.error(err.stack));
};