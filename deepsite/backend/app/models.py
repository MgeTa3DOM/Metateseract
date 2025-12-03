from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

class ResourceStats(BaseModel):
    cpu_percent: float
    ram_used_gb: float
    ram_total_gb: float
    gpu_utilization: Optional[float] = None
    network_rx_mbps: float
    network_tx_mbps: float

class Node(BaseModel):
    id: str
    name: str
    provider: Literal["proxmox", "infomaniak", "ovh", "gcp", "vercel"]
    tailscale_ip: str
    status: Literal["online", "offline", "deploying"]
    stats: ResourceStats
    updated_at: datetime
