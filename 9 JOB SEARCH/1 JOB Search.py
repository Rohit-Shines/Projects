import requests
import re
from bs4 import BeautifulSoup

query = "HL7 Developer job"
url = f"https://www.google.com/search?q={query}"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all search result links
    links = [link.get("href") for link in soup.find_all("a")]

    # Filter the links to only include job postings
    job_links = [link for link in links if "jobs" in link]

    # Print the job links
    for link in job_links:
        print(link)
else:
    print("Request failed with status code:", response.status_code)
