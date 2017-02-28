import json

#python dict
data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
print data

#python dict => json str
json_str = json.dumps(data)  
print json_str

#json str => json structure
json_structure = json.loads(json_str)

print 'name',json_structure['name']
print 'share',json_structure['shares']
print 'price',json_structure['price']

#--------------------------------------

## Writing JSON data
#with open('test_json.json', 'w') as f:
#  json.dump(json_structure, f)

# Reading data back
with open('test_json.json', 'r') as f:
	data = json.load(f)
	print data['price']

