"""
A simple slack message sender
"""
import collections
import json
import os
import requests


def send(msg, use_raw=False, webhook=None):
    """
    A function to send messages on slack
    :param msg: string, list of strings, dictionary (or defaultdict/OrderedDict)
    :param use_raw: if True, msg (dict) is dumped as json and sent to slack. Use for advanced messages
    :param webhook: Slack webhook URL. Either this or SANDESH_WEBHOOK environment variable should be present
    """
    if webhook is None:
        webhook = os.environ.get("SANDESH_WEBHOOK")
    
    if webhook is None:
        raise Exception("No webhooks found")
    
    data = dict()
    
    if isinstance(msg, str):
        data["text"] = msg
        requests.post(webhook, json.dumps(data))
    
    elif isinstance(msg, list):
        data["text"] = '\n'.join(msg)
        requests.post(webhook, json.dumps(data))
    
    elif isinstance(msg, (dict, collections.defaultdict, collections.OrderedDict)):
        values = []
        for k, v in msg.items():
            values.append(str(k) + ": " + str(v))
        data["text"] = '\n'.join(values)
        requests.post(webhook, json.dumps(data))
    
    elif isinstance(msg, dict) and use_raw is True:
        requests.post(webhook, json.dumps(msg))
    
    else:
        raise Exception("Type for variable: msg, is currently not supported")
