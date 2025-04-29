# create a nested dictionary with 3 
# fields of 3 students
data = {
   "principal":"apj",
   "Student":[
      {
         "Name":"Bobby",
         "Id":1,
         "Age":20
      },
      {
         "Name":"Tom",
         "Id":2,
         "Age":30
      },
      {
         "Name":"Harry",
         "Id":3,
         "Age":24
      }
   ],
   "testin":{
      "hello":"abc"
   }
}

# iterate all the nested dictionaries with
# both keys and values
# for key,value in data['testin'].items():
#     # display
#     print(key,value)

for i in data['Student']:
    if i['Age']>20:
        print(i['Name'])

print(data['Student'][0])
