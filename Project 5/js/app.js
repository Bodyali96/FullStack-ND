
var map;

// Create a new blank array for all the listing markers.
var markers = [];
// Create placemarkers array to use in multiple functions to have control
// over the number of places that show.
var placeMarkers = [];

var styles = [
    {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
    {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
    {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
    {
      featureType: 'administrative.locality',
      elementType: 'labels.text.fill',
      stylers: [{color: '#d59563'}]
    },
    {
      featureType: 'poi',
      elementType: 'labels.text.fill',
      stylers: [{color: '#d59563'}]
    },
    {
      featureType: 'poi.park',
      elementType: 'geometry',
      stylers: [{color: '#263c3f'}]
    },
    {
      featureType: 'poi.park',
      elementType: 'labels.text.fill',
      stylers: [{color: '#6b9a76'}]
    },
    {
      featureType: 'road',
      elementType: 'geometry',
      stylers: [{color: '#38414e'}]
    },
    {
      featureType: 'road',
      elementType: 'geometry.stroke',
      stylers: [{color: '#212a37'}]
    },
    {
      featureType: 'road',
      elementType: 'labels.text.fill',
      stylers: [{color: '#9ca5b3'}]
    },
    {
      featureType: 'road.highway',
      elementType: 'geometry',
      stylers: [{color: '#746855'}]
    },
    {
      featureType: 'road.highway',
      elementType: 'geometry.stroke',
      stylers: [{color: '#1f2835'}]
    },
    {
      featureType: 'road.highway',
      elementType: 'labels.text.fill',
      stylers: [{color: '#f3d19c'}]
    },
    {
      featureType: 'transit',
      elementType: 'geometry',
      stylers: [{color: '#2f3948'}]
    },
    {
      featureType: 'transit.station',
      elementType: 'labels.text.fill',
      stylers: [{color: '#d59563'}]
    },
    {
      featureType: 'water',
      elementType: 'geometry',
      stylers: [{color: '#17263c'}]
    },
    {
      featureType: 'water',
      elementType: 'labels.text.fill',
      stylers: [{color: '#515c6d'}]
    },
    {
      featureType: 'water',
      elementType: 'labels.text.stroke',
      stylers: [{color: '#17263c'}]
    }
];

function initMap() {
    // Constructor creates a new map - only center and zoom required
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 30.044430, lng: 31.235719},
        zoom: 15,
        styles: styles,
        mapTypeControl: false
    });
    ko.applyBindings(new ViewModel());
}

var ViewModel = function () {
    // Make this accessible
    var self = this;

    // Sidebar status observable
    self.isActiveSidebar = ko.observable(false);
    // Toggle Show/Hide Sidebar
    self.toggleSidebar = function () {
        self.isActiveSidebar(!self.isActiveSidebar());
    };

    // Create a searchbox in order to execute a places search
    var searchBox = new google.maps.places.SearchBox(
        document.getElementById('places-search'));
    // Bias the searchbox to within the bounds of the map.
    searchBox.setBounds(map.getBounds());

    // These are the real estate listings that will be shown to the user.
    // Normally we'd have these in a database instead.
    var locations = [
        {title: 'Tahrir Square Egypt', location: {lat: 30.044420, lng: 31.235712}},
        {title: 'Cairo Tower', location: {lat: 30.046195, lng: 31.224333}},
        {title: 'Mokhtar Altitch Stadium', location: {lat: 30.045043, lng: 31.223531}},
        {title: 'Egyptian Museum', location: {lat: 30.047848, lng: 31.233637}},
        {title: 'Ethnographic Museum', location: {lat: 30.041198, lng: 31.235847}},
        {title: 'Mahmoud Mukhtar Museum', location: {lat: 30.040734, lng: 31.222866}},
        {title: 'Beit El Umma Museum', location: {lat: 30.038133, lng: 31.237478}},
        {title: 'Cairo Opera House', location: {lat: 30.042684, lng: 31.223981}},
        {title: 'Al Ahly Sports Club', location: {lat: 30.044913, lng: 31.222372}},
        {title: 'The Great Pyramid at Giza', location: {lat: 29.979249, lng: 31.134181}},
    ];

    var largeInfowindow = new google.maps.InfoWindow();

    // Style the markers a bit. This will be our listing marker icon.
    var defaultIcon = makeMarkerIcon('0091ff');

    // Create a "highlighted location" marker color for when the user
    // mouses over the marker.
    var highlightedIcon = makeMarkerIcon('FFFF24');

    var bounds = new google.maps.LatLngBounds();


    // The following group uses the location array to create an array of markers on initialize.
    for(var i = 0; i < locations.length; i++){
        // Get the position from the location array.
        var position = locations[i].location;
        var title = locations[i].title;
        // Create a marker per location, and put into markers array.
        var marker = new google.maps.Marker({
            map: map,
            position: position,
            title: title,
            icon: defaultIcon,
            animation: google.maps.Animation.DROP,
            id: i
        });

        // Extend the boundaries of the map for each marker
        bounds.extend(marker.position);
        // Create an onclick event to open an infowindow at each marker.
        var markerClick = function() {
            populateInfoWindow(this, largeInfowindow);
            for (var i = 0; i < markers.length; i++){
                markers[i].setAnimation(null);
            }
            this.setAnimation(google.maps.Animation.BOUNCE);
        };
        marker.addListener('click', markerClick);
        // Two event listeners - one for mouseover, one for mouseout,
        // to change the colors back and forth.
        marker.addListener('mouseover', function () {
            this.setIcon(highlightedIcon);
        });
        marker.addListener('mouseout', function () {
            this.setIcon(defaultIcon);
        });
        // Push the marker to our array of markers.
        markers.push(marker);
        // Getting sidebar unordered list
        var sidebar = document.getElementById('sidebar-list');
        // Creating list item for each marker
        var marker_li = document.createElement('li');
        // Creating anchor element
        var marker_anch = document.createElement('a');
        marker_anch.setAttribute('href', '#');
        // Setting Text content of each anchor element to marker title
        marker_anch.textContent = marker.title;
        // Putting anchor element inside list item
        marker_li.appendChild(marker_anch);
        // Click event for list item to select each marker
        marker_li.addEventListener('click', function (markerCopy) {
            return function () {
                populateInfoWindow(markerCopy, largeInfowindow);
                for (var j = 0; j < markers.length; j++){
                    markers[j].setAnimation(null);
                }
                markerCopy.setAnimation(google.maps.Animation.BOUNCE);
            }
        }(marker));
        // Putting list item into sidebar unordered list
        sidebar.appendChild(marker_li);
    }

    // Change Text of button upon next action
    document.getElementById('toggle-markers').addEventListener('click', function () {
        this.innerText = isActiveMarkers ? 'Show Markers' : 'Hide Markers';
        toggleShowMarker();
    });

    // Listen for the event fired when the user selects a prediction from the
    // picklist and retrieve more details for that place.
    searchBox.addListener('places_changed', function() {
      searchBoxPlaces(this);
    });

    // Listen for the event fired when the user selects a prediction and clicks
    // "go" more details for that place.
    document.getElementById('go-places').addEventListener('click', textSearchPlaces);

    // This function populates the infowindow when the marker is clicked. We'll only allow
    // one infowindow which will open at the marker that is clicked, and populate based
    // on that markers position.
    function populateInfoWindow(marker, infowindow) {
        // Check to make sure the infowindow is not already opened on this marker.
        if (infowindow.marker != marker) {
            infowindow.marker = marker;

            infowindow.setContent('<ul class="wiki"><li>' + marker.title + '</li></ul>');
            var wikiURL = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + marker.title + '&format=json&callback=wikiCallback';
            var wikiData = '';

            $.ajax({
                url: wikiURL,
                dataType: "jsonp",
                success: function(response) {
                    for(var i = 0; i < response[1].length; i++) {
                        infowindow.setContent(infowindow.getContent()+'<li><a href="' + response[3][i] + '">'+response[1][i]+'</a></li>');
                    }
                }
            });
            infowindow.open(map, marker);
            // Make sure the marker property is cleared if the infowindow is closed.
            infowindow.addListener('closeclick',function(){
                infowindow.setMarker = null;
            });
        }
    }
    // Boolean that holds marker's visibility state
    var isActiveMarkers = true;
    // This function checks whether Marker is shown or hidden and toggles it's visibility
    function toggleShowMarker() {
        if(isActiveMarkers)
            hideMarkers();
        else
            showMarkers();
    }
    // This function will loop through the markers array and display them all.
    function showMarkers() {
        isActiveMarkers = true;
        var bounds = new google.maps.LatLngBounds();
        // Extend the boundaries of the map for each marker and display the marker
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(map);
            bounds.extend(markers[i].position);
        }
        map.fitBounds(bounds);
    }
    // This function will loop through the listings and hide them all.
    function hideMarkers() {
        isActiveMarkers = false;
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
        }
    }

    // This function takes in a COLOR, and then creates a new marker
    // icon of that color. The icon will be 21 px wide by 34 high, have an origin,
    // of 0, 0 and be anchored at 10, 34).
    function makeMarkerIcon(markerColor) {
        var markerImage = new google.maps.MarkerImage(
            'http://chart.googleapis.com/chart?chst=d_map_spin&chld=1.15|0|'+ markerColor +
            '|40|_|%E2%80%A2',
            new google.maps.Size(21, 34),
            new google.maps.Point(0, 0),
            new google.maps.Point(10, 34),
            new google.maps.Size(21, 34));
        return markerImage;
    }

    // This function fires when the user selects a searchbox picklist item.
    // It will do a nearby search using the selected query string or place.
    function searchBoxPlaces(searchBox) {
        hideMarkers(placeMarkers);
        var places = searchBox.getPlaces();
        // For each place, get the icon, name and location.
        createMarkersForPlaces(places);
        if (places.length == 0) {
          window.alert('We did not find any places matching that search!');
        }
    }

    // This function firest when the user select "go" on the places search.
    // It will do a nearby search using the entered query string or place.
    function textSearchPlaces() {
        var bounds = map.getBounds();
        hideMarkers(placeMarkers);
        var placesService = new google.maps.places.PlacesService(map);
        placesService.textSearch({
          query: document.getElementById('places-search').value,
          bounds: bounds
        }, function(results, status) {
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            createMarkersForPlaces(results);
          }
        });
    }


    // This function creates markers for each place found in either places search.
    function createMarkersForPlaces(places) {
        var bounds = new google.maps.LatLngBounds();
        for (var i = 0; i < places.length; i++) {
          var place = places[i];
          var icon = {
            url: place.icon,
            size: new google.maps.Size(35, 35),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(15, 34),
            scaledSize: new google.maps.Size(25, 25)
          };
          // Create a marker for each place.
          var marker = new google.maps.Marker({
            map: map,
            icon: icon,
            title: place.name,
            position: place.geometry.location,
            id: place.id
          });
          // If a marker is clicked, do a place details search on it in the next function.
          marker.addListener('click', function() {
            getPlacesDetails(this, place);
          });
          placeMarkers.push(marker);
          if (place.geometry.viewport) {
            // Only geocodes have viewport.
            bounds.union(place.geometry.viewport);
          } else {
            bounds.extend(place.geometry.location);
          }
        }
        map.fitBounds(bounds);
    }


};

