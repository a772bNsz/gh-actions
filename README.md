<p align="center">
    <a href="https://github.com/actions" rel="noopener">
        <img width=50px height=50px src="img/ghactions.png" alt="GitHub Actions Logo">
    </a>
    <a href="https://www.autodesk.com/products/maya" rel="noopener">
        <img width=50px height=50px src="img/maya.png" alt="Maya 2020 Logo">
    </a>
    <a href="https://www.docker.com/" rel="noopener">
        <img height=50px src="img/docker.png" alt="Docker Moby Logo">
    </a>
  <h2 align="center">Maya Docker Testing</h5>
  <h5 align="center">How to run a python test suite using the GitHub Actions CI in a Maya Docker Container</h5>
  <div align="center">
    <a href="https://github.com/AndresMWeber/gh-actions/actions" >
        <img alt="Github CI" src="https://github.com/AndresMWeber/gh-actions/workflows/CI/badge.svg" />
    </a>
    <a href="https://github.com/AndresMWeber/gh-actions/releases">
      <img alt="Github Latest Release" src="https://flat.badgen.net/github/release/andresmweber/gh-actions" />
    </a>
    <a href="https://github.com/AndresMWeber/gh-actions/commits/master">
      <img alt="Github Last Commit" src="https://flat.badgen.net/github/last-commit/andresmweber/gh-actions" />
    </a>
    <a href="https://github.com/andresmweber/gh-actions/issues">
      <img alt="Github Issues" src="https://flat.badgen.net/github/open-issues/andresmweber/gh-actions" />
    </a>
    <a href="https://github.com/AndresMWeber/gh-actions/blob/master/LICENSE.md">
      <img alt="Github License"src="https://flat.badgen.net/github/license/andresmweber/gh-actions" />
    </a>
    <a href="http://makeapullrequest.com">
      <img alt="PRs Welcome"  src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" />
    </a>
  </div>
</p>

# ⚙️ Configuration

1.  In order to run different versions of maya, you need to check if that version is available in Marcus Ottosson's Maya docker image: https://hub.docker.com/r/mottosso/maya
2.  Copy/paste another Dockerfile-`<mayaversion>`, fix the FROM maya version to your desired image version.
3.  Modify main.yml and add another job (change all instances of `<version>`):

```
  maya_<version>_tests:
    runs-on: ubuntu-latest
    name: Runs Maya <version>
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Build Container
        run: /usr/bin/docker build -t maya -f "Dockerfile-<version>" .
      - name: Run Container
        run: /usr/bin/docker run -v "$(pwd):/root/workdir" maya
```

# ⛏️ Built Using

- Docker - Containerization
- Maya - 3D Runtime Environment
- GitHub Actions - CI

# ✍️ Authors

- [a772bNsz](https://github.com/a772bNsz/)
- [andresmweber](https://github.com/andresmweber/)

# 🎉 Acknowledgements

- [marcusottosson](https://github.com/mottosso) as always for his fantastic resources
