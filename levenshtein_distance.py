#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import time

# DEFINICIÓ DE CONSTANTS (per fer més comprensible l'anàlisi del codi):
DELETION_COST = 2
INSERTION_COST = 1
SUBSTITUTION_COST = 1


def main():
    pattern = "ALGORITHM"
    text = "ADVANCED"
    t =  time.clock()
    print u"DISTÀNCIA DE LEVENSHTEIN:\nPatró: {}\nText: {}\n\nCost d'eliminació: {}\nCost d'inserció: {}\nCost de substitució: {}\n".format(pattern, text, DELETION_COST, INSERTION_COST, SUBSTITUTION_COST)
    print u"Distància d'edició: {}".format(levenshtein_distance(pattern, text))
    print u"Temps de càlcul: {} segons".format(time.clock() - t) 

    
    
def levenshtein_distance(pattern, text):
    '''Funció que retorna la distància d'edició de Levenshtein entre un patró i un text, donats uns costos d'eliminació, inserció i substitució determinats'''
    m = len(pattern)
    n = len(text)
    
    # matriu de distàncies d'edició
    E = [[0 for x in range (m + 1)] for x in range (n+1)]
    
    # primera columna inicialitzada
    for i in range(n + 1):
        E[i][0] = i * DELETION_COST
      
    # primera fila inicialitzada  
    for j in range (m + 1):
        E[0][j] = j * INSERTION_COST
        
    # recorrem cada fila de la resta, omplint cada casella amb la distància d'edició del prefix fins a i del patró i fins a j del text; aquest valor és el mínim entre la distància d'edició entre patró[0:i-1] i text[0:j] més el cost d'eliminació, la distància d'edició entre patró[0:i] i text[0:j-1] més el cost d'inserció i la distància d'edició entre patró[0:i-1] i text[0:j-1] més el cost de substitució (en cas de diferència del darrer caràcter de les cadenes estudiades)
    for i in range(1, (n + 1)):
        for j in range(1, (m + 1)):
            E[i][j] = min(E[i-1][j] + DELETION_COST, E[i][j-1] + INSERTION_COST, E[i-1][j-1] + diff(pattern, text, j, i))           
            
    showMatrix(E, n+1, m+1)  
    
    return E[n][m]


def diff(pattern, text, i, j):
    '''Funció que retorna el valor de diferència (0 en cas d'igualtat i el valor de substitució en cas de desigualtat) resultant de comparar l'ièssim caràcter del patró i el jèssim del text'''
    if pattern[i-1] == text[j-1]:
        return 0
    return SUBSTITUTION_COST


def showMatrix(matrix, rowCount, columnCount):   
    print "Matriu:"
    for row in range(rowCount):
        for column in range(columnCount):
            space = ""
            if int(matrix[row][column]) <= 10:
                space = " "
            print str(matrix[row][column]) + space,
        print "\n" 
        


if __name__ == "__main__":
    main(*sys.argv[1:])
