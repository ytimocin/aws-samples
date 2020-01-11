import boto3

session = boto3.Session(profile_name='ytimocin')

client = session.client('kinesis')

response = client.list_streams()

print(response)