#!/usr/bin/env python3

import certbot.main as certhandle

def hello(event, context):
    certbot_args = [
        # Override directory paths so script doesn't have to be run as root
        '--config-dir', CERTBOT_DIR,
        '--work-dir', CERTBOT_DIR,
        '--logs-dir', CERTBOT_DIR,

        # Obtain a cert but don't install it
        'certificates'
        
    ]
    return certhandle.main(certbot_args)
