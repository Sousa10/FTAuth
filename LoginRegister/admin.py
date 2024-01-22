from django.contrib import admin
from .models import PersonM
from .models import AcctRollupsM
from .models import AcctRollupsD
from .models import CalendarIncrements
from .models import Calendars
from .models import Views
from .models import Dates
from .models import DefaultParams
from .models import Transactions

# Register your models here.
admin.site.register(PersonM)
admin.site.register(AcctRollupsM)
admin.site.register(AcctRollupsD)
admin.site.register(CalendarIncrements)
admin.site.register(Calendars)
admin.site.register(Views)
admin.site.register(Dates)
admin.site.register(DefaultParams)
admin.site.register(Transactions)
