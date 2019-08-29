dead_guest = 'Alan Turing'
guests  = ['Michelle Pfeiffer', 'Stephen Fry', 'Jessica Green', dead_guest]
message = "I'm formally inviting, "
suffix  = ", to dinner"

print (message + guests[0] + suffix)
print (message + guests[1] + suffix)
print (message + guests[2] + suffix)
print (message + guests[3] + suffix)

print ("It seems that " + guests[-1] + " cannot make it on account of being slightly dead.")

guests.remove(dead_guest)

print (guests)

print (message + guests[0] + suffix)
print (message + guests[1] + suffix)
print (message + guests[2] + suffix)
