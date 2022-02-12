from django.urls import path
from home.views import home, about, portfolio, contact_us, blog, blog_post, Extra

app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("Extra/", Extra, name="Extra"),
    path("portfolio/", portfolio, name="portfolio"),
    path("contact_us/", contact_us, name="contact_us"),
    path("blog/", blog, name="blog"),
    path("blog_post/<slug>", blog_post, name="blog_post"),
]


