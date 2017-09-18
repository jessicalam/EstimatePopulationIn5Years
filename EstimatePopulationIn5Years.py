#This program is supposed to output the estimated population for the next 5 years. Using the given inputs which was the current population and the days in years.
#This program was written by Jessica Lam and Kevin Kye.
#Date Completed: Sepetember 21, 2017

import math
#assumptions given in instructions
current_population = 312032486
one_year= 365
#number of years specified in document
years=1
years_specified= 5

#rates in seconds
birth_rate= 7
death_rate= 13
new_immigrant_rate=45
#initializing these values
one_day=24
one_hour=60
one_minute= 60

#rates in minute
birth_rate_minute= float(one_minute/birth_rate)
death_rate_minute= float(one_minute/death_rate)
immigrant_rate_minute= float(one_minute/new_immigrant_rate)

#rates in an hour
birth_rate_hour=float(one_hour*birth_rate_minute)
death_rate_hour=float(one_hour*death_rate_minute)
immigrant_rate_hour=float(one_hour*immigrant_rate_minute)

#rates in a day
birth_rate_day=float(one_day*birth_rate_hour)
death_rate_day=float(one_day*death_rate_hour)
immigrant_rate_day=float(one_day*immigrant_rate_hour)

#rate in a year
number_of_births=float(one_year*birth_rate_day)
number_of_deaths=float(one_year*death_rate_day)
number_of_immigrants=float(one_year*immigrant_rate_day)

#interates through the 5 years using the estimated population for each year and re-assigning it as the current population.
for years in range(1,years_specified+1):
  estimated_population=float(current_population + number_of_births - number_of_deaths + number_of_immigrants )
  current_population=float(estimated_population)
  estimated_per_year=int(estimated_population)

  #checks if it is the first year to change the word year to a years
  if years == 1:
    print("Estimated population for the next", years, "year:", estimated_per_year)
  if years !=1:
    print("Estimated population for the next", years, "years:", estimated_per_year)
