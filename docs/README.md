# Clouduct
## Create complete projects running on AWS in minutes

**WARNING: As of now this is complete vaporware. This is just a proposal to get some feedback**

When you need to get up and running with your cloud project as fast as possible 
it is great to have as much as possible done fow you. So on Amazon [AWS][AWS] you might use 
[CodeStar][CodeStar]. CodeStar creates all the necessary resources for you: All the
infrastructure needed as well as a build pipeline, a code repository and even some starter 
code that already is deployed. 

With just a few steps you really are up and running. You can start implementing features and
whenever you commit, everything immediately gets deployed on your environment. You can show 
it to your stakeholders, you are progressing quickly. 

But then you need to add a build step or a database or an EMail service. And then you will get 
trapped in IAM permission hell. The CodePipeline or the CodeDeploy will tell you that 
"The provided role does not have the permission arn::aws::s3::...". After some cursing you will
track down the permission needed, you will somehow find the role where you need to add the policy 
in some cumbersome JSON syntax.

But this is still not the end of the story: Imagine you have proudly launched your new web site.
Still: every commit will be deployed to your environment. Your only environment. Now you will have
to add environments with all the resources and permissions and roles and whatever. This is where
CodeStar currently leaves you on your own. Some [extensions][codestar-extend] to your project are "supported" 
and most are not. But anyway you have to do all the changes using the AWS "Console" (the web ui)
or the Command Line Interface – although CodeStar uses [CloudFormation][CloudFormation] 
internally there is no way to build on that foundation and extend it:

> There is no clear path 
  to **infrastructure as code**, which you will need sooner or later to keep your sanity.              

### Clouduct

Clouduct aims to give you the speed of AWS CodeStar while allowing you to build upon the 
foundation and extend it to your needs. You start with a simple, minimal environment and
some starter code just as with CodeStar

![Starting simple][clouduct-start]

Some of the created resources will rarely change, like the network. And you do not want to 
risk your basic network or your database by a misconfiguration of a build step.  
Therefore, Clouduct templates are already internally separated in different parts: 
Network, Storage, Compute, and Build

You can apply each layer independently of the others. Reducing the risk of damaging your
environment and keeping each part smaller and easier to understand.

And if you want to go beyond your initial environment, Clouduct templates already have
everything in place: You can easily create test, staging, and production environments.

![Grow your environment][clouduct-grow]


To be honest, you will need to learn quite some stuff: You _really_ need to understand
AWS resources and Policies etc. And to adapt the templates you need to learn 
[Terraform][Terraform]. But you are still able to start your project and deliver your MVP
in record time, because you can learn everything as you go.

#### Install

You need to install Terraform: [https://www.terraform.io/][Terraform]
And to use Clouduct you need a Python version 3.4 or later (2.7 is not supported!)

Then all you have to do is 

    pip install clouduct
    
(you probably want to use a [virtual environment][venv]).

And we suggest that you configure AWS using [named profiles][aws-named-profiles] which allows
you to easily switch between different AWS accounts. But it is not necessary 

    


[AWS]: https://aws.amazon.com/
[CodeStar]: https://aws.amazon.com/codestar/
[codestar-extend]: https://docs.aws.amazon.com/codestar/latest/userguide/how-to-change-project.html
[CloudFormation]: https://aws.amazon.com/cloudformation/
[clouduct-start]: clouduct-cropped-small.001.png "Starting Simple"
[clouduct-grow]: clouduct-cropped-small.002.png "Grow your environment"
[aws-named-profiles]: https://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html
[Terraform]: https://www.terraform.io/
[venv]: https://docs.python.org/3/library/venv.html