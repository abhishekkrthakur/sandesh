
 +-+-+-+-+-+-+-+
 |s|a|n|d|e|s|h|
 +-+-+-+-+-+-+-+

sandesh (संदेश) in Hindi means message. 
his is a simple python library to send messages to Slack using webhook urls.

### Installing

You can install the bleeding edge version of this library by doing:

```
git clone git@github.com:abhishekkrthakur/sandesh.git
cd sandesh
python setup.py install
```

Or from pip:

```
pip install sandesh
```

### Usage

Using sandesh is very easy.

First of all you need a webhook. You can either keep this webhook as environment variable: `SANDESH_WEBHOOK`
Or you can send it in the `send` function: `sandesh.send(msg, webhook="XXXXX")`.

I like to keep it as environment variable so that I dont accidently push it to GitHub ;)

You can send a message to the provided webhook by doing:

```
import sandesh

loss = 0.15
msg = f"Training loss was {loss}"
sandesh.send(msg)
```

sandesh also supports dictionaries, OrderedDict and defaultdict. An example for OrderedDict is provided below:

```
import collections
import sandesh

log = collections.OrderedDict([
        ('training_epoch', 5),
        ('loss', 0.08)
    ])
sandesh.send(log)
```

If you want to go fancy, take a look at custom messages for slack. You can create your own custom message and send using:

```
import sandesh

# data = Fancy slack json
sandesh.send(data, use_raw=True)
```


This is a simple app that I use to send me notifications of my training processes from home workstation or AWS/GCP machines.

In case of any doubts/troubles, feel free to contact me: abhishek4@gmail.com
