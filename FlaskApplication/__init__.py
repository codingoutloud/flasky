import os
import logging
from datetime import *
from flask import Flask
from flask import render_template

app = Flask(__name__)
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

@app.route('/')
def home():
    simple_counter = simple_counter + 1
    logging.debug('hello #%d from the LOGGER', simple_counter)
	#logging.debug('home page visit at %s UTC [currently running on COMPUTERNAME = %s]' %
	#    (datetime.utcnow(), os.getenv('COMPUTERNAME', '<i>unknown</i>')))
    text = { 'content': 'Welcome to this rather fine flask application! [%d]' % simple_counter } 
    return render_template('home.html',
        title = 'Home of The Flasky',
        text = text)

app.debug = True
if __name__ == "__main__":
    app.run()


