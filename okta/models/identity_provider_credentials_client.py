"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject


class IdentityProviderCredentialsClient(
    OktaObject
):
    """
    A class for IdentityProviderCredentialsClient objects.
    """

    def __init__(self, config=None):
        if config:
            self.client_id = config["clientId"]\
                if "clientId" in config else None
            self.client_secret = config["clientSecret"]\
                if "clientSecret" in config else None
        else:
            self.client_id = None
            self.client_secret = None

    def request_format(self):
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
