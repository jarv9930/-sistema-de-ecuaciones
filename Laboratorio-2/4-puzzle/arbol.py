class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_coste(self, coste):
        self.coste = coste

    def get_coste(self):
        return self.coste

    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        en_la_lista = False
        lista_nodosAux = []
        lista_nodosAux = lista_nodos
        #print("Logitud lista",len(lista_nodos))
        #print("Self",self.get_datos())
        for n in lista_nodosAux:
            #print("Nodo Self",n.get_datos())
            if self.get_datos() == n.get_datos():
                en_la_lista = True
                #EL CODIGO TENIA UN ERROR QUE NO PERMITIA QUE SE EVALUARAN TODOS LOS NODOS DE LA LISTA,
                #DEBIDO A QUE JUSTO DESPUES DE LA PRIMERA ITERACION, SE RETORNA EL VALOR DE LA en_la_lista
                #SE MODIFICO LA IDENTACION PARA RETORNAR TRUES SOLO EN CASO DE QUE EL NODO ESTE EN LA LISTA
                #Y SE AGREGO UN RETURN DESPUES DE TERMINAR EL FOR, PARA QUE EN CASO DE QUE NO ESTE EN LA LISTA, 
                # SE RETORNE EL VALOR DE en_la_lista FALSE
                return en_la_lista
        return en_la_lista

    def __str__(self):
        return str(self.get_datos())