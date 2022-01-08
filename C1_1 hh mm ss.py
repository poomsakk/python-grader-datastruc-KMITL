import sys
print("*** Converting hh.mm.ss to seconds ***")
h, m, s = [int(x) for x in input("Enter hh mm ss : ").split()]
if h < 0:
    print("hh({}) is invalid!".format(h))
    sys.exit(0)
if m < 0 or m >= 60:
    print("mm({}) is invalid!".format(m))
    sys.exit(0)
if s < 0 or s >= 60:
    print("ss({}) is invalid!".format(s))
    sys.exit(0)
print("{:02d}:{:02d}:{:02d} = {:,} seconds".format(h, m, s, h*60*60+m*60+s))
