fTimeH=int(input("Add the hour! "))
fTimeM=int(input("Add the minute! "))
fTimeS=int(input("Add the second! "))

sTimeH=int(input("Add the hour! "))
sTimeM=int(input("Add the minute! "))
sTimeS=int(input("Add the second! "))

sumF=fTimeS+(fTimeM*60)+(fTimeH*60*60)
sumS=sTimeS+(sTimeM*60)+(sTimeH*60*60)

diff=sumF-sumS

print("The difference between these two timelines: " , abs(diff))
