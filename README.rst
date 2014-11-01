======
pockyt
======

A usable, customizable commandline client to automate and manage your pocket collection.

.. image:: http://img.shields.io/pypi/v/pockyt.svg?style=flat
    :target: https://pypi.python.org/pypi/pockyt

.. image:: http://img.shields.io/pypi/dm/pockyt.svg?style=flat
    :target: https://pypi.python.org/pypi/pockyt

.. image:: http://img.shields.io/pypi/l/pockyt.svg?style=flat
    :target: https://pypi.python.org/pypi/pockyt

Links
-----

* `PyPi <https://pypi.python.org/pypi/pockyt>`_
* `GitHub <https://github.com/arvindch/pockyt>`_

About
-----

`Pocket <https://getpocket.com/>`_ is an application for managing a reading list of articles from the Internet.

This commandline client interfaces the pocket API and provides a way to interact with your pocket collection.

Using simple command sequences, routine tasks can be automated and reusable scripts can be created.

Quick Start
-----------

``pockyt`` supports Python ``2.7.x`` and ``3.4.x``

1. ``$ pip install pockyt --upgrade``
2. ``$ pockyt reg``
3. Follow the prompts to connect your pocket account to pockyt.
4. Refer the Documentation and Examples for usage info and ideas.

Examples
--------

* Get the latest 5 items' links & excerpts and save them to a file.
  ::
      $ pockyt get -n 5 -f '{link} - {excerpt}' -o readlater.txt

* Get the oldest 10 items and delete them from Pocket.
  ::
      $ pockyt get -n 10 -r oldest -f '{id}' | pockyt mod -d -i redirect

* Get all the items about 'python' and open them in a browser.
  ::
      $ pockyt get -q 'python' -o browser

* Get all the links from a 'links.txt' and add them to Pocket.
  ::
      $ pockyt put -i links.txt

* Get all favorited items and archive them.
  ::
      $ pockyt get -v 1 | pockyt mod -a 1 -i redirect


Documentation
-------------

**pockyt -h** :

    -h, --help         show this help message and exit
    reg
        connect a pocket account
    get
        get pocket collection, with useful item_info
    put
        add to pocket collection, using links
    mod
        modify pocket collection, using item_ids

**pockyt get -h** :

  -h, --help            show this help message and exit
  -c <type>, --content <type>
                        content type : <type> : {all, [article, video, image]}
  -s <state>, --state <state>
                        collection state : <state> : {all, [unread, archive]}
  -r <order>, --sort <order>
                        item sorting : <order> : {newest, [oldest, title,
                        site]}
  -n <amount>, --count <amount>
                        number of items : <amount> : {-1: all, [n: amount]}
  -q <query>, --query <query>
                        search query : <query> : {None}
  -t <option>, --tag <option>
                        filter tag : {-1: nofilter, [tagname: tagged, 0:
                        untagged}
  -v <option>, --favorite <option>
                        filter favorites : <option> : {-1: No Filter, [1:
                        favorited, 0: un-favorited]}
  -d <domain>, --domain <domain>
                        restrict items to domain : <domain> : {None}
  -f <specifier>, --format <specifier>
                        format output : <specifier> : {'{id} | {title} |
                        {link}', [id, title, link, excerpt, tags]}
  -o <option>, --output <option>
                        redirect output : <option> : {None, [browser,
                        filename]}

**pockyt put -h** :

  -h, --help            show this help message and exit
  -f <specifier>, --format <specifier>
                        unformat input : <specifier> : {'{link}', [id, title,
                        link, excerpt, tags]}
  -i <option>, --input <option>
                        obtain input : <option> : {console, [redirect,
                        filename]}

**pockyt mod -h** :

  -h, --help            show this help message and exit
  -f <specifier>, --format <specifier>
                        unformat input : <specifier> : {'{id}', [id, title,
                        link, excerpt, tags]}
  -i <option>, --input <option>
                        obtain input : <option> : {console, [redirect,
                        filename]}
  -d, --delete          delete items
  -a <option>, --archive <option>
                        archive items : <option> : {-1: None, [1: archive, 0:
                        unarchive]}
  -v <option>, --favorite <option>
                        favorite items : <option> : {-1: None, [1: favorite,
                        0: unfavorite]}

Contribute
----------

Feel free to contribute features, bugfixes, improvements, and usage ideas.

`Fork <https://github.com/arvindch/pockyt/fork>`_ pockyt.
Work on the source code.
::
    git clone git@github.com:<username>/pockyt.git
    cd pockyt
    pip install -e .
    git checkout -b new-feature
    ...
    # do stuff
    ...
    git add .
    git commit -am 'commit msg'
    git push origin new-feature

Then, submit a `pull request <https://github.com/arvindch/pockyt/compare>`_.

License
-------

This project uses the `GNU GPLv3 License <https://github.com/arvindch/pockyt/blob/master/LICENSE.txt>`_.
