from crewai import Crew
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from tools.search_tools import SearchTools
from tools.search_hotels_tools import SearchHotelsTool
from tools.calculator_tools import CalculatorTools

from dotenv import load_dotenv

load_dotenv()


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom tools here
        search_tools = SearchTools()
        search_hotel_tools = SearchHotelsTool()
        calculator_tools = CalculatorTools()

        # Define your custom agents and tasks here
        city_selection_expert = agents.city_selection_expert(
            search_tools, search_hotel_tools
        )
        local_tour_guide = agents.local_tour_guide(search_tools, search_hotel_tools)
        expert_travel_agent = agents.expert_travel_agent(calculator_tools)

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range,
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide, self.cities, self.date_range, self.interests
        )

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent, self.cities, self.date_range, self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[city_selection_expert, local_tour_guide, expert_travel_agent],
            tasks=[identify_city, gather_city_info, plan_itinerary],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("-------------------------------")
    origin = input(
        dedent(
            """
      From where will you be traveling from?
    """
        )
    )
    cities = input(
        dedent(
            """
      What are the cities options you are interested in visiting?
    """
        )
    )
    date_range = input(
        dedent(
            """
      What is the date range you are interested in traveling (YYYY-MM-DD format)?
    """
        )
    )
    interests = input(
        dedent(
            """
      What are some of your high level interests and hobbies?
    """
        )
    )

    trip_crew = TripCrew(origin, cities, date_range, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)
