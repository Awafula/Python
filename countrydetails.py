#This program details the country details of any country in the whole world. 

from countryinfo import CountryInfo

#user input for country name

count = input("Enter your country: ")
country = CountryInfo(count)

print("capital is: ", country.capital())
print("Currencies is: ", country.currencies())
print("Language is: ", country.languages())
print("Borders are: ", country.borders())
print("other names are: ", country.alt_spellings())

#end 
