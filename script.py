import requests

# Parameter als Dictionary
params = {
    "q": "pokemon",   # Wir wollen Repositories für beliebige Themen untersuchen,
    "sort": "stars",  # sortiert nach Stars ("Likes"),
    "order": "desc"   # in absteigender Reihenfolge.
}

# API-Anfrage mit JSON-Antwort
response = requests.get("https://api.github.com/search/repositories",
                       params=params)

if response.status_code == 200:
    # JSON automatisch zu Python Dictionary
    data = response.json()
    print(f"\n Gefunden: {data['total_count']} Repositories")

    # Erste 10 Ergebnisse
    for repo in data['items'][:10]:
        print(f"- {repo['name']}: {repo['stargazers_count']}")
    print("\n")
else:
    print(f"Fehler: {response.status_code}")

print("Hello TUD! :)")
print("Hello TUD! :)")
print("Hello TUD! :)")

# print("\n"*2, data)
# - {repo['html_url']}