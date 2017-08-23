import array
import logging
import random

logging.basicConfig(format='%(message)s', level=logging.INFO)


def brute_force(searched_distances, seed):
    """Brute force seed seach for ascii distances."""
    length = len(searched_distances)
    while True:
        seed = seed + 1L
        random.seed(seed)
        random_ints = map(lambda _: random.randint(0, 27), xrange(length))
        random_distances = map(lambda c: random_ints[0] - c, random_ints)
        if searched_distances == random_distances:
            logging.info('seed: {}'.format(seed))
            logging.debug('searched_distances: {}'.format(searched_distances))
            logging.debug('random_distances: {}'.format(random_distances))
            return seed
        elif seed % 100000 == 0:
            logging.debug('seed: {}'.format(seed))


def brute_force_search(str, seed):
    """Search the seed for composing the pseudo-random string."""
    ascii_list = array.array('B', str).tolist()
    ascii_distances = map(lambda c: ascii_list[0] - c, ascii_list)
    brute_force(searched_distances=ascii_distances, seed=seed)


def string_from_random_seed(seed, initial_char, length):
    """Print a string from a random seed."""
    random.seed(seed)
    random_distances = map(lambda _: random.randint(0, 27), xrange(length))
    offset = ord(initial_char) - random_distances[0]
    random_ascii_list = map(lambda i: i + offset, random_distances)
    return array.array('B', random_ascii_list).tostring()


brute_force_search("arbor", seed=507500L)
brute_force_search("net", seed=3800L)
brute_force_search("works", seed=185200L)

# Looked so far for `networks`: [-900000000L, 2457100000L]
# brute_force_search("networks", seed=759300000L)

# Original idea from:
# - https://stackoverflow.com/q/15182496/81444
# - https://stackoverflow.com/q/2145510/81444
