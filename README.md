# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### Important links ###
* https://github.com/scy-phy/scy-phy.github.io/blob/master/minicps-oc.md
* https://scy-phy.net/slides/minicps.pdf

### How do I get set up? ###

* Note that this version of the SWAT emulator is only compatible with cpppo 4.3.0 and lesser. Install cpppo with 'sudo pip install cpppo==4.3.0'
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Dropping packets on mininet switch ###
* https://hackmd.io/@pmanzoni/SyWm3n0HH
- Checking mapping between mininet interfaces and openflow controller: sh ofctl show s1
- Add flows manually: Start the mininet network with the option: --controller=none
* Alternatively, use tc qdisc - see attack.sh

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
