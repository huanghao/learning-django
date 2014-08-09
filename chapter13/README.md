Caching
=======

Django offers different levels of cache granularity: You can cache the
output of *specific views*, you can cache only *the pieces that are difficult
to produce*, or you can cache your *entire site*.

Backends
--------

Memcached

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': [
                '172.19.26.240:11211',
                '172.19.26.242:11212',
                '172.19.26.244:11213',
            ]
        }
    }

Database

    $ python manage.py createcachetable [cache_table_name]

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_table_name',
        }
    }

Filesystem

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/django_cache',
        }
    }

Local-memory

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake'
        }
    }

    Specify unique LOCATION for each cache.

    Note that each process will have its own private cache instance, which
    means no cross-process caching is possible. This obviously also means
    the local memory cache isn’t particularly memory-efficient, so it’s
    probably not a good choice for production environments. It’s nice for
    development.

Dummy (for development)

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

    It just implements the cache interface without doing anything.

    This is useful if you have a production site that uses heavy-duty
    caching in various places but a development/test environment where
    you don’t want to cache and don’t want to have to change your code
    to special-case the latter.

Cache arguments
---------------

TIMEOUT: in seconds, default to 5 minutes

OPTIONS

    Any options that should be passed to the cache backend.

    - MAX_ENTRIES, default to 300

    - CULL_FREQUENCY, default to 3
    The actual ratio is 1 / CULL_FREQUENCY

The per-site cache
------------------

    MIDDLEWARE_CLASSES = (
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    )

The per-view cache
------------------

    from django.views.decorators.cache import cache_page

    @cache_page(60 * 15)
    def my_view(request):
        ...

    urlpatterns = ('',
        (r'^foo/(\d{1,2})/$', my_view),
    )

    /foo/1/ and /foo/23/ will be cached separately

Template fragment caching
-------------------------

    {% load cache %}
    {% cache 500 sidebar %}
        .. sidebar ..
    {% endcache %}

Sometimes you might want to cache multiple copies of a fragment
depending on some dynamic data that appears inside the fragment.

    {% load cache %}
    {% cache 500 sidebar request.user.username %}
        .. sidebar for logged in user ..
    {% endcache %}

Fragment key

    django.core.cache.utils.make_template_fragment_key(fragment_name, vary_on=None)

    >>> from django.core.cache import cache
    >>> from django.core.cache.utils import make_template_fragment_key
    # cache key for {% cache 500 sidebar username %}
    >>> key = make_template_fragment_key('sidebar', [username])
    >>> cache.delete(key) # invalidates cached template fragment

The low-level cache API
-----------------------

Django exposes a simple, low-level cache API. You can use this API to
store objects in the cache with any level of granularity you like.

You can cache any Python object that can be pickled safely: strings,
dictionaries, lists of model objects, and so forth. (Most common Python
objects can be pickled)

Accessing the cache

    the 'default' entry in the CACHES setting
    >>> from django.core.cache import cache

    >>> from django.core.cache import get_cache
    >>> cache = get_cache('alternate')

Basic usage

    >>> cache.set('my_key', 'hello, world!', 30)
    >>> cache.get('my_key')
    'hello, world!'

    # Wait 30 seconds for 'my_key' to expire...
    >>> cache.get('my_key')
    None

    >>> cache.set_many({'a': 1, 'b': 2, 'c': 3})
    >>> cache.get_many(['a', 'b', 'c'])
    {'a': 1, 'b': 2, 'c': 3}

    >>> cache.delete('a')

    >>> cache.delete_many(['a', 'b', 'c'])

    >>> cache.clear()

    >>> cache.set('num', 1)
    >>> cache.incr('num')
    2
    >>> cache.incr('num', 10)
    12
    >>> cache.decr('num')
    11
    >>> cache.decr('num', 5)
    6

    incr()/decr() methods are not guaranteed to be atomic. On those
    backends that support atomic increment/decrement (most notably,
    the memcached backend), increment and decrement operations will
    be atomic.

    >>> cache.close()