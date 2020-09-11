#!/usr/bin/env python3

import certbot.main as certhandle

CERTBOT_DIR = "/tmp/certbot"

def hello(event, context):
    certbot_args = [
        '--config-dir', CERTBOT_DIR,
        '--work-dir', CERTBOT_DIR,
        '--logs-dir', CERTBOT_DIR,
        'certificates'
        
    ]
    return certhandle.main(certbot_args)
