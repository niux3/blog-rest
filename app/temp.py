import re

pattern = re.compile(r'^([a-z0-9]+[-._]?[a-z0-9]+)+@([a-z0-9]+[-._]?[a-z0-9]+)+\.[a-z]{2,}$')
print(pattern.search('bla@ss.ss'))
