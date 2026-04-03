import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

# When scanning the limits are:
# - 1MB of data
# - Scan can set a limit on the number of items to return
response = table.scan()

for item in response['Items']:
    print(item)

print(f"\nTotal items: {response['Count']}")
