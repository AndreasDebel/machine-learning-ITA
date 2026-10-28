# Games.zip (Flask example site)

Source: `Example - Flask website/Games.zip`. Extracted to scratchpad (not run). No README.

Files:

- `Games/app.py` - Flask app with routes `/` (home) and `/js-games`; registers the `game_of_life_bp` blueprint from `main.py`.
- `Games/main.py` - defines the Game of Life blueprint/logic.
- `Games/templates/home.html`, `game_of_life.html`, `js_games.html` - HTML pages.
- `Games/static/js/cardgame.js`, `snake.js`, `spaceinvaders.js` - browser games.
- `Games/static/images/students-1..6.jpg` - six photos.

No data/docs beyond HTML templates. Purpose: example of a small Flask website hosting Game of Life plus JavaScript games.
