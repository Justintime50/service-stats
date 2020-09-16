from service.stats.memory import Memory


def test_memory_serve():
    result = Memory.serve()
    assert 'Memory Information' in result
