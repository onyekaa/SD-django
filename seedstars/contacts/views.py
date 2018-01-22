# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import resolve, reverse
from django.utils.safestring import mark_safe

from .models import Contact
from .forms import ContactForm


def list(request):
    # Fetch all existing contacts.
    contacts = Contact.objects.all()

    return render(
        request, 'contacts/list.html', {
            'contacts': contacts
        })


def add(request, id=None):

    """ We'll use this function to manage both new
        and existing entries. If it receives and id,
        then the assumption that a contact is being
        modified. If not, we create a new one.
    """

    form = ContactForm()
    contact = []

    if id:
        # If id, attach contact instance to form
        contact = Contact.objects.get(pk=id)
        form = ContactForm(instance=contact)

    if request.method == 'POST':
        if id:
            # Again, ID check to attach instance to bound form
            form = ContactForm(request.POST, instance=contact)
        else:
            form = ContactForm(request.POST)

        if form.is_valid():
            # If no errors, save form, then redirect to list view.
            form.save()

            return HttpResponseRedirect(reverse('list_contacts'))

    return render(
        request, 'contacts/add.html', {
            'contact': contact,
            'form': form
        })
