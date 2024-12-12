# store ip address in mongodb

# find the nearest ip address/network

# get ip address
# geocode ip address to get latitude/longitude of network 
# Create geojson object
# find nearest network using mongodb


db.points.insert( {
    ipAddress: "24.126.25.2",
    address: "Washington, Virginia, US",
   geomentry: { type: "Point", coordinates: [-78.1594,38.7135] },
   category: "networks"
    }
 )

db.points.insert(
  {"geometry":{"type":"Point","coordinates":[-118.2514822,34.1562397]},"type":"Feature","properties":{"timestamp":"2015-04-18T23:43:08.000Z","accuracy":7}
  }
)


db.networks.createIndex( { location: "2dsphere" } )

db.networks.insert( {
   location: { type: "Point", coordinates: [ -73.97, 40.77 ] },
} );

db.networks.insert( {
   location: { type: "Point", coordinates: [ -118.2565695, 34.0560551 ] },
} );

db.networks.insert( {
   location: { type: "Point", coordinates: [ -79.4163, 43.7001 ] },
} );

-78.1594,38.7135

db.networks.insert( {
   location: { type: "Point", coordinates: [ -78.1594,38.7135 ] },
} );