dead_guest = 'Alan Turing'
guests  = ['Michelle Pfeiffer', 'Stephen Fry', 'Jessica Green', dead_guest]
message = "I'm formally inviting, "
suffix  = ", to dinner"

print (message + guests[0] + suffix)
print (message + guests[1] + suffix)
print (message + guests[2] + suffix)
print (message + guests[3] + suffix)

print ("\nIt seems that " + guests[-1] + " cannot make it on account of being slightly dead.\n")

guests.remove(dead_guest)

print (guests)

print (message + guests[0] + suffix)
print (message + guests[1] + suffix)
print (message + guests[2] + suffix)

print ("\nOh look, a bigger dinner table has been found!\n")

guests.insert (0, 'Andrew McCarthy')
guests.insert (3, 'Molly Ringwald')
guests.append ('James Spader')

print (message + guests[0] + suffix)
print (message + guests[1] + suffix)
print (message + guests[2] + suffix)
print (message + guests[3] + suffix)
print (message + guests[4] + suffix)
print (message + guests[5] + suffix)
