# Vat leakage test station
Real life based simulation of a factory line, where vats are being tested for possible leakages. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Current process](#current-process)
* [Project requirments](#project-requirments)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)

## General Information
This project is part of my Python learning journey. I took a real life problem, client's request I saw online, and solve it virtually, in order to train programming skills, and build a portfolio.

First iteration of project relies on a text menu in the console. Factory scene is being drawn, and user, by choosing options, handles the vats and their testing. 

Most of the "coding magic" happens in the `factory.py` module, and `text_data.py` module holds constants that are being used in various places, in order to prevent hardcoded values.

## Technologies Used
- Python 3.10.6

## Current process
1. Worker brings new vat to the station and prepares it for the test. Next, workpiece is moved to free test field, station.

3. Vats are being tested with pressurised air. Depending on the vat construction, according pressure value is being set. After sealing the vat, air is pumped inside, and any possible leakages will result in pressure dropage. 

3. After the vat has been pressurised, an appriopriate amount of time is awaited (10 - 50 min., with mean of 30). If the pressure remains set, then the vat has passed the test, and can be moved to output. Otherwise it needs to be corrected, and tested again, and so on, until positive result.

## Project requirments
Client would like to:
1. Record the following data:
  1. Date and time of tests.
  2. Pressure versus time graph.
  3. Volume of air that had been pressed into a vat.
  4. How many times given vat had been tested.

2. Have a monitor which displays:
  1. Amount of airtight vats (workpieces that passed the test on the first trial)
  2. Amount of leaky vats (workpieces that needed to be corrected)

## Features
- Creating, testing, and handling vats.
- Simulation function for pressure value during the test.

## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->

## Setup
In the modules directory, there needs to be a directory for tests results. It's name needs to be included in `test_fixture.py` constants.

## Project Status
Project is _ongoing_, I'm working on it during spare time.