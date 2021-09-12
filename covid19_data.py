#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Vaccination data for Covid-19, Norway, 3 weeks in August/September")

file = "src/2021-09-12.antall-vaksinasjoner-etter-sykdom-fordelt-på-dag-siste-tre-uker.csv"
vaccinations = pd.read_csv(file,skiprows=[0], sep=';')

# Changing the name of the unnamed column
vaccinations.rename(columns={vaccinations.keys()[0]:'Date'}, inplace=True)

# Information from FHI
info_from_FHI = "Statistikken viser antall vaksinasjoner mot covid-19 registrert i Nasjonalt vaksinasjonsregister SYSVAK. For å unngå identifisering av enkeltpersoner vises ikke tall mellom null og fem."
print(info_from_FHI)

sum = vaccinations['Covid-19'].sum()
print("\nTotal number of vaccinations in the 3 week period:", sum)

# Plotting the data
vaccinations.plot(x='Date', title='Number of Covid-19 vaccinations, by date', kind='bar')
plt.show()
