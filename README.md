# Stamps Internship Mini Test - Developer Role

This repository contains the completed mini-tests for the Developer Internship recruitment process at Stamps. 

The project is divided into two separate directories, each containing the executable Python source code and a screenshot of the expected terminal output.

## Repository Structure

### 1. Small Program (`mini-test-small-program`)
This folder contains the solution for the reverse array "FooBar" program.
* **Source Code:** `stamps_internship_mini test_small program.py`
* **Result Screenshot:** `stamps_internship_mini test_small program_results.png`

### 2. Weather Forecast (`mini-test-weather-forecast-jakarta`)
This folder contains the solution for fetching the 5-day weather forecast for Jakarta using the OpenWeatherMap API.
* **Source Code:** `stamps_internship_mini test_weather forecast jakarta.py`
* **Result Screenshot:** `stamps_internship_mini test_weather forecast jakarta_results.png`
* **Environment Template:** `.env.example`

---

## Setup and Execution

Both programs are written in **Python**. To run the weather forecast script locally, you will need to install the required dependencies and provide your own OpenWeatherMap API key.

### Prerequisites
1. Ensure Python 3 is installed on your system.
2. Install the required external libraries by running:
   ```bash
   pip install requests python-dotenv
   
### Running the Weather Forecast Script
For security purposes, the actual API key is not included in this repository. To execute the weather script successfully:

1. Navigate to the `mini-test-weather-forecast-jakarta` directory.
2. Locate the `.env.example` file.
3. Rename the file from `.env.example` to `.env`.
4. Open the new `.env` file and insert a valid OpenWeatherMap API key:
   ```text
   OPEN_WEATHER_API_KEY=your_api_key_here
