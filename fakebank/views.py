from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm

import time
import random
import json

# TODO make actual user authentication system so that you cannot directly go
# to the /account/ url.


def bank_name():
    """Returns the bank name from `config.json`. It is slightly less efficient
    than creating a global BANK_NAME variable, but the existence of this
    function allows for the bank name to be changed and updated without
    restarting the server."""

    with open("config.json") as f:
        config = json.loads(f.read())

    return config["BANK_NAME"]


def index(request):
    # gets the username and password

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            password = request.POST.get("password", "")

            # The scope of my engineering literally knows no bounds
            if password == "hunter2":

                # Make the server seem like it's actually doing something
                time.sleep(1.5)

                return HttpResponseRedirect("/account/")

            else:
                # Make it seem like the server is processing data
                time.sleep(1)
                # Wrong password was entered

                # TODO display error message here
                form = LoginForm()

    else:
        # Somehow used GET request or something instead
        form = LoginForm()

    phrases = [
        "L'investissement est comme une boîte de chocolats, vous ne savez jamais ce que vous allez recevoir.",
        "Acheter haut, pour pouvoir vendre bas.",
        "Consultez le dictionnaire, nous y sommes.",
        "Faire confiance à sa banque devrait être facile, donc c'est ce que vous devriez faire.",
        "Garder tous ses œufs dans le même panier.",
        "3,33% (en répétant bien sûr) de retour sur vos investissements.",
        "Inspecter les éléments pour que vous n'ayez pas à le faire.",
        "Vous le faites, donc nous n'avons pas à le faire.",
        "Nous mettons le D dans l'épargne.",
        "Pas de chemise. Pas de chaussures. Chèque gratuit.",
        "Ne rejoignez pas une secte. Rejoignez notre banque.",
        "Nos contrats sont étanches, donc vous n'avez pas à les lire.",
        "Votre argent est notre argent.",
        "Inspirer une confiance aveugle à nos clients depuis 1963.",
        "En ligne depuis 1741.",
    ]

    context = {
        "form": form,
        "random_phrase": random.choice(phrases),
        "BANK_NAME": bank_name(),
    }

    return render(request, "fakebank/index.html", context)
