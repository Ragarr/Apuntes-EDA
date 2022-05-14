from graph import Person, Contacts


class contacts2(Contacts):
    def __init__(self):
        super().__init__()
    
    def get_suggestions(self,p:Person, minimumJumps:int):
        