[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Social Media Problems

Social Media can be a nuance to work with. There's too much content to
work and sift through. With too much content to work through, there's
a lot of noise which can be a distraction. One way to reduce this
noise, is to be selective on what content you consume; and
importantly, from whom.

This project proposes to provide a novel solution to this. It scrapes
bio-medical data from known and famous scientists from Twitter in the
Biomedical space. It thereafter passes this data to an NLP model that
filters out non-medical related content, as a pre-processing step; and
finally stores this data(with a 7 day expiry) to a data
ware-house. This data from the data ware-house can be displayed on
some feed.


## How does this work?

See presentation.org for details.

## How do I set things up?

1. Prepare your system. You need to make you have python > 3.8, and
   the ability to install modules.
2. Create and enter your virtualenv:

```bash
virtualenv --python python3 venv
. venv/bin/activate
```
3. Install the required packages

```bash
# The --ignore-installed flag forces packages to
# get installed in the venv even if they existed 
# in the global env
pip install -r requirements.txt --ignore-installed
```


#### Running the flask app

To spin up the server:

```bash
env FLASK_DEBUG=1 FLASK_APP="run_server.py" flask run --port=8080
```

#### Running the redis daemon

This daemon is responsible for writing the tweets to REDIS. Make sure
you have a running REDIS instance!

```bash
python -m redis_worker

```

#### A note on dependencies

Make sure that the dependencies in the `requirements.txt` file match those in
guix. To freeze dependencies:

```bash
# Consistent way to ensure you don't capture globally
# installed packages
pip freeze --path venv/lib/python3.8/site-packages > requirements.txt

```

## Future Work

- Scrape data from other sources, like say, Slack channels, Matrix, Facebook, the Fediverse etc, etc.


## Note

A [virtual
biohackathon](https://github.com/virtual-biohackathons/covid-19-bh20)
that happened last year inspired this idea. A crude manual
implementation can be found
[here](https://git.genenetwork.org/GeneNetwork/feedanalyser.git).
