import re
import requests

def analyze_account(account_url):
    username = extract_username_from_url(account_url)
    if not username:
        return "Invalid Instagram URL"
    
    # Simulate fetching data from Instagram (mocked for this example)
    account_data = fetch_account_data(username)
    
    # Check if account is recently created
    if is_recently_created(account_data['creation_date']):
        return "Fake Account Detected: Recently created account"
    
    # Analyze followers and following count
    if account_data['followers_count'] < 50 and account_data['following_count'] > 1000:
        return "Fake Account Detected: Suspicious follower/following ratio"

    # Check profile picture using Google Images (mocked logic)
    if is_fake_profile_picture(account_data['profile_picture_url']):
        return "Fake Account Detected: Profile picture suspected to be fake"

    return "Account seems legitimate"

def extract_username_from_url(url):
    # Extract the username from the Instagram URL using regex
    match = re.search(r'instagram\.com/([a-zA-Z0-9_.]+)', url)
    return match.group(1) if match else None

def fetch_account_data(username):
    # Mock function to simulate fetching account data
    return {
        'creation_date': '2024-12-01',  # Example creation date
        'followers_count': 45,
        'following_count': 1050,
        'profile_picture_url': 'https://example.com/profile.jpg'
    }

def is_recently_created(creation_date):
    # Logic to check if the account is recently created
    from datetime import datetime, timedelta
    creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
    three_months_ago = datetime.now() - timedelta(days=90)
    return creation_date > three_months_ago

def is_fake_profile_picture(profile_picture_url):
    # Simulated logic to check if a profile picture is fake
    response = requests.get(f"https://fake-image-checker-api.com?image_url={profile_picture_url}")
    return response.json().get('is_fake', False)
