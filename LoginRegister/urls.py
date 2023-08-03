from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'LoginRegister'

urlpatterns = [
    path('LoginRegister/', views.LoginRegister, name='LoginRegister'),
    path('LoginRegister/FTMainMenu/', views.FTMainMenu, name='FTMainMenu'),
    path('LoginRegister/FTFinances/', views.FTFinances, name='FTFinances'),
    path('cashinacctm/update/<int:pk>/', views.cashinacctm_update, name='cashinacctm_update'),
    path('cashinacctm/delete/<int:pk>/', views.cashinacctm_delete, name='cashinacctm_delete'),
    path('LoginRegister/FTCalendar/', views.FTCalendar, name='FTCalendar'),
    path('LoginRegister/FTToDos/', views.FTToDos, name='FTToDos'),
    path('LoginRegister/FTListChores/', views.FTListChores, name='FTListChores'),
    path('listHeader/delete/<int:pk>/', views.listHeader_delete, name='listHeader_delete'),
    path('listDetail/delete/<int:pk>/', views.listDetail_delete, name='listDetail_delete'),
    path('LoginRegister/FTFamilyTracks/', views.FTFamilyTracks, name='FTFamilyTracks'),
    path('LoginRegister/FTFitnessSports/', views.FTFitnessSports, name='FTFitnessSports'),
    path('LoginRegister/FTGrocery/', views.FTGrocery, name='FTGrocery'),
    path('LoginRegister/FTAcministration/', views.FTAcministration, name='FTAcministration'),
    path('LoginRegister/login/', auth_views.LoginView.as_view(template_name='FTperson_login.html', authentication_form=LoginForm), name='login'),
    # KMS 7/3
    path('LoginRegister/FTFinancesMenu/', views.FTFinancesMenu, name='FTFinancesMenu'),
    path('LoginRegister/FTFinMenu/', views.FTFinMenu, name='FTFinMenu'),
    path('LoginRegister/FTDefAcctsMenu/', views.FTDefAcctsMenu, name='FTDefAcctsMenu'),
    path('LoginRegister/FTRevenueAccts/', views.FTRevenueAccts, name='FTRevenueAccts'),
    path('financesacct_update/update/<int:pk>/', views.financesacct_update, name='financesacct_update'),
    path('cashinacctm/delete/<int:pk>/', views.cashinacctm_delete, name='cashinacctm_delete'),
    path('LoginRegister/FTExpAccts/', views.FTExpAccts, name='FTExpAccts'),
    path('cashoutacctm/update/<int:pk>/', views.cashoutacctm_update, name='cashoutacctm_update'),
    path('cashoutacctm/delete/<int:pk>/', views.cashoutacctm_delete, name='cashoutacctm_delete'),
    path('LoginRegister/FTAssetAccts/', views.FTAssetAccts, name='FTAssetAccts'),
    path('assetacctm/update/<int:pk>/', views.assetacctm_update, name='assetacctm_update'),
    path('assetacctm/delete/<int:pk>/', views.assetacctm_delete, name='assetacctm_delete'),
    path('LoginRegister/FTLiabAccts/', views.FTLiabAccts, name='FTLiabAccts'),
    path('liabacctm/update/<int:pk>/', views.liabacctm_update, name='liabacctm_update'),
    path('liabacctm/delete/<int:pk>/', views.liabacctm_delete, name='liabacctm_delete'),                                                             
    path('LoginRegister/FTEquityAccts/', views.FTEquityAccts, name='FTEquityAccts'),
    path('equityacctm/update/<int:pk>/', views.equityacctm_update, name='equityacctm_update'),
    path('equityacctm/delete/<int:pk>/', views.equityacctm_delete, name='equityacctm_delete'),
    path('LoginRegister/FTAcctGroupings/', views.FTAcctGroupings, name='FTAcctGroupings'),
    path('LoginRegister/FTGroupingDrillDown/', views.FTGroupingDrillDown, name='FTGroupingDrillDown'),
    path('LoginRegister/FTAccountDrillDown/', views.FTAccountDrillDown, name='FTAccountDrillDown'),
]
