from django.urls import path, include
from game.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("memu/", include("game.urls.memu.index")),
    path("playground/", include("game.urls.playground.index")),
    path("settings", include("game.urls.settings.index")),
]

