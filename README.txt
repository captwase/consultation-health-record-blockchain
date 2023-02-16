#Pre-Consultation with Health Record Using Blockchain

## Problem Statement
Over decades, medical facilities have evolved elegantly. Still most of us are the witness of the fact that whenever we see a doctor, we need to put forward our medical file in front of him/her. Our file contains our previous prescriptions, medical reports, X-Rays, MRIs etc. It is a tedious task to keep a record of all these.

Currently, EHR systems in hospitals are problematic. They are hacked often (just google 'ehr systems hacked'), are not transparent, and don't keep a record of all changes to the patient record.

## Aim of the Project
We aim to provide a digital solution to this problem so that next time when you visit your doctor, you don’t need to carry your medical file. We will be using Blockchain technology to store the patient records. This will ensure that the information remains secure while being decentralized across different peers.

The basic idea is to use Blockchain for storing patient records. The workflow would be as follows:
1. Anyone can register on the Blockchain network as a doctor or a patient.
2. Whenever a patient visits a doctor, the doctor will have the required permissions to store the diagnosis and medical logs in the patient’s record which would be stored in distributed ledgers across the Blockchain network.
3. The doctor would be required to sign in the transaction (which would be cryptographically encrypted with his private key) to create and modify the records of a patient (who would be uniquely identified by a patient ID).
4. The medical records of a patient will be accessible from any hospital.


🆁🅴🆀🆄🅸🆁🅴🅼🅴🅽🆃🆂

Node JS : https://nodejs.org/en/download/ 
Python: https://www.python.org/downloads/
IPFS : https://dist.ipfs.tech/#go-ipfs 
angular: npm install -g @angular/cli
truffle: npm install -g truffle      if failed run :  npm install -g truffle@5.4.29

download and install git if not installed.
git: https://git-scm.com/downloads


open CMD in Server Directory 

```
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py run server


open GANACHE and import project 
open CMD in the Client Directory

```
npm install --force
truffle migratenpm start

```

setup metamask before opening the project

open: http://localhost:4200/

**** CLEARING THE SERVER  AND CLIENT ***
in Server dir:python manage.py flush
in CLient :truffle migrate

if any confusion please let me know.



```

IPFS Configuration

"Access-Control-Allow-Headers": [
      "X-Requested-With",
      "Access-Control-Expose-Headers",
      "Range"
   ],
   "Access-Control-Expose-Headers": [
      "Location",
      "Ipfs-Hash"
   ],
   "Access-Control-Allow-Methods": [
      "POST",
      "GET"
   ],
   "Access-Control-Allow-Origin": [
      "*"
   ],
   "X-Special-Header": [
      "Access-Control-Expose-Headers: Ipfs-Hash"
   ]