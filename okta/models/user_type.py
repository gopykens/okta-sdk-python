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


class UserType:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.created = config["created"]
            self.created_by = config["createdBy"]
            self.default = config["default"]
            self.description = config["description"]
            self.display_name = config["displayName"]
            self.id = config["id"]
            self.last_updated = config["lastUpdated"]
            self.last_updated_by = config["lastUpdatedBy"]
            self.name = config["name"]
        else:
            self.links = None
            self.created = None
            self.created_by = None
            self.default = None
            self.description = None
            self.display_name = None
            self.id = None
            self.last_updated = None
            self.last_updated_by = None
            self.name = None

# End of File Generation
