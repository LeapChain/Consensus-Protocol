from pathlib import Path

from utils.files import read_json, write_json


class Blockchain:

    def __init__(self, data_dir, node_id):
        self.data_dir = data_dir
        self.blockchain_file = self.data_dir / 'blockchain.json'
        self.config_file = self.data_dir / 'config.json'
        self.node_id = node_id

        self._create_storage_structure()

    def _create_storage_structure(self):
        if not Path(self.data_dir).exists():
            Path.mkdir(self.data_dir)
            write_json(
                file=self.blockchain_file,
                data={}
            )
            write_json(
                file=self.config_file,
                data={}
            )

    def add_block(self, block):
        blockchain = read_json(file=self.blockchain_file)
        block_ids = {int(key) for key in blockchain.keys()}
        last_block_id = max(block_ids)
        next_block_id = last_block_id + 1

        write_json(
            file=self.blockchain_file,
            data={
                **blockchain,
                next_block_id: block
            }
        )
