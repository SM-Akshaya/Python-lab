T1=(19,'python',27.2,'program')
T2=(45,'P')
T3=('Elementsoftuple')
T6=(8,19,2,27,46)
print("The elements of Tulpe 1 are:",T1)
print("The elements of Tulpe 2 are:",T2)
print("1.Datatype\n2.Length\n3.Indexing\n4.Unpacking\n5.Concatenation\n6.Reomve\n7.Exclude characters\n8.Reversing\n9.Fetching elements\n10.Fetching portion\n11.Repeating\n12.Maximum\n13.Minimum\n14.Sum\n15.Sort\n16.Reverse sort\n17.Repeat the elements\n18.Display last element\n19.Immutable sequence")
n=int(input("Enter a number:"))
if(n==1):
  print("The data type is:",type(T1))
elif(n==2):
  print("The length of T1 is:",len(T1))
elif(n==3):
  print("The indexed element is:",T1[1])
elif(n==4):
  a,b,c,d=T1
  print("After unpacking the elements:",T1)
elif(n==5):
  T4=T1+T2
  print("After concatenation the elements are:",T4)
elif(n==6):
  print("After removing 1st element:",T3[1:])
elif(n==7):
  print("Printing all characters except last 5 characters:",T3[:-5])
elif(n==8):
  print("Reversing the elements in Tuple 3:",T3[::-1])
elif(n==9):
  print("Fetching elements from 4 to 8 :",T3[4:8])
elif(n==10):
  print("Fetching a portion of an element :",T1[1][4:9])
elif(n==11):
  T5=T1*3
  print("Repeating the elements in tuple :",T5)
elif(n==12):
  print("The maximum of Tuple6 is :",max(T6))
elif(n==13):
  print("The manimum of Tuple6 is :",min(T6))
elif(n==14):
  print("The sum of elements Tuple6 is :",sum(T6))
elif(n==15):
  print("T6 in sorted order :",sorted(T6))
elif(n==16):
  print("T6 in reverse sorted order :",sorted(T6,reverse=True))
elif(n==17):
  r=str(input("enter the tuple to be repeated : "))
  rn=int(input("enter no of times the tuple to be repeated : "))
  if(r=='T1'):
    print("tuple1 repeatation : ",T1*rn)
  else:
    print("tuple2 repeatation : ",T2*rn)
elif(n==18):
  print("last element of tuple1 : ",T1[-1])
elif(n==19):
  strv="python programming"
  print("datatype of strv is : ",type(strv))
  t1=tuple(strv)
  print("converted into immutable sequence of elements : ",type(t1))
else:
  print("Invalid number")
