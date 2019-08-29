alien_0 = { 'colour': 'green',  'points':  5 }
alien_1 = { 'colour': 'yellow', 'points': 10 }
alien_2 = { 'colour': 'red',    'points': 15 }

aliens = []

for alien in range(30):
    new_alien = { 'colour': 'green', 'points': 5, 'speed': 'slow' }
    aliens.append (new_alien)

for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed']  = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed']  = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print (alien)
print ("...")

print ("Total number of aliens: " + str (len (aliens)))