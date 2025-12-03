# 🌀 METATESERACT // 5DSens System

> **Architecture Fractale d'Intelligence Artificielle & d'Infrastructure Souveraine.**
> *Trinity 369 · IKIGAI 777 · Univershell*

![System Status](https://img.shields.io/badge/STATUS-OPERATIONAL-brightgreen)
![Security](https://img.shields.io/badge/SECURITY-UNIVERSHELL-blueviolet)
![Architecture](https://img.shields.io/badge/ARCH-FRACTAL-orange)

## 🗺️ Vue d'Ensemble (The 5 Dimensions)

Le Metateseract n'est pas un simple bot, c'est un organisme numérique complet déployé sur infrastructure hybride (Proxmox + Cloud).

1.  **5DSens.Core (Trinity)** : Le Cerveau Orchestrateur.
    * *Maître Temps* (Scheduler)
    * *Maître Espace* (Ressources Hardware)
    * *Maître Latent* (Contexte & Mémoire)
2.  **5DSens.DeepSite** : L'Interface de Commandement (Next.js + FastAPI).
3.  **5DSens.Voice (Jarvis)** : Contrôle Vocal & Spatial.
4.  **5DSens.Revenue** : Boucles d'automatisation économique (n8n).
5.  **5DSens.Memory** : Dataset souverain, chiffré et vectorisé.

## 🏗️ Architecture Technique

* **Backend** : Python FastAPI (Async), WebSockets.
* **Frontend** : Next.js 14, TailwindCSS, Recharts.
* **Automation** : n8n (Self-hosted).
* **Infrastructure** : Docker Compose, Firecracker MicroVMs.
* **Réseau** : Tailscale Mesh (Zero Trust).
* **Hardware Hooks** : Nvidia-SMI, Proxmox API.

## 🚀 Installation Rapide (Protocol 369)

### Prérequis
* Docker & Docker Compose
* Proxmox VE (Optionnel mais recommandé)
* GPU Nvidia (Pour l'accélération locale)

### Déploiement

```bash
# 1. Cloner le Metateseract
git clone [https://github.com/MgeTa3DOM/Metateseract.git](https://github.com/MgeTa3DOM/Metateseract.git)
cd Metateseract

# 2. Configurer les clés
cp .env.example .env
nano .env

# 3. Lancer la Matrice
docker-compose -f docker-compose-deepsite.yml up -d --build
```

### 🖥️ Accès Système
* **DeepSite Dashboard** : http://localhost:3000
* **API Swagger** : http://localhost:8000/docs
* **Automation n8n** : http://localhost:5678

## 🛡️ Sécurité (Univershell)

Ce système est protégé par le protocole Univershell.
* Scan d'intention par IA avant exécution.
* Chiffrement fractal du Dataset Flow.
* Architecture "Portes Ouvertes, Coffre Fort Fermé".

---

*Généré par le Collectif 5DSens - 2025*
