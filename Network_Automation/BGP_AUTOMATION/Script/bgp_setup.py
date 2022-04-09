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
      .2         .1 |           |.1        30.30.30.0/30      .2 |          |.1            .2
 IXIA---------------|    R1     |--------------------------------|    R2    |----------------IXIA
     40.40.40.0/30  |           |                                |          | 140.140.140.0/30
                    +-----------+                                +----------+
                     AS 65536                                      AS 65536
##########################################################################################################
'''

import pdb, re, time


class Router_setup_info():

    def topology_info(self):
        self.router1 = dict(host='10.121.233.6',
                            port=830,
                            username='diag',
                            password='ciena123',
                            hostkey_verify=False,
                            port1=7,
                            port2=1)

        self.router2 = dict(host='10.121.233.9',
                            port=830,
                            username='diag',
                            password='ciena123',
                            hostkey_verify=False,
                            port1=7,
                            port2=1)

        self.ixia_port1 = {'id': '1/12/4',
                           'hostName': "10.121.244.242",
                           'ixClientIxNetTclServIp': 'hawv-eit-8.ciena.com',
                           'ixTclHost': "hawv-eit-8.ciena.com",
                           'ixClientIxOsVer': '9.12',
                           'ixClientIxOsVer': '9.12',
                           'ixClientIxNetTclServPort': '8009'}

        self.ixia_port2 = {'id': '1/12/7',
                           'hostName': "10.121.244.242",
                           'ixClientIxNetTclServIp': 'hawv-eit-8.ciena.com',
                           'ixTclHost': "hawv-eit-8.ciena.com",
                           'ixClientIxOsVer': '9.12',
                           'ixClientIxOsVer': '9.12',
                           'ixClientIxNetTclServPort': '8009'}

        # accessing device list
        self.device_list = [self.router1, self.router2]
        self.ixia_port_list = [self.ixia_port1['id'], self.ixia_port2['id']]
