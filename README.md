# tre-lib Package

Common Python Tre API for lambda functions.

You can find a comprehensive read a comprehensive read through for updating setting up
code repository and domains [at this link here](https://github.com/nationalarchives/da-transform-dev-documentation/blob/master/runbooks/github-actions/uploading_software_to_artifactory.md)

The current domain for this package is - tna-da-transform-domain
The current repository is - tna-transform-artifacts

### Updating the package

Changes can be made in the repo, if these changes are merged into the main branch they will trigger the workflow
to update the package.

**NOTE :** If any alterations need to be made to this package, please remember to update the "version" parameter in
the setup.py file, or the package will fail to update due to a versioning conflict.

**ADDITIONAL NOTE:** The workflow that updates this package also runs the local tests, so these will need to pass
in order to update this package.

### Building the package

This package can be installed via pip - it does however require the user to alter pip's upstream source to use AWS
Codeartifact

```bash

export CODEARTIFACT_AUTH_TOKEN=`aws aws codeartifact get-authorization-token --domain ${DOMAIN} --domain-owner ${ARN_NUMBER} --region ${REGION} --query authorizationToken --output text``

pip config set global.index-url https://aws:$CODEARTIFACT_AUTH_TOKEN@${DOMAIN}-${ARN_NUMBER}.d.codeartifact.eu-west-2.amazonaws.com/pypi/${REPOSITORY}/simple/

pip install s3lib
```
# Notes

## json-schema.org

* https://json-schema.org/draft/2020-12/schema
  * Only partial support in https://github.com/python-jsonschema (2022-08-09)
    * See https://github.com/python-jsonschema/jsonschema#features
    * Instead of `"format": "uuid"`, used:
      * `"pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"`
* http://json-schema.org/draft-07/schema
  * No `uuid` support, but can use:
    * `"pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"`
  * No `https` support; i.e. requires: `"$schema": "http://json-schema.org/draft-07/schema"`
