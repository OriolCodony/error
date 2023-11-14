# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:35:09 2023

@author: Principal
"""

from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from error import calculate_error
import openpyxl 

X = [0.04, 0.08, 0.12, 0.16]

potencial = np.array([
    [3.05, 2.85, 2.84],
    [4.81, 4.87, 4.84],
    [6.74, 6.82, 6.83],
    [9.15, 9.16, 9.19]
])
V = []
for row in potencial: 
    mitjana = np.round(np.mean(row),2)
    V.append(mitjana)
    

def E(V, x):
    return (-80 * V) / x

E_valors = [E(V[i], x) for i, x in enumerate(X)]
E_valors = [abs(val) for val in E_valors]
print(E_valors)

E = np.mean(E_valors)


errors = []
for row in potencial:
    error_absolute, error_relative = calculate_error(row,2)
    errors.append((error_absolute, error_relative))

Error_absolut_E, Error_relatiu_E = calculate_error(E_valors,2)
print(V[0])

# Create a DataFrame
dades_df = pd.DataFrame({
    'x(cm)': ['V(A)', 'V(B)', 'V(C)', 'Mitjana'],
    '4 cm': [potencial[0][0], potencial[0][1], potencial[0][2], V[0]],
    '8 cm': [potencial[1][0], potencial[1][1], potencial[1][2], V[1]],
    '12 cm': [potencial[2][0], potencial[2][1], potencial[2][2], V[2]],
    'Entre plaques': [potencial[3][0], potencial[3][1], potencial[3][2], V[3]],
    'Error absolut': [errors[0][0], errors[1][0], errors[2][0], errors[3][0]],
    'Error relatiu': [errors[0][1], errors[1][1], errors[2][1], errors[3][1]]
})

dades_2_df = pd.DataFrame({
    'x(cm)': ['E(x)'],
    '4 cm': [E_valors[0]],
    '8 cm': [E_valors[1]], 
    '12 cm': [E_valors[2]], 
    '16 cm': [E_valors[3]], 
    'Error absolut': [Error_absolut_E],
    'Error relatiu': [Error_relatiu_E]
})

print(dades_df)
"""
dades_df.to_excel('~/Downloads/dades_camp_elèctric_4.xlsx', index=False)
dades_2_df.to_excel('~/Downloads/dades_camp_elèctric_4.1.xlsx', index=False)
"""

plt.plot(X, V, marker = '^',linestyle = 'dotted', color ='red')
plt.title("Potencial elèctric",fontname="cambria")
plt.xlabel("Potencial (V)",fontname="cambria")
plt.ylabel("x (m)")
output_dir = "/Users/Principal/Downloads"
plt.savefig('{}/potencial.png'.format(output_dir))



