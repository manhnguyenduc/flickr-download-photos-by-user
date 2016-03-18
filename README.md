# Introduction
Simple script to download Flickr photos by user

To use it you need to get your own Flickr API key here: [Flickr API key](https://www.flickr.com/services/api/misc.api_keys.html)

Requirements
============

* [argparse](http://docs.python.org/2.7/library/argparse.html) (Python 2.7+)
* [Python Dateutil](http://labix.org/python-dateutil)
* [Python Flickr API](https://github.com/alexis-mignon/python-flickr-api/)
* 

Simple to use

```
python download_all.py 
usage: download_all.py [-h] [-u URL] [-p PAGE]

Downloads Flickr photo user.

To use it you need to get your own Flickr API key here:
https://www.flickr.com/services/api/misc.api_keys.html

  download a given set:
  > download_all.py -u https://www.flickr.com/photos/ericwong888 

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Download the given user
  -p PAGE, --page PAGE  Number page for download

```

==Example==
```
python download_all.py -u https://www.flickr.com/photos/ericwong888 -p 2
```

==Response==

```
total images 1588
total pages 16
num page for download 2
make dirname 99589174_N04
https://farm2.staticflickr.com/1677/25235145833_7aaa9b26d2_h.jpg
https://farm2.staticflickr.com/1457/25833425016_e0d2343b37_h.jpg
https://farm2.staticflickr.com/1620/25558757290_fd8cf1b0a3_h.jpg
https://farm2.staticflickr.com/1508/25738523782_429a69af80_h.jpg
https://farm2.staticflickr.com/1552/25855848335_41996d4d1c_h.jpg
```
