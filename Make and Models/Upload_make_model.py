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

for number in range(1992,2023):
  with open(f'{number}.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')

      make = {}
      model = {}

      for row in csv_reader:
          if make.get(row[1]) == None:
              make[row[1]] = 1
          else:
              make[row[1]] +=1                         

# SECOND PART

# api_token = ""
# headers = {"Authorization": "Bearer {token}".format(token=api_token)}

_transport = RequestsHTTPTransport(
    url='http://localhost:1337/graphql',
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


for key in make:
    Params = {
        "data": {
            "name": key,
            "slug": slugGenerator(key),
            "visible": False,
        }
    }

    Result = client.execute(
        createMakeMutation, variable_values=Params)
        
    print(Result)

print("OK")
