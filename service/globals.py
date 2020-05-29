"""No modules to import"""
# pylint: disable=R0903,R1710


class Global():
    """Global variables and methods"""
    @classmethod
    def get_size(cls, bytes_int, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.8MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes_int < factor:
                return f'{bytes_int:.2f}{unit}{suffix}'
            bytes_int /= factor
