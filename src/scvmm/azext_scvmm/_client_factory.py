# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.client_factory import get_mgmt_service_client
from azure.cli.core import AzCli
from .vendored_sdks.scvmm import ScVmmMgmtClient
from .vendored_sdks.hybridcompute import HybridComputeManagementClient
from .vendored_sdks.resourcegraph import ResourceGraphClient


def cf_scvmm(cli_ctx: AzCli, *_) -> ScVmmMgmtClient:
    """
    Client factory for scvmm clients.
    """
    return get_mgmt_service_client(cli_ctx, ScVmmMgmtClient)


def cf_hybridcompute(cli_ctx: AzCli, *_) -> HybridComputeManagementClient:
    return get_mgmt_service_client(cli_ctx, HybridComputeManagementClient)


def cf_vmmserver(cli_ctx: AzCli, *_):
    """
    Client factory for vmmservers.
    """
    return cf_scvmm(cli_ctx).vmm_servers


def cf_cloud(cli_ctx: AzCli, *_):
    """
    Client factory for clouds.
    """
    return cf_scvmm(cli_ctx).clouds


def cf_virtual_network(cli_ctx: AzCli, *_):
    """
    Client factory for virtual networks.
    """
    return cf_scvmm(cli_ctx).virtual_networks


def cf_virtual_machine_template(cli_ctx: AzCli, *_):
    """
    Client factory for vm templates.
    """
    return cf_scvmm(cli_ctx).virtual_machine_templates


def cf_virtual_machine_instance(cli_ctx: AzCli, *_):
    """
    Client factory for virtual machine instances.
    """
    return cf_scvmm(cli_ctx).virtual_machine_instances


def cf_availability_sets(cli_ctx: AzCli, *_):
    """
    Client factory for availability sets.
    """
    return cf_scvmm(cli_ctx).availability_sets


def cf_inventory_items(cli_ctx: AzCli, *_):
    """
    Client factory for inventory items.
    """
    return cf_scvmm(cli_ctx).inventory_items


def cf_vminstance_guest_agent(cli_ctx: AzCli, *_):
    """
    Client factory for guest agent.
    """
    return cf_scvmm(cli_ctx).guest_agents


def cf_machine(cli_ctx: AzCli, *_):
    """
    Client factory for machines.
    """
    return cf_hybridcompute(cli_ctx).machines


def cf_machine_extension(cli_ctx: AzCli, *_):
    """
    Client factory for machines.
    """
    return cf_hybridcompute(cli_ctx).machine_extensions


def cf_resource_graph(cli_ctx: AzCli, *_) -> ResourceGraphClient:
    """
    Client factory for resource graph.
    """
    # NOTE 1: Adding base_url_bound=False to avoid the following error
    # TypeError: __init__() got multiple values for argument 'base_url'
    # NOTE 2: Hardcoding subscription_bound=False to avoid the following error
    # Bearer token authentication is not permitted for non-TLS protected (non-https) URLs.
    return get_mgmt_service_client(
        cli_ctx,
        ResourceGraphClient,
        subscription_bound=False,
        base_url_bound=False,
    )
