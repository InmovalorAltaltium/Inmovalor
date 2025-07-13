from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin y autenticación
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),

    # Página de bienvenida y estimaciones
    path('', views.welcome, name='welcome'),
    path('estimaciones/', views.estimaciones, name='estimaciones'),
    path('honorarios/', views.honorarios_calculator, name='honorarios_calculator'),
    path('resultados/<int:propiedad_id>/', views.mostrar_resultado, name='mostrar_resultado'),

    # Ajax para colonias y CP
    path('obtener_colonias/', views.obtener_colonias, name='obtener_colonias'),
    path('obtener_municipios/', views.obtener_municipios, name='obtener_municipios'),
    path('obtener_codigos_postales/', views.obtener_codigos_postales, name='obtener_codigos_postales'),

    # Alcaldías
    path('benito/', views.vista_benito_juarez, name='benito'),
    path('alvaro/', views.vista_alvaro, name='alvaro'),
    path('coyoacan/', views.vista_coyoacan, name='coyoacan'),
    path('xochimilco/', views.vista_xochimilco, name='xochimilco'),
    path('azcapotzalco/', views.vista_azcapotzalco, name='azcapotzalco'),
    path('cuajimalpa/', views.vista_cuajimalpa, name='cuajimalpa'),
    path('cuauhtemoc/', views.vista_cuauhtemoc, name='cuauhtemoc'),
    path('miguel/', views.vista_miguel, name='miguel'),
    path('gustavo/', views.vista_gustavo, name='gustavo'),
    path('iztacalco/', views.vista_iztacalco, name='iztacalco'),
    path('iztapalapa/', views.vista_iztapalapa, name='iztapalapa'),
    path('magda/', views.vista_magda, name='magda'),
    path('milpa/', views.vista_milpa, name='milpa'),
    path('tlahuac/', views.vista_tlahuac, name='tlahuac'),
    path('tlalpan/', views.vista_tlalpan, name='tlalpan'),
    path('venustiano/', views.vista_venustiano, name='venustiano'),

    # Panel admin Gentelella
    path('admin-panel/<str:page>/', views.gentelella_view, name='gentelella_page'),

    # Vista de documentación
    path('doc/', views.vista_documentacion, name='documentacion'),
]

# Archivos media (imágenes)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
