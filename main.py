from fastapi import FastAPI, HTTPException, status
from googletrans import Translator

translation = Translator()
app = FastAPI(title='Translator')


@app.post('/', tags=['translator'])
def translator(text: str, lang: str = "en"):
    translation_text = translation.translate(text, dest=lang)
    if translation_text is not None and translation_text.text is not None:
        sentence = translation_text.text
        return {'Translate': sentence}
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error')