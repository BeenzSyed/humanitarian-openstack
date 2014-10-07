# CASE 1: 2 WEB SERVERS, 1 DATABASE SERVER, 1 LOAD BALANCER WITH HA PROXY
from config import get_config
from oslogger import log
from db_node import DBServer
from ha_node import HAProxyServer
from web_node import WebServer
import pdb

if __name__ == "__main__":
    config = get_config()

    log.info("Creating web nodes.")
    nodes = []
    pdb.set_trace()
    web_server = WebServer(config)
    for name in ("sabeen-server-1", "sabeen-server-2"):
        nodes.append(web_server.create_node(name))

    log.info("Creating database node.")
    db_server = DBServer(config)
    db_server.create_node("sabeen-db")

    log.info("Creating haproxy load balancer node.")
    haproxy_server = HAProxyServer(config, nodes)

    lb_node = haproxy_server.create_node("sabeen-haproxy")
    log.info("Access the load balancer at %s", lb_node.public_ips)

