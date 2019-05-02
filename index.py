import sys
import json


def handler(event, context):
    queryStringParameters = event['queryStringParameters'] or {}
    pathParameters = event['pathParameters'] or {}

    if pathParameters and 'proxy' in pathParameters:
        parsedPathParameters = pathParameters['proxy'].split("/")

    try:
        # This is where the magic happens
        apiResponse = callApiMethod(
            parsedPathParameters, queryStringParameters)
    except Exception as e:
        return responseObject(502, "Error executing method. Error information: {}".format(e))

    if not apiResponse:
        return responseObject(404, "Error: No method found.")

    return responseObject(200, apiResponse)


def callApiMethod(pathArgs, qsArgs):
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
