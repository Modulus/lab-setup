#!/bin/bash
ansible lab_login -i inventory_login  -m ping
ansible lab_login -i inventory_login  -m command -a "whoami"
ansible-playbook run_tests.yml
