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


class UserIdentifierPolicyRuleCondition(
    OktaObject
):
    """
    A class for UserIdentifierPolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        if config:
            self.attribute = config["attribute"]\
                if "attribute" in config else None
            self.patterns = config["patterns"]\
                if "patterns" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.attribute = None
            self.patterns = None
            self.type = None

    def request_format(self):
        return {
            "attribute": self.attribute,
            "patterns": self.patterns,
            "type": self.type
        }
