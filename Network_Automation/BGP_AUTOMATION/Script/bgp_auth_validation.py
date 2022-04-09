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
import sys
import logging
import time

import kwargs as kwargs

sys.path.insert(0, 'C:\\Users\\mrusia\\Desktop\\Network_Automation\\BGP_AUTOMATION\\Library\\')
from bgp_setup import RouterSetupInfo
from bgp_lib import BgpLib
from utility import Utility
from bgp_rpc_data import BgpRpcData
log = logging.getLogger(__name__)
try:
    from ncclient import manager
except ImportError as ie:
    print("It cannot import module and submodule, please install it via pip install ncclient command", ie)
    sys.exit(1)

logging.basicConfig(filename="bgp_auth_validation.log", level=logging.DEBUG)


class Bgp_Auth_validation(RouterSetupInfo, BgpLib, Utility, BgpRpcData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.testArgs = kwargs
        self.initLib()
        self.testInit()

    def testInit(self, desc_="This proc will create interface connection to DUT's"):
        self.dut1 = self.create_session(self.router1, session_type="yui")
        self.dut2 = self.create_session(self.router2, session_type="yui")

    def initLib(self, desc_="This proc will initialize the library code from other class"):
        self.topology_info()
        self.config_data()

    def configure_bgp(self,  desc_=""):
        for data in self.dut1_config_data:
            self.config_bgp(self.dut1, data, desc_="This proc will configure BGP on DUT1")
        for data in self.dut2_config_data:
            self.config_bgp(self.dut2, data, desc_="This proc will configure BGP on DUT2")
        # sleeping for 10 sec for BGP peer to get stabilized
        time.sleep(10)

    def validate_bgp_neighbourship(self, expected_state="Established",  desc_=""):
        bgp_get_rpc = """<bgp:bgp-state xmlns:bgp="http://ciena.com/ns/yang/ciena-bgp"/>"""
        self.validate_bgp_neighbor(self.dut1, bgp_get_rpc, expected_state,  desc_="validate BGP state on DUT1")
        self.validate_bgp_neighbor(self.dut2, bgp_get_rpc, expected_state,  desc_="validate BGP state on DUT2")

    def modify_bgp_peer_password(self,  desc_=""):
        try:
            # modify XML file
            # configure new password for BGP peer
            # dict_data = self.convert_xml_to_dict(self.dut1_d5[0])
            # dict_data['config']['bgp']['instance']['peer']['password'] = new_password
            # modify xml to configure new password
            # new_password_xml = dict2xml(dict_data)
            # self.modify_bgp_data(self.dut1, new_password_xml)
            new_pwd_xml = '''<config>
                                <bgp xmlns="http://ciena.com/ns/yang/ciena-bgp">
                                    <instance>
                                        <as>65536</as>
                                        <peer>
                                            <address>30.30.30.2</address>
                                            <password>admin123</password>
                                            <remote-as>65536</remote-as>
                                        </peer>
                                    </instance>
                                </bgp>
                            </config>'''

            self.modify_bgp_data(self.dut1, new_pwd_xml,  desc_="This proc will send RPC to modify data on DUT1")
            # wait for 30 sec after password modification for session to get established
            time.sleep(30)
        except Exception as error:
            log.exception("Exception in BGP modify_bgp_peer_password step")

    def testCleanup(self, desc_=""):
        print("entering code cleanup")
        # closing connections to both DUT
        self.dut1.close_session()
        self.dut2.close_session()
        # shut down logging
        logging.shutdown()
        if not (self.dut1.connected and self.dut2.connected):
            print("All session terminated")


if __name__ == '__main__':
    """
    Case  : BGP auth verification
                connect to routers
                configure BGP neighbours on both the routers with same passwords.
                verify BGP session is coming up
                configure BGP neighbours on both the routers with different passwords.
                verify BGP session is going down.
                disconnect from the routers
    """
    # This step will create object for class to test BGP authentication functionality
    ni = Bgp_Auth_validation()
    ni.configure_bgp(desc_="This step will configure BGP on provided DUT")
    ni.validate_bgp_neighbourship(expected_state="Established", desc_="This step will validate if bgp neighbours is UP or not")
    ni.modify_bgp_peer_password(desc_="This step will modify peer password and apply the config to DUT ")
    ni.validate_bgp_neighbourship(expected_state="Connect", desc_="This step will validate if bgp neighbours is DOWN or not")
    ni.testCleanup(desc_="This step will cleanup code and disconnect routers")