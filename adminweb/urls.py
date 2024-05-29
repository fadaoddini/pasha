from django.urls import path, re_path

from adminweb.views import AdminWebIndex, UpdateAppSetting, UpdateSection1, UpdateSection2, UpdateSection3, \
    UpdateSection4, UpdateSection5, UpdateSection6

urlpatterns = [
    path('', AdminWebIndex.as_view(), name='admin_web-index'),
    path('update_app_setting/', UpdateAppSetting.as_view(), name='update-app-setting'),
    path('section1/', UpdateSection1.as_view(), name='update-section1'),
    path('section2/', UpdateSection2.as_view(), name='update-section2'),
    path('section3/', UpdateSection3.as_view(), name='update-section3'),
    path('section4/', UpdateSection4.as_view(), name='update-section4'),
    path('section5/', UpdateSection5.as_view(), name='update-section5'),
    path('section6/', UpdateSection6.as_view(), name='update-section6'),
]