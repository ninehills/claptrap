# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from claptrap import Connection, Queue, Worker

if __name__ == '__main__':
    # Tell claptrap what Redis connection to use
    with Connection():
        q = Queue()
        Worker(q).work()
