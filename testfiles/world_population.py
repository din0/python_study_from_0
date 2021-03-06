import json
import pygal_maps_world.maps
from country_codes import get_country_code

filename = 'population_json.json'

with open(filename) as f:
    pop_data = json.load(f)
    
cc_population = {}

for pop_dict in pop_data:
    
    if pop_dict['Year'] == 2018:
        country_name = pop_dict['Country Name']
        # country_code = pop_dict['Country Code']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        # print(country_code + ': ' + str(population))
        if code:
            cc_population[code] = population

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2018'
# wm.add('2010', cc_population)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_2010.svg')