#import backend.db_connection
#import Patients.src.backend.db_connection
#import Patients.src.backend.db_connection as m
import logging, argparse

from Patients.src.backend import db_connection

if __name__ == '__main__':
    #backend.db_connection.connection()
    #Patients.src.backend.db_connection.connection()
    #m.connection()

    # Argparse configuration
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group("Required named argument")
    requiredNamed.add_argument('-e', '--email_id', dest='email_id',
                               help="please enter the email address",
                               required=True, nargs='+')
    args = parser.parse_args()
    email_address = args.email_id

    # logging Configuration
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(lineno)d %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler(
        filename=r'C:\Users\kaldh\PycharmProjects\Hospitalapplications\Patients\log\app.log')
    fileHandler.setFormatter(formatter)

    logger.setLevel(level=logging.DEBUG)
    logger.addHandler((fileHandler))
    logger.debug('Starting...')
    logger.debug("Call to connection method...")

    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.CRITICAL)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    db_connection.connection()
    #print("a")

    logger.critical("General Error")
