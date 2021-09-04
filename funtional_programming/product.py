products=[{"p_name":"complan","mrp":230,"avl_qty":50},
        {"p_name":"horlicks","mrp":250,"avl_qty":10},
        {"p_name":"bournvita","mrp":200,"avl_qty":0},
        {"p_name":"nutricharge","mrp":200,"avl_qty":100},
        {"p_name":"mylo","mrp":100,"avl_qty":0}
          ]
#print all product name in the shop
p_name=list(map(lambda product:product["p_name"],products))
print(p_name)
#print all products available in the shop
avialable_product=list(filter(lambda item:item["avl_qty"]>0,products))
print(avialable_product)
#print out of stock items in the shop
out_of_stock=list(filter(lambda item:item["avl_qty"]==0,products))
print(out_of_stock)
#costly product
costly_product=max(list(map(lambda item:item["mrp"],products)))
print(costly_product)
product=list(filter(lambda item:item["mrp"]==costly_product,products))
print(product)
#minimum cost product (1st method)
minimum_cost=min(list(map(lambda item:item["mrp"],products)))
print(minimum_cost)
minimum_cost_product=list(filter(lambda item:item["mrp"]==minimum_cost,products))
print(minimum_cost_product)
#minimum cost product (2st method)
minimum_cost_product=list(filter(lambda item:item["mrp"]==min(list(map(lambda item:item["mrp"],products))),products))
print(minimum_cost_product)

