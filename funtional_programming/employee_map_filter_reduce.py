employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
#printing employee name
e_name=list(map(lambda employee:employee["e_name"],employees))
print(e_name)

#printing employee name in uppercase
e_name_upper=list(map(lambda employee:employee["e_name"].upper(),employees))
print(e_name_upper)
#print department=developer
developer=list(filter(lambda employee:employee["department"]=="developer",employees))
print(developer)
d_e_name=list(map(lambda employee:employee["e_name"],developer))
print(d_e_name)

salaries=list(map(lambda emp:emp["salary"],employees))
print(salaries)

salaries_sum=sum(list(map(lambda emp:emp["salary"],employees)))
print(salaries_sum)

