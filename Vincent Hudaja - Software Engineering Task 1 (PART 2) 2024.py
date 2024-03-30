#S.E. Task 1 2024 - Vincent Hudaja

#Imports & Modules
import requests #Library for HTTP requests (websites etc.)
import json #Functions containing JSON based data
import time #Time module for basic pauses/breaks in terminal
import os #Functions correlating with the operating system
from yachalk import chalk #Yachalk module allows coloured texts in terminal flexibly

#Universal Variables
recent_searches = [] #Create variable for search history as list to store values
start_time = time.time() #Simple runtime session timer to display how long user uses software utilising time module
t = time.localtime() #Retrieve time when session is run using time module
s_time = time.strftime("%H:%M:%S", t) #Define variable to display time

#API Key
api_key = '45f154b77d62266d00ed158436fa5eb3' #My API key to fetch information from openweathermap

#Get Weather Function
def get_weather(location): #Define function and variable
    time.sleep(0.2)
    print (f"Loading {chalk.cyan.bold('weather...')}")
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric' #API endpoint for current weather
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric' #API endpoint for Weekly Forecast
    current_weather_response = requests.get(current_weather_url) #Using request module and getting information from API using previous endpoints for current weather
    forecast_response = requests.get(forecast_url) #Using request module and getting information from API using previous endpoints for Weekly Forecast
    if current_weather_response.status_code == 404 or forecast_response.status_code == 404: #If/Loop statement for error handling if location inputted is not found in API as 404 error code
        print ()
        time.sleep(0.2)
        print(f"--> {chalk.red.bold.underline('Invalid')} location. Please enter a {chalk.green.bold('valid')} location.") #Print in terminal for user to input a valid location (utilising yachalk module for coloured text)
        print () 
        print (f"Press {chalk.yellow.bold('(m)')} to return to {chalk.yellow.bold('menu')} or {chalk.green.bold('(any button)')} and enter to continue.") #Option to return to BETA Menu or continue with search
        c = input() #Allows user input
        if c == "m": #If statement to confirm if user wants to return to menu
            time.sleep(0.2)
            print ()
            print (f"{chalk.yellow.bold('Returning')} to menu...")
            print () 
            time.sleep(0.5)
            os.system('cls')
            time.sleep(0.2)
            beta_weather_process() #Call beta weather process to return to menu
        elif c == "c": #If user press c they can clear terminal
            print (f"{chalk.yellow.bold('Clearing')} terminal...")
            time.sleep(0.2)
            loading() #Call loading function to clear terminal using cls function
            time.sleep(0.2)
            beta_weather_process() #Call beta weather process to return to menu
        else: #If user inputs a key other than 1, they are able to continue with search without returning to BETA menu
            time.sleep(0.2)
            print () 
            return None, None, None, None, None, None #Default return value, success of function and move on, return values (temp, humidity, weather and forecast)
    current_weather_data = json.loads(current_weather_response.text) #Convert JSON response to Python
    forecast_data = json.loads(forecast_response.text) #Convert JSON response to Python
    current_temp = current_weather_data['main']['temp'] #Retrieve temperature data from dictionary
    current_humidity = current_weather_data['main']['humidity'] #Retrieve humidity data from dictionary
    current_pressure = current_weather_data['main']['pressure'] #Retrieve pressure data from dictionary
    current_windspeed = current_weather_data['wind']['speed'] #Retrieve wind speed data from dictionary
    current_weather = current_weather_data['weather'][0]['description'] #Retrieve weather condition data from dictionary
    forecast_list = forecast_data['list'] #Retrieve lists of forecasts from dictionary 
    forecast = {} #Create empty list for forecast storage
    for f in forecast_list: #Loop through list of forecasts
        date = f['dt_txt'][:10] #Retrieve date from forecast
        if date not in forecast: #Check for existing date in forecast
            forecast[date] = {  
                'temp': f['main']['temp'],
                'humidity': f['main']['humidity'],
                'pressure': f['main']['pressure'],
                'speed': f['wind']['speed'],
                'weather': f['weather'][0]['description']  
            }

    return current_temp, current_humidity, current_pressure, current_windspeed, current_weather, forecast #Return weather data

#Loading Function
def loading(): #Define loading function
      loadings = 0 #Create variable that can be used flexibly in function
      while loadings != 1: #Loop for loading
        time.sleep(0.3) #Pause
        os.system('cls') #cls allows terminal to be cleared
        print(f"Loading - {chalk.blue.bold('BETA Weather')}.") #Print loading text
        time.sleep(0.3)
        os.system('cls')
        print(f"Loading - {chalk.green.bold('BETA Weather')}..")
        time.sleep(0.3)
        os.system('cls')
        print(f"Loading - {chalk.yellow.bold('BETA Weather')}...")
        time.sleep(0.3)
        os.system('cls')
        print(f"Loading - {chalk.red.bold('BETA Weather')}.")
        time.sleep(0.3)
        os.system('cls')
        print(f"Loading - {chalk.blue.bold('BETA Weather')}..")
        time.sleep(0.3)
        os.system('cls')
        print(f"Loading - {chalk.green.bold('BETA Weather')}...")
        time.sleep(0.3)
        os.system('cls')
        loadings = loadings + 1 #Add one to variable until loop is satisfied (loading == 1)

#Validate Location Function
def get_valid_location(): #Get valid location function for error handling if user inputs invalid location
    while True: #Boolean loop
        global location #Globalise variable 'location' for usage across all of code
        print ("-----------------------------") 
        print (f"      {chalk.blue.bold.bg_black('- BETA Weather -')}") #Software name
        print ()
        time.sleep(0.2)
        location = input(f"Enter a {chalk.green.bold('LOCATION')} and enter: ") #Allow user to search for a location's weather
        if location == "": #If statement for if user doesn't input any text
            time.sleep(0.2)
            print (f"{chalk.red.bold('No')} location detected, please enter a {chalk.green.bold('valid')} location.") #Print prompt for user
            time.sleep(0.2)
            print () 
        else:
            current_temp, current_humidity, current_pressure, current_windspeed, current_weather, forecast = get_weather(location) #All data to function
            if current_temp is not None: #If location inputted is valid, retrieve information
                return location, current_temp, current_humidity, current_pressure, current_windspeed, current_weather, forecast #Return all weather data
            else:
                time.sleep(0.2)

#Search History Function
def search_history(): #Search history function after user has successfully inputted a valid location and has received weather data
    global recent_searches #Globalise recent searches variable for flexible usage across code
    time.sleep(0.2)
    print (f"{recent_searches}: {chalk.magenta.bold(len(recent_searches))} current searches.") #Display search history list for user availability
    print () 
    def clear_search(): #Once search history is displayed, users are able to clear search history
        print (f"Would you like to {chalk.yellow.bold('clear')} search history?") #Prompt to clear search history
        print (f"{chalk.green.bold('YES - Clear History (1)')} | {chalk.red.bold('NO - Continue (2)')}") #Display options to clear or not to
        c = input() #Universal variable for confirmation
        print() 
        if c == "1": #If user enters 1, search history is cleared
            print ("-----------------------------") 
            print (f"{chalk.red.bold('Clearing')} search history...") #Inform user of history being cleared
            time.sleep(0.2)
            recent_searches.clear() #Clear function to clear values in a list
            print (f"{chalk.magenta.bold('Recent Searches:')} {recent_searches}") #Output new cleared search history
            print ("-----------------------------") 
        elif c == "2": #If users do not want to clear history, software will continue
            print ("Refreshing...")
            time.sleep(0.2)
        elif c == "c": #If user press c they can clear terminal
            print (f"{chalk.yellow.bold('Clearing')} terminal...")
            time.sleep(0.2)
            loading() #Call loading function using cls function
            time.sleep(0.2)
            beta_weather_process() #Call beta weather process function
        else: #If user inputs invalid option, clear search function is called again and the process repeats
            print (f"{chalk.red.bold('Invalid')} option, please re-enter a {chalk.green.bold('valid')} option:") #Prompt to re enter valid option
            print () 
            time.sleep(0.2)
            clear_search() #Call function again
    clear_search() #Call clear search function

#Software Name & Introduction
print ()
print (f"      {chalk.blue.bold.bg_black('- BETA Weather -')}") #Name of Software (Developed by Vincent Hudaja)
print ("-----------------------------") 
time.sleep(0.5) #Pause
print (f"{chalk.bg_black('WELCOME TO ')}{chalk.blue.bold.bg_black('BETA')}{chalk.bg_black(' - WEATHER API')}") #Introduction to BETA Weather Software
print ("-----------------------------") 
time.sleep(0.5)
print () 

#Continue Searching for Weather Function
def more_weather(): #More weather function allows user to continue searching for more than 1 location
    time.sleep(0.5)
    print (f"{chalk.yellow.bold.bg_black('Recent Searches:')}") #Display user search history
    search_history() #Call search history function
    print () 
    print (f"{chalk.green.bold('Continue')} {chalk.green.bold('(1)')} | {chalk.red.bold('Exit')} {chalk.red.bold('(x)')}") #Prompt to allow user to continue with software or exit
    c = input() #Universal variable for confirmation
    if c == "1": #If user enters 1, they are able to continue searching for other locations and get weather for it
        print () 
        loading() #Call loading function to clear terminal and clean up output
        print (f"      {chalk.blue.bold.bg_black('- BETA Weather -')}") #Software name
        print () 
        time.sleep(0.2)
        beta_weather_process() #Call beta weather process function to repeat process
    elif c == "x": #If user enters x they are able to easily exit software
        print () 
        print ("-----------------------------")
        print (f"--> {chalk.red.bold('Exiting')} {chalk.blue.bold('BETA')}...") #Dislay process of exiting
        print (f"{chalk.blue.bold('- BETA Weather -')}") #Display process of exiting
        print() 
        print (f"{chalk.yellow('- Build 1.3.1 - Vincent Hudaja -')}")
        time.sleep(0.5)
        print ("-----------------------------") 
        end_time = time.time() #Utilising time module to end timer
        runtime_session = end_time - start_time #Variable for timer/runtime session
        print (f"{chalk.yellow('Session Time:')} {runtime_session:.2f} seconds") #Display time of session whilst code was running
        print (f"{chalk.yellow('Session Commenced:')} {s_time}") #Display time when session was run
        print ()
        exit() #Exit function allows script to end smoothly
    elif c == "c": #If user presses c they can clear terminal
        print (f"{chalk.yellow.bold('Clearing')} terminal...")
        time.sleep(0.2)
        loading() #Call loading function using cls function
        time.sleep(0.2)
        beta_weather_process() #Call beta weather process to return to menu
    else: #If user inputs invalid option, their history is restored and the process repeats
        print (f"{chalk.red.bold('Invalid')} option, please re-enter a {chalk.green.bold('valid')} option (Refreshing...):")
        print () 
        print ("-----------------------------") 
        more_weather() #Call more weather function again

def menu_return(): #Menu return function to return to BETA Weather Menu
    print (f"{chalk.yellow.bold('Returning')} to menu...")
    print () 
    time.sleep(0.5)
    os.system('cls')
    time.sleep(0.2)
    beta_weather_process() #Call beta weather process to return to menu

def help_error(): #Help error function for help error handling
    print () 
    print (f"Press {chalk.yellow.bold('(m)')} and enter to return to menu:") #After user has read help information they can return back to menu
    c = input() #Universal variable for confirmation
    print () 
    if c == "m": #If user presses i, they will be able to return to menu
        menu_return() #Call menu return function to return to menu
    elif c == "c": #If user presses c, they can clear terminal
        print (f"{chalk.yellow.bold('Clearing')} terminal...")
        time.sleep(0.2)
        loading() #Call loading function
        time.sleep(0.2)
        beta_weather_process() #Call beta weather process function to return to menu
    else: #If user presses an invalid option, they will go through same function again
        print (f"{chalk.red.bold('Invalid')} option, please re-enter {chalk.green.bold('valid')} option:") #Prompt user to re-enter a valid option
        time.sleep(0.2)
        help_error() #Call help error function

#BETA Weather Process - API Fetching & BETA Weather Menu System
def beta_weather_process(): #Beta weather process consisting of menu and continuing processes
    global recent_searches
    print ("-----------------------------")
    print (f"     {chalk.blue.bold.bg_black('BETA Weather')}{chalk.bg_black(' - MENU')}") #Display BETA Weather menu
    print ("-----------------------------") 
    print (f"  [ {chalk.green.bold('CONTINUE')} with {chalk.blue.bold('BETA')} {chalk.green.bold('(1)')} ]") #Display option to continue and get weather
    print (f"  [       {chalk.yellow.bold('HELP')} ? {chalk.yellow.bold('(2)')}       ]") #Display option to request help
    print (f"  [  {chalk.magenta.bold('SEARCH HISTORY')}[] {chalk.magenta.bold('(3)')}  ]") #Display option to display search history
    print ("-----------------------------") 
    print (f"  [    {chalk.cyan.bold('INFO')} & {chalk.cyan.bold('CREDITS')} {chalk.cyan.bold('(i)')}  ]") #Display option to display search history
    print (f"  [      {chalk.red.bold('EXIT')} {chalk.blue.bold('BETA')} {chalk.red.bold('(x)')}     ]") #Display option to exit software
    print () 
    time.sleep(0.2)
    print (f"- To {chalk.yellow.bold('SELECT')} an {chalk.yellow.bold('OPTION')} press the designated {chalk.green.bold('key')} and {chalk.green.bold('(enter)')} -")
    print () 
    c = input() #Univeral variable for confirmation
    if c == "1": #If user enters 1, the software continues with the location search
        print () 
        location, current_temp, current_humidity, current_pressure, current_windspeed, current_weather, forecast = get_valid_location() #Data to function call
        print() 
        time.sleep(0.2)
        os.system('cls') #Use system module to clear terminal
        recent_searches.append(location) #Append user input from previous search into search history list
        print (f"{chalk.blue.bold.bg_black('Weather for ')}{chalk.blue.bold.underline.bg_black(location.capitalize())}") #Title for weather display
        print ("-----------------------------") 
        print ()
        print (f"{chalk.underline.cyan.bold.bg_black('Current ')}{chalk.cyan.bold.underline.bg_black('Weather')}{chalk.underline.bg_black(' in ')}{chalk.green.bold.underline.bg_black(location.capitalize())}{chalk.underline.bg_black(':')}") #Title for current weather information
        print () 
        print(f"--> Current {chalk.cyan.bold('temperature')} in {chalk.green(location.capitalize())}: {current_temp}°C") #Display current temperature
        print(f"--> Current {chalk.red.bold('humidity')} in {chalk.green(location.capitalize())}: {current_humidity}%")  #Display current humidity
        print(f"--> Current {chalk.magenta.bold('pressure')} in {chalk.green(location.capitalize())}: {current_pressure} hpa")  #Display current atomspheric pressure
        print(f"--> Current {chalk.white.bold('wind speed')} in {chalk.green(location.capitalize())}: {current_windspeed} m/s")  #Display current wind speed
        print(f"--> Current {chalk.yellow.bold('weather condition')} in {chalk.green(location.capitalize())}: {current_weather}")  #Display weather conditions
        time.sleep(0.5)
        print ()
        print ("-----------------------------")
        print(f"\n{chalk.cyan.bg_black.bold.underline('Weekly')}{chalk.bg_black.underline(' Forecast for ')}{chalk.green.bg_black.underline(location.capitalize())}{chalk.bg_black.underline(':')}") #Display 5 Day Forecast
        print () 
        for date, weather in forecast.items(): #Find forecast data
            print(f"--> {chalk.green.bold(date)}: {chalk.cyan.bold('Temperature:')} {weather['temp']}°C\n{chalk.yellow.bold('Weather Condition:')} {weather['weather']}") #Print 5 Day Forecast
            print () 
        else: #Once user has searched for location, more weather function is called
            print ("-----------------------------") 
            more_weather() #Call more weather function
    elif c == "x": #If user enters x, they can exit the software
        print () 
        print ("-----------------------------")
        print (f"--> {chalk.red.bold('Exiting')} {chalk.blue.bold('BETA')}...") #Display exit process
        print (f"{chalk.blue.bold('- BETA Weather -')}") #Display exit process
        print () 
        print (f"{chalk.yellow('- Build 1.3.1 - Vincent Hudaja -')}")
        time.sleep(0.5)
        print ("-----------------------------") 
        end_time = time.time() #Utilising time module to end timer
        runtime_session = end_time - start_time #Variable for timer/runtime session
        print(f"{chalk.yellow('Session Time:')} {runtime_session:.2f} seconds") #Display time of session whilst code was running
        print (f"{chalk.yellow('Session Commenced:')} {s_time}") #Display time when session was run
        print ()
        exit() #Easily stop script running
    elif c == "2": #If user enters 2, they are provided with help for usage of software
        print ("-----------------------------") 
        print (f"      {chalk.blue.bold.bg_black('- BETA Weather -')}") #Software name
        time.sleep(0.2)
        print () 
        print (f"{chalk.green.bold.underline.bg_black('BASIC SOFTWARE INTERFACE')}") #Categorise help information
        print () 
        print (f"   --> Use the {chalk.yellow.bold('MENU')} to {chalk.green.bold('search')}, ask {chalk.yellow.bold('help')} or {chalk.red.bold('exit')} {chalk.blue.bold('- BETA Weather -')}.") #Prompt of basic menu options
        time.sleep(0.2)
        print (f"   --> Get {chalk.cyan.bold('weather')} for a location by typing and entering.") #Prompt to tell user how to search for location
        time.sleep(0.2)
        print (f"   --> To access {chalk.magenta.bold('search history')}, press {chalk.magenta.bold('(3)')} and enter in menu.")
        time.sleep(0.2)
        print (f"   --> To {chalk.red.bold('exit')} press {chalk.red.bold('(x)')} and to {chalk.green.bold('continue')} press {chalk.green.bold('(1)')}") #Prompt for user interaction of keys to continue or exit
        time.sleep(0.2)
        print () 
        print (f"{chalk.cyan.bold.underline.bg_black('SEARCH & HISTORY INTERFACE')}") #Categorise help information
        print () 
        print (f"   --> {chalk.yellow.bold('Once')} a location has been searched for it will be recorded in your history.") #Prompt notifying user of search history function
        time.sleep(0.2)
        print (f"   --> To {chalk.red.bold('clear')} your search history, press {chalk.red.bold('(1)')} and to {chalk.green.bold('continue')} press {chalk.green.bold('(2)')}") #Prompt for user interaction of keys to clear history
        time.sleep(0.2)
        print (f"   --> If user does not press {chalk.red.bold('(1)')} or {chalk.green.bold('(2)')}, search history will be restored.")
        print () 
        time.sleep(0.2)
        print (f"{chalk.yellow.bold.underline.bg_black('CLEAR TERMINAL & MENU INTERFACE')}") #Categorise help information
        print () 
        print (f"   --> To {chalk.yellow.bold('clear')} terminal press {chalk.yellow.bold('(c)')} at any provided input (Exception of location input).") #Prompt to tell user how to clear terminal
        time.sleep(0.2)
        print (f"   --> If you {chalk.yellow.bold('clear')} terminal, you will be brought back to {chalk.blue.bold('- BETA Weather -')} Menu.") #Tells user what happens after clearing terminal
        print ("-----------------------------") 
        time.sleep(0.2)
        help_error() #Call help error function to continue to BETA Weather Menu
    elif c == "c": #If user presses c, they will be able to clear terminal
        print (f"{chalk.yellow.bold('Clearing')} terminal...")
        time.sleep(0.2)
        loading() #Call loading function with cls function
        time.sleep(0.2)
        beta_weather_process() #Call beta weather process to return to menu
    elif c == "3": #If user presses 3, they can access their recent search history
        print () #Empty brealk
        print ("-----------------------------") 
        print (f"      {chalk.blue.bold.bg_black('- BETA Weather -')}") 
        print ()
        time.sleep(0.2)
        print (f"Displaying {chalk.yellow.bold('Search History')}:") #Prompt to display search history list
        time.sleep(0.2)
        print (f"{recent_searches}: {chalk.magenta.bold(len(recent_searches))} current searches.") #Display search history list
        time.sleep(0.2)
        print ("-----------------------------") 
        help_error() #Call help error function to return to menu
    elif c == "i": #Provide user information on BETA Weather if i is pressed
        print ()
        time.sleep(0.2)
        print ("-----------------------------") 
        print (f"      {chalk.blue.bold.bg_black('- BETA Weather -')}")
        print ()
        time.sleep(0.2)
        print (f"{chalk.green.bold.underline('INFORMATION:')}")
        print () 
        print (f"   --> {chalk.blue.bold('BETA Weather')} is an API based software that is able to conveniently retrieve weather data through user interface")
        time.sleep(0.2)
        print (f"   --> {chalk.blue.bold('BETA Weather')} can be used to retrieve temperature, humidity, atmospheric pressure, wind speed, weather conditions and weekly forecast.")
        time.sleep(0.2)
        print (f"   --> {chalk.blue.bold('BETA Weather')} has an interactive menu which can be used to navigate through several options for convenience.")
        print () 
        time.sleep(0.2)
        print (f"{chalk.yellow.bold.underline('CREDITS:')}")
        print () 
        print (f"   --> {chalk.blue.bold('BETA Weather')} - Developed by {chalk.green.bold('Vincent Hudaja')}") #Developed by Vincent Hudaja
        time.sleep(0.2)
        print (f"   --> {chalk.yellow.bold('API Resource')} supplied by API key from {chalk.red.bold('OpenWeatherMap')}") #Acknowledge API resource
        time.sleep(0.2)
        print ("-----------------------------") 
        help_error() #Call help error function to return to menu
    else: #If user did not enter a valid option, the menu is called up again
        print () 
        print (f"{chalk.red.bold('Invalid')} option, please re-enter {chalk.green.bold('valid')} option:") #Promot for invalid option
        print () 
        time.sleep(0.5)
        beta_weather_process() #Call beta weather process function

beta_weather_process() #Call beta weather process function (menu)