import json
import re
import os

# Directory containing your JSON files
json_directory = 'jsons'

# Define regular expressions for emails and websites based on your criteria
email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
website_regex = r'(https?://[^\s]+(\.ca|\.com|\.org|\.co|\.net))|(www\.[^\s]+(\.ca|\.com|\.org|\.co|\.net))'

# Function to recursively search for emails and websites in JSON data
def find_emails_websites(data):
    emails = set()
    websites = set()

    if isinstance(data, dict):
        for value in data.values():
            found_emails, found_websites = find_emails_websites(value)
            emails.update(found_emails)
            websites.update(found_websites)
    elif isinstance(data, list):
        for item in data:
            found_emails, found_websites = find_emails_websites(item)
            emails.update(found_emails)
            websites.update(found_websites)
    elif isinstance(data, str):
        emails.update(re.findall(email_regex, data))
        websites.update(re.findall(website_regex, data))

    return emails, websites

# Initialize sets to store unique emails and websites across all files
all_unique_emails = set()
all_unique_websites = set()

# Process each JSON file in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        with open(os.path.join(json_directory, filename), 'r') as file:
            json_data = json.load(file)
        
        # Extract unique emails and websites from the current file
        unique_emails, unique_websites = find_emails_websites(json_data)
        
        # Update the global sets with unique emails and websites
        all_unique_emails.update(unique_emails)
        all_unique_websites.update(unique_websites)

# Export the unique emails and websites to txt files
with open('all_unique_emails.txt', 'w') as email_file:
    for email in all_unique_emails:
        email_file.write(f"{email}\n")

with open('all_unique_websites.txt', 'w') as website_file:
    for website in all_unique_websites:
        website_file.write(f"{website}\n")

print("Emails and websites have been exported to all_unique_emails.txt and all_unique_websites.txt")
