from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    densecoin=math.Object(
        PARENT=networks.nets['densecoin'],
        SHARE_PERIOD=24, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=30, # blocks
        IDENTIFIER='10B9BA04D572A49F'.decode('hex'),
        PREFIX='151FF21E89F4F277'.decode('hex'),
        P2P_PORT=20000,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=30000,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-Dnc',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Densecoin to >=0.8.4.2!' if v < 80402 else None,
    ),
    densecoin_testnet=math.Object(
        PARENT=networks.nets['densecoin_testnet'],
        SHARE_PERIOD=24, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=30, # blocks
        IDENTIFIER='10B9BA04D572A49F'.decode('hex'),
        PREFIX='10B9BA04D572A49F'.decode('hex'),
        P2P_PORT=20000,
        MIN_TARGET=2**256//50 - 1,
        MAX_TARGET=2**256//50 - 1,
        PERSIST=False,
        WORKER_PORT=30000,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-tDnC',
        VERSION_CHECK=lambda v: True,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
