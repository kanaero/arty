var map;

function initialize() {
  //var myLatlng = new google.maps.LatLng(44.4325, 26.1039);
  var myLatlng = new google.maps.LatLng(25.040388,55.116134);
  var mapOptions = {
    zoom: 12,
	scrollwheel: false,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById('mapCanvas'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
	  animation: google.maps.Animation.DROP,
      title: 'Hello World!'
  });
  
  var contentString = '<div class="info-window-content"><h2>ARTY Transport Company LLC.</h2>'+
  					  '<h3>Award Winning Service!</h3>'+
					  '</div>';
					  
  var infowindow = new google.maps.InfoWindow({
      content: contentString
  });
  
  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });
}

google.maps.event.addDomListener(window, 'load', initialize);

$('a[data-type="gmap"]').on('shown.bs.tab', function (e) {
  initialize();
})