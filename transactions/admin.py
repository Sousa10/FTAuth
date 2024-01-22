from django.contrib import admin
from .models import CashInAcctM
from .models import StatementSections
from .models import StatementLinesLine
from .models import StatementLineAccounts
from .models import TransBatch
from .models import TransHeader
from .models import TransDetail


# Register your models here.
admin.site.register(CashInAcctM)
admin.site.register(StatementSections)
admin.site.register(StatementLinesLine)
admin.site.register(StatementLineAccounts)
admin.site.register(TransBatch)
admin.site.register(TransHeader)
admin.site.register(TransDetail)