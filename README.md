# Test_GitHub_webhooks-
# GitHub Commit Notifier for Slack
This Python application utilizes GitHub webhooks to monitor changes on the main branch of a specified repository and sends notifications to a Slack channel with details about each commit.

# Setup Instructions
1. Clone the Repository
Clone this repository to your local machine:
git clone https://github.com/osnatash/Test_GitHub_webhooks-.git

2. Install Dependencies
Install the required Python packages using pip:
pip install -r requirements.txt

3. Set Up GitHub Webhook
Go to your GitHub repository settings.
Navigate to "Webhooks" or "Hooks" settings.
Click on "Add webhook" or "Create webhook".
Set the payload URL to your Flask application URL followed by /webhook (e.g., http://yourdomain.com/webhook).
(you can use ngrok URL)
Choose "application/json" as the content type.
Select "Just the push event" or configure as desired.
Click "Add webhook" to save.

5. Set Up Slack Integration
Go to the Slack API website.
Click on "Your Apps" in the top-right corner and then click "Create New App".
Enter a name for your app and select the Slack workspace where you want to install it.
Once the app is created, you'll be taken to the app's settings page.
Navigate to "Incoming Webhooks" and activate it.
Choose the channel where you want to send notifications and click "Allow".
Copy the Webhook URL provided.

6. Configure Environment Variables
SLACK_WEBHOOK_URL=https://your-slack-webhook-url
Replace https://your-slack-webhook-url with the actual Webhook URL you copied in step 7 of the Slack setup.

Running the Application
Run the Flask application using the following command:
python main.py

my ngrok URL = https://888e-2a06-c701-9666-3c00-8c51-bfd-9261-69c7.ngrok-free.app/webhook
