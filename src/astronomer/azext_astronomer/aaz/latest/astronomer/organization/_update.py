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
    "astronomer organization update",
)
class Update(AAZCommand):
    """Update the Azure resource configuration for an Astronomer organization

    :example: Update a OrganizationResource
        az astronomer organization update -g MyResourceGroup -n MyAstronomerOrganization --tags key1=value1
    """

    _aaz_info = {
        "version": "2023-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/astronomer.astro/organizations/{}", "2023-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.organization_name = AAZStrArg(
            options=["-n", "--name", "--organization-name"],
            help="Name of the Organizations resource",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_\\-.: ]*$",
                max_length=50,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Properties",
            help="The managed service identities assigned to this resource.",
        )
        _args_schema.partner_organization = AAZObjectArg(
            options=["--partner-organization"],
            arg_group="Properties",
            help="Organization properties",
        )
        _args_schema.user = AAZObjectArg(
            options=["--user"],
            arg_group="Properties",
            help="Details of the user.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Properties",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            required=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        partner_organization = cls._args_schema.partner_organization
        partner_organization.organization_id = AAZStrArg(
            options=["organization-id"],
            help="Organization Id in partner's system",
        )
        partner_organization.organization_name = AAZStrArg(
            options=["organization-name"],
            help="Organization name in partner's system",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_\\-.: ]*$",
                max_length=50,
                min_length=1,
            ),
        )
        partner_organization.single_sign_on_properties = AAZObjectArg(
            options=["single-sign-on-properties"],
            help="Single Sign On properties for the organization",
        )
        partner_organization.workspace_id = AAZStrArg(
            options=["workspace-id"],
            help="Workspace Id in partner's system",
        )
        partner_organization.workspace_name = AAZStrArg(
            options=["workspace-name"],
            help="Workspace name in partner's system",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_\\-.: ]*$",
                max_length=50,
                min_length=1,
            ),
        )

        single_sign_on_properties = cls._args_schema.partner_organization.single_sign_on_properties
        single_sign_on_properties.aad_domains = AAZListArg(
            options=["aad-domains"],
            help="List of AAD domains fetched from Microsoft Graph for user.",
        )
        single_sign_on_properties.enterprise_app_id = AAZStrArg(
            options=["enterprise-app-id"],
            help="AAD enterprise application Id used to setup SSO",
        )
        single_sign_on_properties.single_sign_on_state = AAZStrArg(
            options=["single-sign-on-state"],
            help="State of the Single Sign On for the organization",
            enum={"Disable": "Disable", "Enable": "Enable", "Initial": "Initial"},
        )
        single_sign_on_properties.single_sign_on_url = AAZStrArg(
            options=["single-sign-on-url"],
            help="URL for SSO to be used by the partner to redirect the user to their system",
        )

        aad_domains = cls._args_schema.partner_organization.single_sign_on_properties.aad_domains
        aad_domains.Element = AAZStrArg()

        user = cls._args_schema.user
        user.email_address = AAZStrArg(
            options=["email-address"],
            help="Email address of the user",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\\.)+[A-Za-z]{2,}$",
            ),
        )
        user.first_name = AAZStrArg(
            options=["first-name"],
            help="First name of the user",
        )
        user.last_name = AAZStrArg(
            options=["last-name"],
            help="Last name of the user",
        )
        user.phone_number = AAZStrArg(
            options=["phone-number"],
            help="User's phone number",
        )
        user.upn = AAZStrArg(
            options=["upn"],
            help="User's principal name",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.OrganizationsUpdate(ctx=self.ctx)()
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

    class OrganizationsUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Astronomer.Astro/organizations/{organizationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "organizationName", self.ctx.args.organization_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2023-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZIdentityObjectType, ".identity")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("partnerOrganizationProperties", AAZObjectType, ".partner_organization")
                properties.set_prop("user", AAZObjectType, ".user")

            partner_organization_properties = _builder.get(".properties.partnerOrganizationProperties")
            if partner_organization_properties is not None:
                partner_organization_properties.set_prop("organizationId", AAZStrType, ".organization_id")
                partner_organization_properties.set_prop("organizationName", AAZStrType, ".organization_name")
                partner_organization_properties.set_prop("singleSignOnProperties", AAZObjectType, ".single_sign_on_properties")
                partner_organization_properties.set_prop("workspaceId", AAZStrType, ".workspace_id")
                partner_organization_properties.set_prop("workspaceName", AAZStrType, ".workspace_name")

            single_sign_on_properties = _builder.get(".properties.partnerOrganizationProperties.singleSignOnProperties")
            if single_sign_on_properties is not None:
                single_sign_on_properties.set_prop("aadDomains", AAZListType, ".aad_domains")
                single_sign_on_properties.set_prop("enterpriseAppId", AAZStrType, ".enterprise_app_id")
                single_sign_on_properties.set_prop("singleSignOnState", AAZStrType, ".single_sign_on_state")
                single_sign_on_properties.set_prop("singleSignOnUrl", AAZStrType, ".single_sign_on_url")

            aad_domains = _builder.get(".properties.partnerOrganizationProperties.singleSignOnProperties.aadDomains")
            if aad_domains is not None:
                aad_domains.set_elements(AAZStrType, ".")

            user = _builder.get(".properties.user")
            if user is not None:
                user.set_prop("emailAddress", AAZStrType, ".email_address")
                user.set_prop("firstName", AAZStrType, ".first_name")
                user.set_prop("lastName", AAZStrType, ".last_name")
                user.set_prop("phoneNumber", AAZStrType, ".phone_number")
                user.set_prop("upn", AAZStrType, ".upn")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _schema_on_200.identity = AAZIdentityObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.marketplace = AAZObjectType(
                flags={"required": True},
            )
            properties.partner_organization_properties = AAZObjectType(
                serialized_name="partnerOrganizationProperties",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.user = AAZObjectType(
                flags={"required": True},
            )

            marketplace = cls._schema_on_200.properties.marketplace
            marketplace.offer_details = AAZObjectType(
                serialized_name="offerDetails",
                flags={"required": True},
            )
            marketplace.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"required": True},
            )
            marketplace.subscription_status = AAZStrType(
                serialized_name="subscriptionStatus",
            )

            offer_details = cls._schema_on_200.properties.marketplace.offer_details
            offer_details.offer_id = AAZStrType(
                serialized_name="offerId",
                flags={"required": True},
            )
            offer_details.plan_id = AAZStrType(
                serialized_name="planId",
                flags={"required": True},
            )
            offer_details.plan_name = AAZStrType(
                serialized_name="planName",
            )
            offer_details.publisher_id = AAZStrType(
                serialized_name="publisherId",
                flags={"required": True},
            )
            offer_details.term_id = AAZStrType(
                serialized_name="termId",
            )
            offer_details.term_unit = AAZStrType(
                serialized_name="termUnit",
            )

            partner_organization_properties = cls._schema_on_200.properties.partner_organization_properties
            partner_organization_properties.organization_id = AAZStrType(
                serialized_name="organizationId",
            )
            partner_organization_properties.organization_name = AAZStrType(
                serialized_name="organizationName",
                flags={"required": True},
            )
            partner_organization_properties.single_sign_on_properties = AAZObjectType(
                serialized_name="singleSignOnProperties",
            )
            partner_organization_properties.workspace_id = AAZStrType(
                serialized_name="workspaceId",
            )
            partner_organization_properties.workspace_name = AAZStrType(
                serialized_name="workspaceName",
            )

            single_sign_on_properties = cls._schema_on_200.properties.partner_organization_properties.single_sign_on_properties
            single_sign_on_properties.aad_domains = AAZListType(
                serialized_name="aadDomains",
            )
            single_sign_on_properties.enterprise_app_id = AAZStrType(
                serialized_name="enterpriseAppId",
            )
            single_sign_on_properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            single_sign_on_properties.single_sign_on_state = AAZStrType(
                serialized_name="singleSignOnState",
            )
            single_sign_on_properties.single_sign_on_url = AAZStrType(
                serialized_name="singleSignOnUrl",
            )

            aad_domains = cls._schema_on_200.properties.partner_organization_properties.single_sign_on_properties.aad_domains
            aad_domains.Element = AAZStrType()

            user = cls._schema_on_200.properties.user
            user.email_address = AAZStrType(
                serialized_name="emailAddress",
                flags={"required": True},
            )
            user.first_name = AAZStrType(
                serialized_name="firstName",
                flags={"required": True},
            )
            user.last_name = AAZStrType(
                serialized_name="lastName",
                flags={"required": True},
            )
            user.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            user.upn = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""


__all__ = ["Update"]
