import base64

# The flag is encoded in base64 to hide it
encoded_flag = "bmM0e3M0Y2Nlc3NmMGxseV9kMHdubDA0ZGVkX0ZyMG1fZzF0aHVifQ=="

# Decode the flag at runtime
flag = base64.b64decode(encoded_flag).decode('utf-8')

# Display the flag
print(flag)
