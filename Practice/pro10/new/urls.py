from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('export_to/',views.export_to,name = "export_to"),
    path('Maths/',views.Maths,name = "Maths"),
    path('Eng/',views.Eng,name = "Eng"),
    path('Sci/',views.Sci,name = "Sci"),
    path('Hindi/',views.Hindi,name = "Hindi"),
    path('History/',views.History,name = "History"),
    path('merage/',views.merage,name = "merage"),
    path('student_information/',views.student_information,name = "student_information"),
    path('chart_view/',views.chart_view,name = "graph")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)