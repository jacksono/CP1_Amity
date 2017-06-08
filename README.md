[![Build Status](https://travis-ci.org/jacksono/CP1_Amity.svg?branch=dev)](https://travis-ci.org/jacksono/CP1_Amity)
[![Coverage Status](https://coveralls.io/repos/github/jacksono/CP1_Amity/badge.svg?branch=dev)](https://coveralls.io/github/jacksono/CP1_Amity?branch=dev)
# CP1A - Office Space Allocation (AMITY)

>Check point One project at Andela as part of the training program

1.Project definition.**

The project models a room allocation system for one of Andela’s facilities called Amity.

**Who?**

Fellows and Staff at Andela's Amity facility are the immediate consumers of the system.

**What?**

Offices and Living spaces are created and can be allocated to Staff and Fellows in Amity

>An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

**When? On request to occupy a space.**

A new Fellow or Staff member added to Amity is automatically assigned a room ( office and living space as applicable). If there are no available rooms at the time the person is being created then they can be allocated later after a new room is created or becomes available.

**Why?**
To optimize room allocations in Amity and keep track of the same. The people not having rooms are also tracked and can be reallocated to room.

2. Commands.

Command | Argument | Example
--- | --- | ---
create_room | <room_type> <room_name>... | create_room O Tsavo
add_person | <first_name> <second_name> <person_type> [wants accomodation] |add_person Jeremy Stan Fellow Y
reallocate |  <first_name> <second_name> <new_room_name> | reallocate Jermy Stan Tsavo
load_people | <filename> | load_people samplefile.txt
print_allocations| [filename] | print_allocations allocations.txt
print_unallocated| [filename] | print_unallocated unallocated.txt
print_room | <room_name> | print_room Tsavo
save_state | [db_name]| save_state amity.db
load_state |[db_name]|load_state amity.db

#3. Installation and set up.

1. First clone this repository to your local machine

2. Checkout into the **dev** branch using `git checkout develop`

3. Create a **virtualenv** on your machine and install the dependencies via `pip install -r requirements.txt` and activate it.

4. cd into the **CP1_Amity** folder and run `python main.py`

#4. Usage
Screencast!

![screencast-amity-jackson](https://user-images.githubusercontent.com/4943363/26920387-9465038c-4c41-11e7-802b-5cbe8cee297b.gif)
