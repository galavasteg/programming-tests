"""
Sort global string inplace with minimal memory consumption.
(original task: long-long string -> sorted long-long string, no disk, no ctypes)

"""
import urllib.request


ALPHABET = 'qwertyuiopasdfghjklzxcvbnm...'
LOG_FILE = 'http://www.almhuette-raith.at/apache-log/access.log'
RECORDS_MAX_NUM = 5000


long_long_string = ''
with urllib.request.urlopen(LOG_FILE) as log_file:
    for _ in range(RECORDS_MAX_NUM):
        long_long_string += log_file.readline().decode()


# ------------- CODE FROM HERE -------------

def get_alpha_count(alpha) -> int:
    alpha_filter = filter(None, map(lambda char: char == alpha,
                                    long_long_string))
    all_alphas = tuple(alpha_filter)  # most CPU-bound code
    return len(all_alphas)


alpha_count_map = {}
for alpha in ALPHABET:
    alpha_count_map[alpha] = get_alpha_count(alpha)

# free space from old string
del long_long_string

# make the same link for new object
long_long_string = ''.join((alpha * count for alpha, count
                            in alpha_count_map.items()))

print(long_long_string[:20], '...')
