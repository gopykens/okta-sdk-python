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
from okta.models.password_policy_recovery_email_properties\
    import PasswordPolicyRecoveryEmailProperties


class PasswordPolicyRecoveryEmail(
    OktaObject
):
    """
    A class for PasswordPolicyRecoveryEmail objects.
    """

    def __init__(self, config=None):
        if config:
            if "properties" in config:
                if isinstance(config["properties"],
                              PasswordPolicyRecoveryEmailProperties):
                    self.properties = config["properties"]
                else:
                    self.properties = PasswordPolicyRecoveryEmailProperties(
                        config["properties"]
                    )
            else:
                self.properties = None
            self.status = config["status"]\
                if "status" in config else None
        else:
            self.properties = None
            self.status = None

    def request_format(self):
        return {
            "properties": self.properties,
            "status": self.status
        }
