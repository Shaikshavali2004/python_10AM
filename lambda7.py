employees=[
{"eid":1,"ename":"Shana","gender":"Female"},
{"eid":2,"ename":"Sascha","gender":"Male"},
{"eid":3,"ename":"Mayer","gender":"Male"},
{"eid":4,"ename":"Stepha","gender":"Female"},
{"eid":5,"ename":"Pablo","gender":"Male"},
{"eid":6,"ename":"Mallorie","gender":"Female"},
{"eid":7,"ename":"Carol-jean","gender":"Female"},
{"eid":8,"ename":"Arron","gender":"Male"},
{"eid":9,"ename":"Conrade","gender":"Male"},
{"eid":10,"ename":"Dusty","gender":"Female"},
{"eid":11,"ename":"Winni","gender":"Female"},
{"eid":12,"ename":"Delaney","gender":"Male"},
{"eid":13,"ename":"Vlad","gender":"Male"},
{"eid":14,"ename":"Jodie","gender":"Male"},
{"eid":15,"ename":"Emmanuel","gender":"Male"},
{"eid":16,"ename":"Norene","gender":"Female"},
{"eid":17,"ename":"Johny","gender":"Male"},
{"eid":18,"ename":"Fred","gender":"Female"},
{"eid":19,"ename":"Egbert","gender":"Agender"},
{"eid":20,"ename":"Fernande","gender":"Non-binary"},
{"eid":21,"ename":"Simone","gender":"Non-binary"},
{"eid":22,"ename":"Courtnay","gender":"Agender"},
{"eid":23,"ename":"Iain","gender":"Male"},
{"eid":24,"ename":"Antonius","gender":"Male"},
{"eid":25,"ename":"Dav","gender":"Male"},
{"eid":26,"ename":"Bran","gender":"Male"},
{"eid":27,"ename":"Ricky","gender":"Male"},
{"eid":28,"ename":"Harrietta","gender":"Female"},
{"eid":29,"ename":"Yevette","gender":"Female"},
{"eid":30,"ename":"Mirna","gender":"Female"}
]

# def check_gender(emp):
#     return emp['gender']=='Female'

# female_emps=list(filter(check_gender,employees))

# print(len(female_emps))

print(len(list(filter(lambda emp:emp['gender']=='Female',employees))))




