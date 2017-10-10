team = 'New England Patriots'
index = team.find('a')
print(index)

print(team.find('a', 10)) 

name = 'bob'
print(name.find('b', 1, 2))

response = request.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)