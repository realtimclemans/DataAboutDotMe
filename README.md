# DataAbout.me
Launched by [The Real Tim Clemans Startup Launch Company](https://realtimclemans.com) on December 21, 2020, **[DataAbout.me](https://dataabout.me)** aims to become the most important for-profit tech company in the world by providing identity verification and authorization services, online voting, digital criminal, civil law, and organization policy violation prevention, retail store theft prevention, swatting prevention, non-digital criminal, civil law, and organization policy violation reporting and prevention attempts, free public profile pages for people and organizations with all legally publishable government public records data, customer feedback, blog and microblog, and organized pricing data, secure no-knowledge cloud data storage of all personal and business data each customer wants to store, and extremely useful carefully developed apps. It will use all of its profits in the first twenty years to lobby all governments to mandate identity verification and archival, for customer use, of all customer data and data the company generates about its customers through its platform.

It will offer a browser plugin to autofill fields and archive web history and webpages. It will offer third parties OAuth permissions to those who pass our security and privacy review process. To solve the problem where app developers are harvesting data from sites, like Facebook via OAuth, and selling it, we'll provide a secure managed app platform where personal data is never disclosed to the app maker and we're responsible for security, privacy, safety, reliability, and accessibility regulatory compliance. We'll only provide OAuth access to big companies that can't reasonablely move to our managed app platform.

## Founding developer Tim Clemans

Written by Tim: Hi there! I'm Tim Clemans and I'm on a mission to solve the world's biggest problems using technology. I'm inspired by and steal the best parts of:
* Elon Musk for launching a thousand satellites to provide fast internet worldwide
* Bill Gates for Microsoft and Gates Foundation
* Todd Bishop for taking me out to dinner and recording me chat about how I'm going to cause him to hire writers to do nothing but write about me
* Haben Girma for accessibility advocacy
* Molly Burke for accessibility advocacy
* Rikki Poynter for #nomorecraptions
* Mr. Beast for consistently getting millions of views, opening up 300 fast food deliverly locations overnight, giving away tons of money and stuff
* Candace Faber for helping me with my mental health
* Frank Wang for creating cheap awesome drones, note I don't support DJI's involvement with human rights violations
* Sean Whitcomb for being my boss in 2015 and continuing to support me
* Whitney Wolfe Herd for creating the woman write first online dating site Bumble
* Kathleen O'Toole for fixing issues at Seattle Police, hiring Mike Wagers and Greg Russell and me
* Jay Reitz for being super cool with me at Axon
* Marcus Womack for being super cool with at Axon
* Mike Wagers for hiring me and suggesting I create a bot to handle my records request bots
* Brandon Bouier for being an awesome boss when I worked at Seattle Police loaning me books and coaching me
* Bill Danner for taking me to church and Dollar Tree every Sunday and letting me hang out with him
* Bill Schrier for being cool with me and helping me at the Tech to Protect Hackathon
* Melinda Gates for her advocacy
* Jeff Bezos for making products cheaper and access to millions of books for about $10/month
* Nancy Lublin for Crisis Text Line
* Rick Smith for Taser which saved my life and body cams which are preventing misconduct, clearing officers of false allegations, showing the public good and bad policing, reducing the number of criminal trials, and catching misconduct
* George Hotz for making an inexpensive alternative to Tesla Autopilot
* Larry Page and Sergey Brin for Google
* Steve Jobs and Wozniak for Apple
* Sal Kahn for Kahn Academy
* Robert Greene for 48 Laws of Power
* Lex Fridman for interviewing engineers, Joe Rogan for interviewing Elon Musk
* Barack Obama for getting the Affordable Care Act passed
* Donald Trump for being transparent by speaking his mind
* Joe Biden for beating Trump
* Mark Zuckerberg for Facebook and Chan Zuckberg Initative
* Priscilla Chan for Chan Zuckberg Initative.

### Tim's moviation for launching DataAbout.me

I'm fed up with entering my address repeatedly, my password manager not understanding that subdomains each have their own passwords, creating secure answers to security questions, and filling out the same info for each dating site I use. I want all websites to use one authentication provider with mandatory two-factor app auth so I don't get hacked. I also want to automatically screenrecord everything on my computer especially tweets I see that get deleted. I also want my computer systems to know everything about me so they can assist me better. For example I want ads for stuff I would want to buy and have the budget for.

## Goals 
* **Eliminate indentity theft:** On sign up we'll require live webcam video of customer and photo of front and back government ID and human verification of it. Our goal is to become the sole authentication and authorization platform in the world. If a customer lost their government ID an authorized organization can look them up by entering in the info the customer provides and comparing the photos to the customer trying to be authenticated. 
* **Stop mass-surveillance:** Governments will have to get a warrant and convince the data owner to unencrypt the data. Customers are required to prove they have enabled disk encryption with Mac Filevault or Windows Bitlocker or Linux disk encryption. 
* **Accuracy:** All data submitted for storage by a third-party is digitally signed. This way hospitals can use the medical records the customer has without worrying that the customer or another party modified the records.
* **Prevent criminal, civil law, and policy violations:** Record everything and ensure that every digital action is authorized before allowing it. 
* Make it easy for app developers to launch useful regulatory compliant apps
* Give customers to ability to electronically store everything about their lives and make the data useful to them
* Allow customers to sell their data
* Enable secure online voting 

## How the site currently operates
* Data is stored on the [AWS S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) compliant provider [Wasabi](https://wasabi.com) because of the significant cost savings. 

## Security strategy
* **Make discovery of email addresses hard:** Instead of storing email addresses in plaintext we store them as a hash with a unique salt. To prevent our system from ever seeing the customer's password the client hashes it with a salt. This way if the database where to ever get leaked we would worry less about email addresses being disclosed. This isn't foolproof becausse an attacker could try a dictionary of email addresseses. For Gmail addresses we add `+` and a 3 digit number that we tell the customer to write down in a safe place. On login attempt the server loops through each customer row hashing the unique salt and email/username
* **Never transmit the customer's password** There are two salts. One is for server-side use and the other is for client-side use. The client gets the client-side salt, hashes the password with it and sends the server the hashed password then the server hashes it with the server side salt.
* **Ban IP addresses knowned to be used by a server, proxy, residential IP rental, compromised IP, or privacy VPN company:** 
* **Make using stolen session keys hard:** Session tokens are tied to ip address and browser fingerprint to make it harder to use stolen session tokens.

## Revenue streams
* **Subscription:** $9.99/TB, a $4 markup on Wasabi 
* **Selling data with customer's permission:** 10% fee
* **App revenue fee:** 15% under $1 million and 30% over $1 million
* **OAuth fee:** A penny per unique customer authed
* **Ads on profile pages:**
* **Consulting:** We will develop secure software that works with our platform

