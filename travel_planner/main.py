import os
from crewai import Agent, Task, Crew, Process

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv

load_dotenv()


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range= date_range
        self.interests= interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            agent=expert_travel_agent,
            cities=self.cities,
            interests=self.interests,
            travel_dates=self.date_range  
        )


        identify_city = tasks.identify_city(
            agent=city_selection_expert, 
            origin=self.origin, 
            cities=self.cities ,
            interests=self.interests, 
            travel_dates=self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            agent=local_tour_guide, 
            city=self.cities, 
            travel_dates=self.date_range,
            interests=self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to `Trip Planner`")
    print("-------------------------------")
    origin = input(dedent("""What are you traveling from?"""))
    cities = input(dedent("""What are the city options you are interested in visiting?"""))
    date_range = input(dedent("""What is the date range you are interested in traveling?"""))
    interests = input(dedent("""What are some of your high level interetests and hobbies?"""))

    trip_crew = TripCrew(origin, cities, date_range, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is your trip plan:")
    print("########################\n")
    print(result)
