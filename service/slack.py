import os
import slack
from dotenv import load_dotenv


class Slack():
    @classmethod
    def message(cls, message):
        """Send the output of Service to Slack
        """
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
            raise Exception('Could not send the Service Slack message.')
