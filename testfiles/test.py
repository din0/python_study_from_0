#import func
#import fibo

from fibo import fib

from func import hello, transport

names = ['jim','tom','lisa']
hello(names)

warehouse = ['apple','orange','banana']
shop = []
transport(warehouse, shop)

fib(1000)