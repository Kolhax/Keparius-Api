from fastapi import FastAPI, Request, Query
from fastapi.responses import RedirectResponse
import hmtai
import requests
import json
import uvicorn

app = FastAPI()

@app.get("/api/nsfw/{type1}/")
async def read_item(request: Request,type1: str,go: str | None = Query(default='False', max_length=5)):
    if go == 'False':
        hmtaichoices = ['anal','ass','bdsm','cum','classic','creampie','manga','femdom','hentai','incest','masturbation','public','ero','orgy','elves','yuri','pantsy','glasses','cuckold','blowjob','boobjob','footjob','handjob','boobs','thighs','pussy','ahegao','uniform','gangbang','tentacle','gif','nsfwneko','nsfwmobilewallpaper','zettaiRyouiki']
        purrchoices = ['anal','blowjob','cum','neko','solo','threesome_fff','threesome_ffm','threesome_mmf','yaoi','yuri']
        nekoschoices = ['4k','ass','blowjob','boobs','cum','feet','hentai','wallpapers','spank','gasm','lesbian','lewd','pussy']
        if type1 in hmtaichoices:
            res = hmtai.get('hmtai',type1)
            return {"image" : res}
        
        elif type1 in nekoschoices:
            with requests.get(f"http://api.nekos.fun:8080/api/{type1}") as ril:
                res = ril.json()
                image = res['image']
                if 'https' in image:
                    return {"image" : image}
                else:
                    return {'Error' : 'Nekos API is acting like a bitch'}

        elif type1 in purrchoices:
            resp = requests.get(url=f'https://purrbot.site/api/img/nsfw/{type1}/gif')
            data = resp.json()
            if "link" in data :
                image = data['link']
                return {"image" : image}
            else:
                return {"Error" : 'Purr Api is acting like a bitch'}
        
        else:
            return {'Error': 'No such category found!'}
        
    elif go == 'True':
        hmtaichoices = ['anal','ass','bdsm','cum','classic','creampie','manga','femdom','hentai','incest','masturbation','public','ero','orgy','elves','yuri','pantsy','glasses','cuckold','blowjob','boobjob','footjob','handjob','boobs','thighs','pussy','ahegao','uniform','gangbang','tentacle','gif','nsfwneko','nsfwmobilewallpaper','zettaiRyouiki']
        purrchoices = ['anal','blowjob','cum','neko','solo','threesome_fff','threesome_ffm','threesome_mmf','yaoi','yuri']
        nekoschoices = ['4k','ass','blowjob','boobs','cum','feet','hentai','wallpapers','spank','gasm','lesbian','lewd','pussy']
        if type1 in hmtaichoices:
            res = hmtai.get('hmtai',type1)
            RedirectResponse(res)
        
        elif type1 in nekoschoices:
            with requests.get(f"http://api.nekos.fun:8080/api/{type1}") as ril:
                res = ril.json()
                image = res['image']
                if 'https' in image:
                    return RedirectResponse(image)
                else:
                    return {'Error' : 'Nekos API is acting like a bitch'}

        elif type1 in purrchoices:
            resp = requests.get(url=f'https://purrbot.site/api/img/nsfw/{type1}/gif')
            data = resp.json()
            if "link" in data :
                image = data['link']
                return RedirectResponse(image)
            else:
                return {"Error" : 'Purr Api is acting like a bitch'}
        
        else:
            return {'Error': 'No such category found!'}
    else:
        return {'Error' : 'BAD QUERY'}

@app.get("/api/nsfw/")
async def read_item(request: Request):
    list1 = []
    hmtaichoices = ['anal','ass','bdsm','cum','classic','creampie','manga','femdom','hentai','incest','masturbation','public','ero','orgy','elves','yuri','pantsy','glasses','cuckold','blowjob','boobjob','footjob','handjob','boobs','thighs','pussy','ahegao','uniform','gangbang','tentacle','gif','nsfwneko','nsfwmobilewallpaper','zettaiRyouiki']
    purrchoices = ['anal','blowjob','cum','neko','solo','threesome_fff','threesome_ffm','threesome_mmf','yaoi','yuri']
    nekoschoices = ['4k','ass','blowjob','boobs','cum','feet','hentai','wallpapers','spank','gasm','lesbian','lewd','pussy']
    list1.extend(hmtaichoices)
    list1.extend(nekoschoices)
    list1.extend(purrchoices)
    list1 = list(set(list1))
    return {'avaible':list1}

if __name__ == "__main__":
    uvicorn.run("apitry:app", debug=True, reload=True)