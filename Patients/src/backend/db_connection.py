import logging

logger = logging.getLogger(__name__)
def connection():
    print("DB Connection")
    logger.debug("DB Connection")

if __name__ == '__main__':
    print("DB connection module")
    connection()
elif __name__ == 'Patients.src.backend.db_connection':
    print("else")
    print(__name__)