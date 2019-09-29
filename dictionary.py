states={'MH':'Maharashtra','NY':'New York','TS':'Telangana'}
print(states['MH'])

print(states.get('MH','Not Found'))

print(states.get('GH','Not Found'))

print(states.keys())

print(states.values())

#list in dict
animal={
	'cat':["meow","purr"],
	'dog':["woof","bark"]
}

print(animal['cat'][0])
#dict in list
abhi={'name':'abhi','age':'21'}
vaibhav={'name':'vaibhav','age':'21'}
pranay={'name':'pranay','age':'21'}

ls=[abhi,vaibhav,pranay]
for people in ls:
	print(people['age'])