
# very big log: http://www.almhuette-raith.at/apache-log/access.log
#  берём из него, например, 20 записей.
#  Как с помощью стандартных консольных средств найти десять IP-адресов,
#  от которых было больше всего запросов? Написать скрипт такого анализа

import urllib.request
from collections import defaultdict


LOG_FILE = 'http://www.almhuette-raith.at/apache-log/access.log'
IP_SEPARATOR = ' - - '
LOG_FRAME_LENGTH_WITH_IP = 50
RECORDS_THRESHOLD = 1000
TOP_COUNT = 10


ip_count_map = defaultdict(lambda: 0)

with urllib.request.urlopen(LOG_FILE) as log_file:
    for _ in range(RECORDS_THRESHOLD):
        record = log_file.readline().strip()
        try:
            ip, _ = record[:LOG_FRAME_LENGTH_WITH_IP].decode().split(IP_SEPARATOR, 1)
        except ValueError as e:
            err_msg = '{}: {}, record={}'.format(
                    type(e).__name__, e, record)
            print(err_msg)
        else:
            ip_count_map[ip] += 1

    most_requests_top_ips = sorted(ip_count_map,
                                   key=ip_count_map.__getitem__,
                                   reverse=True
                                   )[:TOP_COUNT]

    print(*most_requests_top_ips, sep='\n')
