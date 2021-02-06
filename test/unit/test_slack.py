import mock
import pytest
from service_stats import Slack


def test_slack_error():
    with pytest.raises(Exception):
        Slack.message('dummy message')


@mock.patch('service_stats.slack.SLACK_BOT_TOKEN', '123')
@mock.patch('service_stats.slack.SLACK_CHANNEL', 'mock-channel')
@mock.patch('slack.WebClient.chat_postMessage')
def test_slack_success(mock_slack):
    message = 'dummy message'
    Slack.message(message)
    mock_slack.assert_called_once_with(channel='mock-channel', text=message)
