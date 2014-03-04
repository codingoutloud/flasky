from datetime import *
import os
import logging


simple_counter = 0

# assumes import os and import logging
# pass in root folder where logging is allowed (correct permissions are assumed)
# returns log_file_path
def init_logging(plat_root_log_dir):
    log_level = logging.DEBUG
    log_file_dir = os.path.join(plat_root_log_dir, 'flaskylogs')
    log_file_path = os.path.join(log_file_dir, 'flasky.log')

    log_file_dir_already_exists = os.path.exists(log_file_dir)
    if not log_file_dir_already_exists:
        os.makedirs(log_file_dir)

    logging.basicConfig(format='%(levelname)s [%(asctime)s]: %(message)s', filename=log_file_path, level=log_level)

    if not log_file_dir_already_exists:
        logging.info('Created %s logging directory', log_file_dir)
    logging.info('Flasky is logging to %s at level %s', log_file_path, log_level)
    return log_file_path

plat_root_log_dir = 'd:\\home\\logfiles'
log_file_path = init_logging(plat_root_log_dir)

simple_counter = simple_counter + 1
logging.debug('hello #%d from the LOGGER', simple_counter)
text = { 'content': 'Welcome to this rather fine flask application! [%d]' % simple_counter } 
print(simple_counter)
print(text)




with open (log_file_path, "r") as log_file:
    log_file_contents=log_file.read()

print("Log file '%s' contents:" % log_file_path)
print(log_file_contents)



