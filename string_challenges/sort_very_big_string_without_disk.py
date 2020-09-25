"""
Sort global string `A` inplace with minimal memory consumption.
(orig.: long-long string -> sorted long-long string, no disk, no ctypes)

"""
long_long_string = 'abchdk…abchdk,abchdkabchdk::Llk;klj;lkjl;::Lkjlabchdk...'
alphabet = ''.join(sorted(set(long_long_string)))

# not OrderedDict: from Python 3.6 regular dict is ordered by insertion order
alpha_count_map = {}
for alpha in alphabet:
    filter_alpha = filter(None, map(lambda char: char == alpha, long_long_string))
    alpha_count_map[alpha] = len(tuple(filter_alpha))

del long_long_string

long_long_string = ''.join((alpha * count for alpha, count
                            in alpha_count_map.items()))

print(long_long_string[:20], '...')
