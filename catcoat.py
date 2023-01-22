'''
if Red,
will get dad's red + one of the red genes from mum
if male, only gets one from mum

Black 0.328125000
Black-Red Tortie 0.328125000
Blue 0.109375000
Blue-Cream Tortie 0.109375000
Chocolate 0.046875000
Chocolate-Red Tortie 0.046875000
Lilac 0.015625000
Lilac-Cream Tortie 0.015625000

(Too Many)
Black 0.2777777777777778
Black-Red Tortie 0.2777777777777778

(Too Little)

Blue 0.1388888888888889
Blue-Cream Tortie 0.1388888888888889

(Too Many)
Chocolate 0.05555555555555555
Chocolate-Red Tortie 0.05555555555555555

(Too Many)
Lilac 0.027777777777777776
Lilac-Cream Tortie 0.027777777777777776


---
(Too Little)
Red 0.8888888888888888

(Too many)
Cream 0.1111111111111111

Red 0.937500000 
Cream 0.062500000
---
(too little)
Cream 0.25
(too little)
Blue 0.3333333333333333
(too little)
Blue-Cream Tortie 0.16666666666666666

(Too many)
Lilac 0.16666666666666666
(too many)
Lilac-Cream Tortie 0.08333333333333333

Blue 0.375000000
Cream 0.250000000
Blue-Cream Tortie 0.187500000
Lilac 0.125000000
Lilac-Cream Tortie 0.062500000


'''

from itertools import product
from collections import Counter

'''
male_dict2 = {'Red': ['BBDDO', 'BBDdO', 'BbDDO', 'BbDdO', 'bbDDO', 'bbDdO'],
            'Black': ['BBDDo', 'BBDdo', 'BbDDo', 'BbDdo'], 
            'Cream': ['BBddO', 'BbddO', 'bbddO', 'bbddO'], 
            'Blue': ['BBddo', 'Bbddo'], 
            'Chocolate': ['bbDDo', 'bbDdo'], 
            'Lilac': ['bbddo']}

female_dict2 =  {'Red': ['BBDDOO', 'BBDdOO', 'BbDDOO', 'BbDdOO', 'bbDDOO', 'bbDdOO'],
    'Black-Red Tortie': ['BBDDOo', 'BBDdOo', 'BbDDOo', 'BbDdOo'], 
    'Black': ['BBDDoo', 'BBDdoo', 'BbDDoo', 'BbDdoo'], 
    'Cream': ['BBddOO', 'BbddOO', 'bbddOO', 'bbddOO'], 
    'Blue-Cream Tortie': ['BBddOo', 'BbddOo'], 
    'Blue': ['BBddoo', 'Bbddoo'], 
    'Chocolate-Red Tortie': ['bbDDOo', 'bbDdOo'], 
    'Chocolate': ['bbDDoo', 'bbDdoo'], 
    'Lilac-Cream Tortie': ['bbddOo'], 
    'Lilac': ['bbddoo']}
'''


def dominant(gene):
    # takes in 2char strings
    if gene.islower():
        return False
    else:
        return True


def extractor(dna):
    return dna[0:2:1], dna[2:4:1], dna[4::1]


def dna_to_colour(dna):
    b, d, o = extractor(dna)
    b_, d_, o_ = dominant(b), dominant(d), dominant(o)
    if o_:
        if len(dna) == 5:
            if d_:
                return "Red"
            else:
                return "Cream"
        elif o == "OO":
            if d_:
                return "Red"
            else:
                return "Cream"
        elif (o == "Oo") or (o == "oO"):
            if b_ and d_:
                return "Black-Red Tortie"
            elif b_ and not d_:
                return "Blue-Cream Tortie"
            elif not b_ and d_:
                return "Chocolate-Red Tortie"
            elif not b_ and not d_:
                return "Lilac-Cream Tortie"
    elif b_:
        if d_:
            return "Black"
        else:
            return "Blue"
    else:
        if d_:
            return "Chocolate"
        else:
            return "Lilac"


def generate_dict(dna_list):
    temp = {}
    for dna in dna_list:
        colour = dna_to_colour(dna)
        if colour in temp:
            old = temp.get(colour)
            old.append(dna)
            temp.update({colour: old})
        else:
            temp.update({colour: [dna]})
    return temp


def child_dna(dna_mother, dna_father, male):
    bm, dm, om, = extractor(dna_mother)
    bf, df, of, = extractor(dna_father)
    bm = list(bm)
    dm = list(dm)
    om = list(om)
    bf = list(bf)
    df = list(df)
    of = list(of)
    new_dna = []
    if not male:
        p = product(bm, bf, dm, df, om, of)
        for i in p:
            new_dna.append("".join(i))
    else:
        p = product(bm, bf, dm, df, om)
        for i in p:
            new_dna.append("".join(i))
    return new_dna


def generate_dna(mother, father):
    mother_dna = female_dict[mother]
    father_dna = male_dict[father]
    dna_outcomes = []
    for m in mother_dna:
        for f in father_dna:
            for x in [True, False]:
                dna_outcomes.extend(child_dna(m, f, x))
    return dna_outcomes


def colour_list(dna_list):
    colour_list = []
    for dna in dna_list:
        colour_list.append(dna_to_colour(dna))
    return colour_list

    
male_dna = []
for i in ["BB", "Bb", "bb"]:
    for j in ["DD", "Dd", "dd"]:
        for k in ["O", "o"]:
            male_dna.append(i + j + k)

female_dna = []
for i in ["BB", "Bb", "bb"]:
    for j in ["DD", "Dd", "dd"]:
        for k in ["OO", "Oo", "oo"]:
            female_dna.append(i + j + k)


male_dict = generate_dict(male_dna)
female_dict = generate_dict(female_dna)


mother = input()
father = input()

outcome_list = generate_dna(mother, father)
       
count_dict = Counter(colour_list(outcome_list))

x = list(count_dict.keys())
y = list(count_dict.values())

total = sum(y)
tup_list = []
for i in range(len(x)):
    tup_list.append(((y[i] / total), x[i]))
tup_list = sorted(tup_list, key=lambda x: (-x[0], x[1]))
for y, x in tup_list:
    print(x + " " + str(y))
