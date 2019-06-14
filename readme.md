### zappa-cd

Basic set up of a Flask app running on AWS Lambda, using Zappa and Travis-CI for continuous delivery.

#### Deploying from a local environment

```sh
$ zappa deploy dev
```

#### CD

Push/merge to master and Travis will take care of the rest.

#### References

https://blog.zappa.io/posts/continuous-zappa-deployments-with-travis
