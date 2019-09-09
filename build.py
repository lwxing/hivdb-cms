#! /usr/bin/env python

import os
import re
import json
from datetime import datetime

import yaml
from yaml import Loader
from distutils.dir_util import copy_tree

BASEDIR = os.path.dirname(os.path.abspath(__file__))
PAGEDIR = os.path.join(BASEDIR, 'pages')
RESOURCEDIR = os.path.join(BASEDIR, 'resources')
IMAGEDIR = os.path.join(BASEDIR, 'images')
BUILDDIR = os.path.join(BASEDIR, 'build')

YAML_PATTERN = re.compile(r'^(.*)\.ya?ml$')


def load_resources(data):
    mtime = 0
    if isinstance(data, dict):
        for key, val in data.items():
            if isinstance(val, dict) and '_resource' in val:
                resource_path = os.path.join(RESOURCEDIR, val['_resource'])
                mtime = max(os.path.getmtime(resource_path), mtime)
                with open(resource_path) as fp:
                    data[key] = fp.read()
            mtime = max(load_resources(val), mtime)
    elif isinstance(data, list):
        for val in data:
            mtime = max(load_resources(val), mtime)
    return mtime


def main():
    os.makedirs(BUILDDIR, exist_ok=True)
    for folder, _, files in os.walk(PAGEDIR):
        for filename in files:
            if not YAML_PATTERN.match(filename):
                continue
            yamlpath = os.path.join(folder, filename)
            mtime = os.path.getmtime(yamlpath)
            rel_yamlpath = os.path.relpath(yamlpath, BASEDIR)
            jsonpath = os.path.join(
                BUILDDIR, YAML_PATTERN.sub(r'\1.json', rel_yamlpath))
            os.makedirs(os.path.dirname(jsonpath), exist_ok=True)
            with open(yamlpath) as yamlfp, open(jsonpath, 'w') as jsonfp:
                data = yaml.load(yamlfp, Loader=Loader)
                mtime = max(load_resources(data), mtime)
                data['lastModified'] = (
                    datetime.utcfromtimestamp(mtime).isoformat() + 'Z'
                )
                json.dump(data, jsonfp)
                print('create: {}'.format(jsonpath))
    copy_tree(IMAGEDIR, os.path.join(BUILDDIR, 'images'))
    copy_tree(IMAGEDIR, os.path.join(BUILDDIR, 'downloads'))


if __name__ == '__main__':
    main()
