humanitarian-openstack
======================
* [Workshop Etherpad](https://etherpad.openstack.org/p/ghc-openstack-2014): use it to ask questions and share information.
* [Workshop Requirements](https://github.com/rackerlabs/humanitarian-openstack/blob/master/Workshop%20Requirements.md): minimal requirements for running examples
* [Reference and Reading Resources] (https://github.com/rackerlabs/humanitarian-openstack/blob/master/Reference%20and%20Reading%20Resources.md): find out more about python, OpenStack, GitHub, etc.
* volunteers/
  * volunteer_packet.txt- Instructions for volunteers

* usercases.txt - Example usecases to implement for building fault tolerant, scalable architectures

  
* participants/
  * code/ 
  * keys/ - add your own public and private keys
  * deployment/ - Contains scripts to deploy webservers, databases, haproxy
  * libcloud.conf - Template file to include cloud provider details for libcloud
  * case-1.py - Implements code for usecase - 2 webservers with a load balancer and a database node
  * Ushahidi deployment instructions: step-by-step how to deploy Ushahidi on Rackspace cloud using orchestration templates.
    
  To run the code:

    1. Set credentials in libcloud.conf

    2. Create a venv - http://docs.python-guide.org/en/latest/starting/install/linux/#virtualenv (optional)
    
    3. pip install -r participants/code/requirements.txt
    
    4. Run python case-1.py

    Build your own use cases and try them!
