from config.settings import DATA_DIR
from .blockchain import Blockchain


class Node:

    def __init__(self, node_id):
        self.block_queue = []
        self.data_dir = DATA_DIR / f'node_{node_id}'
        self.node_id = node_id

        self.blockchain = Blockchain(
            data_dir=self.data_dir,
            node_id=node_id
        )
