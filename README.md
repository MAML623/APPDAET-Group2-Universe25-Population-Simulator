# Universe 25 Population Simulator

**APPDAET — Python Programming | Group 2**

## Project Overview

The Universe 25 Population Simulator is a Python desktop application that simulates changes in a mouse population across multiple generations. The simulation considers the initial male and female populations, reproduction rates, death rates, and available resources.

The project aims to demonstrate how these factors affect population growth and decline using a simplified mathematical model. Users can adjust simulation settings and observe how the population changes over time.

## Planned Features

The application will include the following features:

- **Scenario Setup:** Enter the initial male and female populations, starting resources, and number of generations.
- **Model Controls:** Adjust birth rates, death rates, and resource replenishment settings.
- **Population Simulation:** Calculate births, deaths, and population changes for each generation.
- **Resource Management:** Track resource consumption and replenishment while preventing negative values.
- **Simulation Controls:** Run, Step, and Reset the simulation.
- **Generation Reports:** Display male and female populations, total population, births, deaths, and remaining resources.
- **Data Visualization:** Display population and resource changes through graphs.
- **Input Validation:** Prevent invalid inputs and impossible simulation values.
- **Final Summary:** Display the population and resource conditions at the end of the simulation.

## Simulation Algorithm

The application will use a generation-based population simulation algorithm.

The simulation begins at Generation 0 using the initial population and resources entered by the user. For each following generation, the program will:

1. Apply resource replenishment.
2. Calculate deaths based on the mortality rules.
3. Apply additional deaths when resources are insufficient.
4. Calculate possible births based on the surviving male and female populations.
5. Limit births according to available resources.
6. Deduct resource consumption and update the population.
7. Record and display the results for the generation.

The simulation continues until the selected generation limit is reached.

The model follows these basic rules:

- New Population = Previous Population + Births - Deaths
- Total Population = Male Population + Female Population
- Population and resources must never become negative.

The detailed calculation rules will be finalized during development.

## Technologies and Development Tools

- **Programming Language:** Python 3
- **Development Environments:** PyCharm and Visual Studio Code
- **Graphical User Interface:** Tkinter
- **Data Visualization:** Matplotlib
- **Additional Python Libraries:** random and unittest
- **Version Control:** Git and GitHub

Tkinter will be used to create the application's windows, input fields, buttons, and results table. Matplotlib will be used to display population and resource graphs.

## Proposed Project Structure

The application will be organized into separate Python files to make development and testing easier.

- **main.py** — Starts the application.
- **model.py** — Handles population calculations, births, deaths, and resources.
- **validation.py** — Validates user inputs.
- **state.py** — Manages the simulation state and Run, Step, and Reset functions.
- **gui.py** — Handles the graphical interface, results table, and charts.
- **tests/** — Contains automated tests.
- **docs/** — Contains project planning and documentation files.

## Expected Inputs and Outputs

### Inputs

- Initial male and female population counts
- Starting resources
- Number of generations (1–100)
- Birth rate and death rate
- Resource replenishment settings
- Optional random seed

### Outputs

- Generation-by-generation population reports
- Population history chart
- Resource history chart
- Final simulation summary

## Development Status

The project is currently in the planning and preparation stage. The simulation algorithm, graphical interface, and testing components will be implemented during the next development stages.

## Project Limitations

The simulator uses a simplified, assumption-driven population model for educational purposes. It does not scientifically reproduce the historical Universe 25 experiment or simulate detailed mouse behaviors.

The results are based on the rules and assumptions used in the application and should not be interpreted as accurate predictions of real-world population behavior.

## Group Members

**APPDAET — Group 2**

1. BARBA, RAYMOND JOSEF
2. BARIÑAN, MICKAELA CHARMONDE
3. LEDESMA, MARC ANTON
4. RAMOS, DAN JEON COGIE
5. SANTOS, FREYJA

## Instructor

Engr. Bob Mathew D. Sunga, MSc.

## AI Assistance Disclosure

ChatGPT was used to assist in preparing project planning and documentation. The group is responsible for reviewing, implementing, understanding, and testing the Python application.
