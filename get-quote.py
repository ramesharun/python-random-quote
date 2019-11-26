import random;

def primary():
   print("Keep it logically awesome.")
   f=open("quotes.txt", "a+")
   for i in range(2):
     f.write("Appended line %d\r\n" % (i+1))
   f.close()   
   f = open("quotes.txt","r")
   quotes = f.readlines()
   for x in quotes:
     print x,
   f.close()
   
   #last=len(quotes)-1
   #rnd =random.randint(0,last) 
   #for x in range(rnd): 
     #print x
     #print quotes[x],


if __name__== "__main__":
  primary()
