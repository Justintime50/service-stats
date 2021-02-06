from service_stats import Memory


def test_memory_serve():
    result = Memory.serve_data()
    assert 'Memory Information' in result
