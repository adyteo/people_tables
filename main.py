import pandas as pd
import numpy as np
import sys


"""
Project idea coming from ArsTechnica post: 'The real research behind the wild rumors about OpenAI’s Q* project'
https://arstechnica.com/ai/2023/12/the-real-research-behind-the-wild-rumors-about-openais-q-project/
"""

# This can be read from a CSV file
lst = ['Alice', 'Bethany', 'Ellen', 'Kimmie', 'Chuck', 'Fiona', 'Margaret', 'Jason', 'Donald', 'Henry', 'Grant',
       'Louise', 'Ingrid', 'Nancy', 'Olivia']

# This can be read from a CSV file
not_lst = [['Alice', 'Bethany'], ['Alice', 'Ellen'], ['Alice', 'Kimmie'], ['Chuck', 'Fiona'], ['Bethany', 'Margaret'],
           ['Bethany', 'Jason'], ['Fiona', 'Henry'], ['Chuck', 'Nancy'], ['Margaret', 'Henry'], ['Margaret', 'Louise'],
           ['Jason', 'Donald'], ['Henry', 'Louise'], ['Henry', 'Olivia'], ['Grant', 'Ingrid'], ['Grant', 'Nancy'],
           ['Grant', 'Olivia'], ['Louise', 'Olivia']]

# This can be read from a CSV file
tables = ['A', 'B', 'C', 'D', 'E']

w = len(tables)
h = len(lst) / len(tables)
if not h.is_integer():
    print('You need the number of persons per table to be constant '
          '(e.g. 15 persons at 5 tables = 3 persons at each table)')
    sys.exit()
h = int(h)

not_permitted = 0

while True:
    perm = np.random.permutation(lst)  # The solution is found faster if using random lists

    tbl_grp = []
    k = False
    i = 0

    for table in range(w):
        group = []

        for person in range(h):
            group.append(perm[i])
            i += 1

        group = sorted(group)
        tbl_grp.append(group)

        for nt in not_lst:
            not_permitted = 0
            for grp in group:
                if nt[0] == grp or nt[1] == grp:
                    not_permitted += 1
            if not_permitted == 2:
                break

        if not_permitted < 2:
            k = True
        else:
            k = False
            break
    if k:
        print(f'First solution found:')
        for table in range(w):
            print(f'table {tables[table]}: {tbl_grp[table]}')

        df = pd.DataFrame([tbl_grp], columns=tables)
        df.to_csv('solution.csv', index=False)

        sys.exit()
