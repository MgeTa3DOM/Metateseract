'use client';
import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function DeepSiteDashboard() {
  const [nodes, setNodes] = useState<any[]>([]);

  useEffect(() => {
    // Connexion API
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/infrastructure`)
      .then(res => res.json())
      .then(data => setNodes(data));

    // Connexion WebSocket pour le temps réel
    const ws = new WebSocket(`${process.env.NEXT_PUBLIC_WS_URL}/ws/monitoring`);
    ws.onmessage = (event) => console.log("Live update:", JSON.parse(event.data));
    return () => ws.close();
  }, []);

  return (
    <div className="min-h-screen bg-black text-green-500 font-mono p-6">
      <header className="flex justify-between items-center border-b border-green-800 pb-4 mb-8">
        <h1 className="text-3xl font-bold tracking-widest">5DSENS.DEEPSITE // INFRASTRUCTURE</h1>
        <div className="flex gap-4">
          <span className="animate-pulse">● SYSTEM ONLINE</span>
          <span>MEM: 64GB</span>
          <span>GPU: RTX3080</span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Carte des Noeuds */}
        <div className="border border-green-800 bg-gray-900 p-4 rounded">
          <h2 className="text-xl mb-4">[ NODES STATUS ]</h2>
          {nodes.map(node => (
            <div key={node.id} className="flex justify-between items-center mb-2 border-b border-gray-800 pb-2">
              <div>
                <div className="font-bold">{node.name}</div>
                <div className="text-xs text-gray-500">{node.tailscale_ip}</div>
              </div>
              <div className={`text-xs px-2 py-1 rounded ${node.status === 'online' ? 'bg-green-900 text-green-100' : 'bg-red-900'}`}>
                {node.status.toUpperCase()}
              </div>
            </div>
          ))}
        </div>

        {/* Graphique Performance */}
        <div className="border border-green-800 bg-gray-900 p-4 rounded col-span-2">
          <h2 className="text-xl mb-4">[ REAL-TIME METRICS ]</h2>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={[{time: '10:00', cpu: 20}, {time: '10:05', cpu: 45}, {time: '10:10', cpu: 30}]}>
                <XAxis dataKey="time" stroke="#4ade80" />
                <YAxis stroke="#4ade80" />
                <Tooltip contentStyle={{backgroundColor: '#111', borderColor: '#4ade80'}} />
                <Line type="monotone" dataKey="cpu" stroke="#4ade80" strokeWidth={2} dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
