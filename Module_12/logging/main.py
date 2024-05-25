import requests as rq
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']


def check_access() -> None:
    # Открываем несколько файлов логов для записи с добавлением 'a' ('w' - перезапись), если их нет, то будут созданы
    with open('success_responses.log', 'a') as success_log, \
            open('bad_responses.log', 'a') as bad_log, \
            open('blocked_responses.log', 'a') as blocked_log:
        for site in sites:
            try:
                # Делаем запрос, с временем на подключение
                response = rq.get(site, timeout=3)

                # Проверка статуса
                if response.status_code == 200:
                    # Вывод в консоль
                    logger.info(f'{site}, response - 200')
                    # Запись в файл
                    success_log.write(f"INFO: '{site}', response - 200\n")
                else:
                    logger.warning(f'{site}, response - {response.status_code}')
                    bad_log.write(f"WARNING: '{site}', response - {response.status_code}\n")

            except (rq.exceptions.RequestException, rq.exceptions.ConnectionError) as e:
                logger.error(f'{site}, {e}')
                blocked_log.write(f"ERROR: '{site}', {e}\n")
            except Exception as e:
                logger.error(f'{site}, {e}')
                blocked_log.write(f"COMMON ERROR: '{site}', {e}\n")


if __name__ == '__main__':
    check_access()
