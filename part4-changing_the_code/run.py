import sys

if sys.version_info[0] < 3:
  sys.stdout.write("You need Python 3.0 or higher to run this.\nTry: python3 run.py\n")
  sys.exit(1)

from printer import main

if __name__ == '__main__':
  main()