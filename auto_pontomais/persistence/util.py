def get_headers_for_json():
    """
    :return: Headers for json requests
    """
    return {'Content-Type': 'application/json'}


def get_user_headers(config):
    """
    :param config: Current user configurations
    :return: Json with needed headers
    """
    headers = get_headers_for_json()
    headers.update({
        'uid': config.uid,
        'client': config.client,
        'token-type': 'Bearer',
        'access-token': config.token
    })
    return headers
