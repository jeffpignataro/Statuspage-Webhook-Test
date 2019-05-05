import sys
import json

from models.statusPageResponse import StatusPageResponse


def handler(event, context):
    try:
        queryStringParameters = event['queryStringParameters'] or {}
        pathParameters = event['pathParameters'] or {}
    except:
        queryStringParameters = {}
        pathParameters = {}

    if pathParameters and 'proxy' in pathParameters:
        parsedPathParameters = pathParameters['proxy'].split("/")
    else:
        parsedPathParameters = []

    try:
        statusPageResponse = json.load(event["body"])
    except Exception as e:
        return responseObject(502, "Error executing method. Error information: {}".format(e))

    try:
        # This is where the magic happens
        apiResponse = statusPageResponse
        # generateResponse(parsedPathParameters, queryStringParameters)
    except Exception as e:
        return responseObject(502, "Error executing method. Error information: {}".format(e))

    if not apiResponse:
        return responseObject(404, "Error: No method found.")

    return responseObject(200, apiResponse)


def generateResponse(pathArgs, qsArgs):
    return 'Sample Response Object'


def responseObject(statusCode, message):
    return {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Origin,Content-Type,Accept,cache-control",
            "Access-Control-Allow-Credentials": "true"},
        "body": json.dumps(message)
    }
