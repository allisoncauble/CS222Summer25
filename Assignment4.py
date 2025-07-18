import requests

USER_AGENT = "MuncieForecastApp (allisoncauble123@gmail.com)"

def fetch_json(url):
    resp = requests.get(url, headers={"User-Agent": USER_AGENT})
    resp.raise_for_status()
    return resp.json()

def main():
    point = fetch_json("https://api.weather.gov/points/40.1934,-85.3864")
    forecast_url = point["properties"]["forecast"]

    forecast = fetch_json(forecast_url)
    periods = forecast["properties"]["periods"]

    for i, p in enumerate(periods):
        if i >= 14:
            break
        print(f"{p['name']}: {p['temperature']}°{p.get('temperatureUnit','')}")
        print(f"  {p['detailedForecast']}\n")

if __name__ == "__main__":
    main()

