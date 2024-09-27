# Environment variables
# .env file allows you to set our environment variables

import os

# environ method take the value from the enviroment file
api_key = os.environ.get("SENGRID_API_KEY")
print(api_key)
