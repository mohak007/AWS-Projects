import json
import os
import uuid
import boto3
from boto3.dynamodb.conditions import Attr  # Needed for scan filter

TABLE = os.environ['TODOS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)

def response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',   # important for frontend
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(body, default=str)
    }

def lambda_handler(event, context):
    method = event.get('httpMethod')
    if method == 'OPTIONS':
        return response(200, {"message": "CORS preflight OK"})

    if method == 'POST':  # Register User
        body = json.loads(event.get('body') or '{}')
        username = body.get('username')
        password = body.get('password')
        if not username or not password:
            return response(400, {"error": "username and password are required"})

        # Before inserting, check if user already exists
        res = table.scan(
            FilterExpression=Attr("username").eq(username)
        )
        if res.get("Items"):
            return response(409, {"error": "User already exists"})

        item = {
            'id': str(uuid.uuid4()),
            'username': username,
            'password': password
        }
        table.put_item(Item=item)
        return response(201, {"message": "User registered successfully", "username": username})

    if method == 'GET':
        params = event.get("queryStringParameters") or {}
        username = params.get("username")
        password = params.get("password")

        if username and not password:
            # ✅ Check existence only
            res = table.scan(
                FilterExpression=Attr("username").eq(username)
            )
            if res.get("Items"):
                return response(200, {"exists": True, "username": username})
            else:
                return response(200, {"exists": False, "username": username})

        if username and password:
            # ✅ Normal login
            res = table.scan(
                FilterExpression=Attr("username").eq(username) & Attr("password").eq(password)
            )
            if res.get("Items"):
                return response(200, {"message": "Login successful", "username": username})
            else:
                return response(401, {"error": "Invalid credentials"})

        return response(400, {"error": "username (and password for login) are required"})

    return response(405, {"error": "Method not allowed"})
