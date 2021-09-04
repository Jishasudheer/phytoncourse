employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
#print employee_id
for employee in employees:
    print(employee["e_id"])

#print employee_id using map
emp_id=list(map(lambda employee:employee["e_id"],employees))
print(emp_id)

print()
#print employee names in uppercase
for employee in employees:
    print(employee["e_name"].upper())#effects all employee

#print employee names in uppercase using map
e_name=list(map(lambda emp:emp["e_name"].upper(),employees))
print(e_name)

print()
#print employee as developer
for employee in employees:
    if employee["department"]=="developer":#condition
        print(employee["e_name"])
print()
#total salary
total_salary=0
for employee in employees:
    total_salary+=employee["salary"]#reduce to one value
print(total_salary)

#print employee name starting with letter a->filter
#minimum Salary->reduce
#add bonus 5000 to all employees->map
#add bonus of 5000 to developers->filter