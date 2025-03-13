# Chess Game Downloader

This project is a Python tool for downloading chess games in PGN format from [Chess.com](https://www.chess.com). It uses **Selenium** for web scraping and **BeautifulSoup** for parsing HTML. The tool allows you to download a specified number of games for multiple players.

---

## Features

-   **Download Games by Player**: Specify a dictionary of players and the number of games to download (e.g., `{'Garry Kasparov': 100, 'Mikhail Tal': 50}`).
-   **Dynamic Page Loading**: Automatically scrolls through pages to load all games.
-   **PGN Export**: Downloads games in PGN format, which can be imported into chess software like ChessBase or Lichess.

---

## Requirements

-   Python 3.7+
-   Libraries: `selenium`, `beautifulsoup4`, `requests`
-   ChromeDriver (download from [here](https://sites.google.com/chromium.org/driver/))

---

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/yourusername/chess-game-downloader.git](https://github.com/yourusername/chess-game-downloader.git)
    cd chess-game-downloader
    ```

2.  Install dependencies:

    ```bash
    pip install selenium beautifulsoup4 requests
    ```

3.  Download ChromeDriver and ensure it is in your system's PATH.

---

## Usage

1.  Create a dictionary with player names and the number of games to download:

    ```python
    players_dict = {
        "Garry Kasparov": 105,
        "Mikhail Tal": 55,
        "Viswanathan Anand": 50
    }
    ```

2.  Run the script:

    ```python
    downloader = ChessGameDownloader()
    downloader.download_games_for_players(players_dict)
    ```

3.  The PGN files will be saved in the current directory with names like `Garry_Kasparov_games.pgn`.

---

## Example

```python
from chess_game_downloader import ChessGameDownloader

players_dict = {
    "Garry Kasparov": 100,
    "Mikhail Tal": 50
}

downloader = ChessGameDownloader()
downloader.download_games_for_players(players_dict)
```

---

## Notes
Ensure you have a stable internet connection.
Chess.com may block frequent requests. Add delays (time.sleep()) if necessary.
Use this tool responsibly and comply with Chess.com's terms of service.

---

## License
This project is licensed under the MIT License. See the [LICENSE](docs/LICENSE) file for details.
