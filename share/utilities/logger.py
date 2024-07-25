import uuid
import traceback
import logging

from utilities.redis_controller import RedisController

class Logger:
    def __init__(self):
        self.client = RedisController()
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def debug(self, *args):
        if len(args) == 1:
            message = args[0]
        elif len(args) == 3:
            file_name, function_name, message = args
            message = f"{file_name}::{function_name} - {message}"
        else:
            raise TypeError("Logger.debug() takes 1 or 3 arguments")
        self.logger.debug(message)

    def error(self, file_name, function_name, error_message):
        error_id = str(uuid.uuid4())
        error_details = {
            "file_name": file_name,
            "function_name": function_name,
            "error_message": error_message,
            "traceback": traceback.format_exc()
        }
        self.client.set_token(error_id, str(error_details), 48 * 3600)
        self.logger.error(f"{error_message} (Logged with ID: {error_id})")
        return error_id
