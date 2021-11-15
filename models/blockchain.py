from utils.files import read_json, write_json


class Blockchain:

    def __init__(self, blockchain_file, node_id):
        self.blockchain_file = blockchain_file
        self.node_id = node_id

    def add_block(self, *, block):
        blockchain = read_json(file=self.blockchain_file)
        block_ids = {int(key) for key in blockchain.keys()}
        last_block_id = max(block_ids) if block_ids else 0
        next_block_id = last_block_id + 1

        write_json(
            file=self.blockchain_file,
            data={
                **blockchain,
                next_block_id: block
            }
        )
