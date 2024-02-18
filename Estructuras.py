class Pila:
    def __init__(self): 
        self.items = []
        
    def push(self, X):
         self.items.append(x)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila se encuentra vacía")
    def isEmpty(self):
        return self.items == []
    def top(self):
        try: 
            return self.items[-1]
        except IndentationError:
            raise ValueError("La pila se encuantra vacía")
    def deletePile(self):
        del self.items
    
             