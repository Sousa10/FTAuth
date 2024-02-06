from django.contrib import admin
from .models import FinStatements
from .models import StatementSections
from .models import SectionLines
from .models import LineAccounts
from .models import CashInAcctM
from .models import TransHeader
from .models import TransDetail


# Register your models here.
admin.site.register(FinStatements)
admin.site.register(StatementSections)
admin.site.register(SectionLines)
admin.site.register(LineAccounts)
admin.site.register(CashInAcctM)
admin.site.register(TransHeader)
admin.site.register(TransDetail)