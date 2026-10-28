# DataCoSupplyChainDataset.csv - schema note

Source: `Supply Chain Management/DataCoSupplyChainDataset.csv`. **180,519 rows x 53 columns** (one row per order item, 65,752 distinct orders, 20,652 customers). Encoding is latin-1/cp1252, not UTF-8 (accents garble, e.g. "Rajastán"). Used for the Supply Chain option of the mandatory assignment (see `Ita_ML_SupplyChain_Titanic.md`).

Obvious targets: `Late_delivery_risk` (0/1; tied to `Delivery Status`), or `Order Profit Per Order` / `Benefit per order`, `Sales`.
Leakage warning: `Days for shipping (real)`, `Delivery Status` and `Order Status` are known only after the outcome.

Apparent duplicates (identical examples/unique counts): `Benefit per order` = `Order Profit Per Order`; `Sales per customer` = `Order Item Total`; `Order Item Product Price` = `Product Price`; `Order Customer Id` = `Customer Id`; `Order Item Cardprod Id` = `Product Card Id`; `Category Id` = `Product Category Id`.
Useless: `Customer Email`, `Customer Password` (all "XXXXXXXXX"), `Product Status` (always 0), `Product Description` (100% missing).

| Column                        | Type | Missing | Unique | Examples                                          |
|-------------------------------|------|---------|--------|---------------------------------------------------|
| Type                          | str  | 0       | 4      | DEBIT, TRANSFER, CASH (payment type)              |
| Days for shipping (real)      | num  | 0       | 7      | 3, 5, 4                                           |
| Days for shipment (scheduled) | num  | 0       | 4      | 4, 1, 2                                           |
| Benefit per order             | num  | 0       | 21998  | 91.25, -249.09                                    |
| Sales per customer            | num  | 0       | 2927   | 314.64, 311.36                                    |
| Delivery Status               | str  | 0       | 4      | Advance shipping, Late delivery, Shipping on time |
| Late_delivery_risk            | num  | 0       | 2      | 0, 1                                              |
| Category Id                   | num  | 0       | 51     | 73, 17, 29                                        |
| Category Name                 | str  | 0       | 50     | Sporting Goods, Cleats                            |
| Customer City                 | str  | 0       | 563    | Caguas, San Jose                                  |
| Customer Country              | str  | 0       | 2      | Puerto Rico, EE. UU.                              |
| Customer Email                | str  | 0       | 1      | XXXXXXXXX                                         |
| Customer Fname                | str  | 0       | 782    | Cally, Irene                                      |
| Customer Id                   | num  | 0       | 20652  | 20755, 19492                                      |
| Customer Lname                | str  | 8       | 1109   | Holloway, Luna                                    |
| Customer Password             | str  | 0       | 1      | XXXXXXXXX                                         |
| Customer Segment              | str  | 0       | 3      | Consumer, Home Office, Corporate                  |
| Customer State                | str  | 0       | 46     | PR, CA, NY                                        |
| Customer Street               | str  | 0       | 7458   | 5365 Noble Nectar Island                          |
| Customer Zipcode              | num  | 3       | 995    | 725, 95125                                        |
| Department Id                 | num  | 0       | 11     | 2, 4, 5                                           |
| Department Name               | str  | 0       | 11     | Fitness, Apparel, Golf                            |
| Latitude                      | num  | 0       | 11250  | 18.25, 37.29                                      |
| Longitude                     | num  | 0       | 4487   | -66.04, -121.88                                   |
| Market                        | str  | 0       | 5      | Pacific Asia, USCA, Africa                        |
| Order City                    | str  | 0       | 3597   | Bekasi, Bikaner                                   |
| Order Country                 | str  | 0       | 164    | Indonesia, India                                  |
| Order Customer Id             | num  | 0       | 20652  | 20755                                             |
| order date (DateOrders)       | str  | 0       | 65752  | "1/31/2018 22:56" (M/D/YYYY H:MM)                 |
| Order Id                      | num  | 0       | 65752  | 77202, 75939                                      |
| Order Item Cardprod Id        | num  | 0       | 118    | 1360, 365                                         |
| Order Item Discount           | num  | 0       | 1017   | 13.11, 16.39                                      |
| Order Item Discount Rate      | num  | 0       | 18     | 0.04, 0.05                                        |
| Order Item Id                 | num  | 0       | 180519 | 180517 (row key)                                  |
| Order Item Product Price      | num  | 0       | 75     | 327.75, 59.99                                     |
| Order Item Profit Ratio       | num  | 0       | 162    | 0.29, -0.80                                       |
| Order Item Quantity           | num  | 0       | 5      | 1, 2, 3                                           |
| Sales                         | num  | 0       | 193    | 327.75, 119.98                                    |
| Order Item Total              | num  | 0       | 2927   | 314.64                                            |
| Order Profit Per Order        | num  | 0       | 21998  | 91.25                                             |
| Order Region                  | str  | 0       | 23     | Southeast Asia, South Asia, Oceania               |
| Order State                   | str  | 0       | 1089   | Java Occidental, Queensland                       |
| Order Status                  | str  | 0       | 9      | COMPLETE, PENDING, CLOSED                         |
| Order Zipcode                 | num  | 155679  | 609    | 99301, 90049 (86% missing)                        |
| Product Card Id               | num  | 0       | 118    | 1360, 365                                         |
| Product Category Id           | num  | 0       | 51     | 73, 17                                            |
| Product Description           | str  | 180519  | 0      | (empty)                                           |
| Product Image                 | str  | 0       | 118    | http://images.acmesports.sports/...               |
| Product Name                  | str  | 0       | 118    | Smart watch, Perfect Fitness Perfect Rip Deck     |
| Product Price                 | num  | 0       | 75     | 327.75, 59.99                                     |
| Product Status                | num  | 0       | 1      | 0                                                 |
| shipping date (DateOrders)    | str  | 0       | 63701  | "2/3/2018 22:56"                                  |
| Shipping Mode                 | str  | 0       | 4      | Standard Class, First Class, Second Class         |
