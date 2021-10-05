import store, product

soup = product.Product("soup", 5, category="food")
eggs = product.Product("eggs", 8, category="food")
beer = product.Product("beer", 10, category="liquor")
socks = product.Product("socks", 12, category="clothing")

sears = store.Store("Sears")

sears.add_product(soup).add_product(eggs).add_product(beer).add_product(socks)
sears.print_product_list()
sears.inflation(.50).set_clearance("food", .25)
sears.print_product_list()