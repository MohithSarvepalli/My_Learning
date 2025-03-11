import os
import sys

print("Current Workig Directory:", os.getcwd())

print("Home Directory:",os.environ.get('HOME'))

print("Script arguments:", sys.argv)