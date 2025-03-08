from django.shortcuts import render,redirect
from .models import Transaction
def index(request):
    transactions=Transaction.objects.all().order_by('id')
    # balance=0
    # for t in transactions[::-1]:
    #     balance+=t.credit-t.debit
    #     t.running_balance=balance
    #     t.save()
    return render(request,'index.html',{'transactions':transactions})

def add_transactions(request):
    if request.method=='POST':
        date=request.POST['date']
        description=request.POST['description']
        credit=float(request.POST['credit']) if request.POST['credit']  else 0.0 
        print(credit,"---credit",type(credit))
        debit=float(request.POST['debit']) if request.POST['debit']  else 0.0 
        transaction=Transaction.objects.all().last()
        balance=0
        if transaction:
            balance=transaction.running_balance

        if credit:
            balance=balance+credit
        elif debit:
            balance=balance-debit



        transaction=Transaction.objects.create(
            date=date,
            description=description,
            credit=credit,
            debit=debit,
            running_balance=balance,

        )   
        return redirect('/')
    return redirect('/')