from datetime import datetime
import datetime as dt
import pickle

def parse_date(dt):
	return(datetime.strptime(dt, 'camera_%Y-%m-%dT%H_%M_%S.avi'))


with open('C:\\Users\\Anna\\aws\\video_N.log') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]


with open('C:\\Users\\Anna\\aws\\offset_N.log') as file1:
	offset = file1.readlines()
	offset = [line.rstrip() for line in offset]


N={}
N_offset={}

for line in lines:
	s=line.split('\t')
	if (len(s)>2):
		tmp=[parse_date(s[1]),parse_date(s[2])]
	else:
		tmp=[parse_date(s[1])]
	N[s[0]]=tmp


for line in offset:
	s=line.split('\t')
	delta1=dt.timedelta(minutes=int(s[1].split(':')[0]), seconds=int(s[1].split(':')[1]))
	if (len(s)>2):
		delta2=dt.timedelta(minutes=int(s[2].split(':')[0]), seconds=int(s[2].split(':')[1]))
		tmp=[N[s[0]][0]+delta1, N[s[0]][1]+delta2]
	else:
		tmp=[N[s[0]][0]+delta1]
	N_offset[s[0]]=tmp

with open('N_starttime.pickle', 'wb') as handle:
	pickle.dump(N, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('N_endtime.pickle', 'wb') as handle:
	pickle.dump(N_offset, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('C:\\Users\\Anna\\aws\\video_C.log') as file:
	lines = file.readlines()
	lines = [line.rstrip() for line in lines]

with open('C:\\Users\\Anna\\aws\\offset_C.log') as file1:
	offset = file1.readlines()
	offset = [line.rstrip() for line in offset]



C={}
C_offset={}

for line in lines:
	s=line.split('\t')
	if (len(s)>2):
		tmp=[parse_date(s[1]),parse_date(s[2])]
	else:
		tmp=[parse_date(s[1])]
	C[s[0]]=tmp


for line in offset:
	s=line.split('\t')
	delta1=dt.timedelta(minutes=int(s[1].split(':')[0]), seconds=int(s[1].split(':')[1]))
	if (len(s)>2):
		delta2=dt.timedelta(minutes=int(s[2].split(':')[0]), seconds=int(s[2].split(':')[1]))
		tmp=[C[s[0]][0]+delta1, C[s[0]][1]+delta2]
	else:
		tmp=[C[s[0]][0]+delta1]
	C_offset[s[0]]=tmp


with open('C_endtime.pickle', 'wb') as handle:
	pickle.dump(C_offset, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(C)
print(N)
print(N_offset)
print(C_offset)

with open('C_starttime.pickle', 'wb') as handle:
	pickle.dump(C, handle, protocol=pickle.HIGHEST_PROTOCOL)