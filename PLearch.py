import webbrowser

def search_social_media(query, platform):
    # Construct the Google search URL with the site: operator for the specified platform
    search_url = f"https://www.google.com/search?q={query}+site%3A{platform}.com"
    return search_url

if __name__ == "__main__":
    platform = input("Enter the platform you'd like to search through: ")
    query = input("Enter keywords: ")
    final_search_url = search_social_media(query, platform)
    
    if final_search_url:
        print("Opening search in browser...")
        webbrowser.open(final_search_url)
    else:
        print("Failed to construct search URL.")

