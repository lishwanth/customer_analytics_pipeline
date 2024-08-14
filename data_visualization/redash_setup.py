# Example configuration script for setting up Redash
import os

def setup_redash():
    os.system("docker-compose -f setup/docker-compose.yml up")
    print("Redash is now running on http://localhost:5000")

if __name__ == "__main__":
    setup_redash()
