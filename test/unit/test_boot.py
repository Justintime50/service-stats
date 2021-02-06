from service_stats import Boot


def test_boot_time_serve():
    result = Boot.serve_data()
    assert 'Boot Time' in result
