from typing import List, Dict, Any
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field
import os
import json
import requests


class SearchResult(BaseModel):
    title: str
    link: str
    snippet: str


class SearchToolInput(BaseModel):
    query: str = Field(..., description="The search query to be executed.")


class SearchTools(BaseTool):
    name: str = "Search the internet"
    description: str = (
        "Useful to search the internet about a given topic and return relevant results"
    )
    args_schema: type[BaseModel] = SearchToolInput

    def _run(self, query: str) -> str:
        top_result_to_return = 4
        url = "https://google.serper.dev/search"

        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # This will raise an exception for HTTP errors

        response_data: Dict[str, Any] = response.json()

        if "organic" not in response_data:
            return "Sorry, I couldn't find anything about that, there could be an error with your serper api key."

        results: List[Dict[str, Any]] = response_data["organic"]
        string_results: List[str] = []

        for result in results[:top_result_to_return]:
            try:
                search_result = SearchResult(
                    title=result["title"],
                    link=result["link"],
                    snippet=result["snippet"],
                )
                string_results.append(
                    "\n".join(
                        [
                            f"Title: {search_result.title}",
                            f"Link: {search_result.link}",
                            f"Snippet: {search_result.snippet}",
                            "\n-----------------",
                        ]
                    )
                )
            except KeyError:
                continue

        return "\n".join(string_results)
