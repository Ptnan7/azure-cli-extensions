# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# --------------------------------------------------------------------------------------------
# pylint: disable=too-few-public-methods,unnecessary-pass,unused-argument

"""
Internal Network tests scenarios
"""

from azure.cli.testsdk import ScenarioTest

from .config import CONFIG


def setup_scenario1(test):
    """Env setup_scenario1"""
    pass


def cleanup_scenario1(test):
    """Env cleanup_scenario1"""
    pass


def call_scenario1(test):
    """# Testcase: scenario1"""
    setup_scenario1(test)
    step_create(test, checks=[])
    step_update(test, checks=[])
    step_show(test, checks=[])
    step_list_resource_group(test, checks=[])
    step_delete(test, checks=[])
    cleanup_scenario1(test)


def step_create(test, checks=None):
    """internalnetwork create operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric internalnetwork create --resource-group {rg} --l3-isolation-domain-name {l3Domain} --resource-name {name}"
        " --vlan-id {vlanId} --native-ipv4-prefix-limit {nativeIpv4PrefixLimit} --native-ipv6-prefix-limit {nativeIpv6PrefixLimit}"
        " --mtu {mtu} --connected-ipv4-subnets {connectedIpv4Subnets}"
        " --static-route-configuration {staticRouteConf} --bgp-configuration {bgpConf}",
        checks=checks,
    )


def step_update(test, checks=None):
    """internalnetwork update operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric internalnetwork update --resource-group {rg} --resource-name {name} --l3domain {l3Domain} "
        " --connected-ipv4-subnets {updatedConnectedIpv4Subnets}  --static-route-configuration {updatedStaticRouteConf}"
        " --bgp-configuration {updatedBgpConf}  --native-ipv4-prefix-limit {updatedNativeIpv4PrefixLimit}"
        " --native-ipv6-prefix-limit {updatedNativeIpv6PrefixLimit}",
        checks=checks,
    )


def step_show(test, checks=None):
    """internalnetwork show operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric internalnetwork show --resource-name {name} --l3domain {l3Domain} --resource-group {rg}"
    )


def step_list_resource_group(test, checks=None):
    """internalnetwork list by resource group operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric internalnetwork list --resource-group {rg} --l3domain {l3Domain}"
    )


def step_delete(test, checks=None):
    """internalnetwork delete operation"""
    if checks is None:
        checks = []
    test.cmd(
        "az networkfabric internalnetwork delete --resource-name {name} --l3domain {l3Domain} --resource-group {rg}"
    )


class GA_InternalNetworkScenarioTest1(ScenarioTest):
    """Internal Network Scenario test"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs.update(
            {
                "name": CONFIG.get("INTERNAL_NETWORK", "name"),
                "rg": CONFIG.get("INTERNAL_NETWORK", "resource_group"),
                "l3Domain": CONFIG.get("INTERNAL_NETWORK", "l3_domain"),
                "vlanId": CONFIG.get("INTERNAL_NETWORK", "vlan_id"),
                "mtu": CONFIG.get("INTERNAL_NETWORK", "mtu"),
                "extension": CONFIG.get("INTERNAL_NETWORK", "extension"),
                "isMonitoringEnabled": CONFIG.get(
                    "INTERNAL_NETWORK", "is_monitoring_enabled"
                ),
                "connectedIpv4Subnets": CONFIG.get(
                    "INTERNAL_NETWORK", "connected_Ipv4_subnets"
                ),
                "updatedConnectedIpv4Subnets": CONFIG.get(
                    "INTERNAL_NETWORK", "updated_connected_Ipv4_subnets"
                ),
                "staticRouteConf": CONFIG.get("INTERNAL_NETWORK", "static_route_conf"),
                "updatedStaticRouteConf": CONFIG.get(
                    "INTERNAL_NETWORK", "updated_static_route_conf"
                ),
                "bgpConf": CONFIG.get("INTERNAL_NETWORK", "bgp_conf"),
                "updatedBgpConf": CONFIG.get("INTERNAL_NETWORK", "updated_bgp_conf"),
                "importRoutePolicy": CONFIG.get(
                    "INTERNAL_NETWORK", "import_route_policy"
                ),
                "exportRoutePolicy": CONFIG.get(
                    "INTERNAL_NETWORK", "export_route_policy"
                ),
                "nativeIpv4PrefixLimit": CONFIG.get(
                    "INTERNAL_NETWORK", "native_ipv4_prefix_limit"
                ),
                "updatedNativeIpv4PrefixLimit": CONFIG.get(
                    "INTERNAL_NETWORK", "updated_native_ipv4_prefix_limit"
                ),
                "nativeIpv6PrefixLimit": CONFIG.get(
                    "INTERNAL_NETWORK", "native_ipv6_prefix_limit"
                ),
                "updatedNativeIpv6PrefixLimit": CONFIG.get(
                    "INTERNAL_NETWORK", "updated_native_ipv6_prefix_limit"
                ),
            }
        )

    def test_GA_internalnetwork_scenario1(self):
        """test scenario for internalnetwork CRUD operations"""
        call_scenario1(self)
