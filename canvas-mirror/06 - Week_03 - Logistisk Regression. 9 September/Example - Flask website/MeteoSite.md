# MeteoSite.zip (Flask example site)

Source: `Example - Flask website/MeteoSite.zip`. Extracted to scratchpad (not run). No README.

Files:

- `MeteoSite/app.py` - Flask app; routes `/`, `/weather`, `/radar`; helpers `get_latest_temperature(station_id)`, `get_active_warnings()`, `get_radar_timestamp()` fetch live data over HTTP (requests, XML parsing) for Danish weather.
- `MeteoSite/requirements.txt` - flask, requests, tzdata.
- `MeteoSite/templates/index.html`, `weather.html`, `radar.html` - pages.
- `MeteoSite/static/css/style.css`, `static/img/denmark.svg` - styling and a Denmark map.

Purpose: example of a Flask site showing Danish weather, warnings and radar.
