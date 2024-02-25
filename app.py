from flask import Flask, render_template
from backend.data import Data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flocator')
def flocator():
    data = Data()
    buildings = data.getDummyData()
    json_buildings = []
    for building in buildings:
        json_bathrooms = []
        for bathroom in building.getBathrooms():
            json_bathroom = {
                'name': bathroom.getName(),
                'pads': bathroom.getPad(),
                'tampons': bathroom.getTampon(),
                'pad_running_low': bathroom.padLow(),
                'tampon_running_low': bathroom.tamponLow(),
                'is_free': bathroom.getisFree(),
                'pad_restock': bathroom.getPadRestock(),
                'tampon_restock': bathroom.getTamponRestock()
            }
            json_bathrooms.append(json_bathroom)
        json_building = {
            'name': building.getName(),
            'lat': building.getLatitude(),
            'long': building.getLongitude(),
            'bathrooms': json_bathrooms
        }
        json_buildings.append(json_building)
    return render_template('flocator.html', buildings=json_buildings)

@app.route('/update')
def update():
    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True)