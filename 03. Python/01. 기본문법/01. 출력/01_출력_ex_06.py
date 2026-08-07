import math

h = 170
w = 68.6345

#h = str(h)
#w = int(w * 10)/10
#w = str(w)

#print("My height is", h,"cm.\n" "cm and weight is", int(w * 10)/10, "kg")
#print("My height is", h + "cm.\n" "cm and weight is", w + "kg")

print("My height is", h, "cm.")
print("My weight is", w, "kg.")
print()
print("My height is %dcm." % h)
print("My weight is %.1fcm." % w)
print()
print("My height is {}cm." .format(h))
print("My weight is {:.1f}kg." .format(w))