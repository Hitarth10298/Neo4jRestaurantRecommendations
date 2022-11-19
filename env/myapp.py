from fastapi import FastAPI
import recommender
import atexit

#global variables
uri = "neo4j://localhost:7687"
user = "neo4j"
password = "neo4j" # modify this accordingly based on your own password

neo_db = recommender.Recommender(uri, user, password)

# exit handler
def exit_application():
    neo_db.close()

atexit.register(exit_application)

app = FastAPI()

@app.get('/get-recommedation')
async def get_recommedation(cuisine = '', location = '', person = '', max: bool = False):
    # convert string to list, (Alice,Judy,Sayaka) => ['Alice', 'Judy', 'Sayaka']
    person_list = [] if person == '' else person.split(',')
    
    # call the function from recommender module, matching is case-sensitive
    result = neo_db.find_recommendation(cuisine, location, person_list, max)
    return result