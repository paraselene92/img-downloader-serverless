import feedparser
import boto3

def hello(event, context):
    feed_links = []
    d = feedparser.parse("https://mkr-note.net/feeds/all.atom.xml")

    for entry in d["entries"]:
        feed_links.insert(0, entry.link)

    create_db()

    return feed_links

def create_db():
    db = boto3.client("dynamodb")
    db.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'url',
                'AttributeType': 'S',
            },
        ],
        TableName='testdb',
        KeySchema=[
            {
                'AttributeName': 'url',
                'KeyType': 'HASH',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        }
    )


    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
