# DataAbout.me
**DataAbout.me** aims to become the most important for-profit tech company in the world by providing identity verification and authorization services, secure no-knowledge cloud data storage of personal and business data, and extremely useful carefully developed apps.

It will offer a browser plugin to autofill fields and archive web history and webpages. It will offer third parties who pass our security and privacy review OAuth access. To solve the problem where app developers are harvesting data from sites, like Facebook via OAuth, and selling it, we'll provide a secure hosted app platform where personal data is never disclosed to the app maker and we're responsible for security, privacy, safety, reliability, and accessibility regulatory compliance.

## Goals 
* **Eliminate indentity theft:** On sign up we'll require live webcam video of user and photo of front and back government ID and human verification of it. Our goal is to become the sole authentication and authorization platform in the world. If a user lost their government ID an authorized organization can look them up by entering in the info the user provides and comparing the photos to the user trying to be authenticated. 
* **Stop mass-surveillance:** Governments will have to get a warrant and convince the data owner to unencrypt the data. Users are required to prove they have enabled disk encryption with Mac Filevault or Windows Bitlocker or Linux disk encryption. 
* **Accuracy:** All data submitted for storage by a third-party is digitally signed. This way hospitals can use the medical records the user stores without worrying that the user or another party modified the records.
* **Prevent criminal, civil law, and policy violations:** Record everything and ensure that every digital action is authorized before allowing it. 
* Make it easy for app developers to launch useful regulatory compliant apps
* Give users to ability to electronically store everything about their lives and make the data useful to them
* Allow users to sell their data
* Enable secure online voting 

## How the site currently operates
* Data is stored on the AWS S3 API compliant provider Wasabi because of the significant cost savings. 

## Security strategy
* **Make discovery of email addresses hard:** Instead of storing email addresses in plaintext we store them as a hash with a unique salt. To prevent our system from ever seeing the user's password the client hashes it with a salt. This way if the database where to ever get leaked we would worry less about email addresses being disclosed. This isn't foolproof becausse an attacker could try a dictionary of email addresseses. For Gmail addresses we add `+` and a 3 digit number that we tell the user to write down in a safe place. On login attempt the server loops through each user row hashing the unique salt and email/username, and hashed with salt password.
* **Make using stolen session keys hard:** Session tokens are tied to ip address and browser fingerprint to make it harder to use stolen session tokens.

## Revenue streams
* **Subscription:** $9.99/TB, a $4 markup on Wasabi 
* **App revenue fee:** 15% under $1 million and 30% over $1 million
* **OAuth fee:** No idea what to charge.
* **Consulting:** We will develop secure software that works with our platform

