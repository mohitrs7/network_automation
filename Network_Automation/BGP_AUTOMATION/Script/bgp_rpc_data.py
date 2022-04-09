'''
##########################################################################################################
                    +-----------+                                +----------+
                 .1 |           |.1        30.30.30.0/30      .2 |          |.1
                    |    R1     |--------------------------------|    R2    |
                    |           |                                |          |
                    +-----------+                                +----------+
                     AS 65536                                      AS 65536
##########################################################################################################
'''


class BgpRpcData():

    def config_data(self):
        # DUT1 config rpc data
        self.dut1_d1 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><address-family><afi>ipv4</afi><safi>unicast</safi></address-family></instance></bgp></config>''',
            "cofig BGP global")
        self.dut1_d2 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><router-id>1.1.1.1</router-id></instance></bgp></config>''',
            "config BGP router ID")
        self.dut1_d3 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><address-family><afi>ipv4</afi><safi>unicast</safi><redistribute><protocol>connected</protocol></redistribute></address-family></instance></bgp></config>''',
            "config BGP redistribution protocol")
        self.dut1_d4 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><address-family><afi>ipv4</afi><safi>unicast</safi></address-family></instance></bgp></config>''',
            "config BGP ipv4 type")
        # password RPC for DUT1
        self.dut1_d5 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.2</address><password>ciena123</password><remote-as>65536</remote-as></peer></instance></bgp></config>''',
            "configure BGP peer and password")

        self.dut1_d6 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.2</address><address-family><afi>ipv4</afi><safi>unicast</safi></address-family></peer></instance></bgp></config>''',
            "config BGP peer address family")
        self.dut1_d7 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.2</address><address-family><afi>ipv4</afi><safi>unicast</safi><activate>true</activate></address-family></peer></instance></bgp></config>''',
            "activate BGP peer address family")
        self.dut1_d8 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.2</address><address-family><afi>ipv4</afi><safi>unicast</safi><next-hop-self>true</next-hop-self></address-family></peer></instance></bgp></config>''',
            "configure next hop self for BGP")

        # DUT2 config rpc data
        self.dut2_d1 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><address-family><afi>ipv4</afi><safi>unicast</safi></address-family></instance></bgp></config>''',
            "cofig BGP global")
        self.dut2_d2 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><router-id>2.2.2.2</router-id></instance></bgp></config>''',
            "config BGP router ID")
        self.dut2_d3 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><address-family><afi>ipv4</afi><safi>unicast</safi><redistribute><protocol>connected</protocol></redistribute></address-family></instance></bgp></config>''',
            "config BGP redistribution protocol")
        self.dut2_d4 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><address-family><afi>ipv4</afi><safi>unicast</safi></address-family></instance></bgp></config>''',
            "config BGP ipv4 type")
        # password RPC FOR dut2
        self.dut2_d5 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.1</address><password>ciena123</password><remote-as>65536</remote-as></peer></instance></bgp></config>''',
            "configure BGP peer and password")

        self.dut2_d6 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.1</address><address-family><afi>ipv4</afi><safi>unicast</safi></address-family></peer></instance></bgp></config>''',
            "config BGP peer address family")
        self.dut2_d7 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.1</address><address-family><afi>ipv4</afi><safi>unicast</safi><activate>true</activate></address-family></peer></instance></bgp></config>''',
            "activate BGP peer address family")
        self.dut2_d8 = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.1</address><address-family><afi>ipv4</afi><safi>unicast</safi><next-hop-self>true</next-hop-self></address-family></peer></instance></bgp></config>''',
            "configure next hop self for BGP")

        # password RPC for DUT1
        self.dut1_pwd_rpc = (
            '''<config><bgp xmlns="http://ciena.com/ns/yang/ciena-bgp"><instance><as>65536</as><peer><address>30.30.30.2</address><password>admin123</password><remote-as>65536</remote-as></peer></instance></bgp></config>''',
            "configure BGP peer and password")

        self.dut1_config_data = [self.dut1_d1, self.dut1_d2, self.dut1_d3, self.dut1_d4, self.dut1_d5, self.dut1_d6,
                                 self.dut1_d7, self.dut1_d8]
        self.dut2_config_data = [self.dut2_d1, self.dut2_d2, self.dut2_d3, self.dut2_d4, self.dut2_d5, self.dut2_d6,
                                 self.dut2_d7, self.dut2_d8]
