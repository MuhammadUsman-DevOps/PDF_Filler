from datetime import datetime

from django.shortcuts import render, redirect


def dashboard(request):
    return render(request, template_name="dashboard/dashboard.html")


def co_trust_protector_only_default_ebinder(request):
    trust_name = ""
    trustee_name = ""
    date = ""
    trust_protector_name = ""
    co_trust_protector_name = ""
    trustee_gender = ""
    successor_trust_protector_name = ""
    coin_inventory = ""
    country_name = ""
    beneficiary_1 = ""
    beneficiary_2 = ""
    beneficiary_3 = ""
    street_address = ""
    address_city = ""
    state_abbriviation = ""
    zip_code = ""

    if request.method == "POST":
        trust_name = request.POST.get("trust_name")
        trustee_name = request.POST.get("trustee_name")
        date_new = request.POST.get("date")
        trust_protector_name = request.POST.get("trust_protector_name")
        co_trust_protector_name = request.POST.get("co_trust_protector_name")
        trustee_gender = request.POST.get("trustee_gender")
        successor_trust_protector_name = request.POST.get("successor_trust_protector_name")
        coin_inventory = request.POST.get("coin_inventory")
        country_name = request.POST.get("country_name")
        beneficiary_1 = request.POST.get("beneficiary_1")
        beneficiary_2 = request.POST.get("beneficiary_2")
        beneficiary_3 = request.POST.get("beneficiary_3")
        street_address = request.POST.get("street_address")
        address_city = request.POST.get("address_city")
        state_abbriviation = request.POST.get("state_abbriviation")
        zip_code = request.POST.get("zip_code")
        state = request.POST.get("state")
        date_new = datetime.strptime(date_new, '%Y-%m-%d')
        context = {
            "trust_name": trust_name,
            "trustee_name": trustee_name,
            "date": date_new,
            "trust_protector_name": trust_protector_name,
            "co_trust_protector_name": co_trust_protector_name,
            "trustee_gender": trustee_gender,
            "successor_trust_protector_name": successor_trust_protector_name,
            "coin_inventory": coin_inventory,
            "country_name": country_name,
            "beneficiary_1": beneficiary_1,
            "beneficiary_2": beneficiary_2,
            "beneficiary_3": beneficiary_3,
            "street_address": street_address,
            "address_city": address_city,
            "state_abbriviation": state_abbriviation,
            "zip_code": zip_code,
            "state": state,
        }

        return render(request, template_name="documents/CO-TRUST PROTECTOR ONLY DEFAULT EBINDER.html", context=context)

    return render(request, template_name="filler/co_trust_protector_only_default_ebinder.html")
<span class="ffe fc1">T<span class="_ _0"></span>RUST <span class="_ _1"></span>NAME<span class="fc0"> <span class="_ _3"></span>P<span class="_ _0"></span>RIVATE <span class="_ _3"></span>T<span class="_ _0"></span>RUST<span class="fff">” <span class="_ _1"></span>and <span class="_ _3"></span>“<span class="ffe fc1">T<span class="_ _0"></span>RUSTEE <span class="_ _1"></span>NAME<span class="fff fc0">” <span class="_ _3"></span>is the<span class="_ _1"></span><span class="ffd"> <span class="_ _1"></span>designated </span></span></span></span></span></span>

def co_trustee_co_protector_default_ebinder(request):
    if request.method == "POST":
        trust_name = request.POST.get("trust_name")
        trustee_name = request.POST.get("trustee_name")
        co_trustee_name = request.POST.get("co_trustee_name")
        date_new = request.POST.get("date")
        trust_protector_name = request.POST.get("trust_protector_name")
        co_trust_protector_name = request.POST.get("co_trust_protector_name")
        trustee_gender = request.POST.get("trustee_gender")
        successor_trust_protector_name = request.POST.get("successor_trust_protector_name")
        coin_inventory = request.POST.get("coin_inventory")
        country_name = request.POST.get("country_name")
        beneficiary_1 = request.POST.get("beneficiary_1")
        beneficiary_2 = request.POST.get("beneficiary_2")
        street_address = request.POST.get("street_address")
        address_city = request.POST.get("address_city")
        state_abbriviation = request.POST.get("state_abbriviation")
        zip_code = request.POST.get("zip_code")
        state = request.POST.get("state")
        date_new = datetime.strptime(date_new, '%Y-%m-%d')
        context = {
            "trust_name": trust_name,
            "trustee_name": trustee_name,
            "co_trustee_name": co_trustee_name,
            "date": date_new,
            "trust_protector_name": trust_protector_name,
            "co_trust_protector_name": co_trust_protector_name,
            "trustee_gender": trustee_gender,
            "successor_trust_protector_name": successor_trust_protector_name,
            "coin_inventory": coin_inventory,
            "country_name": country_name,
            "beneficiary_1": beneficiary_1,
            "beneficiary_2": beneficiary_2,
            "street_address": street_address,
            "address_city": address_city,
            "state_abbriviation": state_abbriviation,
            "zip_code": zip_code,
            "state": state,
        }

        return render(request, template_name="documents/CO-TRUSTEE _ CO-PROTECTOR DEFAULT EBINDER.html",
                      context=context)

    return render(request, template_name="filler/co_trustee_co_protector_default_ebinder.html")


def test(request):
    context = {
        "trust_name": "trust_name",
        "trustee_name": "trustee_name",
        "date": "date",
        "trust_protector_name": "trust_protector_name",
        "co_trust_protector_name": "co_trust_protector_name",
        "trustee_gender": "trustee_gender",
        "successor_trust_protector_name": "successor_trust_protector_name",
        "coin_inventory": "coin_inventory",
        "country_name": "country_name",
        "beneficiary_1": "beneficiary_1",
        "beneficiary_2": "beneficiary_2",
        "beneficiary_3": "beneficiary_3",
        "street_address": "street_address",
        "address_city": "address_city",
        "state_abbriviation": "state_abbriviation",
        "zip_code": "zip_code",
    }
    return render(request, template_name="documents/CO-TRUST PROTECTOR ONLY DEFAULT EBINDER.html", context=context)
