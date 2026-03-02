#!/usr/bin/env python3

import argparse
from core import template, update_log


def main():
    parser = argparse.ArgumentParser(prog="task")
    sub = parser.add_subparsers(dest="command")

    # ------------------------
    # CREATE COMMAND
    # ------------------------
    create_parser = sub.add_parser(
        "create",
        help="Create a new file from a template"
    )
    create_parser.add_argument(
        "type",
        help="Template type (public_task, private_task, routine, bin, log)"
    )
    create_parser.add_argument(
        "name",
        help="File name"
    )

    # ------------------------
    # LOG COMMAND
    # ------------------------
    log_parser = sub.add_parser(
        "log",
        help="Update today's log file"
    )

    args = parser.parse_args()

    if args.command == "create":
        template(args.type, args.name)

    elif args.command == "log":
        update_log()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()