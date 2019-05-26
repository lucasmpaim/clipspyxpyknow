
## Commands

### Clipspy

Run:
```bash
docker-compose run python python ./run.py --type clipspy --track n --with-fix y
```


Run with Time Track:
```bash
docker-compose run python python ./run.py --type clipspy --track y
```

### Pyknow

```bash
docker-compose run python python ./run.py --type pyknow --track n
```


Run with Time Track:
```bash
docker-compose run python python ./run.py --type pyknow --track y
```

### Comparison
Run:
```bash
docker-compose run python python ./comparison.py
```
And check the "img" folder with graphics


#### Notes:
The clipspy is not installed with `requirements.txt` because a 
environment problems with alpine linux the alternative is use a Ubuntu/Debian Image, but it's a largest image compared to Alpine

On Clipsypy version, the code will raise a 


```[BLOAD2] File /app/clipspy_version/knowledge_base/base.clp is not a binary construct file.```

Ignore it, for fix it, we need to call a private function called: `_load_text(<dir>)`

##### Time Track:

Both time-track functions set the same fact's on base, not to be influenced by input time.
