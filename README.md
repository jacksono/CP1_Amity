[![Build Status](https://travis-ci.org/jacksono/CP1_Amity.svg?branch=dev)](https://travis-ci.org/jacksono/CP1_Amity)

[![Coverage Status](https://coveralls.io/repos/github/jacksono/CP1_Amity/badge.svg?branch=dev)](https://coveralls.io/github/jacksono/CP1_Amity?branch=dev)
# CP1A - Office Space Allocation (AMITY)

A project done in fulfillment of the first checkpoint of the Andela training program.

#1. Problem definition / statement.

The main objective of this project is to model a room allocation system for one of Andela’s facilities called Amity.

**Who? Fellows and staff at one of Andela's facilities alias Amity.**

Fellows and staff at Andela's Amity facility are the immediate consumers of the system.

**What? A room allocation system**

The goal is to model and build a room allocation system that smoothens the problem of keeping track of office ad living spaces at Amity, providing a scalable and usable solution.

>An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

**Where? Office spaces and living spaces.**

The system manages office spaces as well as living spaces and ensures they are allocated effectively.

**When? On request to occupy a space.**

The spaces mentioned above need to be allocated when vacant or occupied and/or reallocated as well as give status on their status when required.
The system serves to also tell how many people are in a given space at any given time.

**Why? To ensure smooth and seamless allocation and transfer of rooms amongst fellow and staff.**

The criteria set to solve the problem is to ensure the rooms can and will be allocated on request to get a new space whether office space or living space.
There is also the need to have a way of determing how many people are at a particular space from time to time.


#2. Commands.

Command | Argument | Example
--- | --- | ---
create_room | L or O | create_room O Krypton
add_person | (first_name) (last_name) (person_type) [--accomodate] |add_person Jermaine Cole Fellow --accomodate=Y
reallocate_person | (identifier) (new_room_name) | reallocate_person F1 Dreameville
load_people | (filename) | load_people samplefile.txt
print_allocations| [--o=filename] | print_allocations --o=allocations
print_unallocated| [--o=filename] | print_unallocated --o=allocations
print_room | (room_name) | print_room Fayetteville
save_state | [--db=sqlite_database]| save_state --db=carolina
load_state |(sqlite_database)|load_state my_newdatabase

#3. Installation and set up.

1. First clone this repository to your local machine using `git clone https://github.com/andela-kndegwa/CP1.git`

2. Checkout into the **develop** branch using `git checkout develop`

3. Create a **virtualenv** on your machine and install the dependencies via `pip install -r requirements.txt` and activate it.

4. cd into the **amity** folder and run `python main.py`

#4. Usage
The following screencast shows how to run the different commands. Check it out:

[![asciicast](https://asciinema.org/a/ecendttdj3a4lrp89n8luus30.png)](https://asciinema.org/a/ecendttdj3a4lrp89n8luus30)

#5. Tests.

To run nosetests ensure that you are within the *virtual environment* and have the following installed:

1. *nose*

2. *coveralls*

3. *coverage*

After ensuring the above, within the **amity folder** run :

`nosetests --with-coverage` and

`coverage report`

To run tests and view coverage.

#6. IceBox.

1. Making the CI work online.


## Credits

1.

## License

### The MIT License (MIT)
