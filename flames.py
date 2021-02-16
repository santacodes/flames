yn=str(input('Type in your name: '))
pn=str(input('Type in your partner\'s name: '))

yn=yn.lower()
pn=pn.lower()

yn_list = list(yn)
pn_list = list(pn)

first_list = []
second_list = []
flames = ['F','L','A','M','E','S']
flames_dict = {'F':'Friends','L':'Love','A':'Affection','M':'Marriage','E':'Enemy','S':'Siblings'}

for i in yn_list:
    if i not in pn_list:
        first_list.append(i)
    else:
        continue

print(first_list)

for j in pn_list:
    if j not in yn_list:
        second_list.append(j)

print(second_list)        

final_list = first_list + second_list

print(final_list)
        
n = len(final_list)

number = 0

while len(flames)>1:
    if len(flames)>len(final_list):
        flames.pop(n-1)
    else: 
        number = len(final_list)%len(flames) 
        flames.pop(number-1)    
print(flames)
print('Your Relationship Status with your partner is:',flames_dict[flames[0]])