
from django import forms

# this is a custom django form
class CalculatorForm(forms.Form):
    number1 = forms.IntegerField(required=False)
    number2 = forms.IntegerField(required=False)


    # def __init__(self,*args,**kwargs):
    #     print("the",args,kwargs)
    #     # self.number1=number1
    #     # self.number2=number2

    # def add(self):
    #     return self.number1 + self.number2 

  
    
    
