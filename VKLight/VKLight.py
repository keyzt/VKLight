#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2020 Ivan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import requests


host = "api.vk.me"
proxyHost = "v-api-proxy.xtrafrancyz.net"
apiVersion = "5.125"

userAgent = {'user-agent': 'VKAndroidApp/6.2.1 (5112)'}



class VKLight:
    """VKLight - Light wrapper for VK's API"""

    def __init__(self, param: dict = dict()):
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

    def __call__(self, method:str, args:dict=dict()):
        return self.call(method, args)


    def call(self, method:str, args:dict=dict()) -> dict:
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
            raise VKLightException(f"{resp}")

        return resp
    
    def execute(self, code:str=""):
        """Calls Execute method
           Learn More: https://vk.com/dev/execute
           
           param:code= VKScript code 
        """
        return self.call("execute", {"code": code})

    def __v(self, key, dict_data: dict):
        return dict_data[key] if key in dict_data else ""



class VKLightException(Exception):
    """ """
    pass