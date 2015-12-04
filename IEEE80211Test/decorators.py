from decorator import decorator



def _trace(f, *args, **kw):
    print "calling %s with args %s, %s" % (f.__name__, args, kw)
    return f(*args, **kw)

def trace(f):
    return decorator(_trace, f)