import os
import sys
import shutil
import subprocess

MAKEFILE = open("Makefile")

DEFAULTS = {
    "TARGET_IP": "127.0.0.1",
    "TARGET_PORT": "4444",
    "TARGET_USER": "root",
    "TARGET_PASSWORD" : "password",
    "TARGET_PATH": "/tmp",
    "TARGET_ARCH": "x86_64",
    "TARGET_OS": "linux"
}

