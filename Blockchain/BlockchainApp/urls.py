from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("AddPeerAction", views.AddPeerAction, name="AddPeerAction"),
	       path("AddPeer.html", views.AddPeer, name="AddPeer"),
	       path("AddToBlock.html", views.AddToBlock, name="AddToBlock"),
	       path("BlockAdded", views.BlockAdded, name="BlockAdded"),
	       path("Transactions.html", views.Transactions, name="Transactions"),
	       path("TransactionsSubmit", views.TransactionsSubmit, name="TransactionsSubmit"),
	       path("ViewChain.html", views.ViewChain, name="ViewChain"),
]