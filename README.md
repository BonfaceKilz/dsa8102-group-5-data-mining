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

TODO

## How do I set things up?

TODO

## Running in a python environment

TODO

## Running in a GNU Guix container

TODO

## Future Work

- Scrape data from other sources, like say, Slack channels, Matrix, Facebook, the Fediverse etc, etc.


## Note

A [virtual
biohackathon](https://github.com/virtual-biohackathons/covid-19-bh20)
that happened last year inspired this idea. A crude manual
implementation can be found
[here](https://git.genenetwork.org/GeneNetwork/feedanalyser.git).
