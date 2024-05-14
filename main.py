import requests
from flask import Flask, request

app = Flask(_name_)

# Define your Slack webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"


def send_slack_notification(message):
    try:
        payload = {"text": message}
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses
    except requests.RequestException as e:
        print(f"Failed to send Slack notification: {e}")

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Parse the JSON payload from GitHub
        payload = request.json

        # Check if the event is for the main branch
        branch = payload.get('ref')
        if not branch or not branch.startswith('refs/heads/'):
            print("Webhook ignored (Invalid branch information)")
            return 'Webhook ignored (Invalid branch information)', 200

        branch_name = branch[len('refs/heads/'):]
        if branch_name != 'main':
            print(f"Webhook ignored (Not for main branch: {branch_name})")
            return 'Webhook ignored (Not for main branch)', 200

        # Extract commit information from the payload
        commits = payload.get('commits', [])
        if not commits:
            print("No commits found in the payload")
            return 'Webhook received for main branch', 200

        # Loop through each commit and extract commit hash and message
        for commit in commits:
            commit_hash = commit.get('id')
            commit_message = commit.get('message')
            print(f"Commit Hash: {commit_hash}, Message: {commit_message} (Main branch)")

            # Construct the message to send to Slack
            slack_message = f"New commit on main branch:\nCommit Hash: {commit_hash}\nMessage: {commit_message}"

            # Send the message to Slack
            send_slack_notification(slack_message)

        return 'Webhook received for main branch', 200
    except Exception as e:
        print(f"Error processing webhook event: {e}")
        return 'Error processing webhook event', 500


if _name_ == '_main_':
    app.run(debug=True)
