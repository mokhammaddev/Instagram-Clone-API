from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer, ContactCreateSerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = []


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer


class ContactRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class MyContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(account=self.request.user)
        return qs
