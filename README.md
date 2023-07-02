# Logging in Python

# Why? When? And How?

PyCon PL 2023\, Vagiz Duseev

Vagiz Duseev

@vduseev

vagiz@duseev\.com

# Why logging is a problem?

First\, it starts very simple

Gets more complicated over time

Adds more overhead in production

Becomes crucial during incidents

Turns into a headache at large scale and distribution

![](img/python-logging2.png)

# It starts simple

_Let’s take a look_

![](img/python-logging3.png)

# How about a timestamp?

_Let’s take a look_

![](img/python-logging4.gif)

![](img/python-logging5.png)

# Let’s get logging

_Let’s take a look_

![](img/python-logging6.png)

# Give me my timestamp back

_Let’s take a look_

![](img/python-logging7.png)

# Let’s try something else

_Let’s take a look_

![](img/python-logging8.png)

# Managing logging in other modules

_Let’s take a look_

![](img/python-logging9.png)

# Logging to a file

_Let’s take a look_

![](img/python-logging10.png)

# Files need rotation

_Let’s take a look_

![](img/python-logging11.jpg)

# Your honour, objection!

Who rotates the log if the program stops?

How are we going to update rotation config?

What if logs occupy all space on the disk?

![](img/python-logging12.png)

# Files need rotation

# Log search

Just  __grep__  itgrep –i “192\.168\.2\.3” my\-logs\.log

What if it’s archived?zcat my\-logs\.5\.tar\.gz | grep –i “192\.168\.2\.3”

Grep with regex? Grep not through terminal? Aggregate? Regex?

# Let’s add indexationElastic / Splunk / Graylog / …

![](img/python-logging13.png)

![](img/python-logging14.png)

![](img/python-logging15.png)

![](img/python-logging16.png)

# Configure handler

![](img/python-logging17.png)

# Still configuring handler …

![](img/python-logging18.png)

# Same processing

_Let’s take a look_

![](img/python-logging19.png)

![](img/python-logging20.jpg)

![](img/python-logging21.png)

# Big brain time

Logging config to control every aspect

Docker daemon drivers

FluentD for log collection

Let’s take a look

![](img/python-logging22.gif)

# Perfect system

* Open source
* Stores logs\, metrics\, and traces
* Tailored for
  * Lots of writes\, small number of reads
  * On the flight analytics for alerting
  * Timeseries: all data has a timestamp
* Horizontally scalable
* Does not require running instances \(except for alerting\)
* Does not require schema to be defined upfront
* Agnostic to underlying storage

# This concludes: Logging in Python

github\.com/vduseev/python\-logging

@vduseev

vagiz@duseev\.com

![](img/python-logging23.png)

![](img/python-logging24.png)

![](img/python-logging25.png)
