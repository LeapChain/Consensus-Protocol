# Consensus-Protocol

Consensus protocol for thenewboston blockchain.

Run `scripts/node_service.sh` to start the node service.

Run the following command in another terminal to interact with the service:

```
nameko shell
>>> n.rpc.node_service.accept_pv_block(node_id=3)
```
