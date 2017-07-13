print('Time for lunch!')

breadslices = 10
peanutbutter = 100
jelly = 100
sandwich = 0

while breadslices > 0:
  print("It's peanutbutter jelly time!")
  breadslices = breadslices - 2
  jelly -= 5
  peanutbutter -= 5
  sandwich += 1

print('I made %s sandwiches' % (sandwich))
print('I have %dg of peanutbutter and %dg of jelly left over' % (peanutbutter, jelly))
print('Delicious.')
