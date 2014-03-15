#!/usr/bin/env python
# encoding: utf-8
"""
Copyright (c) 2014 tiptap. All rights reserved.

"""
import beanstalkt

import logging
log = logging.getLogger(__name__)


class TTWorkQueue(beanstalkt.Client):
    """
    Adds initialize and get_status methods to the beanstalkt client
    """
    def initialize(self, tubeName, status_callback=None, reconnect=None):
        self._init_status(status_callback)
        self.connect(callback=self._connect_callback)
        self.use(tubeName, callback=self._use_callback)
        self.watch(tubeName, callback=self._watch_callback)
        self.ignore("default")
        if reconnect:
            self.set_reconnect_callback(reconnect)

    def get_status(self):
        return self.useSet and self.watchSet and self.connected

    def _use_callback(self, resp):
        if isinstance(resp, Exception):
            log.warning("queue error: %s" % str(resp))
        else:
            self.useSet = True

        self._update_status()

    def _watch_callback(self, resp):
        if isinstance(resp, Exception):
            log.warning("queue error: %s" % str(resp))
        else:
            self.watchSet = True

        self._update_status()

    def _connect_callback(self):
        self.connected = True
        self._update_status()

    def _init_status(self, status_callback):
        self.status_callback = status_callback
        self.useSet = False
        self.watchSet = False
        self.connected = False
        self.ready = False

    def _update_status(self):
        ready = self.get_status()
        if self.ready != ready:
            self.ready = ready
            if self.status_callback:
                self.status_callback(self.ready)
