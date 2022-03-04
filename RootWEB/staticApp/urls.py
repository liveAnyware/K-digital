from django.urls    import path , include
from staticApp        import views

urlpatterns = [
    # http://127.0.0.1:8000/user/login
    path('index/',          views.index , name='static_index'),
    path('line/',          views.line , name='line_index'),
    path('bar/',            views.bar, name='bar_index'),
    path('order/',          views.order, name='order'),

]



