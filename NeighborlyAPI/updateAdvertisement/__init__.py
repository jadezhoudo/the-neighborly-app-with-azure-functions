import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://codeninjacosmosdb:6l3D42zvFznQOcKISYnRqDVODkUFS4mS6ApCLaftMWWQCLkqyjmxhfWbLkVrmh0tVNuJPcO0A5w6ACDbonRpSA==@codeninjacosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@codeninjacosmosdb@"
            client = pymongo.MongoClient(url)
            database = client['codeninjaDB']
            collection = database['advertisements']

            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)
