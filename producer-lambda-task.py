import json
import boto3
import uuid
import os

# Initialize AWS Clients
sqs = boto3.client('sqs')
dynamodb = boto3.resource('dynamodb')
# Use an environment variable for the table name for extra security
table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE', 'YourTableName'))
QUEUE_URL = os.environ.get('QUEUE_URL')

def lambda_handler(event, context):
    # 1. Handle CORS Preflight
    method = event.get('requestContext', {}).get('http', {}).get('method')
    if method == 'OPTIONS':
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS,PATCH",
                "Access-Control-Allow-Headers": "Content-Type,Authorization",
                "Access-Control-Max-Age": "3600"
            }
        }

    # 2. Extract Identity from JWT
    try:
        user_id = event['requestContext']['authorizer']['jwt']['claims']['sub']
    except KeyError:
        return {
            "statusCode": 401, 
            "body": json.dumps({"error": "Unauthorized"})
        }
    
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PATCH",
        "Access-Control-Allow-Headers": "Content-Type,Authorization"
    }

    try:
        if method == 'GET':
            response = table.scan(
                FilterExpression=boto3.dynamodb.conditions.Attr('userId').eq(user_id)
            )
            return {"statusCode": 200, "headers": headers, "body": json.dumps(response.get('Items', []))}

        elif method == 'POST':
            body = json.loads(event.get('body', '{}'))
            task_id = str(uuid.uuid4())
            payload = {
                "action": "ADD", 
                "taskId": task_id, 
                "userId": user_id,
                "taskName": body.get('taskName', 'New Task'), 
                "dueDate": body.get('dueDate', 'No Date'),
                "status": "pending"
            }
            sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(payload))
            return {"statusCode": 200, "headers": headers, "body": json.dumps({"taskId": task_id})}
            
        # ... rest of PATCH/DELETE logic
    except Exception as e:
        return {"statusCode": 500, "headers": headers, "body": json.dumps({"error": str(e)})}