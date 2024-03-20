import os

curworkingdir = os.getcwd()
print('Current directory is:', curworkingdir)

curdir = os.path.basename(curworkingdir)
print('The current folder is:', curdir)
