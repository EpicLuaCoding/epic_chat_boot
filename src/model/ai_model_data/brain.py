from .model_ai_data_dict import KNOW


class Memory():
    def __init__(self, know_data : KNOW):
        self.know : dict = {"" : []}
        self.know = know_data
      
    
    def text_process(self, text : str): # Wird in Ai verwendet um die eingabe zu Prüfen
        for x in self.know:
            if text == x: # Geht die wissendent wörter durch und schaut ob er sie kennt 
                return self.know[x]
        print("fehler")
       

        
                