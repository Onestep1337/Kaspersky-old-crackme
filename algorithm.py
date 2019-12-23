def check_nums1(a):
	return bool((a[0] != a[5]) and (a[5] != a[10]) and (a[10] != a[15]))

def check_nums2(a):
	return bool((a[1] != a[6]) and (a[6] != a[11]) and (a[11] != a[16]))

def check_nums3(a):
	return bool((a[2] != a[7]) and (a[7] != a[12]) and (a[12] != a[17]))

def check_nums4(a):
	return bool((a[3] != a[8]) and (a[8] != a[13]) and (a[13] != a[18]))

#for example
text = "1111-2222-3333-4444"

s1 = 0
s2 = 0
s3 = 0
s4 = 0

for i in range(4):
	if i == 3:
		s1 += (ord(text[i])*4)
		break
	s1 += ord(text[i])
s1 -=0x150

for i in range(5,9):
	if i == 8:
		s2 += (ord(text[i])*4)
		break
	s2 += ord(text[i])
s2 -=0x150

for i in range(10,14):
	if i == 13:
		s3 += (ord(text[i])*4)
		break
	s3 += ord(text[i])
s3 -=0x150

for i in range(15,19):
	if i == 18:
		s4 += (ord(text[i])*4)
		break
	s4 += ord(text[i])
s4 -=0x150

s = s1+s2+s3+s4

s = s >> 2

if ((s1 == s or s2 == s or s3 == s or s4 == s) and (check_nums1(text)) and (check_nums2(text)) and (check_nums3(text)) and (check_nums4(text))):
	print("Password is correct")
else:
	print("Password is incorrect")