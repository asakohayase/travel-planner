from typing import Type
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field
import os
import json
import requests


class HotelDetails(BaseModel):
    hotel_name: str
    hotel_id: str
    price: float


class SearchHotelsToolInput(BaseModel):
    """Input for SearchHotelsTool."""

    city: str = Field(..., description="The city to search for hotels in.")
    checkin: str = Field(..., description="Check-in date in YYYY-MM-DD format.")
    checkout: str = Field(..., description="Check-out date in YYYY-MM-DD format.")


class SearchHotelsTool(BaseTool):
    name: str = "Search for hotels"
    description: str = "Searches for hotels based on location and other parameters."
    args_schema: Type[BaseModel] = SearchHotelsToolInput

    def _run(self, city: str, checkin: str, checkout: str) -> str:
        """Search for hotels based on location and other parameters."""
        top_results_to_return = 4  # Limit the number of results returned

        # First, search for the destination ID using the Location Search API
        location_search_url = "https://booking-com.p.rapidapi.com/v1/location/search"
        location_search_payload = json.dumps({"name": city})
        location_search_headers = {
            "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
            "X-RapidAPI-Host": "booking-com.p.rapidapi.com",
            "content-type": "application/json",
        }
        location_search_response = requests.post(
            location_search_url,
            headers=location_search_headers,
            data=location_search_payload,
        )
        location_search_response.raise_for_status()
        location_search_data = location_search_response.json()
        destination_id = location_search_data[0]["destinationId"]

        # Then, search for hotels using the Hotel Search API
        hotel_search_url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
        hotel_search_payload = json.dumps(
            {
                "destination_id": destination_id,
                "order_by": "popularity",
                "filter_by_currency": "USD",
                "checkin": checkin,
                "checkout": checkout,
                "adults_number": 2,
                "room_number": 1,
                "dest_type": "city",
                "locale": "en-gb",
                "units": "metric",
            }
        )
        hotel_search_headers = {
            "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
            "X-RapidAPI-Host": "booking-com.p.rapidapi.com",
            "content-type": "application/json",
        }
        hotel_search_response = requests.post(
            hotel_search_url, headers=hotel_search_headers, data=hotel_search_payload
        )
        hotel_search_response.raise_for_status()
        hotel_search_data = hotel_search_response.json()

        # Process the hotel search results
        results = []
        for hotel in hotel_search_data["result"][:top_results_to_return]:
            try:
                hotel_details = HotelDetails(
                    hotel_name=hotel["hotel_name"],
                    hotel_id=hotel["hotel_id"],
                    price=hotel["price"],
                )
                results.append(
                    "\n".join(
                        [
                            f"Hotel Name: {hotel_details.hotel_name}",
                            f"Hotel ID: {hotel_details.hotel_id}",
                            f"Price: {hotel_details.price}",
                            "\n-----------------",
                        ]
                    )
                )
            except KeyError:
                continue

        return "\n".join(results)
