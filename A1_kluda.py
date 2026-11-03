skaits =0
with open("fails.log" , "r", encoding="utf-8") as f:
          for rinda in f:
             if "WARNING" in rinda:
               skaits +=1
               print (skaits) 
