from service_stats import Disk


def test_disk_serve():
    result = Disk.serve_data()
    assert 'Disk Information' in result
