from service.stats.network import Network


def test_network_serve():
    result = Network.serve()
    assert 'Network Information' in result
