#!/usr/bin/env python
# encoding: utf-8
"""
Copyright (c) 2014 tiptap. All rights reserved.

schema for tweets passed in the body of a call to
the indirect service

"""

import json


def colander_converter(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()

    if isinstance(obj, set):
        return list(obj)


def colander_dumps(obj, **kwargs):
    return json.dumps(obj, default=colander_converter, **kwargs)
