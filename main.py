from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

class MasterGameDownloader:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)

    def __del__(self):
        # Close the browser when the object is deleted
        self.driver.quit()

    def get_game_ids(self, player_name, max_games):
        """
        Retrieves a list of game IDs for the specified player.
        :param player_name: Player's name (e.g., 'Garry Kasparov').
        :param max_games: Maximum number of games to download.
        :return: List of game IDs.
        """
        game_ids = set()
        page = 1

        while len(game_ids) < max_games:
            # Form the URL for searching games
            url = f"https://www.chess.com/games/search?fromSearchShort=1&p1={player_name.replace(' ', '%20')}&page={page}"
            self.driver.get(url)
            time.sleep(3)

            # Scroll the page to load all games
            scroll_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_scroll_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_scroll_height == scroll_height:
                    break
                scroll_height = new_scroll_height

            # Parse HTML to extract game IDs
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            game_links = soup.select("a.master-games-clickable-link.master-games-td-user")

            for link in game_links:
                href = link["href"]
                game_id = href.split("/")[-1]  # Extract ID from the URL
                if game_id.isdigit():
                    game_ids.add(game_id)
                    if len(game_ids) >= max_games:
                        break

            print(f"Player {player_name}: found {len(game_ids)} games on page {page}")
            page += 1

        return list(game_ids)[:max_games]

    def download_pgn(self, game_ids, filename):
        """
        Downloads games in PGN format using a list of game IDs.
        :param game_ids: List of game IDs.
        :param filename: Name of the file to save the PGN.
        """
        if not game_ids:
            print("No game IDs to download.")
            return

        # Form the URL to download PGN
        url = f"https://www.chess.com/games/downloadPgn?game_ids={','.join(game_ids)}"
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Saved {len(game_ids)} games to {filename}")
        else:
            print(f"Error downloading PGN: {response.status_code}")

    def download_games_for_players(self, players_dict: dict):
        """
        Downloads games for all players in the dictionary.
        :param players_dict: Dictionary of the form {'Player': number_of_games}.
        """
        for player_name, max_games in players_dict.items():
            print(f"Processing player: {player_name}")
            game_ids = self.get_game_ids(player_name, max_games)
            filename = f"./Games PGN/{player_name.replace(' ', '_')}_games.pgn"
            self.download_pgn(game_ids, filename)

# Example usage
if __name__ == "__main__":
    # Dictionary with players and the number of games
    players_dict = {
        "Garry Kasparov": 105,
        "Mikhail Tal": 55
    }

    downloader = MasterGameDownloader()
    downloader.download_games_for_players(players_dict)