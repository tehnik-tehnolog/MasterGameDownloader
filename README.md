<details>
  <summary>English</summary>
    
## Chess Game Downloader

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

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

</details>

<details>
  <summary>Русский</summary>
    
## Chess Game Downloader

Этот проект представляет собой инструмент на Python для загрузки шахматных партий в формате PGN с сайта [Chess.com](https://www.chess.com). Он использует **Selenium** для веб-скрейпинга и **BeautifulSoup** для парсинга HTML. Инструмент позволяет загружать указанное количество партий для нескольких игроков.

---

## Возможности

-   **Загрузка партий по игрокам**: Укажите словарь с именами игроков и количеством партий для загрузки (например, `{'Гарри Каспаров': 100, 'Михаил Таль': 50}`).
-   **Динамическая загрузка страниц**: Автоматически прокручивает страницы, чтобы загрузить все партии.
-   **Экспорт в PGN**: Загружает партии в формате PGN, который можно импортировать в шахматные программы, такие как ChessBase или Lichess.

---

## Требования

-   Python 3.7+
-   Библиотеки: `selenium`, `beautifulsoup4`, `requests`
-   ChromeDriver (скачайте [здесь](https://sites.google.com/chromium.org/driver/))

---

## Установка

1.  Клонируйте репозиторий:

    ```bash
    git clone [https://github.com/yourusername/chess-game-downloader.git](https://github.com/yourusername/chess-game-downloader.git)
    cd chess-game-downloader
    ```

2.  Установите зависимости:

    ```bash
    pip install selenium beautifulsoup4 requests
    ```

3.  Скачайте ChromeDriver и убедитесь, что он добавлен в PATH вашей системы.

---

## Использование

1.  Создайте словарь с именами игроков и количеством партий для загрузки:

    ```python
    players_dict = {
        "Garry Kasparov": 100,
        "Mikhail Tal": 50
    }
    ```

2.  Запустите скрипт:

    ```python
    downloader = ChessGameDownloader()
    downloader.download_games_for_players(players_dict)
    ```

3.  Файлы PGN будут сохранены в текущей директории с именами вида `Garry_Kasparov_games.pgn`.

---

## Пример

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

## Примечания
Убедитесь, что у вас стабильное подключение к интернету.
Chess.com может блокировать частые запросы. При необходимости добавьте задержки (time.sleep()).

---

## Лицензия
Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

</details>


