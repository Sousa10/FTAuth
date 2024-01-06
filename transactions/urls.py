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
    path('statement_lines/<int:listheader_id>/', views.statement_lines, name='statement_lines'),
    path('StatementLinesHeader/delete/<int:pk>/', views.StatementLinesHeader_delete, name='StatementLinesHeader_delete'),
    path('StatementLinesDetails/delete/<int:pk>/', views.StatementLinesDetails_delete, name='StatementLinesDetails_delete'),
    path('StatementLinesHeader_update/update/<int:pk>/', views.StatementLinesHeader_update, name='StatementLinesHeader_update'),
    path('StatementLinesDetails_update/update/<int:pk>/', views.StatementLinesDetails_update, name='StatementLinesDetails_update'),
]