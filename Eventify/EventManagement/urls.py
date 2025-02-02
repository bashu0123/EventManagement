from django.urls import path
from . import views

urlpatterns = [
    path("EventManagement/", views.index, name="EventManagementHome"),
    path("about/", views.about, name="AboutUs"),
    path("EventManagement/contact/", views.contact, name="ContactUS"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("EventManagement/products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
