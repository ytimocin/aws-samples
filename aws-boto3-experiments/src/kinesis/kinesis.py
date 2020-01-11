import boto3

session = boto3.Session(profile_name='ytimocin')

client = session.client('kinesis')

list_of_streams = client.list_streams()

print(list_of_streams)

# create_test_stream = client.create_stream(StreamName='test_stream', ShardCount=1)
#
# print(create_test_stream)

put_record_to_test_stream = client.put_record(
    StreamName='test_stream',
    Data=b'bytes',
    PartitionKey='test',
    ExplicitHashKey='123456',
    SequenceNumberForOrdering='1'
)

print(put_record_to_test_stream)

get_records_from_test_stream = client.get_records(
    ShardIterator='test',
    Limit=123
)

print(get_records_from_test_stream)
