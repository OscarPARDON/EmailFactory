# Email Factory

## Disclaimer
Cette application est simplement le résultat de l'amélioration d'un outil d'usage personnel que j'ai décidé de partager, 
il ne s'agit donc pas d'un programme optimisé et stable. De plus, il n'a été testé qu'uniqument via un compte et le server Gmail, 
son bon fonctionnement avec d'autres services est theroiquement possible mais pas garanti.
Néanmoins, cette application est parfaitement fonctionnelle et m'a permis d'automatiser l'envoi de plusieurs centaines de mails.

## Dépendences 
* Python
* Connexion internet requise
* Une liste de distribution sous format .txt, avec un email / ligne
* Pour Gmail, Clé d'application requise : [Comment créer une clé d'application](https://support.google.com/accounts/answer/185833?hl=fr)

## Comment utiliser EmailFactory CLI
* Depuis votre terminal
* Cloner le repository
* Se rendre dans le répértoire cloné "EmailFactory"
* Lancer l'application avec python : python main.py
* Les configurations requise manquantes sont indiquées en rouge
* Configurer l'accès à votre compte, la liste d'emails, ainsi que le contenu de l'email
* Une fois cela effectué, vous pourrez débuter l'envoi automatique d'emails via l'option "send emails" (5)

# Fonctionnalités
* Configurer votre compte (Adresse email d'envoi et clé ou mot de passe pour utiliser le compte)
* Configurer votre liste de distribution
* Configurer votre email (Objet, Contenu, Pièces Jointes)
* Configurer le server de mailing (Adresse, Port)
* Mailer robuste, resistant aux anomalies dans la liste de distribution
* Temps d'attente aléatoire configurable entre l'envoi des emails pour évité d'être signalé en tant que robot
* Logging en direct de l'envoi des emails
