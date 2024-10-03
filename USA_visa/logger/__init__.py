import logging
import os
from datetime import datetime

project_root = os.getcwd()

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = "logs"
logs_path = os.path.join(project_root, log_dir, LOG_FILE)

if not os.path.exists(os.path.join(project_root, log_dir)):
    os.makedirs(os.path.join(project_root, log_dir), exist_ok=True)
    print(f"Created log directory at: {os.path.join(project_root, log_dir)}")

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
