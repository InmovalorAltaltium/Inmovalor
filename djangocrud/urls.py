from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin y autenticación
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),  # Mantenemos el nombre 'signout' como en el original

    # Rutas de recuperación de contraseña
    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='recuperacion/forgotpassword.html',
        email_template_name='recuperacion/password_reset_email.html',
        subject_template_name='recuperacion/password_reset_subject.txt'
    ), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='recuperacion/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='recuperacion/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='recuperacion/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Página de bienvenida y estimaciones
    path('', views.welcome, name='welcome'),
    path('estimaciones/', views.estimaciones, name='estimaciones'),
    path('analisis/', views.analisis, name='analisis'),
    path('honorarios/', views.honorarios_calculator, name='honorarios_calculator'),
    path('resultados/<int:propiedad_id>/', views.mostrar_resultado, name='mostrar_resultado'),
    # Rutas añadidas para reportes
    path('reporte_individual/<int:propiedad_id>/', views.reporte_individual, name='reporte_individual'),
    path('reporte_completo/<int:propiedad_id>/', views.generar_reporte_completo, name='reporte_completo'),

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

    # URL para el acceso de vista de la documentación
    path('doc/', views.vista_documentacion, name='documentacion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)