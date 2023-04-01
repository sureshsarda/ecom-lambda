import boto3
import json
import decimal
import uuid
import datetime


print('Loading lambda function')

dynamo = boto3.resource('dynamodb')
datawarehouse = dynamo.Table('datawarehouse')


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def validate_supported_keys(payload):
    supported_keys = {'productName', 'imageURL', 'quantity'}
    extra_keys = set(filter(lambda x: x not in supported_keys, payload.keys()))
    if extra_keys:
        raise ValueError('Unsupported Keys Found: ' + ', '.join(extra_keys) + ' Supported Keys: ' + ', '.join(supported_keys))
    else:
        print('Keys are valid')


def respond(err, res=None):


    if err:
        payload = {
            'status': 'failure',
            'message': str(err)
        }
    else:
        payload = {
            'status': 'success',
            'data': res
        }

    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps(payload, cls=DecimalEncoder),
        'headers': {
            'Content-Type': 'application/json',
        }
    }

def get_one(itemId):
    print('Get Single Item: ' + str(itemId))
    return datawarehouse.get_item(Key={'id': itemId}).get('Item')

def put_one(itemId, payload):
    print('Updating Single Item: ' + itemId)
    validate_supported_keys(payload)
    payload['lastModified'] = str(datetime.datetime.utcnow())
    print(json.dumps(payload, indent=4))

    payload['id'] = itemId
    datawarehouse.put_item(Item=payload)
    return get_one(itemId)


def delete_one(itemId):
    print('Deleting Item: ' + str(itemId))
    datawarehouse.delete_item(Key={'id': itemId})
    return {'status': 'ok'}



def insert_item(payload):
    print("Insert New Item")
    print(json.dumps(payload, indent=4))
    validate_supported_keys(payload)
    payload['id'] = str(uuid.uuid4())
    payload['lastModified'] = str(datetime.datetime.utcnow())
    datawarehouse.put_item(Item=payload)
    return get_one(payload['id'])


def get_all():
    res = datawarehouse.scan(TableName='datawarehouse')
    print(res)
    return res.get('Items', [])


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    print("Received event: " + json.dumps(event, indent=4))

    operation = event['httpMethod']

    pathParameters = event['pathParameters']

    itemId = None
    if pathParameters:
        itemId = pathParameters['itemid']

    try:
        if itemId is not None:
            # handle single item
            if operation == 'GET':
                return respond(None, get_one(itemId))

            elif operation == 'PUT':
                return respond(None, put_one(itemId, json.loads(event['body'])))

            elif operation == 'DELETE':
                return respond(None, delete_one(itemId))

            else:
                return respond(ValueError('Unsupported method "{}"'.format(operation)))


        else:
            # handle bulk operation
            if operation == 'POST':
                return respond(None, insert_item(json.loads(event['body'])))

            elif operation == 'GET':
                return respond(None, get_all())

            else:
                return respond(ValueError('Unsupported method "{}"'.format(operation)))

    except ValueError as e:
        print(str(e))
        return respond(e)
    except Error as err:
        print(str(err))
        return respond(err)