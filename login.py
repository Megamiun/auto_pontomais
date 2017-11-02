#!/usr/bin/env python3

import requests

def sign_in():
    return requests.post(get_url(), data = get_login_json(), headers = get_headers_for_json())

def get_url():
    return 'https://api.pontomaisweb.com.br/api/auth/sign_in'

def get_login_json():
    return open("./config.yml").read()

def get_headers_for_json():
    return { 'Content-Type' : 'application/json;charset=utf-8' }
