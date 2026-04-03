import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

# Scan with a filter expression to find users by status.
# Note: this uses scan() with a FilterExpression, not query(),
# because "status" is not a key attribute on this table.
response = table.scan(
    FilterExpression=Attr('status').eq('active')
)

for item in response['Items']:
    print(item)

print(f"\nActive users: {response['Count']}")
