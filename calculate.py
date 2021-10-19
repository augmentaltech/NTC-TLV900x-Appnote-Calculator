#!/bin/python
import math
import numpy as np
import sys

# python helper for https://www.ti.com/lit/an/sboa323a/sboa323a.pdf "Analog Engineer's Circuit - Temperature sensing with NTC circuit"
# calculates all resistor values for a given temperature range (Tmin, Tmax), the NTCs Beta value (Beta), its resistance at 25°C and R4 (typical 1.5kOhm)
# run make to calculate all values, print them to a LaTeX _f and render the _f via xelatex, just run python calculate.py to print them to your console

val = {}
res = {}

# NTC values
res['R25'] = 10.0 # kOhm
val['Beta'] = (3380, 'K') # K
# System values
res['R4'] = 10
val['Vdd'] = (3.3, 'V') # V
# Target range
val['Tmin'] = (32, '^\circ C') # °C
val['Tmax'] = (42, '^\circ C') # °C
# print and resistor selection preferences
print_values = ['R1', 'R2', 'R3', 'R4', 'Vdd', 'Beta', 'Tmin', 'Tmax', 'gain']
E_preference = 'E48'
# LaTeX _f

# E-series of preffered numbers
E48 = [1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53]
E96 = [1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76]
E192 = [1.00, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10, 1.11, 1.13, 1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23, 1.24, 1.26, 1.27, 1.29, 1.30, 1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42, 1.43, 1.45, 1.47, 1.49, 1.50, 1.52, 1.54, 1.56, 1.58, 1.60, 1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98, 2.00, 2.03, 2.05, 2.08, 2.10, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, 2.32, 2.34, 2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61, 2.64, 2.67, 2.71, 2.74, 2.77, 2.80, 2.84, 2.87, 2.91, 2.94, 2.98, 3.01, 3.05, 3.09, 3.12, 3.16, 3.20, 3.24, 3.28, 3.32, 3.36, 3.40, 3.44, 3.48, 3.52, 3.57, 3.61, 3.65, 3.70, 3.74, 3.79, 3.83, 3.88, 3.92, 3.97, 4.02, 4.07, 4.12, 4.17, 4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.70, 4.75, 4.81, 4.87, 4.93, 4.99, 5.05, 5.11, 5.17, 5.23, 5.30, 5.36, 5.42, 5.49, 5.56, 5.62, 5.69, 5.76, 5.83, 5.90, 5.97, 6.04, 6.12, 6.19, 6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73, 6.81, 6.90, 6.98, 7.06, 7.15, 7.23, 7.32, 7.41, 7.50, 7.59, 7.68, 7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35, 8.45, 8.56, 8.66, 8.76, 8.87, 8.98, 9.09, 9.20, 9.31, 9.42, 9.53, 9.65, 9.76, 9.88]

# E-Series mapping
preffered_E = {}
preffered_E['E48'] = E48
preffered_E['E96'] = E96
preffered_E['E192'] = E192

# find nearest E value from given value
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def write_formula(formula="",_f=''):
    _f.write("\\begin{equation}\n\t\\begin{gathered}\n\t\t")
    _f.write("%s\n" % (formula))
    _f.write("\t\\end{gathered}\n\\end{equation}\n")

def print_value_table(resistors={},vals={},_pval=print_values,_f=''):
    _f.write("\\begin{table}[h]\n\t\\centering\n\t\\fboxrule=0pt\n\t\\begin{tabular}{p{8cm} p{3cm}}\n\t\t\\toprule\n")
    _f.write("\t\t\\textbf{Input variables} & \\textbf{Value} \\\\ \\midrule \n")

    for i in vals:
        if i in _pval:
            print(i,vals[i][0],vals[i][1])
            _f.write("\t\t%s & $%.2f\,%s$ \\\\ \n" % (i,vals[i][0],vals[i][1]))

    _f.write("\t\t\\bottomrule \\vspace{1.5bp} \\\\ \\toprule \n")
    _f.write("\t\t\\textbf{Calculated E-series resistances} &  \\\\ \n")

    for i in resistors:
        if i in _pval:
            print(i,resistors[i])
            _f.write("\t\t%s & $%.2f\,k\ohm$ \\\\ \n" % (i,resistors[i]))

    _f.write("\t\t\\bottomrule\n\t\\end{tabular}\n\end{table}\n")

def print_real_curve(_Tmin=32, _Tmax=42, _B=4000, _R25=19.0, _Vdd=3.3, _R1=11, _R3=15, _R4=14, _div=13,_f=''):
    for i in range(int(_Tmin),int(_Tmax)+1):
        _f.write("%.1f\t%.3f\n" % (i,calculate_vout(calculate_Rtgt(_B, _R25, _Ttgt=i),_Vdd,_R1,_div,_R3,_R4)[0]))

def calculate_Rtgt(_B=4000,_Rref=10.0,_Tref=25.0,_Ttgt=50.0,_p=False,_f=''):
    _R50=(_Rref*math.exp(_B*((1/(273.15+_Ttgt))-(1/(273.15+_Tref)))))
    #if(_p):
    #    write_formula("R_{50}=R_{ref}*e^{\\beta*(\\frac{1}{273.15+T}-\\frac{1}{273.15+T_0})}\\\\ \
    #                   R_{50}=%.1fk\\ohm*e^{%dK*(\\frac{1}{273.15+%.1f^{\\circ}C}-\\frac{1}{273.15+%.1f^{\\circ}C})}\\\\ \
    #                   R_{50}=%.2fk\\ohm" % (_Rref,_B,_Ttgt,_Tref,_R50))
    return _R50 # kOhm

def calculate_R1(_RNTCmin=10,_RNTCmax=10,_Elst=E48,_p=False,_f=''):
    R1 = math.sqrt(_RNTCmin * _RNTCmax) # Ohm
    R1_real = find_nearest(_Elst,R1)
    return (R1_real,R1,(1-(R1/R1_real))) # Real R1 value, R1, Error

def calculate_voltage_range(_Vdd=3.3,_R1=10.0,_RNTCmax=10,_RNTCmin=11,_p=False,_f=''):
    Vinmin = _Vdd * (_R1/(_RNTCmin+_R1))
    Vinmax = _Vdd * (_R1/(_RNTCmax+_R1))
    return ((Vinmin, 'V'),(Vinmax, 'V')) # (V,V)

def calculate_ideal_gain(_Vinmax=3.3,_Vinmin=0.0,_Voutmax=3.25,_Voutmin=0.05,_p=False,_f=''):
    return ((_Voutmax-_Voutmin)/(_Vinmax-_Vinmin)) # V/V

def calculate_divider(_gain=1.0,_R4=1.5,_p=False,_f=''):
    return (_R4/(_gain-1))

def calculate_R2_R3(_Vdd=3.3,_div=1.0,_Vinmax=3.3,_gain=1.0,_Voutmax=3.25,_R4=1.5,_Elst=E48,_p=False,_f=''):
    _R3 = ((_R4*_Vdd)/((_Vinmax*_gain)-_Voutmax))
    _R3_real = find_nearest(_Elst,_R3)
    _R2 = ((_div*_R3)/(_R3-_div))
    _R2_real = find_nearest(_Elst,_R2)
    return (_R2_real,_R2,(1-(_R2/_R2_real)),_R3_real,_R3,(1-(_R3/_R3_real))) # (Ohm,Ohm)

def calculate_actual_gain(_div,_R4=1.5,_p=False,_f=''):
    return ((_div+_R4)/_div, ' ')

def calculate_vout(_Rntc=10.0,_Vdd=3.3,_R1=1.0,_div=1.0,_R3=1,_R4=1.5,_p=False,_f=''):
    Vout = (_Vdd * (_R1/(_Rntc+_R1)) * ((_div+_R4)/_div)-((_R4/_R3)*_Vdd), 'V')
    return Vout


res['Rlow']                     = calculate_Rtgt(val['Beta'][0], res['R25'], _Ttgt=val['Tmin'][0])
res['Rhigh']                    = calculate_Rtgt(val['Beta'][0], res['R25'], _Ttgt=val['Tmax'][0])
res['R1'],R1ideal,R1Err         = calculate_R1(res['Rlow'], res['Rhigh'], _Elst=preffered_E[E_preference])
val['Vinmin'], val['Vinmax']    = calculate_voltage_range(val['Vdd'][0],res['R1'],res['Rhigh'],res['Rlow'])
gideal                          = calculate_ideal_gain(val['Vinmax'][0],val['Vinmin'][0])
divider                         = calculate_divider(gideal,_R4=res['R4'])
res['R2'], R2ideal, R2Err, res['R3'], R3ideal, R3Err = calculate_R2_R3(val['Vdd'][0],divider,val['Vinmax'][0],gideal,_R4=res['R4'], _Elst=preffered_E[E_preference])
val['gain']                     = calculate_actual_gain(divider,_R4=res['R4'])

if len(sys.argv) > 1:
    tex = open(sys.argv[1], "w")
    print_value_table(res, val, _f=tex)

if len(sys.argv) > 2:
    csv = open(sys.argv[2], "w")
    print_real_curve(val['Tmin'][0],val['Tmax'][0],val['Beta'][0],res['R25'],val['Vdd'][0],res['R1'],res['R3'],res['R4'],divider,csv)
