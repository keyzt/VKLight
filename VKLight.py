#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
VKLight - Light wrapper for VK's API

@author=Ivan
@version=1.1
"""

__author__ = 'Ivan'
__version__ = "1.1"


import requests


host = "api.vk.me"
proxyHost = "v-api-proxy.xtrafrancyz.net"
apiVersion = "5.125"

userAgent = {'user-agent': 'VKAndroidApp/6.2.1 (5112)'}



class VKLight:
    """VKLight - Light wrapper for VK's API"""

    def __init__(self, param= dict()):
        """
        :param: Dictionary including  fields such as 'access_token' (required), 'v' and etc.

        For example: dict(access_token="your access_token", v='5.125', lng="en", host="api.vk.me")
        """
        super(VKLight, self).__init__()

        self.access_token = self.__v("access_token", param) or "en"
        self.apiVersion = self.__v("v", param) or apiVersion
        self.lng = self.__v("lng", param) or ""
        
        self.host = proxyHost if self.__v("proxy", param) else host
        self.host = param['host'] if self.__v("host", param) else host
        self.baseURL = f"https://{self.host}/method/"
        self.url_param = dict(lang=self.lng, v=self.apiVersion)

    def __call__(self, method:str, args=dict()):
        return self.call(method, args)


    def call(self, method:str, args=dict()) -> dict:
        """
        Calls VK API methods
        :param method: VK API method name.
        :param args: arguments of this method.
        """
        args['access_token'] = self.access_token

        try:
            resp = requests.post(
                f"{self.baseURL}{method}", 
                data=args,
                params=self.url_param, 
                headers=userAgent, 
                timeout=10
            ).json()

        except Exception as e:
            raise e

        if 'error' in resp:
            raise VKLightError(resp['error']['error_code'], resp['error']['error_msg'])

        return resp
    
    def execute(self, code:str=""):
        """
        Calls Execute method
        Learn More: https://vk.com/dev/execute
           
        param:code= VKScript code 
        """
        return self.call("execute", {"code": code})

    def __v(self, key, dict_data: dict):
        return dict_data[key] if key in dict_data else ""



class VKLightError(Exception):
    """ VKLight Exception for errros from VK API's """
    def __init__(self, error_code, message):
        """
        :param error_code: Code of Error
        :param message: Error message
        """
        self.message, self.error_code = message, error_code

    def __str__(self):
        return "VKLightError {}: {}".format(self.error_code, self.message)