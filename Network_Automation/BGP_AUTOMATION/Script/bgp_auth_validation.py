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

Description: This script will test BGP auth  by changing peer password and checking neighbour

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
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
# sys.path.insert(0, 'C:\\Users\\mrusia\\Desktop\\Network_Automation\\BGP_AUTOMATION\\Library\\')
from bgp_setup import RouterSetupInfo
from bgp_lib import BgpLib
from utility import Utility
from bgp_rpc_data import BgpRpcData
from sqlite_connector import DatabaseConnections
from bgp_config_data import RouterConfigData
log = logging.getLogger(__name__)
try:
    from ncclient import manager
except ImportError as ie:
    print("It cannot import module and submodule, please install it via pip install ncclient command", ie)
    sys.exit(1)

logging.basicConfig(filename="bgp_auth_validation.log", level=logging.INFO, format = '%(asctime)s %(module)s %(levelname)s: %(message)s')


class BgpAuthValidation(BgpLib, Utility, BgpRpcData, DatabaseConnections, RouterConfigData,RouterSetupInfo):
    def __init__(self, *args, **kwargs):
        __name__ = "BgpAuthValidation"
        super().__init__(*args, **kwargs)
        self.testArgs = kwargs
        self.initLib(desc_="This proc will initialize the library code from other class")
        self.testInit(desc_="This proc will create interface connection to DUT's")
        self.initializeDatabase(desc_="This proc will initiate database connection")
        self.start_time = time.time()

    def testInit(self, desc_=""):
        """
            steps :
                    1. create netconf session for DUT1 using ncclient module
                    2. create netconf session for DUT2 using ncclient module
                    3. create ssh  session for DUT1 using paramiko  module
        """
        self.dut1 = self.create_session(self.router1, session_type="yui", desc_="This proc will create netconf session to device 1")
        self.dut2 = self.create_session(self.router2, session_type="yui", desc_="This proc will create netconf session to device 2")
        self.dut1_ssh = self.create_session(self.router1, session_type="ssh", desc_="This proc will create ssh session to device 1")

    def initLib(self, desc_=""):
        """
            steps :
                    1. initialize topology_info library
                    2. initialize config_data library
                    3. initialize router_data library
        """
        self.topology_info()
        self.config_data()
        self.router_data()

    def initializeDatabase(self, desc_=""):
        """
            steps :
                    1. connect tO sqlite DB
                    2. CREATE table
        """
        self._connectDb()
        self._createDatabaseTable()

    def configure_bgp(self,  desc_=""):
        """
            steps :
                    1. configure BGP based on RPC provided on DUT1
                    2. configure BGP based on RPC provided on DUT2
        """
        for data in self.dut1_config_data:
            self.config_bgp(self.dut1, data, desc_="This proc will configure BGP on DUT1")
        for data in self.dut2_config_data:
            self.config_bgp(self.dut2, data, desc_="This proc will configure BGP on DUT2")
        # sleeping for 10 sec for BGP peer to get stabilized
        time.sleep(10)

    def check_interface_up(self,  desc_=""):
        """
            steps :
                    1. ping interface to check if they arte pingable
        """
        self.ping_interface(self.dut1_ssh, destination=self.dut2_intf1_dict['ipv4'])

    def validate_bgp_neighbourship(self, expected_state="Established",   desc_=""):
        """
            steps :
                    1. Validate BGP neighbour using netconf interface in DUT1
                    2. Validate BGP neighbour using netconf interface in dut2
                    3. Validate BGP neighbour using cli interface in dut1
        """
        print("Validate bgp peering from netconf RPC")
        bgp_get_rpc = """<bgp:bgp-state xmlns:bgp="http://ciena.com/ns/yang/ciena-bgp"/>"""
        self.validate_bgp_neighbor(self.dut1, bgp_get_rpc, expected_state,   desc_="validate BGP state on DUT1")
        self.validate_bgp_neighbor(self.dut2, bgp_get_rpc,  expected_state,   desc_="validate BGP state on DUT2")
        print("Validate bgp peering from cli")
        self.get_bgp_state_cli(self.dut1_ssh, "show bgp peers", expected_state, desc_="validate BGP state on DUT1 via CLI")

    def modify_bgp_peer_password(self,  desc_=""):
        """
            steps :
                    1. Modify BGP data based on RPC provided
        """
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
        """
            steps :
                    1. update DATABASE for start and end time for the test
                    2. get detail of run result from DATABASE
                    3. close netconf connections from both DUT
                    4. close database connection
                    5. shut down logging
                    6. close ssh connection for DUT
        """
        print("entering code cleanup")
        self.end_time = time.time()
        # update Database
        self._update_DatabaseTable(self.start_time, self.end_time)
        # fetch details
        self._getRunDetail()
        # total run time for script
        time_taken = self.end_time - self.start_time
        print(f"Total time taken by script to run {BgpAuthValidation.__name__} suit is {time_taken}")
        # closing connections to both DUT
        self.dut1.close_session()
        self.dut2.close_session()
        self.dut1_ssh.close()
        # close DatabaseConnections
        self._dbConnClose()
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
                
    Prerequisites: 
                create classifier , flow-point , forwarding domain and ip interface.
                 
    """
    # This step will create object for class to test BGP authentication functionality
    ni = BgpAuthValidation()
    ni.check_interface_up(desc_="check if connected interface is pingable")
    ni.configure_bgp(desc_="This step will configure BGP on provided DUT")
    ni.validate_bgp_neighbourship(expected_state="Established",
                                  desc_="This step will validate if bgp neighbours is UP or not")
    ni.modify_bgp_peer_password(desc_="This step will modify peer password and apply the config to DUT ")
    ni.validate_bgp_neighbourship(expected_state="Connect", desc_="This step will validate if bgp neighbours is DOWN or not")
    ni.testCleanup(desc_="This step will cleanup code and disconnect routers")
