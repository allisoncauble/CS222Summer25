import sys
import requests

USER_AGENT = "WikipediaRevisionTrackerApp (allisoncauble123@gmail.com)"
API_URL = "https://en.wikipedia.org/w/api.php"

def get_revisions(title):
    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "titles": title,
        "rvprop": "timestamp|user",
        "rvlimit": "30",
        "redirects": ""
    }

    try:
        response = requests.get(API_URL, headers={"User-Agent": USER_AGENT}, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(3)

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a Wikipedia article name.")
        sys.exit(1)

    title = " ".join(sys.argv[1:])
    data = get_revisions(title)

    if "redirects" in data["query"]:
        new_title = data["query"]["redirects"][0]["to"]
        print(f"Redirected to {new_title}")
        title = new_title  # update title to final

    pages = data["query"]["pages"]
    page = next(iter(pages.values()))

    if "missing" in page:
        print(f"No Wikipedia page found for '{title}'.")
        sys.exit(2)

    revisions = page.get("revisions", [])
    for rev in revisions:
        print(f"{rev['timestamp']} {rev['user']}")

    sys.exit(0)

if __name__ == "__main__":
    main()
