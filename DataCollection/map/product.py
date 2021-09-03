
products=[{"p_name":"complan","mrp":230,"avl_qty":50},
        {"p_name":"horlicks","mrp":250,"avl_qty":10},
        {"p_name":"bournvita","mrp":200,"avl_qty":0},
        {"p_name":"nutricharge","mrp":200,"avl_qty":100},
        {"p_name":"mylo","mrp":100,"avl_qty":0}
          ]
#print all products name
product_name=list(map(lambda item:item["p_name"],products))
print(product_name)
#available products
ava_products=list(filter(lambda item:item["avl_qty"]>0,products))
print(ava_products)
#print out of stock
out_stock=list(filter(lambda item:item["avl_qty"]==0,products))
print(out_stock)
#print costly product
prices=list(map(lambda product:product["mrp"],products))
print(max(prices))

