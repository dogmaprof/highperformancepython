o = [1,2,3]
oi = iter(o)

while True:
  try:
    i = oi.__next__()
    print(i)
  except StopIteration:
    break
