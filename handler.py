import feedparser
import boto3

def hello(event, context):
    feed_links = []
    d = feedparser.parse("https://mkr-note.net/feeds/all.atom.xml")

    for entry in d["entries"]:
        feed_links.insert(0, entry.link)

    return feed_links

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
