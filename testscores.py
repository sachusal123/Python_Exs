score_array=[]
i=d=c=0
score_sum=0
#Enter scores
while i<10:
    score=int(input("Enter Score :"))
    score_array.append(score)
    score_sum=score_sum+score
    i=i+1

print("Scores are:=",score_array)

#warning message

while i<10:
   if score_array[i]>100:
    #program to display warning a message
      import warnings

      # displaying the warning message
      warnings.warn('A value over 100 has been entered...!!')
   i=i+1

#find average of all scores

score_average=score_sum//10

i=1
small_score=score_array[0]
large_score=score_array[0]

#finding large&small scores

while i<10:
    #find large score
    if large_score<score_array[i]:
        c=i
        large_score=score_array[i]
    #find small score
    if small_score>score_array[i]:
        d=i
        small_score=score_array[i]

    i=i+1


score_array.pop(c)
length_array=len(score_array)
second_large_score=score_array[0] 
i=1  
#find second largest score
while i<length_array:
    if second_large_score<score_array[i]:
        c=i
        second_large_score=score_array[i]
    i=i+1

score_array.append(large_score)

i=1
small_score=score_array[0]

#we again find small score bcz positions were changed 
#when we appending large_score in to the array

while i<10:

    if small_score>score_array[i]:
        d=i
        small_score=score_array[i]
    i=i+1


score_array.pop(d)
length2_array=len(score_array)
second_small_score=score_array[0]
i=1
c=0
#finding second smallest score
while i<length2_array:
    if second_small_score>score_array[i]:
        c=i
        second_small_score=score_array[i]
    i=i+1
score_array.pop(c)

print("Highest Score=",large_score,"\n Lowest Score=",small_score)
print("Average of the test scores are:-",score_average)
print("Second Largest Score=",second_large_score)
print("Two lowest Scores are=",small_score,second_small_score)
print("Scores after dropping two lowest scores",score_array)

length3_array=len(score_array)
i=0
score_average2=score_sum2= 0

#find average of scores after dropping two lowest scores

while i<length3_array:
    score_sum2= score_sum2 + score_array[i]
    i=i+1
score_average2=score_sum2//length3_array

print("Avearge of scores after dropping two lowest scores=",score_average2)
