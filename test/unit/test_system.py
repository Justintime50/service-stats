from service_stats import System


def test_system_serve():
    result = System.serve_data()
    assert 'System Information' in result
