ones = {0: '',1: 'One', 2: 'Two',3: 'Three',4: 'Four',5: 'Five',6: 'Six',7: 'Seven',8: 'Eight',9: 'Nine'}
tens10 = {0:"",10: 'Ten',11: 'Eleven', 12: 'Twelve',13: 'Thirteen',14: 'Fourteen',15: 'Fifteen',16: 'Sixteen',17: 'Seventeen',18: 'Eighteen',19: 'Nineteen'}
tens = {0:"",2: 'Twenty',3: 'Thirty',4: 'Forty',5: 'Fifty',6: 'Sixty',7: 'Seventy',8: 'Eighty',9: 'Ninety'}
no=int(input("Enter a no"))
if no>9999999:
	while(no>10000000):
		print("Enter integer Less Than One Crore")
		no=int(input("Enter a no"))
o=int(str(no)[-1])

if no>9:
	if no%100>19:t=int(str(no)[-2])
	else: t=int(str(no)[-2])*10+o
if no>=100:h=int(str(no)[-3])
if no>=1000:th=int(str(no)[-4])
if no>=10000:th=int(str(no)[-5])*10+int(str(no)[-4])
if no>=100000:l=int(str(no)[-6])
if no>=1000000:l=int(str(no)[-7])*10+int(str(no)[-6])
tp=""
hp=""
thp=""
tthp=""
lp=""
if no%100<10:tp=ones[o]
if no%100>9 and no%100<20:tp=tens10[t]
if no%100>19:tp=tens[t]+" "+ones[o]
if no>99:
	hp=ones[h]
	if h!=0:hp+=" Hundred "
if no>999:
	if th<10:thp=ones[th]
	if th>9 and th<20: thp=tens10[th]
	if th>19:thp=tens[th//10]+" "+ones[th%10]
	if th!=0: thp+=" Thousand "
if no>99999:
	if l<10:lp=ones[l]
	if l>9 and l<20: lp=tens10[l]
	if l>19:lp=tens[l//10]+" "+ones[l%10]
	if l!=0: lp+=" Lakhs "
res=lp+tthp+thp+hp+tp
if no<10:res=ones[o]
print("IN words::  ",res)
