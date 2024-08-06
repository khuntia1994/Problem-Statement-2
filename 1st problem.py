import psutil
import logging
from datetime import datetime

logging.basicConfig(filename='system_moniter.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

cpu_usage_threshold = 80
memory_usage_threshold = 80
disk_usage_threshold = 80 
running_process_threshold = 200  

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > cpu_usage_threshold :
        logging.warning(f'High CPU usage detected: {cpu_usage}%')

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage >memory_usage_threshold:
        logging.warning(f'High memory usage detected: {memory_usage}%')

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > disk_usage_threshold:
        logging.warning(f'High disk usage detected: {disk_usage}%')

def check_running_processes():
    processes = list(psutil.process_iter())
    num_processes = len(processes)
    if num_processes > running_process_threshold:
        logging.warning(f'High number of running processes detected: {num_processes}')

def monitor_system():
    logging.info('Starting system health monitoring...')
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    logging.info('System health monitoring completed.')

if __name__ == '__main__':
    monitor_system()
