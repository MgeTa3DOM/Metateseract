from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .models import Node, ResourceStats
from .clients.proxmox import ProxmoxClient
import asyncio
from datetime import datetime

app = FastAPI(title="5DSens.DeepSite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

proxmox = ProxmoxClient()

@app.get("/api/infrastructure", response_model=list[Node])
async def get_infrastructure():
    # Ici, on agrégerait Tailscale + Proxmox
    # Simulation pour la réponse immédiate
    return [
        Node(
            id="proxmox-local",
            name="T7 Legion",
            provider="proxmox",
            tailscale_ip="100.10.10.1",
            status="online",
            stats=ResourceStats(cpu_percent=12.5, ram_used_gb=32, ram_total_gb=64, gpu_utilization=45, network_rx_mbps=150, network_tx_mbps=400),
            updated_at=datetime.now()
        )
    ]

@app.websocket("/ws/monitoring")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Push real-time metrics
        await websocket.send_json({"type": "heartbeat", "timestamp": datetime.now().isoformat()})
        await asyncio.sleep(2)
