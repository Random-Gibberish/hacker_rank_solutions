# Replace all ______ with rjust, ljust or center.
import math as m
t = int(input())    # This must be an odd number
c = 'H'

# The following prints the Hacker Rank logo
# Top Cone
for i in range(t):
    print((c*i).rjust(t-1, ' ') + c + (c*i).ljust(t-1, ' '))

# Top Pillars
for i in range(t+1):
    print(' ' * m.floor(t/2) + (c*t).ljust(t*2) + (c*t).rjust(t*3))

# Middle Belt
for i in range((t+1)//2):
    print((c*t*5).center(t*6))

# Bottom Pillars
for i in range(t+1):
    print(' ' * m.floor(t/2) + (c*t).ljust(t*2) + (c*t).rjust(t*3))

# Bottom Cone
for i in range(t):
    print(((c*(t-i-1)).rjust(t) + c + (c*(t-i-1)).ljust(t)).rjust(t*6))
