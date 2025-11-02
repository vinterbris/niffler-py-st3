from faker import Faker

bitcoin_spend_1 = {
        "amount": "100",
        "description": "Bitcoin",
        "category": {"name": "Bitcoin"},
        "spendDate": "2025-10-29T21:53:45.016Z",
        "currency": "RUB",
    }

bitcoin_spend_0_amount = {
        "amount": "0",
        "description": "Bitcoin",
        "category": {"name": "Bitcoin"},
        "spendDate": "2025-10-29T21:53:45.016Z",
        "currency": "RUB",
    }

ethereum_spend_1 = {
        "amount": "100",
        "description": "Ethereum",
        "category": {"name": "Ethereum"},
        "spendDate": "2025-10-29T21:53:45.016Z",
        "currency": "RUB",
    }

fake = Faker()
crypto_name = fake.company()
crypto_name_new = fake.company()
crypto_name_archive = fake.company()

username_edit = fake.name()

amount = 100
category = "Bitcoin"
description = "Description"
date_type_1 = "10/16/2025"
date_type_2 = "Oct 16, 2025"

amount_edit = 5000
category_edit = "Ethereum"
description_edit = "Description"
date_type_1_edit = "11/15/2024"
date_type_2_edit = "Nov 15, 2024"

currency_usd = "USD"
currency_rub = "RUB"
