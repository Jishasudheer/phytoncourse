employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
# for employee in employees:
#     if(employee["department"]=="developer"):
#         print("developer",employee["department"])
# total=0
# for employee in employees:
#     total+=employee["salary"]
# print(total)
salary=sum(list(map(lambda emp:emp["salary"],employees)))
print(salary)

develpoers=list(filter(lambda emp:emp["department"]=="developer",employees))
print(develpoers)
develpoers_name=list(map(lambda developer:developer["e_name"],develpoers))
print(develpoers_name)

