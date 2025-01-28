from django.urls import path, include
from django.contrib import admin
from api.resources import NoteResource
note_resource = NoteResource()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(note_resource.urls)),
]