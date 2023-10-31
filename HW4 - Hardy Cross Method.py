# -*- coding: utf-8 -*-
"""
Stephen Kridel

CE588 - HW 4
"""

'''Problem A and B'''

k1 = 2.0
k2 = 3.0
k3 = 8.0
k4 = 5.0
k5 = 11.0
k6 = 11.0
k7 = 5.0
k8 = 5.0
k9 = 2.0

q1 = 40
q2 = 18
q3 = 22
q4 = 3
q5 = 25
q6 = 10
q7 = 35
q8 = 3
q9 = 35

Za = 450
Zb = 300

n = 2

''''''
def dQ1_func(q2, q3, q4, q8):
    num = (
    - k2 * abs(q2) * q2
    + k3 * abs(q3) * q3
    - k4 * abs(q4) * q4
    - k8 * abs(q8) * q8)

    den = -n * (
    + k2 * abs(q2)
    + k3 * abs(q3)
    + k4 * abs(q4)
    + k8 * abs(q8))

    return num/den

''''''
def dQ2_func(q4, q5, q6, q7): 
    num = (
    + k4 * abs(q4) * q4
    + k5 * abs(q5) * q5
    - k6 * abs(q6) * q6
    - k7 * abs(q7) * q7)

    den = -n * (
    + k4 * abs(q4)
    + k5 * abs(q5) 
    + k6 * abs(q6)
    + k7 * abs(q7))
    
    return num/den

''''''
def dQ3_func(q1, q2, q8, q9):
    num = (
    + k1 * abs(q1) * q1
    + k2 * abs(q2) * q2
    + k8 * abs(q8) * q8
    - k9 * abs(q9) * q9
    + (Za - Zb))
    
    den = -n * (
    + k1 * abs(q1)  
    + k2 * abs(q2)  
    + k8 * abs(q8)
    + k9 * abs(q9))
    
    return num/den

''''''

def dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9):
    deltaQ1 = dQ1_func(q2, q3, q4, q8)
    deltaQ2 = dQ2_func(q4, q5, q6, q7)
    deltaQ3 = dQ3_func(q1, q2, q8, q9)
    return deltaQ1, deltaQ2, deltaQ3

deltaQ1, deltaQ2, deltaQ3 = dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9)

tol = 0.0000001

i= 0
while abs(deltaQ1 + deltaQ2 + deltaQ3) > tol:
    i = i+1
    q1 = q1 + deltaQ3
    q2 = q2 + deltaQ3 - deltaQ1
    q3 = q3 + deltaQ1
    q4 = q4 - deltaQ1 + deltaQ2
    q5 = q5 + deltaQ2
    q6 = q6 - deltaQ2
    q7 = q7 - deltaQ2
    q8 = q8 - deltaQ1 + deltaQ3
    q9 = q9 - deltaQ3
    
    deltaQ1, deltaQ2, deltaQ3 = dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9)

q_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9]

for i, q in enumerate(q_list):
    print(f"q{i+1} = {q:0.3f}")
'''    

'''Problem C'''
'''
f = [0.024, 0.024, 0.022, 0.018, 0.024, 0.020, 0.024, 0.022]
L = [4000, 6000, 6000, 6500, 7000, 3000, 5000, 300]
D = [10, 10, 12, 24, 10, 18, 10, 12]
A = []
k = []

'Calculating Areas (converting D to inches in loop)'
for val in D:
    a = 3.1415*(val/24)**2
    A.append(a)

'Calculating K values (converting D to inches in loop)'
for i in range(len(f)):
    val = (f[i]*L[i])/((D[i]/12)*2*32.2*A[i]**2)
    k.append(val)

k1, k2, k3, k4, k5, k6, k7, k8 = k

q1 = 0.56
q2 = 2.78
q3 = 1.67
q4 = 5.57
q5 = 1.67
q6 = 1.67
q7 = 1.67
q8 = 4.45

Ztank = 315

n = 2

''''''
def dQ1_func(q1, q3, q4, q6):
    num = (
    - k1 * abs(q1) * q1
    - k3 * abs(q3) * q3
    + k4 * abs(q4) * q4
    + k6 * abs(q6) * q6)

    den = -n * (
    + k2 * abs(q2)
    + k3 * abs(q3)
    + k4 * abs(q4)
    + k6 * abs(q6))

    return num/den

''''''
def dQ2_func(q2, q4, q5, q7): 
    num = (
    + k2 * abs(q2) * q2
    - k4 * abs(q4) * q4
    + k5 * abs(q5) * q5
    - k7 * abs(q7) * q7)

    den = -n * (
    + k2 * abs(q2)
    + k4 * abs(q4) 
    + k5 * abs(q5)
    + k7 * abs(q7))
    
    return num/den

''''''

def dQ_func(q1, q2, q3, q4, q5, q6, q7, q8):
    deltaQ1 = dQ1_func(q1, q3, q4, q6)
    deltaQ2 = dQ2_func(q2, q4, q5, q7)
    return deltaQ1, deltaQ2

deltaQ1, deltaQ2 = dQ_func(q1, q2, q3, q4, q5, q6, q7, q8)

tol = 0.0000001

i= 0
while abs(deltaQ1 + deltaQ2) > tol:
    i = i+1
    q1 = q1 - deltaQ1
    q2 = q2 + deltaQ2
    q3 = q3 - deltaQ1
    q4 = q4 + deltaQ1 - deltaQ2
    q5 = q5 + deltaQ2
    q6 = q6 + deltaQ1
    q7 = q7 - deltaQ2
    
    deltaQ1, deltaQ2 = dQ_func(q1, q2, q3, q4, q5, q6, q7, q8)

'Adjusting q8 based on mass flow of final q1 and q2 values'
q8 = q1 + q2 + 1.11

q = [q1, q2, q3, q4, q5, q6, q7, q8]

for i, val in enumerate(q):
    print(f"q{i+1} = {val:0.3f}")


'Finding Pressures'    

'Calculating hL using hL = K*Q^2'
hL = []
for i in range(len(q)):
    hL.append(k[i] * q[i]**2)

'hL[i] = head loss for pipe i+1 (indicies start at 0)'
H2 = Ztank - hL[7]
H1 = H2 - hL[0]
H3 = H2 - hL[1]
H6 = H3 - hL[4]
H4 = H1 - hL[2]
H5 = H2 - hL[3]
    
H = [H1, H2, H3, H4, H5, H6]

for i, val in enumerate(H):
    print(f"H{i+1} = {val:0.3f}")

    
'''Problem D'''

f = [0.024, 0.024, 0.022, 0.018, 0.024, 0.020, 0.024, 
     0.022, 0.020, 0.024, 0.018, 0.022, 0.026, 0.022]
L = [4000, 6000, 6000, 6500, 7000, 3000, 5000, 
     300, 500, 4000, 4000, 4000, 3000, 5000]
D = [10, 10, 12, 24, 10, 18, 10, 
     12, 18, 10, 24, 12, 8, 12]
A = []
k = []

'Calculating Areas (converting D to inches in loop)'
for val in D:
    a = 3.1415*(val/24)**2
    A.append(a)

'Calculating K values (converting D to inches in loop)'
for i in range(len(f)):
    val = (f[i]*L[i])/((D[i]/12)*2*32.2*A[i]**2)
    k.append(val)

k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14 = k

q1 = 0.116
q2 = 2.053
q3 = 1.226
q4 = 6.741
q5 = 0.943
q6 = 2.114
q7 = 2.397
q8 = 3.279
q9 = 1.448
q10 = 0.56
q11 = 3.34
q12 = 0.56
q13 = 0.56
q14 = 0.56

Ztank_1 = 315
Ztank_2 = 155

A = -0.2
B = -0.5
C = 200

n = 2

''''''
def dQ1_func(q1, q3, q4, q6):
    num = (
    + k1 * abs(q1) * q1
    - k3 * abs(q3) * q3
    + k4 * abs(q4) * q4
    - k6 * abs(q6) * q6)

    den = -n * (
    + k2 * abs(q2)
    + k3 * abs(q3)
    + k4 * abs(q4)
    + k6 * abs(q6))

    return num/den

''''''
def dQ2_func(q2, q4, q5, q7): 
    num = (
    + k2 * abs(q2) * q2
    - k4 * abs(q4) * q4
    + k5 * abs(q5) * q5
    - k7 * abs(q7) * q7)

    den = -n * (
    + k2 * abs(q2)
    + k4 * abs(q4) 
    + k5 * abs(q5)
    + k7 * abs(q7))
    
    return num/den

''''''
def dQ3_func(q6, q11, q13, q10):
    num = (
    + k6 * abs(q6) * q6
    - k11 * abs(q11) * q11
    + k13 * abs(q13) * q13
    - k10 * abs(q10) * q10)

    den = -n * (
    + k6 * abs(q6)
    + k11 * abs(q11) 
    + k13 * abs(q13)
    + k10 * abs(q10))
    
    return num/den

''''''
def dQ4_func(q7, q12, q14, q11):
    num = (
    + k7 * abs(q7) * q7
    + k12 * abs(q12) * q12
    + k14 * abs(q14) * q14
    - k11 * abs(q11) * q11)

    den = -n * (
    + k7 * abs(q7)
    + k12 * abs(q12) 
    + k14 * abs(q14)
    + k11 * abs(q11))
    
    return num/den

''''''
def dQ5_func(q8, q1, q3, q9):
    num = (
    + k8 * abs(q8) * q8
    - k1 * abs(q1) * q1
    + k3 * abs(q3) * q3
    - k9 * abs(q9) * q9
    +(A * abs(q9) * q9 + B * abs(q9) + C)
    + (Ztank_2 - Ztank_1))

    den = -n * (
    + k8 * abs(q8)
    + k1 * abs(q1) 
    + k3 * abs(q3)
    + k9 * abs(q9)
    (2*(A*abs(q9) + B)))
    
    return num/den

''''''


def dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14):
    deltaQ1 = dQ1_func(q1, q3, q4, q6)
    deltaQ2 = dQ2_func(q2, q4, q5, q7)
    deltaQ3 = dQ3_func(q6, q11, q13, q10)
    deltaQ4 = dQ3_func(q7, q12, q14, q11)
    deltaQ5 = dQ3_func(q8, q1, q3, q9)
    return deltaQ1, deltaQ2, deltaQ3, deltaQ4, deltaQ5

deltaQ1, deltaQ2, deltaQ3, deltaQ4, deltaQ5 = (
    dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14))

tol = 0.0001

i= 0
while abs(deltaQ1 + deltaQ2 + deltaQ3 + deltaQ4 + deltaQ5) > tol:
    i = i+1
    q1 = q1 - deltaQ5 + deltaQ1
    q2 = q2 + deltaQ2
    q3 = q3 + deltaQ5 - deltaQ1
    q4 = q4 + deltaQ1 - deltaQ2
    q5 = q5 + deltaQ2
    q6 = q6 - deltaQ1 + deltaQ3
    q7 = q7 + deltaQ4 - deltaQ2
    q8 = q8 + deltaQ5
    q9 = q9 - deltaQ5
    q10 = q10 - deltaQ3
    q11 = q11 - deltaQ3 + deltaQ4
    q12 = q12 + deltaQ4
    q13 = q13 + deltaQ3
    q14 = q14 + deltaQ4
    
    deltaQ1, deltaQ2, deltaQ3, deltaQ4, deltaQ5 = (
        dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14))


q = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14]

for i, val in enumerate(q):
    print(f"q{i+1} = {val:0.3f}")


'Finding Pressures'

'Calculating hL using hL = K*Q^2'
hL = []
for i in range(len(q)):
    hL.append(k[i] * q[i]**2)


'hL[i] = head loss for pipe i+1 (indicies start at 0)'
H2 = Ztank_1 - hL[7]
H3 = H2 - hL[1]
H5 = H2 - hL[3]
H6 = H3 - hL[4]
H9 = H6 - hL[11]
H8 = H9 - hL[13]
H7 = H8 - hL[12]
H1 = H2 + hL[0]
H4 = H1 - hL[2]
    
H = [H1, H2, H3, H4, H5, H6, H7, H8, H9]

for i, val in enumerate(H):
    print(f"H{i+1} = {val:0.3f}")


'''Problem E'''

phi = 4.37
n = 1.85
c = [140, 100, 100, 100, 100, 100, 100, 100, 100, 100]
L = [1000, 2000, 2000, 1500, 1000, 1500, 2000, 2000, 3000, 3000]
D = [30, 24, 24, 16, 16, 12, 6, 8, 6, 6]
A = []
k = []

'Calculating Areas (converting D to inches in loop)'
for val in D:
    a = 3.1415*(val/24)**2
    A.append(a)

'Calculating K values (converting D to inches in loop)'
for i in range(len(c)):
    val = ((phi*L[i])/(c[i]**n*(D[i]/12)**4.87))
    k.append(val)

k1, k2, k3, k4, k5, k6, k7, k8, k9, k10 = k

q1 = 15
q2 = 2
q3 = 13
q4 = 5
q5 = 7
q6 = 3
q7 = 1
q8 = 1
q9 = 7
q10 = 1

Ztank_1 = 200
Ztank_2 = 0

A = -0.9376
C = 240
v = 0
''''''
def dQ1_func(q2, q4, q7, q3):
    num = (
    + k2 * pow(abs(q2), n-1) * q2
    - k4 * pow(abs(q4), n-1) * q4
    + k7 * pow(abs(q7), n-1) * q7
    - k3 * pow(abs(q3), n-1) * q3)

    den = -n * (
    + k2 * abs(q2)
    + k4 * abs(q4)
    + k7 * abs(q7)
    + k3 * abs(q3))

    return num/den

''''''
def dQ2_func(q7, q6, q8, q5): 
    num = (
    - k7 * pow(abs(q7), n-1) * q7
    - k6 * pow(abs(q6), n-1) * q6
    + k8 * pow(abs(q8), n-1) * q8
    - k5 * pow(abs(q5), n-1) * q5)

    den = -n * (
    + k7 * abs(q7)
    + k6 * abs(q6) 
    + k8 * abs(q8)
    + k5 * abs(q5))
    
    return num/den

''''''
def dQ3_func(q10, q6, q4, q9):
    num = (
    - k10 * pow(abs(q10), n-1) * q10
    + k6 * pow(abs(q6), n-1) * q6
    + k4 * pow(abs(q4), n-1) * q4
    - k9 * pow(abs(q9), n-1) * q9)

    den = -n * (
    + k10 * abs(q10)
    + k6 * abs(q6) 
    + k4 * abs(q4)
    + k9 * abs(q9))
    
    return num/den

''''''
def dQP_func(q9, q2, q1):
    num = (
    + k9 * pow(abs(q9), n-1) * q9
    - k2 * pow(abs(q2), n-1) * q2
    - k1 * pow(abs(q1), n-1) * q1
    - (A * abs(q9) * q9 + C)
    + (Ztank_1 - Ztank_2))

    den = -n * (
    + k9 * abs(q9)
    + k2 * abs(q2)
    + k1 * abs(q1)
    + (2*(A*abs(q9))))
    
    return num/den

''''''


def dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    deltaQ1 = dQ1_func(q2, q4, q7, q3)
    deltaQ2 = dQ2_func(q7, q6, q8, q5)
    deltaQ3 = dQ3_func(q10, q6, q4, q9)
    deltaQP = dQP_func(q9, q2, q1)
    return deltaQ1, deltaQ2, deltaQ3, deltaQP

deltaQ1, deltaQ2, deltaQ3, deltaQP = (
    dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))

tol = 0.000001

i= 0
while abs(deltaQ1 + deltaQ2 + deltaQ3 + deltaQP) > tol:
    i = i+1
    q1 = q1 - deltaQP
    q2 = q2 + deltaQ1 - deltaQP
    q3 = q3 - deltaQ1
    q4 = q4 - deltaQ1 + deltaQ3
    q5 = q5 - deltaQ2
    q6 = q6 + deltaQ3 - deltaQ2
    q7 = q7 + deltaQ1 - deltaQ2
    q8 = q8 + deltaQ2
    q9 = q9 - deltaQ3 + deltaQP
    q10 = q10 - deltaQP
    
    deltaQ1, deltaQ2, deltaQ3, deltaQP = (
        dQ_func(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))


q = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

for i, val in enumerate(q):
    print(f"q{i+1} = {val:0.3f}")


'Finding Pressures'

'Calculating hL using hL = K*Q^2'
hL = []
for i in range(len(q)):
    val = (phi*L[i]*q[i]**n) / (c[i]**n * (D[i]/12)**4.87)
    hL.append(val)


'hL[i] = head loss for pipe i+1 (indicies start at 0)'

H1 = Ztank_1 - hL[0]
H2 = H1 - hL[1]
H3 = H2 + hL[8]
H4 = H3 + hL[9]
H5 = H4 - hL[7]
H6 = H5 + hL[4]
H7 = H6 + hL[6]

H = [H1, H2, H3, H4, H5, H6, H7]

for i, val in enumerate(H):
    print(f"H{i+1} = {val:0.3f}")
