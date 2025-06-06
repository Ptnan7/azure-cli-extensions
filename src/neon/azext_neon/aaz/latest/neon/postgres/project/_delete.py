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
    "neon postgres project delete",
    confirmation="Are you sure you want to perform this operation?",
)
class Delete(AAZCommand):
    """Delete an existing Neon project resource within Azure.

    :example: Delete Neon Project
        az neon postgres project delete --resource-group rgneon --organization-name org-cli-test --project-id old-frost-16758796
    """

    _aaz_info = {
        "version": "2025-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/neon.postgres/organizations/{}/projects/{}", "2025-03-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return None

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
        _args_schema.project_id = AAZStrArg(
            options=["--project-id"],
            help="Id of the Neon project",
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
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ProjectsDelete(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class ProjectsDelete(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)
            if session.http_response.status_code in [204]:
                return self.on_204(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Neon.Postgres/organizations/{organizationName}/projects/{projectName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

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
                    "projectName", self.ctx.args.project_id,
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

        def on_200(self, session):
            pass

        def on_204(self, session):
            pass


class _DeleteHelper:
    """Helper class for Delete"""


__all__ = ["Delete"]
