import ipinfo
from pymongo import MongoClient

uri = 'mongodb://' + 'localhost'+ ':' + '27017' +'/'
client = MongoClient(uri)
db = client['geospatial']
collection = db['networks']

handler = ipinfo.getHandler()


def insert_ip(ip):
    try: 
        details = handler.getDetails(ip)
        latlng = details.loc.split(',')
    except AttributeError:
        latlng = None

    if latlng:
        # turn coordinates from string to float
        coordinates = map(lambda x: float(x), latlng)
        coordinates = list(coordinates)
        coordinates = coordinates[::-1]
        print(details.city)

        
        location = {
            "location": { "type": "Point", "coordinates": coordinates },
            "ip": details.ip,
            "city": details.city, 
            "region": details.region,
            "country": details.country
        }

        result = collection.insert_one(location)
        print(result)
    
def set_available(ip):
    pass

def get_nearest(ip):
    pass


ip_addresses = [
    '199.7.157.0', 
    '10.0.0.239', 
    '75.75.75.75', 
    '75.75.76.76'
    ]
for ip in ip_addresses:
    insert_ip(ip)