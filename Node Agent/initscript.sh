echo "Ading new user agent-user..."
sudo adduser agent-user
echo "Ading agent-user in sudo group..."
sudo usermod -aG sudo agent-user
echo "Setting up the agent-user to use without password..."
sudo visudo
echo 'agent-user ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/agent-user
