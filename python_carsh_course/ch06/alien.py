alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


new_points = alien_0['points']
print("you just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['points']
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("original x-position :" + str(alien_2['x_position']))
alien_2['speed'] = 'fast'
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_2['x_position'] += x_increment
print("new x-position :" + str(alien_2['x_position']))


