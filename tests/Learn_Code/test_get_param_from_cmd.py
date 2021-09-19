import sys

print("-------!!@#-------")
print(len(sys.argv))
print(sys.argv)
#pytest test_get_param_from_cmd.py stg android
#4
# ['/Library/Frameworks/Python.framework/Versions/3.9/bin/pytest', 'test_get_param_from_cmd.py', 'stg', 'android']

for x in sys.argv:
    print(x)
