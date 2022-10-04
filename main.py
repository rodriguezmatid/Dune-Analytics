from duneanalytics import DuneAnalytics
import dotenv as dotenv
import os as os

dotenv.load_dotenv()

GRAPH_URL = 'https://core-hsr.dune.com/v1/graphql'

username = os.environ["username"]
password = os.environ["password"]

# initialize client
dune = DuneAnalytics(username, password)

# try to login
dune.login()

# fetch token
dune.fetch_auth_token()

# fetch query result id using query id
result_id = dune.query_result_id(query_id=1294932)

# fetch query result
data = dune.query_result(result_id)

print(data)