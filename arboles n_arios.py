class Nodo:
    def __init__(self, valor, hijos):
        self.valor = valor
        self.hijos = hijos



def parabuscar(palabra,raiz,n):
    if n < 1:
        return palabra[0]
    else:
        if n >= 1 and n < len(palabra):
            return raiz+palabra[n]

def recorrerhijos(raiz,arbol,n,y):
    if y < 1:
        if arbol.valor == raiz:
            return arbol.hijos
        else:
            return "el arbol en el que busca no lo es"
    else:
        if y >= 1:
            print arbol[n].valor
            if arbol[n].valor == raiz:
                return arbol[n].hijos
            else:
                if arbol[n].valor!= raiz and n < len(arbol):
                    return recorrerhijos(raiz,arbol,n+1,y)
                
    
        
def hacerlo(palabra,raiz,n,arbol,y):
    print raiz
    if n < len(palabra) and n==0:
        return hacerlo(palabra,parabuscar(palabra,raiz,n),n+1,arbol,y)
    else:
        if n < len(palabra) and n!=0:
            return hacerlo(palabra,parabuscar(palabra,raiz,n),n+1,recorrerhijos(raiz,arbol,0,y),y+1)
        else:
            if n >= len(palabra):
                return recorrerhijos(raiz,arbol,0,y)
            

def yloshijos(palabra,arbol):
    if len(hacerlo(palabra,"",0,arbol,0)) != 0:
        return quienessonesosbastardos(hacerlo(palabra,"",0,arbol,0),n)
    else:
        if len(hacerlo(palabra,"",0,arbol,0)) == 0:
            return "no tengo a ninguno de esos bastardos"
        

def ver_hijos(Nodo):
    print Nodo.valor
    [ver_hijos(x) for x in Nodo.hijos]
        
    
    
    
    
                
             


    

