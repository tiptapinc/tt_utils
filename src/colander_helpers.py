#!/usr/bin/env python
# encoding: utf-8
"""
Copyright (c) 2014 tiptap. All rights reserved.

schema for tweets passed in the body of a call to
the indirect service

"""

import colander
import datetime
import uuid


# the following helpers ensure that the schema nodes that use
# them for "missing" attributes get cloned during deserialization

@colander.deferred
def deferred_uuid_me(node, kw):
    return str(uuid.uuid4())


@colander.deferred
def deferred_now(node, kw):
    return datetime.datetime.utcnow()


@colander.deferred
def deferred_never(node, kw):
    return datetime.datetime.fromordinal(1)


@colander.deferred
def deferred_list(node, kw):
    return []


@colander.deferred
def deferred_set(node, kw):
    return set()
