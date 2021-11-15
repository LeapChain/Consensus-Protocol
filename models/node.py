from pathlib import Path

from config.settings import DATA_DIR
from utils.files import read_json, write_json
from .blockchain import Blockchain


class Node:
    name = 'node_service'

    def __init__(self, node_id):
        self.data_dir = DATA_DIR / f'node_{node_id}'
        self.block_queue_file = self.data_dir / 'block_queue.json'
        self.blockchain_file = self.data_dir / 'blockchain.json'
        self.config_file = self.data_dir / 'config.json'
        self.node_id = node_id

        self.blockchain = Blockchain(
            blockchain_file=self.blockchain_file,
            node_id=node_id
        )

        self._create_storage_structure()

    def _create_storage_structure(self):
        if not Path(self.data_dir).exists():
            Path.mkdir(self.data_dir)
            write_json(file=self.block_queue_file, data=[])
            write_json(file=self.blockchain_file, data={})
            write_json(file=self.config_file, data={})

    def accept_pv_block(self, *, block):
        block_queue = read_json(file=self.block_queue_file)
        write_json(
            file=self.block_queue_file,
            data=[*block_queue, block]
        )
