
# Create your views here.
from django.forms import forms
from django.shortcuts import redirect, render

from testapp.forms import CalculatorForm

# Create your views here.
def home(request):
    return render(request,'home.html' )

def addition(request):
    if request.method == "GET":
        calculatorform = CalculatorForm()
        return render(request,'calculator.html',{ "calculatorform":calculatorform })
    else:
        calculatorform = CalculatorForm(request.POST)
        if calculatorform.is_valid():
            num1=int(request.POST['number1'])  # int(str)
            num2=int(request.POST['number2'])
            if "add" in request.POST:
                result=num1+num2
            elif "sub" in request.POST:
                result=num1-num2
            elif "mul" in request.POST:
                result=num1*num2
            elif "div" in request.POST:
                result=num1/num2
                
            # calculatorform = CalculatorForm(request.POST)

        print("The form",calculatorform)
        # res=calculatorform.number1+calculatorform.number2
        return  render(request,'calculator.html',{"result":result,'calculatorform':calculatorform})


