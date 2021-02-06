from service_stats import Network


def test_network_serve():
    result = Network.serve_data()
    assert 'Network Information' in result
