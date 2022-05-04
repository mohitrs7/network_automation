# network_automation
This repo contains code of basic device interaction with netconf/yang
This validates the following sample test case

BGP auth verification
        connect to routers
        configure BGP neighbours on both the routers with same passwords.
        verify BGP session is coming up
        configure BGP neighbours on both the routers with different passwords.
        verify BGP session is going down.
        disconnect from the routers
        
 Prerequisite :
       Router interfaces are already configured
