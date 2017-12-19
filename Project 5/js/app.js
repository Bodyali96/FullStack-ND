'use strict';
var map;

// Create a new blank array for all the listing markers.
var markers = [];


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
    {title: 'The Great Pyramid at Giza', location: {lat: 29.979249, lng: 31.134181}}
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

// Alert the user if google maps isn't working
function googleError() {
     window.alert('Maps is not loading. Please try refreshing the page later.');
}

var Place = function (data) {
    this.title = ko.observable(data.title);
    this.location = ko.observable(data.location);
    this.marker = ko.observable();
    this.url = ko.observable('');
    this.wikiTitles = ko.observableArray([]);
    this.wikiURLs = ko.observableArray([]);
};

var ViewModel = function () {
    // Make this accessible
    var self = this;

    // Sidebar status observable
    self.isActiveSidebar = ko.observable(false);
    // Toggle Show/Hide Sidebar
    self.toggleSidebar = function () {
        self.isActiveSidebar(!self.isActiveSidebar());
    };

    self.placeList = ko.observableArray([]);

    locations.forEach(function (placeItem) {
        self.placeList.push(new Place(placeItem));
    });
    // Create a searchbox in order to execute a places search
    self.searchBox = new google.maps.places.SearchBox(
        document.getElementById('places-search'));
    // Bias the searchbox to within the bounds of the map.
    self.searchBox.setBounds(map.getBounds());

    self.largeInfowindow = new google.maps.InfoWindow();

    // Style the markers a bit. This will be our listing marker icon.
    self.defaultIcon = makeMarkerIcon('0091ff');

    // Create a "highlighted location" marker color for when the user
    // mouses over the marker.
    self.highlightedIcon = makeMarkerIcon('FFFF24');

    self.bounds = new google.maps.LatLngBounds();

    // Initialize marker
    var marker;

    // Return infowindow content needed to be set
    self.populateInfoWindow = function (placeItem) {
        var optionsBox = '<p>'+placeItem.marker.title+'</p><ul>';
        for(var i = 0; i < placeItem.wikiURLs().length; i++) {
            optionsBox += '<li><a href="'+placeItem.wikiURLs()[i]+'">'+placeItem.wikiTitles()[i]+'</a></li>';
        }
        optionsBox += '</ul>';
        return optionsBox;
    };

    // The following group uses the location array to create an array of markers on initialize.
    self.placeList().forEach(function (placeItem) {
        // Get the position from the location array.
        var position = placeItem.location();
        var title = placeItem.title();

        // Create a marker per location, and put into markers array.
        marker = new google.maps.Marker({
            map: map,
            position: position,
            title: title,
            icon: self.defaultIcon,
            animation: google.maps.Animation.DROP
        });

        placeItem.marker = marker;

        var wikiURL = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + marker.title + '&format=json&callback=wikiCallback';
        // Handling response error
        var wikiTimeout = setTimeout(function() {
            placeItem.wikiTitles.push("failed to get Wikipedia resources");
        }, 8000);
        $.ajax({
            url: wikiURL,
            dataType: "jsonp",
            success: function(response) {
                for(var i = 0; i < response[1].length; i++) {
                    placeItem.wikiTitles.push(response[1][i]);
                    placeItem.wikiURLs.push(response[3][i]);
                }
                clearTimeout(wikiTimeout);
            }
        });

        // Extend the boundaries of the map for each marker
        self.bounds.extend(placeItem.marker.position);

        placeItem.marker.addListener('click', function () {
            self.largeInfowindow.open(map, this);
            self.largeInfowindow.setContent(self.populateInfoWindow(placeItem));
            placeItem.marker.setAnimation(google.maps.Animation.BOUNCE);
            // Stop bounce animation after 0.7sec
            setTimeout(function () {
                placeItem.marker.setAnimation(null);
            }, 700);
        });
        // Two event listeners - one for mouseover, one for mouseout,
        // to change the colors back and forth.
        placeItem.marker.addListener('mouseover', function () {
            this.setIcon(self.highlightedIcon);
        });
        placeItem.marker.addListener('mouseout', function () {
            this.setIcon(self.defaultIcon);
        });


    });

    // Focus on It's marker
    self.showInfoWindow = function (placeItem) {
            google.maps.event.trigger(placeItem.marker, 'click');
    };

    // Change Text of button upon next action
    document.getElementById('toggle-markers').addEventListener('click', function () {
        this.innerText = isActiveMarkers ? 'Show Markers' : 'Hide Markers';
        toggleShowMarker();
    });

    // Listen for the event fired when the user selects a prediction from the
    // picklist and retrieve more details for that place.
    self.searchBox.addListener('places_changed', function() {
      searchBoxPlaces(this);
    });

    // Listen for the event fired when the user selects a prediction and clicks
    // "go" more details for that place.
    document.getElementById('go-places').addEventListener('click', textSearchPlaces);

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
        self.placeList().forEach(function (placeItem) {
            placeItem.marker.setMap(map);
            bounds.extend(placeItem.marker.position);
        });
        map.fitBounds(bounds);
    }
    // This function will loop through the listings and hide them all.
    function hideMarkers() {
        isActiveMarkers = false;
        self.placeList().forEach(function (placeItem) {
            placeItem.marker.setMap(null);
        });
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
    function searchBoxPlaces() {
        hideMarkers();
        var places = self.searchBox.getPlaces();
        // For each place, get the icon, name and location.
        createMarkersForPlaces(places);
        if (!places.length) {
          window.alert('We did not find any places matching that search!');
        }
    }

    // This function firest when the user select "go" on the places search.
    // It will do a nearby search using the entered query string or place.
    function textSearchPlaces() {
        var bounds = map.getBounds();
        hideMarkers();
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

          if (place.geometry.viewport) {
            // Only geocodes have viewport.
            bounds.union(place.geometry.viewport);
          } else {
            bounds.extend(place.geometry.location);
          }
        }
        map.fitBounds(bounds);
    }

    // Filter markers per user input
    // Credit http://codepen.io/prather-mcs/pen/KpjbNN?editors=001

    // Array containing only the markers based on search
    self.visible = ko.observableArray([]);

    // All markers are visible by default before any user input
    self.placeList().forEach(function (place) {
        self.visible.push(place);
    });

    // Track user input
    self.userInput = ko.observable('');

    // If user input is included in the place name, make it and its marker visible
    // Otherwise, remove the place & marker
    self.filterMarkers = function () {
        // Set all markers and places to not visible.
        var searchInput = self.userInput().toLowerCase();
        self.visible.removeAll();
        self.placeList().forEach(function (place) {
            place.marker.setVisible(false);
            // Compare the name of each place to user input
            // If user input is included in the name, set the place and marker as visible
            if (place.title().toLowerCase().indexOf(searchInput) !== -1) {
                self.visible.push(place);
            }
        });
        // Show only typed markers on map
        self.visible().forEach(function (place) {
            place.marker.setVisible(true);
        });
    };

};

