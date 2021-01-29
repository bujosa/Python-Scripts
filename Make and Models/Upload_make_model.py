from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pprint import pprint
import datetime
import random
import csv

#Slug generator
def slugGenerator(data):
    data = data.lower().replace(" ","-")
    data = data.replace("&","and")
    return data

make = {} 
model = {}
model_validation = {}

for number in range(1992,2022):
  with open(f'us-car-models-data/{number}.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
          if row[1] != "make":
            if model.get(row[2]) == None:
                model[row[2]] = row[1]                 

# SECOND PART

# api_token = ""
# headers = {"Authorization": "Bearer {token}".format(token=api_token)}

_transport = RequestsHTTPTransport(
    # url='https://api-staging.curbo.co/graphql',
    url = 'http://localhost:1337/graphql',
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
      slug
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

for data in models:
      key = data["slug"]
      if model_validation.get(key) == None:
                model_validation[key] = True

makes = client.execute(getMakes)["makes"]

for data in makes:
      key = slugGenerator(data["name"])
      if make.get(key) == None:
                make[key] = data["id"]

for key in model:

    print(key)

    slug = slugGenerator(key)

    validation = True

    if model_validation.get(slug) != None:
          validation = False

    id_make = make[slugGenerator(model[key])]
    
    if validation:
      Params = {
          "data": {
            "data": {
                "name": key,
                "make": id_make,
                "slug": slug,
                "visible": False
            }
          }
        }
      Result = client.execute(
            createModelMutation, variable_values=Params)   
      print(Result)   

print("OK")
