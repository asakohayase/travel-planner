import os
from langchain.tools import tool

class SearchFlightTools():
    @tool("Search for flights")
    def search_flights(origin, destination, departure_date, return_date):
        """Search for flights between origin and destination on specific dates"""
        api_endpoint = "https://skyscanner-flight-search.p.rapidapi.com/search"
        payload = {
            "origin": origin,
            "destination": destination,
            "departure_date": departure_date,
            "return_date": return_date
        }
        headers = {
            'X-RapidAPI-Key': os.environ['RAPID_API_KEY'],
            'X-RapidAPI-Host': 'skyscanner-flight-search.p.rapidapi.com'
        }
        response = requests.request("GET", api_endpoint, params=payload, headers=headers)
  