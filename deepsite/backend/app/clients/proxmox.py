import httpx
import os

class ProxmoxClient:
    def __init__(self):
        self.base_url = os.getenv("PROXMOX_URL")
        self.token = os.getenv("PROXMOX_TOKEN") # Format: USER@REALM!TOKEN_ID=UUID

    async def get_nodes_status(self):
        headers = {"Authorization": f"PVEAPIToken={self.token}"}
        async with httpx.AsyncClient(verify=False) as client:
            resp = await client.get(f"{self.base_url}/api2/json/nodes", headers=headers)
            return resp.json()['data']

    async def get_resources(self, node_name: str):
        headers = {"Authorization": f"PVEAPIToken={self.token}"}
        async with httpx.AsyncClient(verify=False) as client:
            url = f"{self.base_url}/api2/json/nodes/{node_name}/status"
            resp = await client.get(url, headers=headers)
            return resp.json()['data']
