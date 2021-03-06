# Generated by Django 2.1.2 on 2018-10-26 03:54

from django.db import migrations, models
import django.db.models.manager
import loanservices.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_id', models.IntegerField(default=101)),
                ('loan_acc_no', models.IntegerField(default=loanservices.models.get_random_id)),
                ('loan_type', models.CharField(choices=[('H', 'home'), ('V', 'vehical'), ('E', 'Education')], max_length=100)),
                ('total_loan', models.CharField(choices=[('a', 'one Lakh'), ('b', '5 Lakh'), ('c', '10lakh')], max_length=200)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Transact',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_id', models.IntegerField(default=101)),
                ('loan_acc_no', models.IntegerField()),
            ],
        ),
    ]
