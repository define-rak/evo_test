# coding=utf-8

import random

cube = []
N = 10

for i in xrange(0, N):
	cube.append([])
	for j in xrange(0, N):
		cube[i].append([])
		for k in xrange(0, N):
			cube[i][j].append(random.randint(0, 9))

print cube

# Row and column on horizontal plane and column on vertical plane

sum_ijk = 0

# Biggest row on horizontal plane
max_rh = 0
max_rh_i = -1
max_rh_k = -1

for i in xrange(0, N):
	for k in xrange(0, N):
		rh = 0
		for j in xrange(0, N):
			rh += cube[i][j][k]

		if rh > max_rh:
			max_rh = rh
			max_rh_i = i
			max_rh_k = k

# Biggest column on horizontal plane
max_ch = 0
max_ch_j = -1
max_ch_k = -1

for j in xrange(0, N):
	for k in xrange(0, N):
		ch = 0
		for i in xrange(0, N):
			ch += cube[i][j][k]

		if ch > max_ch:
			max_ch = ch
			max_ch_j = j
			max_ch_k = k

# Biggest column on vertical plane
max_cv = 0
max_cv_i = -1
max_cv_j = -1

for i in xrange(0, N):
	for j in xrange(0, N):
		cv = 0
		for i in xrange(0, N):
			cv += cube[i][j][k]

		if cv > max_cv:
			max_cv = cv
			max_cv_i = i
			max_cv_j = j

sum_ijk = max_rh + max_ch + max_cv
print 'Max sum =', sum_ijk

rh = 'i = '+ str(max_rh_i) + ', k = ' + str(max_rh_k) + ': '
for j in xrange(0, N):
	rh += str(cube[max_rh_i][j][max_rh_k]) + ' '

ch = 'j = '+ str(max_ch_j) + ', k = ' + str(max_ch_k) + ': '
for i in xrange(0, N):
	ch += str(cube[i][max_ch_j][max_ch_k]) + ' '

cv = 'i = '+ str(max_cv_i) + ', j = ' + str(max_cv_j) + ': '
for k in xrange(0, N):
	cv += str(cube[max_cv_i][max_cv_j][k]) + ' '

print rh
print ch
print cv




