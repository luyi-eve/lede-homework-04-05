#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[55]:


url = "http://api.weatherapi.com/v1/current.json?key=0b7eca5ec81f4365a3f175434221406&q=Miami&aqi=no"


# In[56]:


response = requests.get(url)


# In[57]:


data = response.json()


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[58]:


print("The current wind speed of Miami is",data['current']['wind_mph'],"miles per hour.")


# In[60]:


print("It feels", round(data['current']['feelslike_c']-data['current']['temp_c']),"celsius degrees warmer than it actually is.")


# In[ ]:





# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[61]:


# Moon-related API endpoint: Astronomy API


# In[62]:


# Today is 2022-06-15, so url here is for tmr's moon's information which is 2022-06-16.

url_moon_mia = "http://api.weatherapi.com/v1/astronomy.json?key=0b7eca5ec81f4365a3f175434221406&q=Miami&dt=2022-06-16"
response = requests.get(url_moon_mia)
data = response.json()


# In[63]:


print(data['astronomy']['astro']['moon_phase'],"will be visible tomorrow.")


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[74]:


url_differ = "http://api.weatherapi.com/v1/history.json?key=0b7eca5ec81f4365a3f175434221406&q=Miami&dt=2022-06-15"
response = requests.get(url_differ)
data = response.json()


# In[75]:


max = data['forecast']['forecastday'][0]['day']['maxtemp_c']
min = data['forecast']['forecastday'][0]['day']['mintemp_c']
difference = max - min
print(max, min)


# In[76]:


print("The difference between the high and low temperatures for today is", round(difference),"celsius degrees.")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[ ]:


# url, response and data are three variables that will need to be renamed to ensure every time I make another request, my variables won't be overwritten!


# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[77]:


url_forecast = "http://api.weatherapi.com/v1/forecast.json?key=0b7eca5ec81f4365a3f175434221406&q=Miami&days=3&aqi=no&alerts=no"
response_forecast = requests.get(url_forecast)
data_forecast = response_forecast.json()


# In[100]:


for day in data_forecast['forecast']['forecastday']:
    print(day['date'],"'s highest temperature is ",day['day']['maxtemp_c'],"celsius degrees.")
    if day['day']['maxtemp_c'] > 32.6:
        print(day['date'],"will be really hot!")
    else:
        print(day['date'],"will be warm.")


# In[ ]:





# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[110]:


url_seven = "http://api.weatherapi.com/v1/forecast.json?key=&q=Miami&days=7&aqi=no&alerts=no"
response_seven = requests.get(url_seven)
data_seven = response_seven.json()


# In[111]:


print(data_seven)
# it shows: {'error': {'code': 1002, 'message': 'API key is invalid or not provided.'}}


# In[ ]:


# The reasons why it didn't work is probably because:
# Depending upon the subscription plan, WEATHER API provides current and 3 day air quality data for the given location in json and xml


# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[115]:


url_forecast = "http://api.weatherapi.com/v1/forecast.json?key=0b7eca5ec81f4365a3f175434221406&q=Miami&days=3&aqi=no&alerts=no"
response_forecast = requests.get(url_forecast)
data_forecast = response_forecast.json()


# In[126]:


max_temp = 0
max_temp_day = ''

for day in data_forecast['forecast']['forecastday']:
    if  day['day']['maxtemp_c'] > max_temp:
        max_temp = day['day']['maxtemp_c']
        max_temp_day = day['date']
print(max_temp_day,"will be the hottest day in the next three days with the high temperature of",max_temp,"celsius degrees.")


# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[128]:


url_24 = "http://api.weatherapi.com/v1/forecast.json?key=0b7eca5ec81f4365a3f175434221406&q=Miami&days=1&aqi=no&alerts=no"
response_24 = requests.get(url_24)
data_24 = response_24.json()


# In[162]:


for time in data['forecast']['forecastday']:
    for hour in time['hour']:
        if hour['cloud'] > 50:
            print(hour['time'],":",hour["temp_f"], "°F and",hour['cloud'],"% of cloud cover.")
        else:
            print(hour['time'],":",hour["temp_f"], "°F")


# In[ ]:





# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[232]:


url_24 = "http://api.weatherapi.com/v1/forecast.json?key=0b7eca5ec81f4365a3f175434221406&q=Miami&days=1&aqi=no&alerts=no"
response_24 = requests.get(url_24)
data_24 = response_24.json()


# In[244]:


hour_85 = []
max_len = 0

for time in data['forecast']['forecastday']:
    for hour in time['hour']:
        if hour['temp_f'] > 85:
            x = hour['time']
            hour_85.append(x)
            if len(hour_85)> max_len:
                max_len = len(hour_85)
    print(round(max_value/24 * 100,1),"% of the time is the temperature above 85 °F.")

    # be careful print's indent here, should be aligned with the 2nd for!!


# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[ ]:


# https://www.weatherapi.com/pricing.aspx
# It will cost you 4 dollars per month with 2,000,000 Calls persmission.
# That way, if you need to use 1,500,000 API calls, then 1,500,000 API calls might cost you 3 dollars a month(?)


# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[ ]:


# A link back to their service(?)

