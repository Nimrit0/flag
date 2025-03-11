import base64


encoded_flag = "bmM0e3M0Y2Nlc3NmMGxseV9kMHdubDA0ZGVkX0ZyMG1fZzF0aHVifQ=="

flag = base64.b64decode(encoded_flag).decode('utf-8')


print(flag)
