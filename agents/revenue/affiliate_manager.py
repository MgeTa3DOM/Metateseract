import json
import os

def attach_monetization():
    print("💸 VENDEUR: Optimisation du revenu...")

    if not os.path.exists("/tmp/current_trend.json"):
        print("⚠️  PAS DE TENDANCE TROUVÉE.")
        return

    with open("/tmp/current_trend.json", "r") as f:
        trend = json.load(f)

    # Logique de matching : Si Tech -> Lien Affiliation SaaS
    affiliate_links = {
        "Tech": "https://affiliate.com/best-ai-tool?ref=trinity",
        "Finance": "https://affiliate.com/crypto-exchange?ref=trinity"
    }

    link = affiliate_links.get(trend['niche'], "https://monsite.com")

    print(f"🔗 LIEN GÉNÉRATEUR DE CASH : {link}")
    print("🚀 PUBLICATION SUR YOUTUBE/TIKTOK EN COURS...")

    # Ici, appel API YouTube Data API pour upload
    # youtube.upload(video_file, description=f"Click here: {link}")

if __name__ == "__main__":
    attach_monetization()
