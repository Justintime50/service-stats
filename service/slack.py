"""Import modules"""
# pylint: disable=R0903
import os
import sys
import slack
from dotenv import load_dotenv


class Slack():
    """Send message methods"""
    @classmethod
    def message(cls, message):
        """Send the output of Service to Slack"""
        load_dotenv()
        slack_client = slack.WebClient(os.getenv('SLACK_BOT_TOKEN'))
        try:
            slack_client.chat_postMessage(
                channel=os.getenv('SLACK_CHANNEL'),
                text=message
            )
            success = 'Slack message sent!'
            return success
        except slack.errors.SlackApiError:
            final_output = 'Error: could not send the Service Slack message.'
            sys.exit(final_output)
