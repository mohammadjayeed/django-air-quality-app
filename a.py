air_description = {

'green' : ['good', '0 to 50',  'Air quality is satisfactory, and air pollution poses little or no risk'],
'yellow': ['moderate', '51 to 100','Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution'],




}

for key,value in air_description.items():
     print(key)
     print(value[0] + " "+ value [1] + " "+value [2])