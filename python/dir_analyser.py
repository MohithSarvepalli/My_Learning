import os
import sys
import datetime

Directory=sys.argv[1] if len(sys.argv)>1 else '.'

print(f"Analysing the directory: {Directory}")
for filename in os.listdir(Directory):
    filepath=os.path.join(Directory,filename)
    size=os.path.getsize(filepath)
    modified_time=datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
    print(f"{filename}| Size: {size} bytes | Modified: {modified_time}")