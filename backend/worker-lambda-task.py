import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE', 'YourTableName'))

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            data = json.loads(record['body'])
            action = data.get('action')
            task_id = data.get('taskId')

            if action == 'DELETE':
                table.delete_item(Key={'taskId': task_id})
            elif action == 'ADD':
                table.put_item(Item={
                    'taskId': task_id,
                    'userId': data.get('userId'),
                    'taskName': data.get('taskName'),
                    'dueDate': data.get('dueDate'),
                    'status': data.get('status', 'pending')
                })
            elif action == 'UPDATE':
                new_status = data.get('status')
                table.update_item(
                    Key={'taskId': task_id},
                    UpdateExpression="set #st = :s",
                    ExpressionAttributeNames={'#st': 'status'},
                    ExpressionAttributeValues={':s': new_status}
                )
        except Exception as e:
            print(f"Worker Error: {str(e)}")
            raise e
