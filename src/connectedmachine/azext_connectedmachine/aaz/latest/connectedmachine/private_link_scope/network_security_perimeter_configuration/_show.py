# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "connectedmachine private-link-scope network-security-perimeter-configuration show",
)
class Show(AAZCommand):
    """Get the network security perimeter configuration for a private link scope.

    :example: Sample command for NSP show
        az connectedmachine private-link-scope network-security-perimeter-configuration show --resource-group myResourceGroup --scope-name myPrivateLinkScope --perimeter-name aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee.myAssociation --subscription mySubscription
    """

    _aaz_info = {
        "version": "2024-11-10-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.hybridcompute/privatelinkscopes/{}/networksecurityperimeterconfigurations/{}", "2024-11-10-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.perimeter_name = AAZStrArg(
            options=["-n", "--name", "--perimeter-name"],
            help="The name, in the format {perimeterGuid}.{associationName}, of the Network Security Perimeter resource.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[.]{1}.+$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.scope_name = AAZStrArg(
            options=["--scope-name"],
            help="The name of the Azure Arc PrivateLinkScope resource.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="[a-zA-Z0-9-_\.]+",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NetworkSecurityPerimeterConfigurationsGetByPrivateLinkScope(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkSecurityPerimeterConfigurationsGetByPrivateLinkScope(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/privateLinkScopes/{scopeName}/networkSecurityPerimeterConfigurations/{perimeterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "perimeterName", self.ctx.args.perimeter_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "scopeName", self.ctx.args.scope_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-11-10-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.network_security_perimeter = AAZObjectType(
                serialized_name="networkSecurityPerimeter",
            )
            properties.profile = AAZObjectType()
            properties.provisioning_issues = AAZListType(
                serialized_name="provisioningIssues",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_association = AAZObjectType(
                serialized_name="resourceAssociation",
            )

            network_security_perimeter = cls._schema_on_200.properties.network_security_perimeter
            network_security_perimeter.id = AAZStrType(
                flags={"read_only": True},
            )
            network_security_perimeter.location = AAZStrType(
                flags={"read_only": True},
            )
            network_security_perimeter.perimeter_guid = AAZStrType(
                serialized_name="perimeterGuid",
                flags={"read_only": True},
            )

            profile = cls._schema_on_200.properties.profile
            profile.access_rules = AAZListType(
                serialized_name="accessRules",
                flags={"read_only": True},
            )
            profile.access_rules_version = AAZIntType(
                serialized_name="accessRulesVersion",
                flags={"read_only": True},
            )
            profile.diagnostic_settings_version = AAZIntType(
                serialized_name="diagnosticSettingsVersion",
                flags={"read_only": True},
            )
            profile.enabled_log_categories = AAZListType(
                serialized_name="enabledLogCategories",
                flags={"read_only": True},
            )
            profile.name = AAZStrType(
                flags={"read_only": True},
            )

            access_rules = cls._schema_on_200.properties.profile.access_rules
            access_rules.Element = AAZObjectType()
            _ShowHelper._build_schema_access_rule_read(access_rules.Element)

            enabled_log_categories = cls._schema_on_200.properties.profile.enabled_log_categories
            enabled_log_categories.Element = AAZStrType()

            provisioning_issues = cls._schema_on_200.properties.provisioning_issues
            provisioning_issues.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.provisioning_issues.Element
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True, "read_only": True},
            )

            properties = cls._schema_on_200.properties.provisioning_issues.Element.properties
            properties.description = AAZStrType(
                flags={"read_only": True},
            )
            properties.issue_type = AAZStrType(
                serialized_name="issueType",
                flags={"read_only": True},
            )
            properties.severity = AAZStrType(
                flags={"read_only": True},
            )
            properties.suggested_access_rules = AAZListType(
                serialized_name="suggestedAccessRules",
                flags={"read_only": True},
            )
            properties.suggested_resource_ids = AAZListType(
                serialized_name="suggestedResourceIds",
                flags={"read_only": True},
            )

            suggested_access_rules = cls._schema_on_200.properties.provisioning_issues.Element.properties.suggested_access_rules
            suggested_access_rules.Element = AAZObjectType()
            _ShowHelper._build_schema_access_rule_read(suggested_access_rules.Element)

            suggested_resource_ids = cls._schema_on_200.properties.provisioning_issues.Element.properties.suggested_resource_ids
            suggested_resource_ids.Element = AAZStrType()

            resource_association = cls._schema_on_200.properties.resource_association
            resource_association.access_mode = AAZStrType(
                serialized_name="accessMode",
                flags={"read_only": True},
            )
            resource_association.name = AAZStrType(
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_access_rule_read = None

    @classmethod
    def _build_schema_access_rule_read(cls, _schema):
        if cls._schema_access_rule_read is not None:
            _schema.name = cls._schema_access_rule_read.name
            _schema.properties = cls._schema_access_rule_read.properties
            return

        cls._schema_access_rule_read = _schema_access_rule_read = AAZObjectType()

        access_rule_read = _schema_access_rule_read
        access_rule_read.name = AAZStrType(
            flags={"read_only": True},
        )
        access_rule_read.properties = AAZObjectType(
            flags={"client_flatten": True, "read_only": True},
        )

        properties = _schema_access_rule_read.properties
        properties.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
            flags={"read_only": True},
        )
        properties.direction = AAZStrType(
            flags={"read_only": True},
        )

        address_prefixes = _schema_access_rule_read.properties.address_prefixes
        address_prefixes.Element = AAZStrType()

        _schema.name = cls._schema_access_rule_read.name
        _schema.properties = cls._schema_access_rule_read.properties


__all__ = ["Show"]
