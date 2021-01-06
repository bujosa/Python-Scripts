import json
import pprint
import csv

printer = pprint.PrettyPrinter()

data = open("superCarros.json")
carData = json.load(data)


def is_number(number):
    try:
        int(number)
        return True
    except:
        return False


colors = {'Negro': "black",
          'Azul': "blue",
          'Marrón': 'brown',
          'Vino': 'wine',
          'Beige': 'beige',
          'Crema': 'cream',
          'Azul claro': 'blue',
          'Verde': "green",
          'Amarillo': "yellow",
          'Gris': "grey",
          'Plata': "silver",
          'Blanco': "white",
          'Azul Marino': "blue",
          'Dorado': "gold",
          'Verde/Gris': "green",
          'Rojo Vino': "wine",
          'Bronce': "bronze",
          'Azul Agua': "blue",
          'Rojo Esacarlata': "red",
          'Negro/Rojo': "red",
          'Naranja': "orange",
          'Rojo': "red",
          'Rosado': "pink",
          'Gris Plata': 'grey',
          'Gris oscuro': "grey",
          'Negro/Gris': "grey",
          'Blanco perla': "white",
          'Azul Cielo': "blue",
          'Rojo Esacarlata': "red",
          'Champang': 'champagne',
          "Terracota": "terra cotta",
          'Azul/Grís': "grey",
          'Ladrillo': "red",
          'Rojo/Dorado': 'gold',
          'Negro/Crema': 'black',
          'Morado': "purple",
          }

train = {'Delantera': "Front",
         'Trasera': "Rear",
         '2WD': "2WD",
         '4WD Full Time': "4WD",
         '4WD': "4WD"}

gearDict = {'Mecánica o Automática': "Automatic",
            'Semiautomática': "Automatic",
            'Automática': "Automatic",
            'Mecánica': "Mechanical",
            'Sincronizada': "Automatic"}

bodyStyleDict = {'Furgoneta': "Truck",
                 'Planta Electrica': "Truck",
                 'Autobús': "Truck",
                 'Coupé/Deportivo': "Coupe",
                 'Hatchback': "Hatchback",
                 'Convertible': "Cabriolet",
                 'Camioneta': "Truck",
                 'Retropala': "Truck",
                 'JetSki': "Boat",
                 'Coupé': "Coupe",
                 'Trailer': "Truck",
                 'Sedán': "Sedan",
                 'Jeepeta': "Truck",
                 'Carro de Golf': "Minivan / Minibus",
                 'Retroexcavadora': "Truck",
                 'Minibus': "Minivan / Minibus",
                 'MiniVán': "Minivan / Minibus",
                 'Camión': "Truck",
                 'Excabadora': "Truck",
                 'Bote': "Boat",
                 'Grua': "Truck",
                 'Rodillo': "Truck",
                 'Lancha': "Boat",
                 'Volteo': "Truck",
                 'Motocicleta': "Motorcycle",
                 'Tractor': "Truck",
                 'Four Wheel': "Sedan",
                 'Jeep': "Truck",
                 'Pala Mecánica': "Truck",
                 'Tanquero': "Truck",
                 'Casa Rodante': "Truck",
                 'Monta Carga': "Truck"}


colorss = set()

with open('superCarrosData.csv', mode='w') as csv_file:
    fieldnames = ["brand", "model", "price", "year",
                  "Color", "Body_Style",
                  "Horsepower", "Hand_Drive",
                  "Engine_Cylinders", "Engine",
                  "Engine_Volume", "Interior_Color", "Mileage",
                  "Gearbox", "Drive_train", "sold"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for car in carData:

        brand = (car["vehicleName"] if "vehicleName" in car else 'NA').split(' ')[
            0]
        modelName = (car["vehicleName"]
                     if "vehicleName" in car else 'NA').replace(brand, "").strip().split(' ')
        modelName.pop() if is_number(
            modelName[len(modelName)-1]) else modelName
        modelName = " ".join(modelName)

        power = car["vehicleSpecs"]["Motor:"].split(
            ',')[0] if "Motor:" in car["vehicleSpecs"] else ''
        value_to_check = car["vehicleSpecs"]["Motor:"].split(',').pop().split(
            ' ')[0] if "Motor:" in car["vehicleSpecs"] else ''

        color = car["vehicleSpecs"]["Exterior:"] if "Exterior:" in car["vehicleSpecs"] else 'white'
        interior_color = car["vehicleSpecs"]["Interior:"] if "Interior:" in car["vehicleSpecs"] else 'white'
        drive_train = car["vehicleSpecs"]["Tracción:"] if "Tracción:" in car["vehicleSpecs"] else 'Front'
        miles = "".join((car["vehicleSpecs"]["Uso:"]
                         if "Uso:" in car["vehicleSpecs"] else '').split(" ")[0].split(','))
        gearbox = car["vehicleSpecs"]["Transmisión:"] if "Transmisión:" in car["vehicleSpecs"] else 'Automatic'

        body = car["vehicleSpecs"]["Tipo:"] if "Tipo:" in car["vehicleSpecs"] else 'NA'

        writer.writerow({'brand': brand,
                         'model': modelName,
                         'price': "".join(car["vehicleSpecs"]["Precio:"].split(" ").pop().split(',')) if "Precio:" in car["vehicleSpecs"] else 0,
                         'year': car["vehicleName"].split(' ').pop() if "vehicleName" in car else 2020,
                         "Color": colors[color] if color in colors else "white",
                         "Body_Style": bodyStyleDict[body] if body in bodyStyleDict else "Sedan",
                         "Horsepower": int(power) if is_number(power) else 0,
                         "Hand_Drive": "Left",
                         "Engine_Cylinders": int(value_to_check) if is_number(value_to_check) else 4,
                         "Engine": 'Petrol',
                         "Engine_Volume": 2.5,
                         "Interior_Color": colors[interior_color] if interior_color in colors else "white",
                         "Mileage": int(miles) if is_number(miles) else 0,
                         "Gearbox": gearDict[gearbox] if gearbox in gearDict else 'Automatic',
                         "Drive_train": train[drive_train] if drive_train in train else "Front",
                         "sold": 'No',
                         })

        # colorss.add(bodyStyleDict[body] if body in bodyStyleDict else "Sedan")


print(colorss)
