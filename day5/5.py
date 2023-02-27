import json
from typing import List
import shared

org_list = shared.get_day(2022, 5)
print(json.dumps(org_list))