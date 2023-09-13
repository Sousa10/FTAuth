from django.contrib import admin
from .models import PersonM
from .models import CashInAcctM
from .models import CashOutAcctM
from .models import WhatWeOwnAcctM
from .models import DebtsAcctM
from .models import NetworthAcctM
from .models import AcctRollupsM
from .models import AcctRollupsD
from .models import TransBatch
from .models import TransHeader
from .models import TransDetail
from .models import ListHeaderT
from .models import ListDetailsT
from .models import CalendarIncrements
from .models import Calendars
from .models import Views
from .models import Dates
from .models import DefaultParams
from .models import Transactions

# Register your models here.
admin.site.register(PersonM)
admin.site.register(CashOutAcctM)
admin.site.register(WhatWeOwnAcctM)
admin.site.register(DebtsAcctM)
admin.site.register(NetworthAcctM)
admin.site.register(AcctRollupsM)
admin.site.register(AcctRollupsD)
admin.site.register(TransBatch)
admin.site.register(TransHeader)
admin.site.register(TransDetail)
admin.site.register(ListHeaderT)
admin.site.register(ListDetailsT)
admin.site.register(CalendarIncrements)
admin.site.register(Calendars)
admin.site.register(Views)
admin.site.register(Dates)
admin.site.register(DefaultParams)
admin.site.register(Transactions)
