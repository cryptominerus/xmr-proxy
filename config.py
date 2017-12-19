
# Ports for your workers
STRATUM_HOST = "0.0.0.0"
STRATUM_PORT = 8080


# Main pools config
POOLS = {
    'xmr': {
        'host': 'pool.supportxmr.com',
        'port': 80,
        'username': '473qNSUfaUTNNuY6awojiDjfgoEGdSnptUnBnozEt7Cj19KKhmKXNPLhhXAcSTAC55UKEbryfVqj9HKGVaU99Mgj1CKkNxx',
        'password': 'x',
    },
    'etn': {
        'host': 'pool.electroneum.hashvault.pro',
        'port': 80,
        'username': 'etnjzKFU6ogESSKRZZbdqraPdcKVxEC17Cm1Xvbyy76PARQMmgrgceH4krAH6xmjKwJ3HtSAKuyFm1BBWYqtchtq9tBap8Qr4M.eecc02667948320980e87c8307a6fb0d71f154707db0be9e6fc5eb921108474d',
        'password': 'x',
    },
}


# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'xmr-usa.dwarfpool.com'
POOL_PORT_FAILOVER = 8050

# ERROR, INFO, DEBUG
LOGLEVEL = 'INFO'
DEBUG = True
LOGFILE = "logfile.log"
