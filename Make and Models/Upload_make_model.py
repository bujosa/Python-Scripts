from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pprint import pprint
import datetime
import random
import csv

for number in range(1992,2022):
  with open('${number}.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      line_count_two = 0

      top_car = {}
      top_car_viewers = {}
      url_car = {}

      for row in csv_reader:
          if top_car.get(row[2]) == None:
              top_car[row[2]] = 1
              url_car[row[2]] = row[18] 
          else:
              top_car[row[2]] +=1                         

# api_token = ""
# headers = {"Authorization": "Bearer {token}".format(token=api_token)}

_transport = RequestsHTTPTransport(
    url='http://localhost:4000/graphql',
    use_json=True,
    # headers=headers
)

client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

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

createModelMutation = gql("""
mutation($data:CreateCarInput!){
  createCar(input:$data){
    id
  }
}
""")

models = client.execute(
    getModels)["getAllModels"]


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

    modelParams = {
        "data": {
            "name": "",
            "slug": "pruebas",
            "visible": False,
        }
    }

    modelResult = client.execute(
        createModelMutation, variable_values=modelParams)
        
    print(modelResult)

print("OK")
