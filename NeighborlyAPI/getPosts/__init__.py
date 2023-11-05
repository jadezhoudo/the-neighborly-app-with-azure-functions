import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://codeninjacosmosdb:6l3D42zvFznQOcKISYnRqDVODkUFS4mS6ApCLaftMWWQCLkqyjmxhfWbLkVrmh0tVNuJPcO0A5w6ACDbonRpSA==@codeninjacosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@codeninjacosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['codeninjaDB']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
