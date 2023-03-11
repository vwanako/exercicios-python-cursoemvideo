# write a program that reads a value in meters, and shows the result converted in centimeters and millimeters

meter = float(input("Hello user, type a number in meters, and I will convert it to other unities. "))
km = meter / 1_000
hm = meter / 100
dam = meter / 10
dm = meter * 10
cm = meter * 100
mm = meter * 1_000

print("{}m is\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm.".format(meter, km, hm, dam, dm, cm, mm))
