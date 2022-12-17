"""
A simple slack message sender
"""
import collections
import json
import os
import requests
from loguru import logger


def http_post(url: str, timeout: int = 5, payload=None) -> requests.Response:
    try:
        response = requests.post(url=url, data=payload, timeout=timeout)
    except requests.exceptions.ConnectionError:
        logger.error("❌ Failed to reach slack webhook. Check your internet connection")
    except requests.exceptions.HTTPError:
        logger.error("❌ Slack webhook returned an error")
    except requests.exceptions.Timeout:
        logger.error("❌ Slack webhook timed out")
    except requests.exceptions.RequestException:
        logger.error("❌ Slack webhook returned an error")
    except Exception as e:
        logger.error(f"❌ Slack webhook error: {e}")
    if response.status_code != 200:
        logger.error(f"❌ Slack webhook returned status code: {response.status_code}")
    else:
        logger.info("✅ Message sent to slack")


def send(msg, timeout=5, use_raw=False, webhook=None):
    """
    A function to send messages on slack
    :param msg: string, list of strings, dictionary (or defaultdict/OrderedDict)
    :param use_raw: if True, msg (dict) is dumped as json and sent to slack. Use for advanced messages
    :param webhook: Slack webhook URL. Either this or SANDESH_WEBHOOK environment variable should be present
    """
    if webhook is None:
        webhook = os.environ.get("SANDESH_WEBHOOK")

    if webhook is None:
        logger.error("Sandesh: No webhooks found")
        return

    data = dict()

    if isinstance(msg, str):
        data = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": msg,
                    },
                }
            ]
        }
        http_post(webhook, payload=json.dumps(data), timeout=timeout)

    elif isinstance(msg, list):
        data["text"] = "\n".join(msg)
        http_post(webhook, payload=json.dumps(data), timeout=timeout)

    elif isinstance(msg, (dict, collections.defaultdict, collections.OrderedDict)):
        values = []
        for k, v in msg.items():
            values.append(str(k) + ": " + str(v))
        data["text"] = "\n".join(values)
        http_post(webhook, payload=json.dumps(data), timeout=timeout)

    elif isinstance(msg, dict) and use_raw is True:
        http_post(webhook, payload=json.dumps(msg), timeout=timeout)

    else:
        logger.error("Sandesh: Type for variable `msg`, is currently not supported")
