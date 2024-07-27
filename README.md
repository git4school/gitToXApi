# GitToXApi

Library used to turn git change log data to xapi format

## Format

The file consists of a list of xApi statements with each statement that represent a commit of the master branch.
To store git differential on a statement we use extensions in object.definition

```json
"git": [
            {
              "objectType": "Differential",
              "file": "test.txt",
              "parts": [
                {
                  "a_start_line": 0,
                  "a_interval": 2,
                  "b_start_line": 0,
                  "b_interval": 2,
                  "content": [
                    " Hello",
                    "-wold",
                    "+World !",
                  ]
                }
              ]
            }
          ]
```

## Example

### Conversion

```py
import GitToXApi.utils as utils
from tincan import Statement
import git
import json

repo = git.Repo("tp-welcome-2023-2024-Merlinpinpin1")
stmts: list[Statement] = utils.generate_xapi(repo)
```

### Serialization

```py
import json
with open("dump.json", "w") as f:
    f.write(json.dumps([stmt.as_version() for stmt in stmts]))
```

### Deserialization

```py
import json
from tincan import Statement
from GitToXApi import Differential

raw = None
with open("dump.json") as f:
    raw = json.load(f)
stmts = [Statement(e) for e in raw]

# Ensure typing of git extension
for stmt in stmts:

    git_o = stmt.object.definition.extensions["git"]
    if git_o != None and type(git_o) == list:
        stmt.object.definition.extensions["git"] = [Differential(v) for v in git_o]
```
