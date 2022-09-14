print (' PLEASE THINK OF A NUMBER BETWEEN 0 AND 100 ')
low = 0
high = 100
medium = (high + low)//2
state = True
while state :
 print ('is your secret number is '+ str(medium))
 guess = input("Enter 'h'to indicate the guess is too high . Enter 'l'to indicate the guess is too low . Enter 'c'to indicate the guess is Right .")
 if guess == 'c':   
     print ('Game over . your secret number was'+ str(medium))
     state = False
     break
 elif guess == 'h':
    high = medium
    medium = (high + low)//2 
    
 elif guess == 'l':
   low = medium
   medium = (high + low)//2
   
else :
 print ('sorry didnt understand your input')
 

