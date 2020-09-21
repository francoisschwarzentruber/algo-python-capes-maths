# coding=utf-8


import random


#entrée : un tableau T
#sortie : vrai ssi T contient la valeur x
#algo en O(|T|)
#exemple : rechercheClassique([1, 5, 3], 2) retourne False
#rechercheClassique([1, 5, 3], 3) retourne True
def rechercheClassique(T, x):
    for i in range(len(T)):
         if T[i] == x:
             return True
    return False
 
    

#entrée : un tableau T trié par ordre croissant
#sortie : vrai ssi T contient la valeur x
#algo en O(log |T|)
#exemple : rechercheDichotomique([1, 5, 3], 2) n'est pas un appel licite
#rechercheDichotomique([1, 3, 6], 2) retourne False
#rechercheDichotomique([1, 3, 6], 3) retourne True
def rechercheDichotomique(T, x):
    if(len(T) == 0):
        return False
    middle = len(T) // 2
    if(T[middle] == x):
        return True
    elif(T[middle] < x):
        return rechercheDichotomique(T[1:middle-1])
    else:
        return rechercheDichotomique(T[middle+1:])


#entrée : un tableau T
#sortie : permutation triée de T (en place)
#algo en O(|T|^2)
#exemple : triInsertion([5, 3, 8])
def triInsertion(T):
    
    #entrée : un tableau T avec T[0, ..., i-1] trié
    #sortie : le tableau T est tq T[0, ..., i] contienne les même éléments mais est trié ; T[i+1, ...] est inchangé.
    def inserer(T, i):
        j = i
        while j>0 and T[j-1]>T[j]:
            T[j-1],T[j] = T[j],T[j-1]
            j = j-1

    for i in range(len(T)):
        inserer(T, i)
    return T




#entrée : un entier n
#sortie : un tableau de taille n de nombres aléatoires
#exemple : genererTableauAleatoire(100)
def genererTableauAleatoire(n):
    return [random.randint(1,10000) for i in range(n)]



#entrée : un tableau T
#sortie : permutation triée de T
#algorithme du tri fusion concis, mais inefficace à cause des recopies de tableaux
#exemple : triFusion([5, 3, 8, 6])
def triFusion(T):
    def fusion(A, B):
        if len(A) == 0: return B
        if len(B) == 0: return A
        if A[0] < B[0]:
            return [A[0]] + fusion(A[1:], B)
        else:
            return [B[0]] + fusion(A, B[1:])
        
    if len(T) <= 1:
        return T
    else:
        m = len(T) // 2
        return fusion(triFusion(T[:m]), triFusion(T[m:]))






#entrée : un tableau T
#sortie : permutation triée de T
#deuxième version de l'algorithme du tri fusion en O(|T| log |T|)
#exemple : triFusion2([5, 3, 8, 6])
def triFusion2(T):
    #entrée : tableaux A et B, un tableau T de taille |A| + |B|
    #sortie : T est trié et contient maintenant les éléments de A et B (en place pour T)
    #complexité en O(|T|)
    def fusion(T, A, B):
        i = 0
        j = 0
        k = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                T[k] = A[i]
                i = i + 1
            else:
                T[k] = B[j]
                j = j + 1
            k = k + 1
 
        while i < len(A):
            T[k] = A[i]
            i = i + 1
            k = k + 1
 
        while j < len(B):
            T[k] = B[j]
            j = j + 1
            k = k + 1
        
    if len(T) <= 1:
        return T
    else:
        m = len(T) // 2
        fusion(T, triFusion2(T[:m]), triFusion2(T[m:]))
        return T
