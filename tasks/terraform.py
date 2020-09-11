#!/usr/bin/env python
"""PyInvoke Terraform Tasks
These are meant to help shorten the commands that are ran for Terraform so that
you can add long commands and make them shorter.
Useful for local testing then doing the same thing in CI/CD.
"""


# pylint: disable=import-error
import json
import os
from invoke import task
# pylint: enable=import-error


def read_creds(cred_file: str = os.environ.get('AZ_SP_CRED_FILE')) -> dict:
    """Read the Service Principal Credentials
    This is expected to be the JSON output from az ad sp create-for-rbac with
    the SDK output.
    """
    with open(cred_file) as file:
        creds = json.load(file)

    return creds


def set_env():
    """Sets common environment variables
    Set the environment files from the credentials file. Otherwise they'll need
    to be set before hand prior to this script being ran.
    """
    try:
        creds = read_creds()
        os.environ['ARM_CLIENT_ID'] = creds['clientId']
        os.environ['ARM_CLIENT_SECRET'] = creds['clientSecret']
        os.environ['ARM_SUBSCRIPTION_ID'] = creds['subscriptionId']
        os.environ['ARM_TENANT_ID'] = creds['tenantId']
    except:  # pylint: disable=bare-except
        print('Hopefully the Environment Variables are set.')


@task
def fmt(ctx):
    """Format all Terraform files
    """
    ctx.run(' '.join(("terraform",
                      "fmt",
                      "-diff",
                      "-recursive")))


@task
def validate(ctx, mod_dir='.'):
    """Validate the Terraform project
    """
    os.chdir(mod_dir)
    ctx.run(' '.join(("terraform",
                      "init",
                      "-backend=false")))
    ctx.run(' '.join(("terraform",
                      "validate",
                      ".")))


@task
def init(ctx, mod_dir='.'):
    """Terraform Initialization
    """
    set_env()
    os.chdir(mod_dir)
    ctx.run(' '.join(("terraform",
                      "init")))


@task
def plan(ctx, mod_dir='.'):
    """Terraform Plan the execution
    """
    set_env()
    os.chdir(mod_dir)
    ctx.run(' '.join(("terraform",
                      "plan",
                      "-out=tf_plan.tfplan")))


@task
def apply(ctx, mod_dir='.'):
    """Terraform Apply the execution plan
    """
    set_env()
    os.chdir(mod_dir)
    ctx.run(' '.join(("terraform",
                      "apply",
                      "tf_plan.tfplan")))


@task
def plan_destroy(ctx, mod_dir='.'):
    """Terraform Destruction Plan
    """
    set_env()
    os.chdir(mod_dir)
    ctx.run(' '.join(("terraform",
                      "plan",
                      "-destroy",
                      "-out=tf_plan.tfplan")))


@task
def destroy(ctx, mod_dir='.'):
    """Terraform Destoy Infrastructure
    """
    set_env()
    os.chdir(mod_dir)
    ctx.run(' '.join(("terraform",
                      "apply",
                      "tf_plan.tfplan")))
