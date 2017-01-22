file = open('rosalind_iprb.txt', 'r')
rawdata = file.readlines()
data = rawdata[0].split(' ')
dict = {'k':{'number': 0, 'genotype': 'AA'},
        'm':{'number': 0, 'genotype': 'Aa'},
        'n':{'number': 0, 'genotype': 'aa'},}
for i in dict:
    if i == 'k':
        dict['k']['number'] = int(data[0])
    elif i == 'm':
        dict['m']['number'] = int(data[1])
    elif i == 'n':
        dict['n']['number'] = int(data[2])
#I opened the file, split up the numbers within the sole item in the rawdata list
#I made a dictionary template that will contain the data that I will manipulate
#Then I assigned the number to the dictionary keys--i.e. k, m, and n--by via the
#list indexes of 'data'. I also made sure to convert them from string and into
#integers for downsteam calculations


totalpop = 0
for i in dict:
    totalpop += dict[i]['number']
Pr_k_k = (dict['k']['number']/totalpop)*((dict['k']['number']-1)/(totalpop-1))
Pr_k_m = (dict['k']['number']/totalpop)*((dict['m']['number'])/(totalpop-1))+(dict['m']['number']/totalpop)*((dict['k']['number'])/(totalpop-1))
Pr_k_n = (dict['k']['number']/totalpop)*((dict['n']['number'])/(totalpop-1)) + (dict['n']['number']/totalpop)*((dict['k']['number'])/(totalpop-1))
Pr_m_m = (dict['m']['number']/totalpop)*((dict['m']['number']-1)/(totalpop-1))
Pr_m_n = (dict['m']['number']/totalpop)*((dict['n']['number'])/(totalpop-1)) + (dict['n']['number']/totalpop)*((dict['m']['number'])/(totalpop-1))
Pr_n_n = (dict['n']['number']/totalpop)*((dict['n']['number']-1)/(totalpop-1))
#this step is used to crunch the probability of matches


#if 'A' in the genotype combinations
from collections import defaultdict
crossdict = defaultdict(list)
keylist= []
for i in dict:
    Y = i
    geno1 = list(dict[i]['genotype'])
    for i in dict:
        W = i
        geno2 = list(dict[i]['genotype'])
        for i in geno1:
            X = i
            for i in geno2:
                insert = X + i
                Z = Y+ W
                if Y==W:                #for n and n crosses and etc
                    crossdict[Z].append(insert)
                    if Z not in keylist:
                        keylist.append(Z)
                elif Z and Z[::-1] not in crossdict:
                    crossdict[Z].append(insert)
                    if Z not in keylist:
                        keylist.append(Z)
print(crossdict)
print(keylist)

crosscalc = {}
for i in crossdict:
    Name = i
    crosslist = crossdict[i]
    crosscount = 0
    listtotal = 0
    for i in crosslist:
        listtotal += 1
        offspring = i
        if 'A' in offspring:
            crosscount +=1
    crosscalc[Name] = crosscount/listtotal
print(crosscalc)


for i in keylist:
    crossdict[i]
kk=0
km=0
kn=0
mm=0
mn=0
nn=0
for i in keylist:
    name = i
    value = crosscalc[i]
    if 'kk' == name:
        kk = value
        print('kk '+str(kk))
for i in keylist:
    name = i
    value = crosscalc[i]
    if 'kn'==name or 'nk' == name:
        kn = value
        print('kn '+str(kn))
for i in keylist:
    name = i
    value = crosscalc[i]
    if 'km' ==name or 'mk' == name:
        km = value
        print('km '+str(km))
for i in keylist:
    name = i
    value = crosscalc[i]
    if 'mm' == name:
        mm = value
        print('mm '+str(mm))
for i in keylist:
    name = i
    value = crosscalc[i]
    if 'mn'==name or 'nm' == name:
        mn = value
        print('mn '+str(mn))
for i in keylist:
    name = i
    value = crosscalc[i]
    if 'nn' == name:
        nn = value
        print('nn '+str(nn))

final = Pr_k_k*kk + Pr_k_n*kn + Pr_k_m*km + Pr_m_m*mm + Pr_m_n*mn
print(final)
