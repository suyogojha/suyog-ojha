from django.urls import path
from Extra.views import *

app_name = "Extra"

urlpatterns = [
    path("certificates/", certificates, name="certificates"),
    path("projectcode/", projectcode, name="projectcode"),
    path("projectcodedetails/<slug>", projectcodedetails, name="projectcodedetails"),
    path("videosproject/", videosproject, name="videosproject"),
    path("worklist/", worklist, name="worklist"),
    path("Team/", Team, name="Team"),

]


