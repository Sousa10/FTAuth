from django.contrib import admin
from .models import StatementSections
from .models import StatementRollups
from .models import CashInAcctM
from .models import StatementLinesDetails
from .models import StatementLinesHeader


# Register your models here.
admin.site.register(StatementSections)
admin.site.register(StatementRollups)
admin.site.register(CashInAcctM)
admin.site.register(StatementLinesDetails)
admin.site.register(StatementLinesHeader)