from nameko.rpc import rpc

from models.node import Node


class NodeService:
    name = 'node_service'

    @rpc
    def accept_pv_block(self, node_id):
        node = Node(node_id=node_id)
        node.accept_pv_block(block={'3242': 'nice'})
        return 'Not nice'
