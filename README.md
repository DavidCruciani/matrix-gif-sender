# matrix-gif-sender

Bot that send random gif



## Installation

```bash
sudo apt-get update -y
sudo apt-get install libolm-dev -y
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Tenor

It's required an api key and a client key that can be obtain on [tenor website](https://developers.google.com/tenor/guides/quickstart)



## Usage

First, make a copy of `config.sample.py` to `config.py` and fill it.

Then run:

```bash
python main.py
```

Go to a room and enter a message like this:

```
!gif excited
```
