# reading-quantified-server

A Django web server for Reading Quantified.

## Usage

### Local Development

See `docker-compose.yml`.

### Deploying to Heroku

Use Git to deploy to Heroku, but [just push the `web` folder to the remote](https://coderwall.com/p/ssxp5q/heroku-deployment-without-the-app-being-at-the-repo-root-in-a-subfolder):

```bash
git subtree push --prefix web heroku master
```

To force-push to Heroku:

```bash
git push heroku `git subtree split --prefix web master`:master --force
```