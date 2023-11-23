# Weather Data Microservice

This microservice records hourly temperatures for a specified city (default: Kyiv) using the OpenWeatherMap API and
provides an API endpoint to fetch the temperature history for a given day.

## Description

This project is a FastAPI-based microservice that:

1. Stores hourly temperature data for a specified city, which can be configured through environment variables.
2. Offers an API endpoint to retrieve temperature data for a specific day, with basic token-based authentication for
   spam prevention.

## Getting Started

### Dependencies

* Python 3.12
* Managed by Poetry

Ensure you have Python 3.12 or later installed.

### Setting Up and Running

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/karpenkotakeoff/weather_service.git
   cd weather_service
   ```

2. **Install Dependencies with Poetry:**

   ```bash
   poetry install
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**

   Set the environment variable for the city (e.g., Kyiv) and your OpenWeatherMap API key. You can do this in your shell
   or a `.env` file.

   ```bash
   CITY='Kyiv'
   API_KEY = "OpenWeatherMap_API_KEY"
   X_TOKEN = "your_32_char_token"
   DATABASE_URL = "your_database_url"
   
   APP_HOST = "localhost"
   APP_PORT = 7777
   ```

5. **Run the Application:**

   ```bash
   uvicorn app:app --reload
   ```

### API Usage

**Get Temperature History:**

- Endpoint: `/temperature`
- Method: `GET`
- Query Parameter: `day` in `Y-m-d` format
- Header: `x-token` (32-character string, as specified in environment/config)

Example request:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/temperature?day=2023-01-01' \
  -H 'accept: application/json' \
  -H 'x-token: your_32_char_token'
```

## Acknowledgments

* [OpenWeatherMap API](https://openweathermap.org/api)
* [FastAPI](https://fastapi.tiangolo.com/)
