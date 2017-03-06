electronic = []
f = open('msd_genre_dataset.txt','r')
for line in f.xreadlines():
	info = line.split(',', 2)
	if info[0] == 'dance and electronica':
		electronic.append(info[1])
f.close()

f = open('electronic_tracks.txt','w')
for item in electronic:
	f.write("%s\n" % item)
f.close()