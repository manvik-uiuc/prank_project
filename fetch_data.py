from bs4 import BeautifulSoup
import requests
import csv
waybackmachine_id = ['20240421034935', '20240422150355']

for _id in waybackmachine_id:
    try:
        # Read existing unique channel names from the text file
        existing_channel_names = []
        try:
            with open('unique_channel_names.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    existing_channel_names.append(line.strip())
        except FileNotFoundError:
            pass

        archive_response = requests.get(f"https://web.archive.org/web/{_id}/https://socialblade.com/instagram/top/100/followers")
        soup = BeautifulSoup(archive_response.content, 'html.parser')
        # Find all <a> tags with href containing either "user" or "channel"
        filtered_links = soup.find_all('a', href=lambda value: value and ('/user/' in value))

        unique_channel_names = existing_channel_names.copy()

        # Extract and store unique channel names
        for link in filtered_links:
            channel_name = link.text.strip()
            if channel_name:  # Skip empty channel names
                if channel_name not in unique_channel_names:
                    unique_channel_names.append(channel_name)

        # Save unique channel names to a text file
        with open('unique_channel_names.txt', 'w', encoding='utf-8') as file:
            for channel_name in unique_channel_names:
                file.write(channel_name + '\n')

        print(_id)
    
    except:
        continue
