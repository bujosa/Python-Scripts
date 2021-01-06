from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pprint import pprint

# Added your url
_transport = RequestsHTTPTransport(
    url='',
    use_json=True,
    # TODO uncomment header when using token on headers
    # headers=headers
)


client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

carQuery = gql("""
query{
  cars(where: {categories:{name_in:["Communer","Smart"]}}){
    title
    id
    categories{
      name
    }
  }
}
""")

getCategoriesQuery = gql("""
query {
  categories{
    id
    name
  }
}
""")

updateCarMutation = gql("""
mutation carCategoryChange($data:updateCarInput){
  updateCar(input:$data){
    car{
      title
      categories{
        name
      }
    }
  }
}
""")

updateCategoryMutation = gql("""
mutation ($input: updateCategoryInput){
  updateCategory(input:$input){
    category{
      name
    }
  }
} 
""")

# Get cars and categories
# TODO uncomment get car query
# cars = client.execute(carQuery)["cars"]
categories = client.execute(getCategoriesQuery)["categories"]

# cars = [{'categories': [{'name': 'Communer'}, {'name': 'Family'}],
#          'id': '5e79704c0c09ec30af51ce5d',
#          'title': 'Fiat 500 2019 Americana'}
#         ]

originalCategories = dict()
formattedCategories = dict()

familyId = 0

# format categories to fill formateddCategories dict
for cat in categories:
    catId = cat["id"]
    catName = cat["name"]

    if(catName == "Family"):
        # save familyId for later substitution
        familyId = catId
    formattedCategories[catName] = catId
    originalCategories[catName] = catId

# replace Communer and Smart id to be equals to Family
for cat in formattedCategories:

    if(cat == "Communer" or cat == "Smart"):
        formattedCategories[cat] = familyId

# Aplly category change for all cars
for car in cars:

    carCategories = list()

    for cat in car["categories"]:
        carCategories.append(formattedCategories[cat["name"]])

    params = {
        "data": {
            "where": {"id": car["id"]},
            "data": {
                "categories": carCategories
            }
        }
    }

    print(params)
    # TODO uncomment execute mutation here
    # client.execute(updateCarMutation, variable_values=params))


newCategories = {"Sport": "Smart", "Electric": "Communer"}

pprint(originalCategories)

for cat in newCategories:

    params = {
        "input": {
            "where": {"id": originalCategories[newCategories[cat]]},
            "data": {
                "name": cat,
                "slug": cat.lower()
            }
        }
    }
    pprint(params)
    # TODO uncomment execute mutation here
    # client.execute(updateCategoryMutation, variable_values=params)
