# -*- coding: utf-8 -*-

# This code converts a list containing parameters to latex equation expressions
# either linear or polynomial.
# If there is a need of wiriting many equations, this simple code may help
#
#   Abbas Dundar, 2020
#
###############################################################################

#ab=[2,1,3,3]
#make_eq(ab)
#'2x_1+x_2+3x_3=3'
#
#make_eq(ab,False)
#'2x_1+x_2+3x_3+3x_4'
#
#make_eq(ab,True,"pol")
#'2x^2+x^1+3x^0=3'
#
#make_eq(ab,False,"pol")
#'2x^3+x^2+3x^1+3x^0'

# Calling with multiple equations in one list
# For good alignment use with latex "systeme" package set nl=","
#AB=[[2,0,5,3],
#    [1,3,-2,1],
#    [-2,3,6,2]]
#latex_nl="\\"+"\\"
#for i in range(len(AB)):
#    print(make_eq(AB[i])+latex_nl)


def make_ax(a,i,n,etype="lin"):
# This procedure converts input parameter a into ax_i or ax^i
    if a==0:
        ax=""
    else:
        if a>0:
            if i==0:
                s=""
            else:
                s="+"
        else:
            s="-"
        if abs(a)==1:
            v=""
        else:
            v=str(abs(a))
        if etype=="lin":
            xpart=   "x_"+str(i+1) 
        elif etype=="pol":
            if i<n-1:
                xpart="x^"+str(n-i-1)
            else:
                xpart=""
        ax=s+v+xpart
    return ax        

def make_eq(ab,eq=True,etype="lin"):
    n=len(ab)
    if eq:
        range_n=n-1
        lastpart="="+str(ab[n-1])
    else: 
        range_n=n
        lastpart=""
    ex=""
    for i in range(range_n):
        ex+=make_ax(ab[i],i,range_n,etype)
    ex+=lastpart
    return ex
