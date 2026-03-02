#!/usr/bin/env python3

import argparse
from core import template

def main():
    parser = argparse.ArgumentParser(prog="task")
    sub = parser.add_subparsers(dest="command")

    # crate command
    create_parser = sub.add_parser("create", help="Create a new task from a template")
    create_parser.add_argument("type", help="Template type (public_task, private_task, ...")
    create_parser.add_argument("name", help="File name")

    args = parser.parse_args()

    if args.command == "create":
        template(args.type, args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()                           
                                   