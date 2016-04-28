# -*- coding: utf-8 -*-
import functools


class Singleton(object):
    def __init__(self):
        self.instances = {}

    def __call__(self, cls):
        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            cls_name = cls.__name__
            if not self.instances.get(cls_name):
                self.instances[cls_name] = cls(*args, **kwargs)
            return self.instances[cls_name]
        return wrapper

singleton = Singleton()