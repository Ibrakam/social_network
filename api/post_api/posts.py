from api import app

@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = 0):
    pass

@app.put('/api/post')
async def update_post():
    pass

@app.delete('/api/post')
async def delete_post():
    pass
