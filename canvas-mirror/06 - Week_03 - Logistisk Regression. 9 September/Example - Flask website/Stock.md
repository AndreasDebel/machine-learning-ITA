# Stock.zip (Flask example site with ML models)

Source: `Example - Flask website/Stock.zip`. Extracted to scratchpad (not run). No README.

Code files:

- `Stock/main.py` - Flask app; routes `/`, `/predict`, `/today`, `/live`; uses `model.py` and `stocks.py`.
- `Stock/model.py` - training/prediction helpers (`train_ticker`, `get_today_view`, `predict_for_date`, `valid_date_range`).
- `Stock/stocks.py` - the `STOCKS` ticker list.
- `Stock/train_model.py` - loops over STOCKS and trains one model per ticker.
- `Stock/static/script.js`, `today.js`, `style.css`; `Stock/templates/index.html`, `today.html` - front end.
- `Stock/requirements.txt` - Flask, yfinance, pandas, scikit-learn, joblib.

Non-code:

- `Stock/data/<TICKER>.csv` - 15 price histories (AAPL, AMZN, DSV.CO, GOOGL, JNJ, JPM, MAERSK-B.CO, META, MSFT, NOVO-B.CO, NVDA, ORSTED.CO, TSLA, V, VWS.CO); columns `Date,Close`; e.g. AAPL has about 1254 daily rows starting 2021-09-09 (close 150.27).
- `Stock/models/<TICKER>.joblib` - 15 pre-trained scikit-learn models (binary, not inspected).

Purpose: example of serving per-stock ML predictions via a Flask website.
