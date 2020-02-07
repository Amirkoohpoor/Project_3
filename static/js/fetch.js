document.getElementById("submit").onclick = () => {
    const minPrice = document.getElementById("minprice").value;
    const maxPrice = document.getElementById("maxprice").value;

    fetch(`/api/real-estate-search-results?${minPrice}&maxprice=${maxPrice}`)
    .then(response => response.json())
    .then(response => buildGraphs(response.posting))
    .catch(err=> console.error(err.stack));
};