#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------------------------------------
PROJECT     : Network Automation
MODULE      : BGP setup information;
FILE        : bgp_setup.py
Author      : Mohit Rusia
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


class RouterSetupInfo():

    def topology_info(self):
        self.router1 = dict(host='',
                            port=830,
                            username='',
                            password='',
                            hostkey_verify=False,
                            port1="",
                            port2="")

        self.router2 = dict(host='',
                            port=830,
                            username='',
                            password='',
                            hostkey_verify=False,
                            port1="",
                            port2="")

        # accessing device list
        self.device_list = [self.router1, self.router2]
