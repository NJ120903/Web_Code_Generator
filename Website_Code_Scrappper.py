import requests
from bs4 import BeautifulSoup

# Function to scrape the website
def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Print the parsed HTML to check the structure
        print(soup.prettify())  # This will print the entire HTML content

        # Find all blog post titles and links
        posts = soup.find_all('article', class_='post')

        # Check if any posts are found
        if posts:
            # Loop through each post and extract the title and link
            for post in posts:
                title = post.find('h2').text
                link = post.find('a')['href']
                print(f"Title: {title}\nLink: {link}\n")
        else:
            print("No posts found. Check the HTML structure and class names.")
    else:
        print("Failed to access the website. Status code:", response.status_code)

# Get the URL from the user
user_url = input("Enter the URL of the website to scrape: ")
scrape_website(user_url)
