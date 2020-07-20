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
from okta.models.catalog_application_status\
    import CatalogApplicationStatus


class CatalogApplication(
    OktaObject
):
    """
    A class for CatalogApplication objects.
    """

    def __init__(self, config=None):
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.category = config["category"]\
                if "category" in config else None
            self.description = config["description"]\
                if "description" in config else None
            self.display_name = config["displayName"]\
                if "displayName" in config else None
            self.features = config["features"]\
                if "features" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.sign_on_modes = config["signOnModes"]\
                if "signOnModes" in config else None
            if "status" in config:
                if isinstance(config["status"],
                              CatalogApplicationStatus):
                    self.status = config["status"]
                else:
                    self.status = CatalogApplicationStatus(
                        config["status"]
                    )
            else:
                self.status = None
            self.verification_status = config["verificationStatus"]\
                if "verificationStatus" in config else None
            self.website = config["website"]\
                if "website" in config else None
        else:
            self.links = None
            self.category = None
            self.description = None
            self.display_name = None
            self.features = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.sign_on_modes = None
            self.status = None
            self.verification_status = None
            self.website = None

    def request_format(self):
        return {
            "_links": self.links,
            "category": self.category,
            "description": self.description,
            "displayName": self.display_name,
            "features": self.features,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "signOnModes": self.sign_on_modes,
            "status": self.status,
            "verificationStatus": self.verification_status,
            "website": self.website
        }
