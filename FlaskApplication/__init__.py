import os
import logging
from datetime import *
from flask import Flask
from flask import render_template

app = Flask(__name__)
simple_counter = 0

# change the file 5:44

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
    global simple_counter
    simple_counter += 1
    logging.debug('hello #%d from the LOGGER running on COMPUTERNAME = %s', 
        simple_counter, os.getenv('COMPUTERNAME', 'unknown'))

    # http://stackoverflow.com/questions/19274226/how-to-track-the-current-user-in-flask-login
    # http://flask-login.readthedocs.io/en/latest/#configuring-your-application
    #if current_user.is_authenticated():
    #    text = { 'content': 'hello %s' % current_user.get_id() } 
    #else:
    text = { 'content': 'This WICKED SPS sophisticated flask application has been visited [%d] times since last deployment. One might have been by Subrata.' % simple_counter } 

    return render_template('home.html',
        title = 'Home of Flasky',
        text = text)

app.debug = True
if __name__ == "__main__":
    app.run()


