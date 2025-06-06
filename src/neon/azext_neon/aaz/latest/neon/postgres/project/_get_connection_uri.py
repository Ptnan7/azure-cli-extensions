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
    "neon postgres project get-connection-uri",
)
class GetConnectionUri(AAZCommand):
    """Retrieve the connection URI for a specific Neon Postgres database.

    :example: Get Database Connection URI
        az neon postgres project get-connection-uri --resource-group rgneon --organization-name test-org --project-name entity-name --project-id old-frost-16758796 --branch-id br-spring-field-a8vje3tr --database-name neondb --role-name owner_role --endpoint-id ep-purple-voice-a84wphbw --is-pooled false
    """

    _aaz_info = {
        "version": "2025-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/neon.postgres/organizations/{}/projects/{}/getconnectionuri", "2025-03-01"],
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
        _args_schema.organization_name = AAZStrArg(
            options=["--organization-name"],
            help="Name of the Neon organization.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_\\-.: ]*$",
                max_length=50,
                min_length=1,
            ),
            blank=AAZPromptInput(
                msg="Please provide Neon Organization name:",
            ),
        )
        _args_schema.project_name = AAZStrArg(
            options=["--project-name"],
            help="Name of the Neon project.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^\\S.{0,62}\\S$|^\\S$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the Azure resource group.",
            required=True,
        )

        # define Arg Group "ConnectionUriParameters"

        _args_schema = cls._args_schema
        _args_schema.branch_id = AAZStrArg(
            options=["--branch-id"],
            arg_group="ConnectionUriParameters",
            help="Branch Id associated with this connection",
        )
        _args_schema.database_name = AAZStrArg(
            options=["--database-name"],
            arg_group="ConnectionUriParameters",
            help="Database name associated with this connection",
        )
        _args_schema.endpoint_id = AAZStrArg(
            options=["--endpoint-id"],
            arg_group="ConnectionUriParameters",
            help="the endpoint Id with this connection",
        )
        _args_schema.is_pooled = AAZBoolArg(
            options=["--is-pooled"],
            arg_group="ConnectionUriParameters",
            help="Indicates if the connection is pooled",
        )
        _args_schema.project_id = AAZStrArg(
            options=["--project-id"],
            arg_group="ConnectionUriParameters",
            help="Project Id associated with this connection",
        )
        _args_schema.role_name = AAZStrArg(
            options=["--role-name"],
            arg_group="ConnectionUriParameters",
            help="The role name used for authentication",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ProjectsGetConnectionUri(ctx=self.ctx)()
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

    class ProjectsGetConnectionUri(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Neon.Postgres/organizations/{organizationName}/projects/{projectName}/getConnectionUri",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

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
                    "projectName", self.ctx.args.project_name,
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
                    "api-version", "2025-03-01",
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
            _builder.set_prop("branchId", AAZStrType, ".branch_id")
            _builder.set_prop("databaseName", AAZStrType, ".database_name")
            _builder.set_prop("endpointId", AAZStrType, ".endpoint_id")
            _builder.set_prop("isPooled", AAZBoolType, ".is_pooled")
            _builder.set_prop("projectId", AAZStrType, ".project_id")
            _builder.set_prop("roleName", AAZStrType, ".role_name")

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
            _schema_on_200.branch_id = AAZStrType(
                serialized_name="branchId",
            )
            _schema_on_200.connection_string_uri = AAZStrType(
                serialized_name="connectionStringUri",
                flags={"secret": True, "read_only": True},
            )
            _schema_on_200.database_name = AAZStrType(
                serialized_name="databaseName",
            )
            _schema_on_200.endpoint_id = AAZStrType(
                serialized_name="endpointId",
            )
            _schema_on_200.is_pooled = AAZBoolType(
                serialized_name="isPooled",
            )
            _schema_on_200.project_id = AAZStrType(
                serialized_name="projectId",
            )
            _schema_on_200.role_name = AAZStrType(
                serialized_name="roleName",
            )

            return cls._schema_on_200


class _GetConnectionUriHelper:
    """Helper class for GetConnectionUri"""


__all__ = ["GetConnectionUri"]
