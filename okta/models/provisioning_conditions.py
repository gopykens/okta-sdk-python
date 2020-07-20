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
from okta.models.provisioning_deprovisioned_condition\
    import ProvisioningDeprovisionedCondition
from okta.models.provisioning_suspended_condition\
    import ProvisioningSuspendedCondition


class ProvisioningConditions(
    OktaObject
):
    """
    A class for ProvisioningConditions objects.
    """

    def __init__(self, config=None):
        if config:
            if "deprovisioned" in config:
                if isinstance(config["deprovisioned"],
                              ProvisioningDeprovisionedCondition):
                    self.deprovisioned = config["deprovisioned"]
                else:
                    self.deprovisioned = ProvisioningDeprovisionedCondition(
                        config["deprovisioned"]
                    )
            else:
                self.deprovisioned = None
            if "suspended" in config:
                if isinstance(config["suspended"],
                              ProvisioningSuspendedCondition):
                    self.suspended = config["suspended"]
                else:
                    self.suspended = ProvisioningSuspendedCondition(
                        config["suspended"]
                    )
            else:
                self.suspended = None
        else:
            self.deprovisioned = None
            self.suspended = None

    def request_format(self):
        return {
            "deprovisioned": self.deprovisioned,
            "suspended": self.suspended
        }
