#
# Load the location map
#
loadMap = (map_id, drag)->

    updateLatLon = (pos)->
        document.getElementById('id_lat').value = pos.lat().toFixed(15)
        document.getElementById('id_lng').value = pos.lng().toFixed(15)

    #
    # Retrieve the coordinates from the form fields
    #
    lat = document.getElementById('id_lat').value
    lng = document.getElementById('id_lng').value

    first_name = document.getElementById('id_first_name').value
    last_name = document.getElementById('id_last_name').value
    contactTitle =  "#{first_name} #{last_name}"
    contactAddress = get_address()
    #
    # Load the map
    #
    mapOptions =
        zoom: 15
        mapTypeId: google.maps.MapTypeId.ROADMAP
        scrollwheel: false

    if lat and lng
        mapOptions.center = new google.maps.LatLng(lat, lng)

    map = new google.maps.Map(document.getElementById(map_id), mapOptions)

    if lat and lng

        marker = new google.maps.Marker({
            map: map
            position: mapOptions.center
            draggable: drag
        })

        contentHtml = "<div>"
        
        contentHtml += "<span class=\"text-strong\">#{contactTitle}</span><br>#{contactAddress}</div>"

        infowindow = new google.maps.InfoWindow({
            content: contentHtml
        })

        google.maps.event.addListener(marker, 'click', ()->
            infowindow.open(map, marker)
        )
        
        marker.locid = 1;
        marker.infowindow = infowindow;

        if drag
            google.maps.event.addListener(marker, 'dragend', ()->
                updateLatLon(marker.getPosition())
            )

get_address = ->
    address_first_line = document.getElementById('id_first_line').value
    address_area = document.getElementById('id_county').value
    address_postcode = document.getElementById('id_postcode').value
    city = document.getElementById('id_city').value

    contactAddress = "#{address_first_line}"
    if city
        contactAddress += ", #{city}"
    if address_postcode
        contactAddress += ", #{address_postcode}"
    
    return contactAddress

geolocateAddress = (map_id, drag, address)->
    geocoder = new google.maps.Geocoder()
    
    geocoder.geocode( { 'address': address }, (results, status)->
        if status == google.maps.GeocoderStatus.OK
            document.getElementById('id_lat').value = results[0].geometry.location.lat().toFixed(15)
            document.getElementById('id_lng').value = results[0].geometry.location.lng().toFixed(15)
            loadMap(map_id)
        else
            alert("Geocode was not successful for the following reason: " + status)
    )

calcRoute = (from_lat, from_lng, to_lat, to_lng, cb)->

    # Set the google map direction service
    directionsService = new google.maps.DirectionsService()

    total_metres = 0
    from = new google.maps.LatLng(from_lat, from_lng)
    to = new google.maps.LatLng(to_lat, to_lng)


    request = {
        origin: from
        destination: to
        travelMode: google.maps.TravelMode.WALKING
    }

    directionsService.route(request, (response, status)->
        if status == google.maps.DirectionsStatus.OK

            route = response.routes[0]

            for leg in route.legs
                total_metres += leg.distance.value

            cb(total_metres)

    )

if document.getElementById('calculate_distance')
    
    elm = document.getElementById('calculate_distance')
    elm.addEventListener('click', (e)->
        e.preventDefault()

        from_lat = elm.getAttribute('data-from-lat')
        from_lng = elm.getAttribute('data-from-lng')
        to_lat = elm.getAttribute('data-to-lat')
        to_lng = elm.getAttribute('data-to-lng')
        input_id = elm.getAttribute('data-input-id')

        cb = (distance)->
            document.getElementById(input_id).value = distance
        
        calcRoute(from_lat, from_lng, to_lat, to_lng, cb)
        
    )


if document.getElementById('contact-form-map')
    loadMap('contact-form-map', true)

if document.getElementById('contact-view-map')
    loadMap('contact-view-map', false)

if document.getElementById('contact-form-geolocate')

    elm = document.getElementById('contact-form-geolocate')
    elm.addEventListener('click', (e)->
        e.preventDefault()
        geolocateAddress('contact-form-map', true, get_address())
    )

