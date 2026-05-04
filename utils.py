import logger
import validator
import file_manager
import cache_manager

def get_status():
    return {
        "logger": "ready",
        "validator": "active",
        "storage": file_manager.check_disk_space()
    }

def clear_all_caches():
    cache_manager.clear_cache()
    logger.log_info("System cache cleared.")
