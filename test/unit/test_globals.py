from service.stats.globals import Global


def test_get_size():
    result = Global.get_size(1253656)
    assert result == '1.20MB'
