S1={8,41,19,27.2,"set",(1,2,3)}
S2=set([8,31,13,7,90])
print("\n1.Print set elemenets\n2.Datatype\n3.Add an element to S1\n4.Update elements\n5.Discard\n6.Remove\n7.Clear s1\n8.Union of S1 and S2\n9.Intersection of S1 and S2\n10.Difference of S1 and S2\n11.Symmetric difference of S1 and S2\n12.Check S2 is disjoint of S1\n13.Check S2 is subset of S1\n14.Pop operation\n15.Copy\n16.Display elements in S1 using for loop\n17.Display maximum value\n18.Display minimum value\n19.Sum of elements in set\n20.Sort operation\n21.Length of the set")
n=int(input("Enter your choice : "))
if(n==1):
  print("S1 elements : ",S1)
  print("S2 elements : ",S2)
elif(n==2):
  print("Datatype of S1 : ",type(S1))
  print("Datatype of S2 : ",type(S2))
elif(n==3):
  e=str(input("Enter a string element to be added to the S1 : "))
  S1.add(e)
  print(S1)
elif(n==4):
  S2.update([11,22,33,44,55])
  print("Updated elements in S2 : ",S2)
elif(n==5):
  S2.discard(2)
  print("2 in S2 is discarded",S2)
elif(n==6):
  S2.remove(90)
  print("element 90 is removed from S2",S2)
elif(n==7):
  S1.clear()
  print("S1 is cleared : ",S1)
elif(n==8):
  print("Union of S1 and S2 : ",S1|S2)
elif(n==9):
  print("Intersection of S1 and S2 : ",S1&S2)
elif(n==10):
  print("Difference of S1 and S2 : ",S1-S2)
elif(n==11):
  print("Symmetric difference of S1 and S2 : ",S1^S2)
elif(n==12):
  print("Is S2 disjoint of S1 ? :  ",S1.isdisjoint(S2))
elif(n==13):
  print("Is S2 is superset of S1 ? : ",S1.issuperset(S2))
elif(n==14):
  v=S1.pop()
  print("Poped element from s1 : ",v)
  print("S1 after poping a random element : ",S1)
elif(n==15):
  S3=S1.copy()
  print("S1 is copied to S3 : ",S3)
elif(n==16):
  print("Elements in S1 : ")
  for i in set(S1):
    print(i)
elif(n==17):
  print("Maximum value in S2 is : ",max(S2))
elif(n==18):
  print("Minimum value in S2 is : ",min(S2))
elif(n==19):
  print("Sum of elements in S2 : ",sum(S2))
elif(n==20):
  print("Elements of S2 is sorted : ",sorted(S2))
elif(n==21):
  print("Length of S1 is : ",len(S1))
