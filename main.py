from telethon import TelegramClient
import asyncio
import os
from datetime import datetime

# === IDENTIFIANTS ===
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

client = TelegramClient('telegram_session', api_id, api_hash)

# === LISTE DES CANAUX ===
channels = [
    '@ofmlustify',
    '@chattersventure',
    '@marketOFM',
    '@ofmworkk',
    '@ofmjobs',
    '@whalesofmjobs',
    '@shaftofmjobs',
    '@OFMCareers',
    '@OFMgrind',
    '@OFMWorkers',
    '@buyingadsalways',
    '@viberisejobs',
    '@onlyofmjobs',
    '@PromotionsOFM',
    '@OFMPromote',
    '@OSPJobsandServices',
    '@nigeriajobsvacancy',
    '@OFM_Jobs',
    '@POGO_JOBHUNTING',
    '@HauteClubOFM',
    '@opusva',
    '@OFMGROUPSS',
    '@ofmcc',
    '@JobsInLondonGroup',
    '@ofmcrew',
    '@OFM_Hiring',
    '@ofmboardj',
    '@vasearch',
    '@SpicyOFMJobs',
    '@Spicy_OFM_Jobs',
    '@vapirate',
    '@OFMworkers',
    '@EMM_international',
    '@OFM_Hire_Job' 
    '@syndicateofmno1'
    '@pureofm'
    '@ParadiseHiring'
  ]

# === MESSAGE DE RECRUTEMENT ===
recruitment_message = """
🚀 HIRING THREADS VA

We’re looking for people with experience on Threads.

Your task: create Threads accounts on your phone + publish posts daily.

📱 Phone required
⏱ 4-5 hours per day minimum

💰 Salary: $120/month minimum
📆 Paid bi-weekly
📈 Possibility to grow in the team
➕ Salary can increase based on clicks generated

🧪 Trial period: 1 week
💸 Paid if you reach minimum 100 clicks/day

Interested? DM @axendaagency with “VA THREADS US”.
"""

# === CONFIG ===
DELAY_MINUTES = 50  # intervalle entre chaque vague d’envoi


async def send_recruitment_message():
    while True:
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🚀 Envoi des messages…")
        for channel in channels:
            try:
                await client.send_message(channel, recruitment_message)
                print(f"✅ Message envoyé à {channel}")
                await asyncio.sleep(5)  # évite le spam trop rapide
            except Exception as e:
                print(f"❌ Erreur sur {channel}: {e}")
        print(f"🕒 Prochain envoi dans {DELAY_MINUTES} minutes…\n")
        await asyncio.sleep(DELAY_MINUTES * 60)


async def main():
    # Vérifier si la session existe et est valide (>1KB signifie authentifiée)
    if not os.path.exists('telegram_session.session') or os.path.getsize('telegram_session.session') < 1024:
        if os.path.exists('telegram_session.session'):
            os.remove('telegram_session.session')  # Supprimer session vide/invalide

        print("\n" + "="*60)
        print("⚠️  AUTHENTIFICATION REQUISE")
        print("="*60)
        print("\n🔑 Pour utiliser ce bot, vous devez d'abord vous connecter")
        print("    à Telegram de manière interactive.\n")
        print("📝 INSTRUCTIONS:")
        print("   1. Ouvrez le Shell (en bas de l'écran Replit)")
        print("   2. Tapez: python auth.py")
        print("   3. Appuyez sur Entrée")
        print("   4. Entrez votre numéro de téléphone (+33...)")
        print("   5. Entrez le code reçu par SMS/Telegram")
        print("   6. Le bot démarrera automatiquement!\n")
        print("="*60 + "\n")
        return

    await client.connect()
    if not await client.is_user_authorized():
        await client.disconnect()
        # Supprimer la session invalide
        if os.path.exists('telegram_session.session'):
            os.remove('telegram_session.session')
        print("\n❌ Session invalide supprimée! Veuillez exécuter: python auth.py\n")
        return

    me = await client.get_me()
    print(f"✅ Connecté en tant que: {me.first_name} (id: {me.id})")
    await send_recruitment_message()


if __name__ == "__main__":
    asyncio.run(main())
