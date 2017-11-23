# -*- coding: utf-8 -*-
"""
    salt.serializers.toml
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Implements TOML serializer.

    It's just a wrapper around pytoml module.
"""

from __future__ import absolute_import

# Import Salt libs
try:
    import pytoml as toml
except ImportError:
    available = False

# Import Salt libs
from salt.serializers import DeserializationError, SerializationError

# Import 3rd-party libs
from salt.ext import six

__all__ = ['deserialize', 'serialize', 'available']

available = True


def deserialize(stream_or_string, **options):
    """
    Deserialize any string or stream like object into a Python data structure.

    :param stream_or_string: stream or string to deserialize.
    :param options: options given to lower pytoml module.
    """

    try:
        if not isinstance(stream_or_string, (bytes, six.string_types)):
            return toml.load(stream_or_string, **options)

        if isinstance(stream_or_string, bytes):
            stream_or_string = stream_or_string.decode('utf-8')

        return toml.loads(stream_or_string)
    except Exception as error:
        raise DeserializationError(error)


def serialize(obj, **options):
    """
    Serialize Python data to TOML.

    :param obj: the data structure to serialize.
    :param options: options given to lower pytoml module.
    """

    try:
        if 'file_out' in options:
            return toml.dump(obj, options['file_out'], **options)
        else:
            return toml.dumps(obj, **options)
    except Exception as error:
        raise SerializationError(error)
