# Installations
```bash
virtualenv -p python3.8 venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
# create non-crypto currencies and fetch crypto currencies from external api
python manage.py fetch_currencies

# unittest run
python manage.py test
```

## RUN
- `python manage.py runserver`
- Navigate to `http://127.0.0.1:8000/`
- Frontend access to the api via above IP address and Port

## USAGE
#### Currency
- Endpoint: `/api/v1/currencies/`
- Make HTTP GET request. Response will be like this
```json
{
    "next": "http://127.0.0.1:8000/api/v1/currencies/?page=2",
    "previous": null,
    "count": 50,
    "total_pages": 5,
    "current_page": 1,
    "results": [
        {
            "id": 120,
            "name": "Bitcoin",
            "slug": "bitcoin",
            "symbol": "btc",
            "price": 29865.0,
            "created_date": "2022-05-17T21:42:00.887714Z",
            "updated_date": "2022-05-17T21:42:00.887806Z",
            "last_updated": "2022-05-17T21:35:20.969000Z",
            "currencyimage_set": [
                {
                    "id": 1,
                    "created_date": "2022-05-17T21:42:00.892773Z",
                    "updated_date": "2022-05-17T21:42:00.892871Z",
                    "status": "A",
                    "small": "https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1547033579",
                    "thumb": "https://assets.coingecko.com/coins/images/1/thumb/bitcoin.png?1547033579",
                    "large": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579",
                    "currency": 120
                }
            ]
        },
        {
            "id": 121,
            "name": "Ethereum",
            "slug": "ethereum",
            "symbol": "eth",
            "price": 2036.66,
            "created_date": "2022-05-17T21:42:00.894096Z",
            "updated_date": "2022-05-17T21:42:00.894174Z",
            "last_updated": "2022-05-17T21:36:10.169000Z",
            "currencyimage_set": [
                {
                    "id": 2,
                    "created_date": "2022-05-17T21:42:00.895384Z",
                    "updated_date": "2022-05-17T21:42:00.895463Z",
                    "status": "A",
                    "small": "https://assets.coingecko.com/coins/images/279/small/ethereum.png?1595348880",
                    "thumb": "https://assets.coingecko.com/coins/images/279/thumb/ethereum.png?1595348880",
                    "large": "https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880",
                    "currency": 121
                }
            ]
        }
    ]
}
```
- Make HTTP POST Request.
    - Payload `{"name": "Bitcoin","symbol": "btc","slug": "btc","last_updated": "2022-05-18T07:30:40.816359Z"}`
    - Response status HTTP 201 Created

#### Currency Price

- Endpoint: `/api/v1/currency-prices/`
- Make HTTP GET request. Response will be like this
```json
{
    "next": "http://127.0.0.1:8000/api/v1/currency-prices/?page=2",
    "previous": null,
    "count": 21200,
    "total_pages": 2120,
    "current_page": 1,
    "results": [
        {
            "id": 21200,
            "created_date": "2022-05-18T07:07:26.696370Z",
            "updated_date": "2022-05-18T07:07:26.696384Z",
            "price": "1.990319000000",
            "default_currency": 169,
            "vs_currency": 144
        },
        {
            "id": 21199,
            "created_date": "2022-05-18T07:07:26.695584Z",
            "updated_date": "2022-05-18T07:07:26.695598Z",
            "price": "237.390000000000",
            "default_currency": 169,
            "vs_currency": 117
        },
    ]
}
```
- Make HTTP POST Request.
    - Payload `{"price": "32456.0", "default_currency": 1, "vs_currency": 2}`
    - Response status HTTP 201 Created

