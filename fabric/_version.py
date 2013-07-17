__version_info__ = (2, 0, 0)


def _to_str(num_parts=None):
    global __version_info__ # ugh
    return '.'.join(map(str, __version_info__[:num_parts]))

__version__ = _to_str()
__branch__ = _to_str(2)
