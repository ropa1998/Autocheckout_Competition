
TOKEN="9e8864c9-ece9-4d6b-9aad-eea944ce371e"
DB_ADDRESS="mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
API_ADDRESS="http://aifi.io/cpsweek/api/v1"
COMMAND="BASELINE-1"
#COMMAND="cps-test-01"
SAMPLE="nodepth"

argstr = f"--command {COMMAND} --sample {SAMPLE} --db-address {DB_ADDRESS} --api-address {API_ADDRESS} --token {TOKEN}"
cpsdriver_args = argstr.split()
