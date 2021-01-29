from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pprint import pprint
import datetime
import random
import csv

#Slug generator
def slugGenerator(data):
    data = data.lower().replace(" ","-")
    return data

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

# SECOND PART

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

getMakes = gql("""
  query{
    makes{
      id
      name
    }
  }
""")

getModels = gql("""
  query{
      models{
      id
      name
      make{
        id
        name
      }
    }
  }
""")

createMakeMutation = gql("""
  mutation($data: createMakeInput!){
    createMake(input: $data){
      make{
        name
      }
    }
  }
""")

createModelMutation = gql("""
  mutation($data: createModelInput!){
    createModel(input: $data){
      model{
        id
        name
      }
    }
  }
""")

models = client.execute(
    getModels)["models"]

makes = client.execute(getMakes)["makes"]


for i in range(1):
    modelParams = {
        "data": {
            "name": model,
            "slug": slugGenerator(model),
            "visible": False,
        }
    }

    modelResult = client.execute(
        createModelMutation, variable_values=modelParams)
        
    print(modelResult)

print("OK")
