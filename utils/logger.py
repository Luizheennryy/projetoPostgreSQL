import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Configura um logger para registrar logs em um arquivo."""
    os.makedirs("logs", exist_ok=True)  # Garante que a pasta 'logs' existe

    handler = logging.FileHandler(log_file, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
