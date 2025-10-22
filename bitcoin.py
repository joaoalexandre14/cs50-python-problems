import requests
import sys

# --- PLACE API KEY FROM COINCAP HERE ---
API_KEY = "2019caf640ca2ffbdcef2fdc99a51b8109023ea0809b26b8b9d1136deb5a7903"
# ---------------------------------------------

# Check for command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Try to convert the argument to a float
try:
    n_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Construct the API URL using the v3 specification and the API key
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    # Make the API request
    response = requests.get(url)
    response.raise_for_status() # Exit if the request fails (e.g., 401, 403, 404)
    data = response.json()

    # Parse the JSON response to find the price
    # The price is nested in: data -> data -> priceUsd
    price_per_bitcoin = float(data["data"]["priceUsd"])

    # 6. Calculate the total cost
    total_cost = n_bitcoins * price_per_bitcoin

    # 7. Print the formatted result
    print(f"${total_cost:,.4f}")

except requests.RequestException:
    # This catches network/connection errors
    sys.exit("Error fetching data from the API")
except (KeyError, TypeError):
    # This catches errors if the JSON structure is not as expected
    sys.exit("Error parsing API response")
