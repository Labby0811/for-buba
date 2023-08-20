import math

#function to calc Ft
def Ft_calc(P, R, S):
    robo = (math.sqrt((R ** 2) + 1))
    Ft_num = (robo) * math.log((1 - S) / (1 - R*S))
    Ft_den = (R - 1) * math.log((2 - S * (R + 1 - robo)) / (2 - S * (R + 1 + robo))) 

    if(Ft_den != 0):
        Ft = Ft_num / Ft_den
    else: 
        return "error in Ft"
    
    return Ft

#function to calc P
def P_calc(t1, t2, T1):
    P_num = (t2 - t1)
    P_den = (T1 - t1)
    
    if(P_den != 0):
        P = P_num / P_den
    else: 
        return "error in P"
    
    return P
    

#function to calc R
def R_calc(t1, t2, T1, T2):
    R_num = (T1 - T2)
    R_den = (t2 - t1)
    
    if(R_den != 0):
        R = R_num / R_den
    else: 
        return "error in R"
    
    return R
    

#init variables from input
t1_str = input("Inserisci t1: ")
t1 = float(t1_str)

t2_str = input("Inserisci t2: ")
t2 = float(t2_str)

T1_str = input("Inserisci T1: ")
T1 = float(T1_str)

T2_str = input("Inserisci T2: ")
T2 = float(T2_str)

#calc formulas

P = P_calc(t1, t2, T1)
S = P 
X = S
 
R = R_calc(t1, t2, T1, T2)
Y = R

Ft = Ft_calc(P, R, S)

print("Results : ")
print("P = S = X = ", P)
print("R = Y = ", R)
print("Ft = ", Ft)