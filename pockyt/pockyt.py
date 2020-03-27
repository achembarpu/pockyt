from __future__ import absolute_import, print_function, unicode_literals, with_statement

import argparse
import sys

from .api import API
from .auth import Authenticator
from .client import Client
from .wrapper import print_bug_report


class Pockyt(object):
    """
    pockyt - Pocket Commandline Client
    """
    def __init__(self):
        self._setup_parsers()
        self._args = self.parser.parse_args()

    def _setup_parsers(self):
        # main parser
        self.parser = argparse.ArgumentParser(
            description="automate and manage your pocket collection",
            epilog="Project Page: ` {0} `".format(API.REDIRECT_URL),
        )

        # subcommand parsers
        subparsers = self.parser.add_subparsers(dest="do")

        subparsers.add_parser("help", help="show pockyt usage help")

        # connect account
        subparsers.add_parser("reg", help="connect a pocket account")

        # get items from collection
        get_parser = subparsers.add_parser(
            "get",
            help="get pocket collection, with useful item info",
        )
        get_parser.add_argument(
            "-c",
            "--content",
            default="all",
            metavar="<type>",
            choices=["all", "article", "video", "image"],
            help="content type : <type> : {all, [article, video, image]}",
        )
        get_parser.add_argument(
            "-s",
            "--state",
            default="all",
            metavar="<state>",
            choices=["all", "unread", "archive"],
            help="collection state : <state> : {all, [unread, archive]}",
        )
        get_parser.add_argument(
            "-r",
            "--sort",
            default="newest",
            metavar="<order>",
            choices=["newest", "oldest", "title", "site"],
            help="item sorting : <order> : {newest, [oldest, title, site]}",
        )
        get_parser.add_argument(
            "-n",
            "--count",
            metavar="<amount>",
            default=-1,
            type=int,
            help="number of items : <amount> : {-1: all, [n: amount]}",
        )
        get_parser.add_argument(
            "-q",
            "--query",
            metavar="<query>",
            help="search query : <query> : {None}",
        )
        get_parser.add_argument(
            "-t",
            "--tag",
            metavar="<option>",
            default="-1",
            type=str,
            help="filter tag : {-1: nofilter, "
            "[tagname: tagged, 0: untagged}",
        )
        get_parser.add_argument(
            "-v",
            "--favorite",
            metavar="<option>",
            default=-1,
            type=int,
            choices=[-1, 0, 1],
            help="filter favorites : <option> : {-1: No Filter, "
            "[1: favorited, 0: un-favorited]}",
        )
        get_parser.add_argument(
            "-d",
            "--domain",
            metavar="<domain>",
            help="restrict items to domain : <domain> : {None}",
        )
        get_parser.add_argument(
            "-f",
            "--format",
            metavar="<specifier>",
            default="{id} | {title} | {link}",
            help="format output : <specifier> : {'{id} | {title} | {link}', "
            "[id, title, link, excerpt, tags]}",
        )
        get_parser.add_argument(
            "-o",
            "--output",
            metavar="<option>",
            help="redirect output : <option> : {None, [browser, filename]}",
        )
        get_parser.add_argument(
            "-a",
            "--archive",
            metavar="<path>",
            help="save offline copies : <path> : path/to/archive/folder",
        )

        # add items to collection
        put_parser = subparsers.add_parser(
            "put",
            help="add to pocket collection, using links",
        )
        put_parser.add_argument(
            "-f",
            "--format",
            metavar="<specifier>",
            default="{link}",
            help="unformat input : <specifier> : {'{link}', "
            "[id, title, link, excerpt, tags]}",
        )
        put_parser.add_argument(
            "-i",
            "--input",
            default="console",
            metavar="<option>",
            help=
            "obtain input : <option> : {console, [redirect, link, filename]}",
        )

        # modify items in collection
        mod_parser = subparsers.add_parser(
            "mod",
            help="modify pocket collection, using item ids",
        )
        mod_parser.add_argument(
            "-f",
            "--format",
            metavar="<specifier>",
            default="{id}",
            help="unformat input : <specifier> : {'{id}', "
            "[id, title, link, excerpt, tags]}",
        )
        mod_parser.add_argument(
            "-i",
            "--input",
            default="console",
            metavar="<option>",
            help="obtain input : <option> : {console, [redirect, filename]}",
        )
        options = mod_parser.add_mutually_exclusive_group(required=True)
        options.add_argument(
            "-d",
            "--delete",
            action="store_true",
            help="delete items",
        )
        options.add_argument(
            "-a",
            "--archive",
            default=-1,
            metavar="<option>",
            choices=[-1, 0, 1],
            type=int,
            help=
            "archive items : <option> : {-1: None, [1: archive, 0: unarchive]}",
        )
        options.add_argument(
            "-v",
            "--favorite",
            default=-1,
            metavar="<option>",
            choices=[-1, 0, 1],
            type=int,
            help=
            "favorite items : <option> : {-1: None, [1: favorite, 0: unfavorite]}",
        )

    def run(self):
        if not self._args.do or self._args.do == "help":
            self.parser.print_help()
            return

        auth = Authenticator(self._args)

        if self._args.do == "reg":
            auth.setup()
            return

        auth.load()

        pocket = Client(auth.credentials, self._args)
        pocket.run()


def main():
    error = 0
    try:
        app = Pockyt()
        error = app.run()
    except KeyboardInterrupt:
        pass
    except Exception:
        error = 1
        print_bug_report()
    sys.exit(error)


if __name__ == "__main__":
    main()
