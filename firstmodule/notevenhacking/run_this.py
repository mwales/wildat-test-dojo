#!/opt/pwn.college/python

# this is the legacy way...


print("script running")

ff = open("/flag", "r")

print("flag file opened")

flag = ff.read()

print("flag read")

ff.close()

print(flag)

