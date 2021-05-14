import requests

import chime_frb_api
from chime_frb_api import frb_master
import matplotlib.pyplot as plt

# Accessing the CHIME/FRB databases by first generating a token
master = frb_master.FRBMaster(username= 'gordon')
auth = {"authorization": master.API.access_token}
master.events.get_event(65540476)
{'beam_numbers': [185, 1185, 2185, 3185],
 'event_type': 'EXTRAGALACTIC',
 'fpga_time': 271532193792,
 'id': 65540476
}

# Sub-problem #1 
# ===============
# Using the Verifications API get three lists of events classified in each of the “KNOWN CANDIDATE”, “NEW CANDIDATE” and “RFI” categories.

# Querying database for different events classified by tsar
r_RFI= requests.get("https://frb.chimenet.ca/frb-master/v1/verification/get-verifications/RFI", headers=auth)
r_NC = requests.get("https://frb.chimenet.ca/frb-master/v1/verification/get-verifications/New%20CANDIDATE", headers=auth)
r_KC= requests.get("https://frb.chimenet.ca/frb-master/v1/verification/get-verifications/KNOWN%20CANDIDATE", headers=auth)

events_RFI = r_RFI.json()
events_NC = r_NC.json()
events_KC = r_KC.json()

# list for the snr values of the events in each category
snr_RFI=[]
snr_NC=[]
snr_KC=[]

# list for the ids of events in each category
events_id_RFI = []
events_id_New_Candidate = []
events_id_Known_Candidate = []

# Sub-problem #2
# ===============
# Using the Events API get the signal-to-noise ratio (S/N, called “snr” in database) for each event classified in the above categories.

for event in events_RFI:
    events_id_RFI.append(event['event_id'])
    snr_RFI.append(event['snr'])

for event in events_NC:
    events_id_New_Candidate.append(event['event_id'])
    snr_NC.append(event['snr'])

for event in events_KC:
    events_id_Known_Candidate.append(event['event_id'])
    snr_KC.append(event['snr'])


# Sub-problem #3
# ===============
# For each of the “KNOWN CANDIDATE”, “NEW CANDIDATE” and “RFI” categories, make a histogram of S/N.

# Graphs of snr values for each categories 
plt.hist(snr_RFI, bins= 200, range=[0, 20])
plt.title('Signal-to-noise ratio of RFI')
plt.xlabel('Signal-to-noise ratio(snr)')
plt.show()

plt.hist(snr_NC, bins= 200, range=[0, 120])
plt.title('Signal-to-noise ratio of New Candidate')
plt.xlabel('Signal-to-noise ratio(snr)')
plt.show()

plt.hist(snr_KC, bins= 200, range=[0, 120])
plt.title('Signal-to-noise ratio of Known Candidate')
plt.xlabel('Signal-to-noise ratio(snr)')
plt.show()
