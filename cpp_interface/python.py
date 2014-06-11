import ctypes as ct

lib = ct.cdll.LoadLibrary("class.so")

timesTwo_int = lib._Z8timestwoi
print timesTwo_int(5)

timesTwo_double = lib._Z8timestwod
timesTwo_double.restype = ct.c_double
print "direct %f" % timesTwo_double(ct.c_double(5.0))

timesTwo_float = lib._Z8timestwof
timesTwo_float.restype = ct.c_float
print timesTwo_float(ct.c_float(5.0))

timesTwo_ns = lib._ZN7my_func8timestwoEd
timesTwo_ns.restype = ct.c_double
print "namespace %f" % timesTwo_ns(ct.c_double(5.0))

fortytwo = lib._Z8return42v
fortytwo.restype = ct.c_char_p
print fortytwo()

