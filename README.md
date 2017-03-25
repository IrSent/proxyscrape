# proxyscrape

Installation
------------

homebrew (https://brew.sh):
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew update
$ brew install python3
```

env:
```
$ pip3 install virtualenvwrapper
$ export WORKON_HOME=~/envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv proxyscrape -p python3
$ cdvirtualenv
```

repo:
```
$ git clone https://github.com/IrSent/proxyscrape project/
$ cd project/
$ pip install -r requirements.txt
```

Usage
-------------

```
$ cd proxy
$ scrapy crawl proxy_spider
```

# Results stored in `proxydb` sqlite file
