# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO GET LATEST UPDATES OF COVID CASES WORLWIDE & IN ANY COUNTRY USING covid MODULE.

# covid Module is the Python Package to get information regarding novel corona virus provided
# by Johns Hopkins university and worldometers.info

# The module can be installed using the command - pip install covid

# Importing necessary packages
import tkinter as tk
from covid import Covid
from tkinter import *
from datetime import datetime as dt
from tkinter.ttk import Combobox

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    worldwideActiveLabel = Label(root, text="WORLDWIDE ACTIVE CASES : ", bg="thistle4")
    worldwideActiveLabel.grid(row=0, column=0, padx=10, pady=5)
    worldwideActiveEntry = Label(root, width=20, bg='snow3')
    worldwideActiveEntry.grid(row=0, column=1, padx=10, pady=5)

    worldwideConfirmedLabel = Label(root, text="WORLDWIDE CONFIRMED CASES : ", bg="thistle4")
    worldwideConfirmedLabel.grid(row=1, column=0, padx=10, pady=5)
    worldwideConfirmedEntry = Label(root, width=20, bg='snow3')
    worldwideConfirmedEntry.grid(row=1, column=1, padx=10, pady=5)

    worldwideRecoveredLabel = Label(root, text="WORLDWIDE RECOVERED COUNT : ", bg="thistle4")
    worldwideRecoveredLabel.grid(row=2, column=0, padx=10, pady=5)
    worldwideRecoveredEntry = Label(root, width=20, bg='snow3')
    worldwideRecoveredEntry.grid(row=2, column=1, padx=10, pady=5)

    worldwideDeathsLabel = Label(root, text="WORDWIDE DEATHS COUNT : ", bg="thistle4")
    worldwideDeathsLabel.grid(row=3, column=0, padx=10, pady=5)
    worldwideDeathsEntry = Label(root, width=20, bg='snow3')
    worldwideDeathsEntry.grid(row=3, column=1, padx=10, pady=5)

    worldwide_total_active_cases = Covid().get_total_active_cases()
    worldwide_total_confirmed_cases = Covid().get_total_confirmed_cases()
    worldwide_total_recovered = Covid().get_total_recovered()
    worldwide_total_deaths = Covid().get_total_deaths()

    worldwideActiveEntry.config(text=str(worldwide_total_active_cases))
    worldwideConfirmedEntry.config(text=str(worldwide_total_confirmed_cases))
    worldwideRecoveredEntry.config(text=str(worldwide_total_recovered))
    worldwideDeathsEntry.config(text=str(worldwide_total_deaths))

    countryLabel = Label(root, text="COUNTRY NAME : ", bg="thistle4")
    countryLabel.grid(row=4, column=0, padx=10, pady=5)

    countryName = []
    # Fetching and Storing the countries list using the list_countries() of Covid Library
    countriesList = Covid().list_countries()
    for c in range(len(countriesList)):
        countryName.append(countriesList[c]['name'])
    # Displaying the Countries' Name in the Comboobx
    root.countriesComboBox = Combobox(root, width=18, values=countryName, state="readonly")
    root.countriesComboBox.grid(row=4, column=1, padx=5, pady=2)

    findButton = Button(root, text="FIND DETAILS", command=findDetails)
    findButton.grid(row=5, column=1, padx=5, pady=5, columnspan=2)

    activeCasesLabel = Label(root, text="TOTAL ACTIVE CASES :       ", bg="thistle4")
    activeCasesLabel.grid(row=6, column=0, padx=10, pady=5)
    root.activeCases = Label(root, width=20, bg='snow3')
    root.activeCases.grid(row=6, column=1, padx=10, pady=5)

    confirmedCasesLabel = Label(root, text="TOTAL CONFIRMED CASES :    ", bg="thistle4")
    confirmedCasesLabel.grid(row=7, column=0, padx=10, pady=5)
    root.confirmedCases = Label(root, width=20, bg='snow3')
    root.confirmedCases.grid(row=7, column=1, padx=10, pady=5)

    recoveredCasesLabel = Label(root, text="TOTAL RECOVERED COUNT :    ", bg="thistle4")
    recoveredCasesLabel.grid(row=8, column=0, padx=10, pady=5)
    root.recoveredCases = Label(root, width=20, bg='snow3')
    root.recoveredCases.grid(row=8, column=1, padx=10, pady=5)

    deathsLabel = Label(root, text="TOTAL DEATHS COUNT :       ", bg="thistle4")
    deathsLabel.grid(row=9, column=0, padx=10, pady=5)
    root.deaths = Label(root, width=20, bg='snow3')
    root.deaths.grid(row=9, column=1, padx=10, pady=5)

    updatedLabel = Label(root, text="LAST UPDATED AT :    ", bg="thistle4")
    updatedLabel.grid(row=10, column=0, padx=10, pady=5)
    root.updated = Label(root, width=20, bg='snow3')
    root.updated.grid(row=10, column=1, padx=10, pady=5)

# Defining findDetails() function to find the covid details of the user-input city
def findDetails():
    country = root.countriesComboBox.get()
    # Fetching the covid information of the user-input country
    specific_country_covid_info = Covid().get_status_by_country_name(country)

    # Fetching the specific Covid details of country and storing them in respective variables
    country_total_active_cases = specific_country_covid_info['active']
    country_total_confirmed_cases = specific_country_covid_info['confirmed']
    country_total_recovered = specific_country_covid_info['recovered']
    country_total_deaths = specific_country_covid_info['deaths']
    updated_time_epoch = specific_country_covid_info['last_update']
    data_updated_at = dt.fromtimestamp(updated_time_epoch/1000).strftime("%d-%m-%Y %H:%M:%S")

    # Showing the results in the tkinter window
    root.activeCases.config(text=str(country_total_active_cases))
    root.confirmedCases.config(text=str(country_total_confirmed_cases))
    root.recoveredCases.config(text=str(country_total_recovered))
    root.deaths.config(text=str(country_total_deaths))
    root.updated.config(text=str(data_updated_at))

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize & disabling the resizing property
root.title("PyCovidTracker")
root.config(background="thistle4")
root.geometry("470x390")
root.resizable(False, False)
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
