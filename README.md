#Booster 2017

## From Batches to pipelines lab setup
Before you run anything add your aws keys to
1. ec2.ini
2. group_vars/controller.yml
3. Add password to the users/users.json file
4. You also need a ssh key for your aws account. This should be added to ansible.cfg

## Init lab with network
Create static inventory with templates and local_action for adding unique users to all nodes

## Test the setup
run ./verify


## To verify login
ansible lab_login -i inventory_login  -m ping
ansible lab_login -i inventory_login  -m command -a "whoami"

### Tail logs

docker-compose -f docker-compose-single-broker.yml logs --tail=50 -f

### Things to fix
Create vault from the controller.yml file
