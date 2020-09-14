======
pockyt
======

A simple, yet powerful, commandline client for your `Pocket <https://getpocket.com/>`_ collection.

.. image:: http://img.shields.io/pypi/v/pockyt.svg?style=flat
    :target: https://pypi.python.org/pypi/pockyt

.. image:: http://img.shields.io/pypi/l/pockyt.svg?style=flat
    :target: https://pypi.python.org/pypi/pockyt

Links
-----

* `PyPi package <https://pypi.python.org/pypi/pockyt>`_
* `GitHub repository <https://github.com/achembarpu/pockyt>`_

About
-----

`Pocket <https://getpocket.com/>`_ is an application for managing a reading list of articles from the Internet.

**pockyt** is a commandline client that interfaces the pocket API and provides a way to interact with your Pocket collection.
Using simple command sequences, routine tasks can be automated and reusable scripts can be created.

Privacy
-------

**pockyt** does **NOT** track, store, or monitor your usage and/or data.
Moreover, pockyt interacts with the pocket API using local credentials and does not attempt to communicate with any other services.

Installation
------------

**pockyt** supports Python 2.7+ & 3.4+ on Windows, macOS, & GNU/Linux platforms.

1. Install pockyt: :code:`pip install -U pockyt`
2. Connect Pocket account: :code:`pockyt reg`
3. Refer the Examples & Documentation below.

Examples
--------

* Get the latest 5 items' links & excerpts and save them to a file.

    .. code::

        pockyt get -n 5 -f '{link} - {excerpt}' -o readlater.txt

* Get the oldest 10 items and delete them from Pocket.

    .. code::

        pockyt get -n 10 -r oldest -f '{id}' | pockyt mod -d -i redirect

* Get all the items about 'python' and open them in a browser.

    .. code::

        pockyt get -q 'python' -o browser

* Get all the links from a 'links.txt' and add them to Pocket.

    .. code::

        pockyt put -i links.txt

* Get all favorited items and archive them.

    .. code::

        pockyt get -v 1 | pockyt mod -a 1 -i redirect

* Get all favorited items and save offline copies of them.

    .. code::

        pockyt get -v 1 -a ./pocket

Contribute
----------

Feel free to contribute features, bugfixes, improvements, and usage ideas.

1. `Fork <https://github.com/achembarpu/pockyt/fork>`_ pockyt.

2. Work on the source code.

    .. code::

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

3. Submit a `pull request <https://github.com/achembarpu/pockyt/compare>`_.

License
-------

This project uses the `GNU GPLv3 License <https://github.com/achembarpu/pockyt/blob/master/LICENSE.txt>`_.

Documentation
-------------

**pockyt help/-h/--help** :

    help
        show pockyt usage help
    reg
        connect a pocket account
    get
        get pocket collection, with useful item info
    put
        add to pocket collection, using links
    mod
        modify pocket collection, using item ids

**pockyt get -h** :

  -h, --help
                        show this help message and exit
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
  -a <path>, --archive <path>
                        save offline copies : <path> : path/to/archive/folder

**pockyt put -h** :

  -h, --help            show this help message and exit
  -f <specifier>, --format <specifier>
                        unformat input : <specifier> : {'{link}', [id, title,
                        link, excerpt, tags]}
  -i <option>, --input <option>
                        obtain input : <option> : {console, [redirect,
                        link, filename]}

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
