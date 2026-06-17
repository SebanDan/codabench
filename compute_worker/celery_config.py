import os
import ssl

broker_url = os.getenv("BROKER_URL")
if bool(os.getenv("BROKER_USE_SSL", False)):
    broker_use_ssl = {
        "cert_reqs": ssl.CERT_NONE,
    }
worker_concurrency = 1
worker_prefetch_multiplier = 1
task_acks_late = True
broker_connection_retry_on_startup = True

task_soft_time_limit = int(os.getenv("TASK_SOFT_TIME_LIMIT", 3600))
task_time_limit = int(os.getenv("TASK_TIME_LIMIT", 3900))
task_reject_on_worker_lost = True
