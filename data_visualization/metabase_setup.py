# Example configuration script for setting up Metabase
import os

def setup_metabase():
    os.system("docker run -d -p 3000:3000 --name metabase metabase/metabase")
    print("Metabase is now running on http://localhost:3000")

if __name__ == "__main__":
    setup_metabase()
