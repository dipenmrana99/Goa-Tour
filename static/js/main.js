(function() {
  if (typeof window.__INITIAL_POI__ !== "undefined") {
    // initialize Leaflet map
    var map = L.map('map').setView([15.4989, 73.8278], 10); // Panaji approx
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap'
    }).addTo(map);

    var poiData = window.__INITIAL_POI__;
    poiData.forEach(function(p) {
      var m = L.marker([p.lat, p.lng]).addTo(map);
      m.bindPopup('<b>' + p.name + '</b><br>' + p.area + ' • ' + p.category +
        '<br><a href="/poi/' + p.id + '">Details</a>');
    });
  }
})();