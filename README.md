# Test_GitHub_webhooks-
# GitHub Commit Notifier for Slack
This Python application utilizes GitHub webhooks to monitor changes on the main branch of a specified repository and sends notifications to a Slack channel with details about each commit.
Support linux & windows
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
# for linux version:
use: https://test-github-webhooks-2.onrender.com
(Render is a cloud platform for hosting and managing web applications. It provides a production-ready environment for deploying and scaling web applications securely, but not supports Windows)

# for windows version:
create your URL ngrok
my ngrok URL for example = https://888e-2a06-c701-9666-3c00-8c51-bfd-9261-69c7.ngrok-free.app/webhook
(Ngrok is a tool used for quickly exposing local servers to the internet. It's ideal for testing webhooks and also supports windows)

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
take the Webhook URL provided previous, and put it this way:
# for linux version:
Go to your Render project dashboard.
Navigate to the "Environment" tab.
Add a new environment variable with the name SLACK_WEBHOOK_URL and the corresponding value being your Slack webhook URL.
Click "Save" to apply the changes.
# for windows version:
Open a terminal or command prompt.
Set the environment variable using the following command:
set SLACK_WEBHOOK_URL=your Slack webhook URL

7. Running the Application
# for linux version:
Run the Flask application using the following command:
gunicorn -b 0.0.0.0:$PORT main:app

# for windows version:
Run the Flask application using the following command:
python main.py

