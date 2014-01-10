from datetime import *
import os
import logging




# assumes import os and import logging
# pass in root folder where logging is allowed (correct permissions are assumed)
# returns log_file_path
def init_logging(plat_root_log_dir):
    log_level = logging.DEBUG
    log_file_dir = os.path.join(plat_root_log_dir, 'flaskylogs')
    log_file_path = os.path.join(log_file_dir + 'flasky.log')

    logging.basicConfig(format='%(levelname)s [%(asctime)s]: %(message)s', filename=log_file_path, level=log_level)

    if not os.path.exists(log_file_dir):
        os.makedirs(log_file_dir)
        logging.info('Created %s logging directory', log_file_dir)
    logging.info('Flasky is logging to %s at level %s', log_file_path, log_level)
    return log_file_path

plat_root_log_dir = 'd:\\home\\logfiles'
log_file_path = init_logging(plat_root_log_dir)
logging.debug('home page visit at %s UTC [currently running on COMPUTERNAME = %s]' %
    (datetime.utcnow(), os.getenv('COMPUTERNAME', '<i>unknown</i>')))



#logging.basicConfig(format='%(levelname)s [%(asctime)s]: %(message)s', filename='flasky.log', level=logging.DEBUG)


#log_file_dir = 'd:\\home\\logfiles\\foo'
#if not os.path.exists(log_file_dir):
#    os.makedirs(log_file_dir)

#log_file = log_file_dir + "\\flasky.log"
#print(log_file_dir)
#print(log_file)

#logging.basicConfig(filename=log_file,level=logging.DEBUG)
logging.info('LOG FILE ENABLED as file %s' % log_file_path)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

logging.info('home page visit at %s UTC [currently running on COMPUTERNAME = %s]' % 
        (datetime.utcnow(), os.getenv('COMPUTERNAME', '<i>unknown</i>')))





with open (log_file_path, "r") as log_file:
    log_file_contents=log_file.read()

print("Log file '%s' contents:" % log_file_path)
print(log_file_contents)



