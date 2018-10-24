# management_system
## A system manager for newspaper reading:

### USERS:
Users can subscribe newspapers from a news aggregator.
Newspapers can publish news on different height of "permissions" and just who has the right ones
can read it.
Users can also subscribe to all newspapers in the aggregator, and delete themselves from someone.

### PUBLISHERS:
a publisher can write news, send them to the users subscribed, subscribe to more aggregators and detach from these.

### AGGREGATOR:
The central "node" to control the system, where reside the subscriptions of each user to each publisher.
The pattern followed is the Observer and the Aggregator is the object being observed from 
both users (to follow the news published) and from the publishers (to know which subscription they have)


