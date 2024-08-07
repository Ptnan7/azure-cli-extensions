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
    "oracle-database autonomous-database backup update",
)
class Update(AAZCommand):
    """Update a AutonomousDatabaseBackup

    :example: ADBS Backup Update
        az oracle-database autonomous-database backup create --autonomousdatabasename <ADBS name> --resource-group <resource_group> --adbbackupid <id> --retention-period-in-days <days>
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/oracle.database/autonomousdatabases/{}/autonomousdatabasebackups/{}", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.adbbackupid = AAZStrArg(
            options=["-n", "--name", "--adbbackupid"],
            help="AutonomousDatabaseBackup id",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern=".*",
            ),
        )
        _args_schema.autonomousdatabasename = AAZStrArg(
            options=["--autonomousdatabasename"],
            help="The database name.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern=".*",
                max_length=30,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.retention_period_in_days = AAZIntArg(
            options=["--retention-days", "--retention-period-in-days"],
            arg_group="Properties",
            help="Retention period, in days, for long-term backups.",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=3650,
                minimum=60,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AutonomousDatabaseBackupsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AutonomousDatabaseBackupsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AutonomousDatabaseBackupsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/autonomousDatabases/{autonomousdatabasename}/autonomousDatabaseBackups/{adbbackupid}",
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
                    "adbbackupid", self.ctx.args.adbbackupid,
                    required=True,
                ),
                **self.serialize_url_param(
                    "autonomousdatabasename", self.ctx.args.autonomousdatabasename,
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
                    "api-version", "2023-09-01",
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
            _UpdateHelper._build_schema_autonomous_database_backup_read(cls._schema_on_200)

            return cls._schema_on_200

    class AutonomousDatabaseBackupsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/autonomousDatabases/{autonomousdatabasename}/autonomousDatabaseBackups/{adbbackupid}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "adbbackupid", self.ctx.args.adbbackupid,
                    required=True,
                ),
                **self.serialize_url_param(
                    "autonomousdatabasename", self.ctx.args.autonomousdatabasename,
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
                    "api-version", "2023-09-01",
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
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_autonomous_database_backup_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("retentionPeriodInDays", AAZIntType, ".retention_period_in_days")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_autonomous_database_backup_read = None

    @classmethod
    def _build_schema_autonomous_database_backup_read(cls, _schema):
        if cls._schema_autonomous_database_backup_read is not None:
            _schema.id = cls._schema_autonomous_database_backup_read.id
            _schema.name = cls._schema_autonomous_database_backup_read.name
            _schema.properties = cls._schema_autonomous_database_backup_read.properties
            _schema.system_data = cls._schema_autonomous_database_backup_read.system_data
            _schema.type = cls._schema_autonomous_database_backup_read.type
            return

        cls._schema_autonomous_database_backup_read = _schema_autonomous_database_backup_read = AAZObjectType()

        autonomous_database_backup_read = _schema_autonomous_database_backup_read
        autonomous_database_backup_read.id = AAZStrType(
            flags={"read_only": True},
        )
        autonomous_database_backup_read.name = AAZStrType(
            flags={"read_only": True},
        )
        autonomous_database_backup_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        autonomous_database_backup_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        autonomous_database_backup_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_autonomous_database_backup_read.properties
        properties.autonomous_database_ocid = AAZStrType(
            serialized_name="autonomousDatabaseOcid",
        )
        properties.backup_type = AAZStrType(
            serialized_name="backupType",
        )
        properties.database_size_in_tbs = AAZFloatType(
            serialized_name="databaseSizeInTbs",
            flags={"read_only": True},
        )
        properties.db_version = AAZStrType(
            serialized_name="dbVersion",
            flags={"read_only": True},
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
        )
        properties.is_automatic = AAZBoolType(
            serialized_name="isAutomatic",
            flags={"read_only": True},
        )
        properties.is_restorable = AAZBoolType(
            serialized_name="isRestorable",
            flags={"read_only": True},
        )
        properties.lifecycle_details = AAZStrType(
            serialized_name="lifecycleDetails",
            flags={"read_only": True},
        )
        properties.lifecycle_state = AAZStrType(
            serialized_name="lifecycleState",
        )
        properties.ocid = AAZStrType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.retention_period_in_days = AAZIntType(
            serialized_name="retentionPeriodInDays",
        )
        properties.size_in_tbs = AAZFloatType(
            serialized_name="sizeInTbs",
            flags={"read_only": True},
        )
        properties.time_available_til = AAZStrType(
            serialized_name="timeAvailableTil",
            flags={"read_only": True},
        )
        properties.time_ended = AAZStrType(
            serialized_name="timeEnded",
            flags={"read_only": True},
        )
        properties.time_started = AAZStrType(
            serialized_name="timeStarted",
            flags={"read_only": True},
        )

        system_data = _schema_autonomous_database_backup_read.system_data
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

        _schema.id = cls._schema_autonomous_database_backup_read.id
        _schema.name = cls._schema_autonomous_database_backup_read.name
        _schema.properties = cls._schema_autonomous_database_backup_read.properties
        _schema.system_data = cls._schema_autonomous_database_backup_read.system_data
        _schema.type = cls._schema_autonomous_database_backup_read.type


__all__ = ["Update"]
