guitars=[
    {'model':'yamaha f310','price':8400},
    {'model':'faith naptune','price':50000},
    {'model':'faith apollo venus','price':35000},
    {'model':'taylor','price':450000}
 ]
print(sorted (guitars, key = lambda f : f['price']))
print(sorted (guitars, key = lambda d : d['price'],reverse=True))