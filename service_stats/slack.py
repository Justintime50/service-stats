import os

from dotenv import load_dotenv

import slack

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL')


class Slack():
    @staticmethod
    def message(message):
        """Send the output of ServiceStats to Slack
        """
        load_dotenv()
        slack_client = slack.WebClient(SLACK_BOT_TOKEN)
        try:
            slack_client.chat_postMessage(
                channel=SLACK_CHANNEL,
                text=message
            )
            success = 'Slack message sent!'
            return success
        except slack.errors.SlackApiError:
            raise Exception('Could not send the ServiceStats Slack message.')
