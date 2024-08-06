import requests
import logging
from datetime import datetime

logging.basicConfig(filename='app_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

application_url = 'https://www.amazon.in/'

up_status_code = [200, 301, 302]

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code in up_status_code:
            logging.info(f'Application is UP. Status code: {response.status_code}')
            print('Application is UP.')
        else:
            logging.warning(f'Application is DOWN. Status code: {response.status_code}')
            print('Application is DOWN.')
    except requests.exceptions.RequestException as e:
        logging.error(f'Application is DOWN. Error: {str(e)}')
        print('Application is DOWN.')

def main():
    logging.info('Starting application health check...')
    check_application_health(application_url)
    logging.info('Application health check completed.')

if __name__ == '__main__':
    main()
