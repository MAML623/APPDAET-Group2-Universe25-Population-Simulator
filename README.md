# Universe 25 Population Simulator

**APPDAET — Python Programming | Group 2**

## Project Overview

The Universe 25 Population Simulator is a Python desktop application project that simulates changes in a mouse population across multiple generations. The simulation considers the initial male and female populations, reproduction rates, death rates, and available resources.

The project aims to demonstrate how these factors affect population growth and decline using a simplified mathematical model. Users can adjust simulation settings and observe how the population changes over time.

The project currently includes a working command-line prototype developed for Progress Report 2.

## Project Features

### Implemented Features (Progress Report 2)

- **Scenario Setup:** Enter the initial male and female populations, starting resources, and number of generations.
- **Simulation Settings:** Adjust birth rates, death rates, and resource replenishment.
- **Population Simulation:** Calculate births, deaths, and population changes for each generation.
- **Resource Management:** Track resource consumption and replenishment while preventing negative values.
- **Generation Reports:** Display male and female populations, total population, births, deaths, and remaining resources.
- **Input Validation:** Reject invalid population values, simulation settings, and unsupported rates.
- **Final Summary:** Display the final population, total births, total deaths, and remaining resources.
- **Predefined Scenarios:** Run baseline, resource-constrained, boundary, and invalid-input scenarios.
- **Custom Scenarios:** Allow users to enter their own simulation settings.
- **Bookkeeping Verification:** Check whether the simulation follows the required population rules.

### Planned Features

The following features will be implemented in later development stages:

- **Graphical User Interface:** Create an application window using Tkinter.
- **Simulation Controls:** Add Run, Step, and Reset buttons.
- **Data Visualization:** Display population and resource changes using Matplotlib.
- **Graphical Reports:** Present simulation results through tables and charts.

## Simulation Algorithm

The application uses a generation-based population simulation algorithm.

The simulation begins at Generation 0 using the initial population and resources entered by the user.

For each following generation, the program will:

1. Apply resource replenishment.
2. Calculate deaths based on the mortality rules.
3. Apply additional deaths when resources are insufficient.
4. Deduct resources consumed by surviving mice.
5. Calculate possible births based on the surviving male and female populations.
6. Limit births according to available resources.
7. Add newborn mice and deduct their resource consumption.
8. Record and display the updated population and resources.

The simulation continues until the selected generation limit is reached.

The model follows these basic rules:

- New Population = Previous Population + Births - Deaths
- Total Population = Male Population + Female Population
- Reproduction requires at least one male and one female mouse.
- Population and resources must never become negative.
- Births cannot exceed the available resource capacity.

The simulation uses a simplified mathematical model with deterministic calculations.

## Technologies and Development Tools

- **Programming Language:** Python 3
- **Development Environments:** PyCharm and Visual Studio Code
- **Graphical User Interface (Planned):** Tkinter
- **Data Visualization (Planned):** Matplotlib
- **Python Libraries:** math and unittest
- **Version Control:** Git and GitHub

The current command-line prototype uses Python's standard library and does not require additional packages.

Tkinter and Matplotlib will be used during the development of the graphical interface and charts.

## Project Structure

The application is organized into separate Python files to make development and testing easier.

- **main.py** — Initial application entry point, planned for the final application.
- **model.py** — Contains the working population simulation algorithm, resource calculations, and input validation.
- **prototype.py** — Runs the functional command-line prototype, interactive menu, reports, and final summary.
- **validation.py** — Placeholder for future separation of input validation.
- **state.py** — Placeholder for future simulation state management and controls.
- **gui.py** — Placeholder for the planned graphical interface, tables, and charts.
- **tests/** — Directory for automated testing files.
- **docs/** — Contains project planning and progress report documentation.
- **README.md** — Provides project information and instructions.
- **.gitignore** — Excludes unnecessary Python-generated files from version control.

## Expected Inputs and Outputs

### Inputs

- Initial male and female population counts
- Starting resources
- Number of generations (1–100)
- Birth rate (0 to 1)
- Death rate (0 to 1)
- Resource replenishment per generation

### Outputs

- Generation-by-generation population reports
- Male and female population counts
- Total population
- Number of births and deaths
- Remaining resources
- Final simulation summary
- Simulation end-state
- Bookkeeping verification result

Population and resource graphs will be added in a later development stage.

## How to Run the Prototype

### Requirements

- Python 3
- Visual Studio Code, PyCharm, or another Python-compatible editor

No additional packages are required to run the current command-line prototype.

### Running the Program

1. Download or clone the GitHub repository.
2. Open the project folder in VS Code or PyCharm.
3. Open the terminal.
4. Run the following command:

```bash
python3 prototype.py
```

On Windows, you may use `python prototype.py` if Python is configured under that command.

5. Select an option from the interactive menu.

### Available Menu Options

1. Baseline scenario (plenty of resources)
2. Resource-constrained scenario
3. Boundary test (no females)
4. Invalid-input test (negative males)
5. Enter custom simulation settings
0. Exit

The program displays the population changes for each generation, followed by a final simulation summary.

The summary includes:

- Number of generations completed
- Final population
- Total births and deaths
- Remaining resources
- Final simulation status
- Bookkeeping verification result

## Progress Report 1 — Project Foundation

Progress Report 1 focused on planning and preparing the project.

The group completed the following:

- Project understanding and scope
- Algorithm design and program decomposition
- Development environment preparation
- GitHub repository initialization
- Project management and development timeline
- Initial Python project structure
- README and Python .gitignore configuration

The group also demonstrated the Git workflow, including cloning, committing, pushing, and pulling changes.

## Progress Report 2 — Functional Prototype

Progress Report 2 focuses on implementing and testing the main simulation algorithm.

The project now includes a working command-line prototype.

### Completed Developments

- Implemented the main population simulation algorithm in model.py.
- Added calculations for births, deaths, and resource management.
- Implemented input validation and population constraints.
- Created prototype.py with an interactive menu.
- Added predefined and custom simulation scenarios.
- Implemented generation-by-generation result reporting.
- Added a final simulation summary and bookkeeping verification.
- Tested the prototype using sample simulation scenarios.
- Uploaded the working Python files to GitHub.
- Recorded the development progress through meaningful Git commits.

### Current Development Status

The computational algorithm and command-line prototype are functional.

The graphical user interface, interactive GUI controls, and population charts will be developed in the next progress report.

## Project Limitations

The simulator uses a simplified, assumption-driven population model for educational purposes.

It does not scientifically reproduce the historical Universe 25 experiment or simulate individual mouse behaviors and complex social interactions.

The current version uses deterministic calculations and does not include random population events.

The results are based on the rules and assumptions implemented in the application and should not be interpreted as accurate predictions of real-world population behavior.

## Group Members

**APPDAET — Group 2**

1. BARBA, RAYMOND JOSEF
2. BARIÑAN, MICKAELA CHARMONDE
3. LEDESMA, MARC ANTON
4. RAMOS, DAN JEON COGIE
5. SANTOS, FREYJA

## Project Responsibilities

- **Freyja Santos — Project Leader:** Manages project tasks, deadlines, and coordination.
- **Dan Jeon Cogie Ramos — GUI Programmer:** Responsible for developing the graphical user interface and controls.
- **Marc Anton Ledesma — Simulation Programmer:** Assigned to population simulation calculations and computational development.
- **Mickaela Charmonde Bariñan — Graphs and Reports:** Responsible for population graphs, resource graphs, and reports.
- **Raymond Josef Barba — Testing and Documentation:** Responsible for testing and preparing documentation.

All group members participate in project integration, review, and final presentation.

## Instructor

Engr. Bob Mathew D. Sunga, MSc.

## AI Assistance Disclosure

ChatGPT was used to assist in preparing project planning, organizing documentation, and updating the GitHub README.

The group remains responsible for reviewing, implementing, understanding, and testing the Python application.
