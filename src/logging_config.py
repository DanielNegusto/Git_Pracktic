import logging
import os

# Создаем директорию для логов, если она не существует
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Настраиваем логирование
logging.basicConfig(
    filename=os.path.join(log_dir, "application.log"),
    filemode="w",
    encoding="utf-8",  # Перезапись файла при каждом запуске
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,  # Уровень логирования
)

logger = logging.getLogger(__name__)
