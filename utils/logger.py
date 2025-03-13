import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name, log_file, level=logging.INFO):
    """Configura um logger personalizado para registrar logs corretamente"""
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_file, encoding='utf-8')  # 🔹 Define UTF-8 no log
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Criando loggers para cada operação
db_logger = setup_logger("db_logger", os.path.join(LOG_DIR, "db.log"))
delete_logger = setup_logger("delete_logger", os.path.join(LOG_DIR, "delete_process.log"))
insert_logger = setup_logger("insert_logger", os.path.join(LOG_DIR, "insert_process.log"))
test_logger = setup_logger("test_logger", os.path.join(LOG_DIR, "test_execution.log"))
