from service.slack import Slack
import pytest


def test_slack_error():
    with pytest.raises(Exception):
        Slack.message('dummy message')


@pytest.mark.skip('Need to write test first')
def test_slack_success():
    # TODO: Write test
    result = Slack.message('dummy message')
    assert result == ''
