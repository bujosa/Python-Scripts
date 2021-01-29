from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pprint import pprint
import xlsxwriter
import datetime
import random

api_token = ""
headers = {"Authorization": "Bearer {token}".format(token=api_token)}

_transport = RequestsHTTPTransport(
    url='http://localhost:4000/graphql',
    use_json=True,
    # headers=headers
)


client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

getPricesQuery = gql("""
query{
  getAllPrices{
    id
    basePrice
    curboPrice
    discount
    protectionPlan
    curboFee
    licensePlate
    transfer
    tax{
      id
      name
    }
  }
}
""")

getCountryVersions = gql("""
query	{
  getAllCountryVersions{
    id
    name
    slug
  }
}
""")

getCategoriesQuery = gql("""
query{
  getAllCategories{
    id
    name
    slug
    icon
  }
}
""")

getDealersQuery = gql("""
query{
  getAllDealers{
    id
    name
    slug
    telephoneNumber
    location{
      id
    }
    workingHours
    type
  }
}
""")

getColors = gql("""
query{
  getAllColors{
    id
    name
    slug
  }
}
""")

getBodyStyles = gql("""
query{
  getAllBodyStyles{
    id
    name
    slug
    icon
  }
}
""")

getDriveTrains = gql("""
query{
  getAllDriveTrains{
    id
    name
    slug
  }
}
""")

getModels = gql("""
query{
  getAllModels{
    id
    name
    slug
    brand{
      id
      name
      slug
    }
  }
}
""")

getFeatures = gql("""
query{
  getAllFeatures{
    id
    name
    slug
  }
}
""")

getFuelTypes = gql("""
query{
  getAllFuelTypes{
    id
    name
    slug
  }
}
""")

createCarMutation = gql("""
mutation($data:CreateCarInput!){
  createCar(input:$data){
    id
  }
}
""")


prices = client.execute(
    getPricesQuery)["getAllPrices"]

countryVersions = client.execute(
    getCountryVersions)["getAllCountryVersions"]

categories = client.execute(
    getCategoriesQuery)["getAllCategories"]

dealers = client.execute(
    getDealersQuery)["getAllDealers"]

colors = client.execute(
    getColors)["getAllColors"]

bodyStyles = client.execute(
    getBodyStyles)["getAllBodyStyles"]

driveTrains = client.execute(
    getDriveTrains)["getAllDriveTrains"]

models = client.execute(
    getModels)["getAllModels"]

features = client.execute(
    getFeatures)["getAllFeatures"]

fuelTypes = client.execute(
    getFuelTypes)["getAllFuelTypes"]


priceMaxIndex = len(prices) - 1
contryVersionMaxIndex = len(countryVersions)-1
categoryMaxIndex = len(categories)-1
dealerMaxIndex = len(dealers)-1
colorMaxIndex = len(colors)-1
bodyStyleMaxIndex = len(bodyStyles)-1
driveTrainMaxIndex = len(driveTrains)-1
modelMaxIndex = len(driveTrains)-1
featureMaxIndex = len(features)-1
fuelTypeMaxIndex = len(fuelTypes)-1


for i in range(1):

    priceIdx = random.randint(0, priceMaxIndex)
    cvIdx = random.randint(0, contryVersionMaxIndex)
    categoryIdx = random.randint(0, categoryMaxIndex)
    dealerIdx = random.randint(0, dealerMaxIndex)
    colorIdx = random.randint(0, colorMaxIndex)
    bodyStyleIdx = random.randint(0, bodyStyleMaxIndex)
    driveTrainIdx = random.randint(0, driveTrainMaxIndex)
    modelIdx = random.randint(0, modelMaxIndex)
    featureIdx = random.randint(0, featureMaxIndex)
    fuelTypeIdx = random.randint(0, fuelTypeMaxIndex)

    price = prices[priceIdx]
    cv = countryVersions[cvIdx]
    category = categories[categoryIdx]
    dealer = dealers[dealerIdx]
    color = colors[colorIdx]
    bodyStyle = bodyStyles[bodyStyleIdx]
    driveTrain = driveTrains[driveTrainIdx]
    model = models[modelIdx]
    feature = features[featureIdx]
    fuelType = fuelTypes[fuelTypeIdx]

    carParams = {
        "data": {
            "year": random.randint(2008, 2021),
            "description": "pruebas",
            "mileage": 1234,
            "curboPrice": random.randint(5000, 150000),
            "mpg": random.randint(0, 157000),
            "mpgCity": random.randint(0, 50),
            "mpgHgw": random.randint(0, 40),
            "fuelCapacity": random.randint(4, 12),
            "keys": random.randint(1, 3),
            "vinNumber": "1234567",
            "cylinders": random.randint(2, 4),
            "torque": 0,
            "torqueRpm": 0,
            "frontLegRoom": 0,
            "frontHeadRoom": 0,
            "backLegRoom": 0,
            "backHeadRoom": 0,
            "engineDisplacement": 0,
            "cargoCapacity": 0,
            "lwh": "lwh",
            "seats": random.randint(2, 7),
            "doors": random.randint(2, 5),
            "price": price["id"],
            "countryVersion": cv["id"],
            "categories": [category["id"]],
            "dealer": dealer["id"],
            "curboSpot": dealer["id"],
            "interiorColor": color["id"],
            "exteriorColor": color["id"],
            "bodyStyle": bodyStyle["id"],
            "driveTrain": driveTrain["id"],
            "brand": model["brand"]["id"],
            "carModel": model["id"],
            "mainPicture": "https://cnet4.cbsistatic.com/img/UJ3mxFRgZCL_5PyM5iJSM-p0WWc=/2019/07/17/e6640571-f94c-47d6-b026-a69dec844b29/toyota-corolla-2020.jpg",
            "pictures": [],
            "certification": "5fd0f80de8d6560076c3232a",
            "features": [feature["id"]],
            "fuelType": fuelType["id"],
            "location": dealer["id"]
        }
    }

    categoryResult = client.execute(
        createCarMutation, variable_values=carParams)

    print(categoryResult)


print("OK")
