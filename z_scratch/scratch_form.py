from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory, Account

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]
