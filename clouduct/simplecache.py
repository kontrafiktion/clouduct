#!/usr/bin/env python

import base64
import calendar
from functools import wraps
import os
import pickle
import time


def diskcache(directory):
    """A very simple cache decorator that creates a file for each (!) method invocation with
    the same arguments. So if you have a method that is invoked many times with different arguments
    you will get many files!

    This cache is intended to be used for very slow API calls, which 'clouduct' needs to
    invoke to do command line completion. If the result wouldn't be cached then the completion
    function would be to slow to be useful

    Usage:
        cache = diskcache("<directoryname>")

        @cache(100)
        def foo(name):
           ...

        The result of this method will be cahed for 100 seconds before the function foo is really
        called again
    """
    altchars = '_-'.encode()
    cache_dir = os.path.join(os.path.expanduser("~"), directory, "cache")
    try:
        os.makedirs(cache_dir)
    except FileExistsError:
        pass

    def cache(ttl):

        def cache_decorator(func):

            @wraps(func)
            def func_wrapper(*args, **kwargs):
                key = base64.b64encode((args.__str__() + kwargs.__str__()).encode(), altchars=altchars).decode()
                cache_file = os.path.join(cache_dir, func.__qualname__ + '.' + key)
                print(cache_file)
                use_cached_value = False
                try:
                    cache_time = os.path.getmtime(cache_file)
                    now = calendar.timegm(time.gmtime())
                    if now - cache_time < ttl:
                        use_cached_value = True
                except FileNotFoundError:
                    pass
                if use_cached_value:
                    result = pickle.load(open(cache_file, "rb"))
                else:
                    result = func(*args, **kwargs)
                    pickle.dump(result, open(cache_file, "wb"))
                return result
            return func_wrapper
        return cache_decorator
    return cache
