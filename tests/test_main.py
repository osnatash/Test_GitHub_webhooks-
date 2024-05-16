import os
import unittest
from main import app, send_slack_notification, SLACK_WEBHOOK_URL
class TestMain(unittest.TestCase):
    # Test environment setup
    def test_environment_setup(self):
        # Check if the environment variable SLACK_WEBHOOK_URL is set
        self.assertIsNotNone(SLACK_WEBHOOK_URL, "SLACK_WEBHOOK_URL is not set")
    # Test webhook endpoint
    def test_webhook_endpoint(self):
        # Define a mock payload
        mock_payload = {
            "ref": "refs/heads/main",
            "commits": [
                {"id": "commit_id_1", "message": "Commit message 1"},
                {"id": "commit_id_2", "message": "Commit message 2"}
            ]
        }

        # Simulate sending the mock payload to the webhook endpoint
        with app.test_client() as client:
            response = client.post('/webhook', json=mock_payload)

            # Assert that the response status code is 200 OK
            self.assertEqual(response.status_code, 200)

            # Assert that the response message matches the expected message
            self.assertEqual(response.data.decode(), 'Webhook received for main branch')


    # Test Slack integration
    def test_slack_integration(self):
        # Define a test message
        test_message = "This is a test message for Slack integration"

        # Send the test message to Slack
        try:
            send_slack_notification(test_message)
            # If no exception is raised, the notification is sent successfully
            slack_notification_sent = True
        except Exception as e:
            print(f"Failed to send Slack notification: {e}")
            slack_notification_sent = False

        # Assert that the Slack notification was sent successfully
        self.assertTrue(slack_notification_sent)

if __name__ == '__main__':
    unittest.main()
