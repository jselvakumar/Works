import json

filename = 'C:\\Users\\selvaj\\Desktop\\output.txt'

output = {}
with open(filename) as fh:
    for line in fh:
        output, description = line.strip().split(' ', 1)
        output[output] = description.strip()

print(json.dumps(output, indent=2, sort_keys=True))