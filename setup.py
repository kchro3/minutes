import os
import pip

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

for r in requirements:
    pip.main(['install', r])
