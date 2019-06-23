# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_io_stream')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_io_stream')
    _io_stream = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_io_stream', [dirname(__file__)])
        except ImportError:
            import _io_stream
            return _io_stream
        try:
            _mod = imp.load_module('_io_stream', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _io_stream = swig_import_helper()
    del swig_import_helper
else:
    import _io_stream
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class wFILE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, wFILE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, wFILE, name)
    __repr__ = _swig_repr

    def __init__(self, filename, isSTDOUT=0):
        this = _io_stream.new_wFILE(filename, isSTDOUT)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def isSTDOUT(self):
        return _io_stream.wFILE_isSTDOUT(self)

    def getFilename(self):
        return _io_stream.wFILE_getFilename(self)
    __swig_destroy__ = _io_stream.delete_wFILE
    __del__ = lambda self: None
wFILE_swigregister = _io_stream.wFILE_swigregister
wFILE_swigregister(wFILE)


STDOUT = wFILE('__stdout__', isSTDOUT=1)

# This file is compatible with both classic and new-style classes.


