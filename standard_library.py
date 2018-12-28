import sys
i=0
for arg in sys.argv:
	i+=1
	print(arg)
print(i)

print(sys.version_info)

import os,platform,logging
if platform.platform().startswith('Windows'):
	logging_file=os.path.join(os.getenv('HOMEDRIVE'),os.getenv('HOMEPATH'),'test.log')
else:
	logging_file=os.path.join(os.getenv('HOME'),'test.log')
print('Logging to ', logging_file)
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s:%(levelname)s:%(message)s',
	filename=logging_file,
	filemode='w'
)
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
