
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('user.urls')),
    path('budget', include('budget.urls')),
    path('wageandincome', include('wage_and_income.urls')),
    path('dashboard', include('dashboard.urls')),
]
handler404 = 'utils.views.error404'
handler400 = 'utils.views.error400'

handler500 = 'utils.views.error500'

admin.site.index_title = "My Wallet"

admin.site.site_header = "My Wallet Admin"

admin.site.site_title = "My Wallet admin"
