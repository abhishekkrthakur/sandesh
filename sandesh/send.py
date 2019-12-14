"""
A simple slack message sender
@author: Abhishek Thakur (abhishek4@gmail.com)
"""
import collections
import json
import os
import requests


def send(msg, webhook=None):
    if webhook is None:
        webhook= os.environ.get("SLACK_WEBHOOK")
    if webhook is None:
        raise Exception(
    """
    No slack webhooks found. Either provide webhook as an argument 
    to this function or use SLACK_WEBHOOK environment variable
    """
    )
    data = dict()
    if isinstance(msg, str):
        data["text"] = msg
        requests.post(webhook, json.dumps(data))
    elif isinstance(msg, list):
        data["text"] = '\n'.join(msg)
    elif isinstance(msg, (dict, collections.defaultdict, collections.OrderedDict)):
        values = []
        for k, v in msg.items():
            values.append(str(k) + ": " + str(v))
        data["text"] = '\n'.join(msg)
    else:
        raise Exception(
    """
    variable msg can only be a string, list of strings, dictionary, defaultdict or OrderedDict
    """
    )
