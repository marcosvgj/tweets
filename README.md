
<h1 align="center">
  <br>
  <a href="https://developer.twitter.com/en"><img src="docs/images/twitter.png" alt="Tweet" width="200"></a>
  <br>
  <b>
  Tweets
  </b>
  <br>
</h1>

<h4 align="center">A Twitter API data pipeline case using Lambda Architecture.</h4>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue">
  </a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-black"></a>
  
  <a href="https://opensource.org/licenses/Apache-2.0">
      <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
  </a>

  <a href="https://pypi.org/project/tweepy/3.10.0/">
    <img src="https://img.shields.io/badge/tweepy-3.10.0-blue">
  </a>
</p>

<p align="center">
  <a href="#data-archicteture">Data Archicteture</a> •
  <a href="#how-to-run-it">How To Use</a> •
  <a href="#related">References</a> •
  <a href="#todo">Todo's</a>
</p>

&nbsp;

![screenshot](docs/images/archicteture_ref.png)

Data Archicteture
============

This architecture is based on the most common Big Data Archicture, called as **Lambda Archicteture**, that's divided according those topics:
* **Data Source**: Responsible to map a new data source, such as Twitter API. 
* **Batch Layer**: Responsible to mantain components that can handle very large quantities of data.
* **Speed Layer**: Reponsible to maintain components that processes data streams in real time.
* **Serving Layer**: Output from the batch and speed layers are stored in the serving layer, which responds to ad-hoc queries by returning precomputed views or building views from the processed data.


***obs: Those components are wrapped by docker container environment.***

&nbsp;

How To Use
=========

## TODO 

&nbsp;

References
=========

## TODO 

&nbsp;

Todo's
=========

## TODO 

&nbsp;