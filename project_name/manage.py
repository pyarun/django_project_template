#!/usr/bin/env python
import os
import sys, socket

hostname = socket.gethostname()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.local_{}".format(hostname.replace("-", "")))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
