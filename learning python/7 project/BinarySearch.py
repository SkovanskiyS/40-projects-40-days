list_ = sorted([5, 8, 9, 1, 23, 7, 3, 0, 15])
user_number = 23
first = list_[0]
last = list_[-1]
middle = list_[(len(list_)//2)-1]
print(list_)
print(first)
print(last)
print(middle)

answer = 0

while first<=last:
    if middle==user_number:
        answer = middle
    elif middle<user_number:
        first=middle+1
    else:
        last = middle-1





