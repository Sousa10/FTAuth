from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'transactions'

urlpatterns = [
    path('', views.home, name="home"),
    path('main_landing_page/', views.main_landing_page, name='main_landing_page'),
    path('income_accts', views.income_accts, name='income_accts'),
    path('cashinacctm/update/<int:pk>/', views.cashinacctm_update, name='cashinacctm_update'),
    path('cashinacctm/delete/<int:pk>/', views.cashinacctm_delete, name='cashinacctm_delete'),
    path('show_construction', views.show_construction, name='show_construction'),
    path('accounts', views.accounts, name='accounts'),
    path('show_account/<int:account_id>', views.show_account, name='show_account'),
    path('search_accounts', views.search_accounts, name='search_accounts' ),
    path('statement-sectionsV/', views.StatementSectionsV, name='statement_section'),
    path('statement-sectionsV/<int:pk>/', views.StatementSectionsV, name='statement_section_with_id'),
    path('statement-linesline/<int:listheader_id>/', views.StatementLinesLineV, name='statement_linesline'),
    path('statement-line-accountsV/delete/<int:pk>/', views.StatementLineAccountsV, name='StatementLinesDetails_delete'),
]