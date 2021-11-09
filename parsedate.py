from datetime import datetime
import pickle

def parse_date(dt):
	return(datetime.strptime(dt, 'camera_%Y-%m-%dT%H_%M_%S.avi'))


with open('C:\\Users\\Anna\\aws\\video_N.log') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

N={}
N_offset={}

for line in lines:
	s=line.split('\t')
	if (len(s)>2):
		tmp=[parse_date(s[1]),parse_date(s[2])]
	else:
		tmp=[parse_date(s[1])]
	N[s[0]]=tmp

with open('N_starttime.pickle', 'wb') as handle:
	pickle.dump(N, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('C:\\Users\\Anna\\aws\\video_C.log') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

C={}
C_offset={}

for line in lines:
	s=line.split('\t')
	if (len(s)>2):
		tmp=[parse_date(s[1]),parse_date(s[2])]
	else:
		tmp=[parse_date(s[1])]
	C[s[0]]=tmp

print(C)
print(N)

with open('C_starttime.pickle', 'wb') as handle:
	pickle.dump(C, handle, protocol=pickle.HIGHEST_PROTOCOL)