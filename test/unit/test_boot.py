from service.stats.boot_time import Boot


def test_boot_time_serve():
    result = Boot.serve()
    assert 'Boot Time' in result
