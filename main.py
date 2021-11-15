from models.node import Node

if __name__ == '__main__':
    node = Node(node_id=1)
    node.accept_pv_block(block={'3242': 'nice'})
    node.blockchain.add_block(block='Corn')
