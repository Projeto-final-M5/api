mock_adm = {
    "username": "admin",
    "password": "senhaforte",
    "birth": "2010-10-20",
    "email": "adm@adm.com",
}

mock_user = {
    "username": "user",
    "password": "senhaforte",
    "birth": "2000-08-12",
    "email": "user@user.com",
}

mock_address = {
    "district": "Sua Casa",
    "zip_code": "10101010",
    "number": "31C",
    "additional_data": "informações adicionais",
}

mock_user_post = {**mock_user, "address": mock_address}

mock_adm_post = {
    **mock_adm,
    "address": mock_address,
}

mock_adm_login = {
    "username": "admin",
    "password": "senhaforte",
}

mock_user_login = {
    "username": "user",
    "password": "senhaforte",
}

# mock_borrowed = {
#     "shipping_method": "Retirada",
# }
