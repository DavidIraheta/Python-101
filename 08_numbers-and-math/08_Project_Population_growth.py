population = 380123456
seconds_in_3_years = (94608000)
born_in_3_years = (seconds_in_3_years / 6)
dies_in_3_years = (seconds_in_3_years / 12)
immigrates_in_3_years = (seconds_in_3_years / 40)
population_after_3_years = population - dies_in_3_years + born_in_3_years + immigrates_in_3_years
print(population_after_3_years)

