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
    path('statement-sectionsV/delete/<int:pk>/', views.StatementSections_deleteV, name='section_delete'),
    path('statement-sectionsV/update/<int:pk>/', views.StatementSections_updateV, name="section_update"), # type: ignore
    path('statement/delete/<int:pk>/', views.Statement_deleteV, name='statement_delete'), # type: ignore
    path('statement/update/<int:pk>/', views.statement_update, name='statement_update'), # type: ignore
    path('statement-sectionsV/line/delete/<int:pk>/', views.SectionLines_deleteV, name='line_delete'),
    path('statement-sectionsV/line/update/<int:pk>/', views.SectionLines_updateV, name='line_update'),
    path('statement-sectionsV/account/delete/<int:pk>/', views.LineAccounts_deleteV, name='account_delete'),
    path('statement-sectionsV/account/update/<int:pk>/', views.LineAccounts_updateV, name='account_update'),
    path('statement-linesline/<int:listheader_id>/', views.SectionLinesV, name='statement_linesline'),
    path('statement-line-accountsV/delete/<int:pk>/', views.LineAccountsV, name='StatementLinesDetails_delete'),
    path('cash-flow-statement/', views.cash_flow_statement_view, name='cash_flow_statement'),
]