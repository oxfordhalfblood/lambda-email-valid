import json
import re
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def validate(event, context):
    event_body = json.loads(event['body'])
    email_regex = re.compile('^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    matches = email_regex.match(event_body['email']) != None
    response = {
        'statusCode': 200,
        'body': json.dumps({ 'result': matches })
    }
    print(f'Result for {event_body["email"]}: {matches}')
    logger.info("Response is: %s", response)
    return response
    # Hello func
    # body = {
    #     "message": "Go Serverless v2.0! Your function executed successfully!",
    #     "input": event,
    # }