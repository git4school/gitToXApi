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

repo = git.Repo("path/to/example_repo")
stmts: list[Statement] = utils.generate_xapi(repo)

# With custom git diff arguments 
stmts: list[Statement] = utils.generate_xapi(repo, {"unified": 1000})


```

### Serialization

```py
import json
with open("dump.json", "w") as f:
    f.write(utils.serialize_statements(stmts))

    # With custom serializing params
    f.write(utils.serialize_statements(stmts, indent=2))
```

### Deserialization

```py
import GitToXApi.utils as utils

stmts = None
with open("dump.json", "r") as f:
    stmts = utils.deserialize_statements(f)
```
