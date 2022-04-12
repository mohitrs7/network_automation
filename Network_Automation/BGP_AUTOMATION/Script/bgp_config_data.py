#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------------------------------------
PROJECT     : Network Automation
MODULE      : BGP setup information;
FILE        : bgp_setup.py
Author      : Mohit Rusia mrusia@ciena.com
-------------------------------------------------------------------------------------------------------------
Copyright XXXXX.
Group:  India
Manager : XXXXX
Copyright 2022
-------------------------------------------------------------------------------------------------------------

progVersion  =       '1.00'
progLastUpdate       =       '...'

Description: This setup file covers router and ixia information (if any)

##########################################################################################################
                    +-----------+                                +----------+
                 .1 |           |.1        30.30.30.0/30      .2 |          |.1
                    |    R1     |--------------------------------|    R2    |
                    |           |                                |          |
                    +-----------+                                +----------+
                     AS 65536                                      AS 65536
##########################################################################################################
'''
from bgp_setup import RouterSetupInfo


class RouterConfigData(RouterSetupInfo):
    def __init__(self):
        self.topology_info()

    def router_data(self):
        self.dut1_intf1_dict = dict(
            name='intf40',
            ipv4='40.40.40.1',
            prefix_length='30',
            netmask='255.255.255.252',
            network='40.40.40.0/30',
            admin_status='true',
            role='data',
            mtu='1500',
            vrf='default',
            ub_type='fd',
            int_type='ip',
            fpName='fp40',
            fd='fd40',
            fp_port=self.router1['port1'],
            vtag='1',
            classifier='vlan40',
            classifier_precedence='10',
            egress_l2_transform='push-vid-40',
            vid='40',
            fd_mode='vpls',
            vlanStack='vtag-stack',
            tpid='tpid-8100',
            untag='false',
            pushpcp='pcp-7',
            untagged_exclude_priority_tagged='',
            src_mac_addr='00:11:01:00:00:01',
            src_mac_addr_step='00:00:00:00:00:01',
            intf_mode='ethernet',
            phy_mode='fiber',
            speed='ether10Gig',
            duplex='full',
            port_rx_mode='capture_and_measure',
            bgpAs='65536',
            remoteAs='4294967295',
            peerAddr='40.40.40.2',
            activate='true',
            neighborState='Established',
            neighbor_type='external',
            bgpNetwork='160.10.0.0/24',
            pathInfo='*>',
            routerId='1.1.1.1',
        )
        self.dut1_intf2_dict = dict(
            name='intf30',
            ipv4='30.30.30.1',
            prefix_length='30',
            netmask='255.255.255.252',
            network='30.30.30.0/30',
            admin_status='true',
            role='data',
            mtu='1500',
            vrf='default',
            ub_type='fd',
            int_type='ip',
            fpName='fp30',
            fd='fd30',
            fp_port=self.router1['port2'],
            vtag='1',
            classifier='vlan30',
            classifier_precedence='10',
            egress_l2_transform='push-vid-30',
            vid='30',
            fd_mode='vpls',
            vlanStack='vtag-stack',
            tpid='tpid-8100',
            untag='false',
            pushpcp='pcp-7',
            untagged_exclude_priority_tagged='',
            bgpAs='65536',
            remoteAs='65536',
            peerAddr='30.30.30.2',
            activate='true',
            neighborState='Established',
        )
        self.dut2_intf1_dict = dict(
            name='intf30',
            ipv4='30.30.30.2',
            prefix_length='30',
            netmask='255.255.255.252',
            network='30.30.30.0/30',
            admin_status='true',
            role='data',
            mtu='1500',
            vrf='default',
            ub_type='fd',
            int_type='ip',
            fpName='fp30',
            fd='fd30',
            fp_port=self.router2['port1'],
            vtag='1',
            classifier='vlan30',
            classifier_precedence='10',
            egress_l2_transform='push-vid-30',
            vid='30',
            fd_mode='vpls',
            vlanStack='vtag-stack',
            tpid='tpid-8100',
            untag='false',
            pushpcp='pcp-7',
            untagged_exclude_priority_tagged='',
            bgpAs='65536',
            remoteAs='65536',
            peerAddr='30.30.30.1',
            activate='true',
            neighborState='Established',
            pathInfo='*>i',
            routerId='2.2.2.2',
        )
        self.dut2_intf2_dict = dict(
            name='intf140',
            ipv4='140.140.140.1',
            prefix_length='30',
            netmask='255.255.255.252',
            network='140.140.140.0/30',
            admin_status='true',
            role='data',
            mtu='1500',
            vrf='default',
            ub_type='fd',
            int_type='ip',
            fpName='fp140',
            fd='fd140',
            fp_port=self.router2['port2'],
            vtag='1',
            classifier='vlan140',
            classifier_precedence='10',
            egress_l2_transform='push-vid-140',
            vid='140',
            fd_mode='vpls',
            vlanStack='vtag-stack',
            tpid='tpid-8100',
            untag='false',
            pushpcp='pcp-7',
            untagged_exclude_priority_tagged='',
            src_mac_addr='00:12:01:00:00:01',
            src_mac_addr_step='00:00:00:00:00:01',
            intf_mode='ethernet',
            phy_mode='fiber',
            speed='ether10Gig',
            duplex='full',
            port_rx_mode='capture_and_measure',
            bgpAs='65536',
            remoteAs='4294967295',
            peerAddr='140.140.140.2',
            activate='true',
            neighborState='Established',
            neighbor_type='external',
        )
