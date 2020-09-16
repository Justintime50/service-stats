from service.stats.system import System


def test_system_serve():
    result = System.serve()
    assert 'System Information' in result
