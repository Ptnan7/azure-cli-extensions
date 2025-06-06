# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .._resourceTypeValidation import (
    ZoneRedundancyValidationResult,
    register_resource_type,
)
from knack.log import get_logger


# pylint: disable=too-few-public-methods
@register_resource_type("microsoft.recoveryservices")
class microsoft_recoveryservices:
    @staticmethod
    def validate(resource):
        resourceType = resource["type"]
        resourceSubType = resourceType[resourceType.index("/") + 1:]

        _logger = get_logger("microsoft_recoveryservices")
        _logger.debug(
            "Validating Microsoft.recoveryservices resource type: %s", resourceSubType
        )

        # Recovery Services vaults
        if resourceSubType == "vaults":
            # https://learn.microsoft.com/azure/reliability/reliability-backup#availability-zone-support
            # Recovery Services vaults are zone redundant if the storage
            # redundancy was set to ZoneRedundant
            if (
                resource["properties"]["redundancySettings"][
                    "standardTierStorageRedundancy"
                ]
                == "ZoneRedundant"
            ):
                return ZoneRedundancyValidationResult.Yes
            return ZoneRedundancyValidationResult.No

        return ZoneRedundancyValidationResult.Unknown
