def transport(warehouse, shop):
  while warehouse:
    truck = warehouse.pop()
    print(truck)
    shop.append(truck)
  print(shop)

def hello(names):
  for i in names:
    msg = 'hello,' + i + '!'
    print(msg)