import requests

class Dota2Tracker:
    def __init__(self, steam_id):
        self.steam_id = steam_id
        self.api_key = "---"  # Заменить API ключ Steam

    def get_player_summary(self):
        url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids={self.steam_id}"
        response = requests.get(url)
        data = response.json()
        player_summary = data["response"]["players"][0]
        return player_summary

    def get_dota2_mmr(self):
        url = f"https://api.opendota.com/api/players/{self.steam_id}/mmr_estimate"
        response = requests.get(url)
        data = response.json()
        mmr_estimate = data["solo_estimate"]
        return mmr_estimate

if __name__ == "__main__":
    steam_id = "---"  # Заменить API ключ Steam
    tracker = Dota2Tracker(steam_id)
    
    player_summary = tracker.get_player_summary()
    print("Player Summary:")
    print("Name:", player_summary["personaname"])
    print("Real Name:", player_summary["realname"])
    print("Profile URL:", player_summary["profileurl"])
    
    current_mmr = tracker.get_dota2_mmr()
    print("\nCurrent MMR Estimate:", current_mmr)
