with open("story.txt","r") as s:
    story = s.read()
target_start = "<"
target_end = ">"
target_found=-1
words = []
for i,char in enumerate(story):
    if char==target_start and target_found==-1:
        target_found=i

    if char==target_end and target_found!=1:
        words.append(story[target_found:i+1])
        target_found=-1
answers={}
for word in words:
    ans = input("Enter word for"+ word+" : ")
    answers[word] = ans
print(answers)
for adjective in answers:
    story=story.replace(adjective,answers[adjective])
print(story)







