import feedparser
import boto3

def hello(event, context):
    feed_links = []
    d = feedparser.parse("https://mkr-note.net/feeds/all.atom.xml")

    for entry in d["entries"]:
        feed_links.insert(0, entry.link)

    insert_db(feed_links)

    return feed_links

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def insert_db(feed_links):
    db = boto3.resource("dynamodb")
    table = db.Table("testdb")

    for feed_link in feed_links:
        table.update_item(
            Key={
                "url": feed_link
            }
        )

