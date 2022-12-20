from .ai_model_data import Memory
# from ai_model_data.emotion import Emotion
# from ai_model_data.model_personal import Personal



from random import randrange



class AI(Memory):
    def __init__(self, know_datas : dict):
        #----------------
        # constructor der eizelnen einheiten der ai aufrufen und mit std beschreibem
        Memory.__init__(self= self , know_data = know_datas) 
        #-----------------
               
    def chat_mode(self, text_input : str): # Normaler modus
        example_anwser : list = Memory.text_process(self = self, text = text_input)
        x = len(example_anwser)
        
        ran = randrange(0, x, 1)
        return example_anwser[ran]
        
    
    
    
    
        
        