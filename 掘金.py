listJson=[
   {"name":"1","value":"1-1"},
   {"name":"2","value":"2-1"},
   {"name":"3","value":"3-1"},
   {"name":"4","value":"4-1"}
   ]
 
for i,men in enumerate(listJson):
   if men["name"]=="1":
      print("此数字是1")
   elif men["name"]=="2":
      print("此数字是2")
 
   print(listJson[i]["name"])
   print(listJson[i]["value"])
 