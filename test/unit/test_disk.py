from service.stats.disk import Disk


def test_disk_serve():
    result = Disk.serve()
    assert 'Disk Information' in result
