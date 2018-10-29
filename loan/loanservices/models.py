from django.db import models
from random import randint
# Create your models here.
from django.db import models
class Customer(object):
    customer_id = 101
    customer_name = "Niraj"
    saving_acc_no = 123456789
    account_balance = 10000000

def get_random_id():
    return randint(10000,99999)

class Loan(models.Model):
    My_choices =(('H', 'home'),
                 ('V','vehical'),
                 ('E', 'Education'))
    LOAN_TYPE = (( 'a','one Lakh'),
                 ('b','5 Lakh'),
                 ('c','10lakh'))
    loan_id = models.AutoField(primary_key=True)
    cust_id = models.IntegerField(default=Customer.customer_id)
    loan_acc_no = models.IntegerField(default=get_random_id)
    loan_type = models.CharField(max_length= 100 ,choices= My_choices)
    total_loan = models.CharField(max_length= 200,choices= LOAN_TYPE)
    objects = models.Manager()

    def __str__(self):
        return str(self.loan_id)

class Transact(models.Model):
    trans_id = models.AutoField(primary_key=True)
    loan =models.ForeignKey(Loan,on_delete=models.CASCADE,related_name='tranctions')
    cust_id = models.IntegerField(default= Customer.customer_id)


from django.db import models

# Create your models here.
