<a name="readme-top"></a>

<h1>Travel Planner</h1>

<div align="left">
  <p>
   Travel Planner is an intelligent application that helps users discover their ideal destination and plan a detailed itinerary for their trip.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a> </li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#contributing">Getting Started</a></li>
    <li><a href="#contact">Acknowledgments</a></li>
  </ol>
</details>

## Features

1. Best City Recommendation: Input multiple cities you're considering, and our agents will analyze various factors to suggest the best city for your visit.
2. Customized Itinerary Generation: Provide your travel dates, and receive a day-by-day itinerary tailored to your chosen destination.



## Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* crewAI

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Get API Keys at the following websites
   * [https://platform.openai.com/](https://platform.openai.com/)
   * [https://serper.dev/](https://serper.dev/)
   * [https://rapidapi.com/](https://rapidapi.com/)
   
2. Clone the repo
   ```sh
   git clone https://github.com/asakohayase/travel_planner
   ```
3. Install packages
   ```sh
   poetry install
   ```
   You have to install poetry if not already installed.
   
4. Enter your API keys in `.env`
   ```js
   OPENAI_API_KEY='ENTER YOUR API';
   SERPER_API_KEY='ENTER YOUR API';
   RAPIDAPI_KEY='ENTER YOUR API';
   ```
5. Activate the virtual environment
   ```sh
   poetry shell
   ```

### Usage
To use the application, run the .py files:
   ```sh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [https://www.youtube.com/watch?v=swCPic00c30&t=2779s](https://www.youtube.com/watch?v=sPzc6hMg7So&t=1804s)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
