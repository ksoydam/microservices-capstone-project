cd microservices-capstone-project/
ansible-playbook --connection=local --inventory 127.0.0.1, --extra-vars "workspace=$(pwd)" ./ansible/playbooks/pb_run_dummy_selenium_job.yaml